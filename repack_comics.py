#!/usr/bin/env python3
"""Repack mis-packaged comics into a plain zip .cbz that any reader opens.

Three shapes of problem, one pipeline:

  * a 7z or tar archive wearing a .cbr or .cbz name — a real comic in the wrong
    container. PeaZip, MComix and YACReader open these; QComicBook does not.
  * a .cbz that holds whole .cbr comics instead of pages, so there is not one
    image at the top level and no reader opens it. Merged into one omnibus.
  * a `429 Too Many Requests` HTML page wearing a comic's name. Nothing to
    repack — quarantined, and its name written to a re-download list.

Page images are copied byte for byte by default. Converting WebP to JPEG is
lossy and irreversible, so it is opt-in via --convert-nonjpeg: repack the
container first, find out whether the reader was ever unhappy about the image
format, and only then decide to re-encode.

Nothing is deleted. An original is moved into a quarantine folder on the same
filesystem, which costs no space, and only after the new file has been verified
to hold the same number of pages.

Usage:
    python3 repack_comics.py                      # dry run of the built-in list
    python3 repack_comics.py --only "Winter Men"
    python3 repack_comics.py --execute
    python3 repack_comics.py --execute --convert-nonjpeg
    python3 repack_comics.py --execute FILE [FILE ...]
"""
import argparse
import fnmatch
import json
import re
import shutil
import subprocess
import sys
import tarfile
import tempfile
import time
import zipfile
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / 'tests'))
import paths

gen = paths.load_generator()

LIBRARY = Path('/mnt/extramedia/Comics')
QUARANTINE = Path('/mnt/extramedia/_quarantine')
# The original is moved out of the library before a single byte is read from
# it, and only moves on to quarantine once the replacement is verified. So at
# every instant the file exists in exactly one place, and a run that dies
# half-way leaves it in one obvious folder rather than inside a /tmp directory
# that cleans itself up on the way out.
STAGING = Path('/mnt/extramedia/_repack_staging')
LOG_DIR = Path(__file__).resolve().parent / '.logs'
REPACK_LOG = LOG_DIR / 'last_repack.json'
# Every result ever, one JSON object per line. The report is rendered from
# this rather than from the run that happened to be last, because the job is
# done a file at a time and a report showing only the newest row is no use
# for checking that all of them open.
REPACK_HISTORY = LOG_DIR / 'repacks.jsonl'
REPORT = Path(__file__).resolve().parent / 'LIBRARY_REPACK_REPORT.md'
REDOWNLOAD = Path(__file__).resolve().parent / 'LIBRARY_REDOWNLOAD.md'

# Working copies live here, not on the library disk, which is 98% full.
TEMP_ROOT = Path('/tmp')
MIN_FREE_GB = 5

# Found by the page-count sweep. Paths are relative to LIBRARY. The first eight
# are ordinary comics in the wrong container; the ninth is the wrapper.
PHASE1 = [
    "The Living Corpse Omnibus Vol. 1 (2007).cbr",
    "The Winter Men (2005) [RC HQ-Scan 576p] ComixLedger.cbz",
    "3 Guns (2013) TPB.cbr",
    "The Programme (2007) Vol. 1-2 (RC) ComixLedger/The Programme (2007) Vol. 1 [RC HQ-Scan 720p] ComixLedger.cbz",
    "The Programme (2007) Vol. 1-2 (RC) ComixLedger/The Programme (2007) Vol. 2 [RC HQ-Scan 720p] ComixLedger.cbz",
    "Alix Senator  (2012-2020)/Alix Senator v08 - The City of Poisons (2018) (Scanlation) (phillywilly).cbr",
    "Firefly/Firefly 20th Anniversary Special 001.cbr",
    "Tales from Myth - The Fallen Lords.cbz",
    "Patience! Conviction! Revenge! (2018) /Patience! Conviction! Revenge! (2018) .cbz",
]

# The 14 that are an HTTP error page with a comic's name. The name is accurate
# even though the bytes are not, which is the whole value of listing them.
HTML_JUNK = [
    "Star Trek/Star Trek - Strange New Worlds - The Seeds of Salvation (2026) (digital) (The Magicians-Empire).cbr",
    "Planet Atmos - Exordium/Planet Atmos - Exordium v01 (2026) (digital) (Knight Ripper-Empire).cbr",
    "Dwellings (2023)/Dwellings - All Hallows' Eve Special 01 (2024) (Digital Rip) (Hourman-DCP).cbr",
    "Frankenstein - New World - The Speed of Darkness/Frankenstein - New World - The Speed of Darkness 004 (2026) (digital) (Son of Ultron-Empire).cbr",
    "Ripcord/Ripcord 004 (2026) (Digital) (DR & Quinch-Empire).cbr",
    "Beautiful Killer (2002) (Fan-Made TPB).cbr",
    "Murder Podcast/Murder Podcast 007 (2026) (Digital) (DR & Quinch-Empire).cbr",
    "All Night & Every Day (2022) (digital) (Son of Ultron-Empire).cbr",
    "Murder Drones/Murder Drones 05 (of 06) (2026) (Digital Rip) (Hourman-DCP).cbr",
    "Honor and Curse Eternal/Honor and Curse Eternal 004 (2026) (2 covers) (digital) (Knight Ripper-Empire).cbr",
    "Hello Darkness (2024)/Hello Darkness 022 (2026) (Digital Rip) (Hourman-DCP).cbr",
    "A Quiet Place - Storm Warning/A Quiet Place - Storm Warning 004 (2026) (digital) (Son of Ultron-Empire).cbr",
    "White Sky/White Sky 005 (2026) (Digital) (Mephisto-Empire).cbr",
    "Red Roots/Red Roots 004 (2026) (Digital) (Mephisto-Empire).cbr",
]

JPEG_EXTS = {'.jpg', '.jpeg', '.jpe'}

# What a bare --merge picks up in a folder, matching makecbz.py's default.
MERGE_PATTERNS = ['*.cbz', '*.cbr']

# Volumes merged by makecbz.py carry its extraction folders inside them. The
# name is an unambiguous fingerprint, and it still holds the issue index, which
# is what makes a mis-ordered volume repairable rather than merely detectable.
TEMP_EXTRACT = 'temp_extract_'


def natural_key(s):
    """Sort 'Issue 2' before 'Issue 10'.

    Plain string order puts 10 before 2, because '1' < '2' one character in.
    That is the same comparison that scrambled the volumes this tool repairs —
    getting it wrong here would rebuild them in a different wrong order.
    """
    return tuple(int(t) if t.isdigit() else t.lower()
                 for t in re.split(r'(\d+)', str(s)))


def temp_extract_index(name):
    """The issue number out of `temp_extract_7_Some Comic 008`, or None.

    makecbz.py wrote this index without zero-padding, so it sorts 0, 10, 11, 1,
    2 — but it is still *there*, and reading it back is how the true order is
    recovered from a volume that displays in the wrong one.
    """
    if not name.startswith(TEMP_EXTRACT):
        return None
    rest = name[len(TEMP_EXTRACT):]
    digits = rest.split('_', 1)[0]
    return int(digits) if digits.isdigit() else None


# ---------------------------------------------------------------- reading


def detect_format(path):
    """'zip', 'rar', '7z', 'tar' or None, from the bytes rather than the name.

    The same order as list_members() in the generator, and for the same reason:
    a name is a claim, not evidence, and every file here is misnamed.
    """
    if zipfile.is_zipfile(path):
        return 'zip'
    with open(path, 'rb') as f:
        head = f.read(len(gen.ACE_MAGIC) + 7)
    if head.startswith(gen.RAR_MAGIC):
        return 'rar'
    if head.startswith(gen.SEVENZ_MAGIC):
        return '7z'
    if tarfile.is_tarfile(path):
        return 'tar'
    return None


def looks_like_html(path):
    with open(path, 'rb') as f:
        head = f.read(512).lower()
    return head.lstrip().startswith(b'<html') or b'<title>429' in head


def extract(path, dest):
    """Unpack `path` into the empty directory `dest`."""
    fmt = detect_format(path)
    dest.mkdir(parents=True, exist_ok=True)
    if fmt == 'zip':
        with zipfile.ZipFile(path) as z:
            _safe_zip_extract(z, dest)
    elif fmt == 'tar':
        with tarfile.open(path) as t:
            _safe_tar_extract(t, dest)
    elif fmt == '7z':
        _run(['7z', 'x', '-y', f'-o{dest}', str(path)])
    elif fmt == 'rar':
        # `x` keeps the paths inside the archive; `e` would flatten them and
        # silently collide two pages that share a name in different folders.
        _run(['unrar', 'x', '-y', '-idq', str(path), str(dest) + '/'])
    else:
        raise ValueError(f'no format we can extract: {path}')
    return fmt


def _run(cmd):
    out = subprocess.run(cmd, capture_output=True, text=True, timeout=1800)
    if out.returncode != 0:
        raise RuntimeError(f'{cmd[0]} failed ({out.returncode}): '
                           f'{out.stderr.strip()[:300]}')


def _inside(dest, member_name):
    """Resolved path of a member, or None if it would escape `dest`.

    Python 3.11's tarfile has no `filter=` argument, so the guard against an
    archive containing `../../etc/…` has to be written out.
    """
    target = (dest / member_name).resolve()
    try:
        target.relative_to(dest.resolve())
    except ValueError:
        return None
    return target


def _safe_zip_extract(z, dest):
    for info in z.infolist():
        if info.is_dir():
            continue
        target = _inside(dest, info.filename)
        if target is None:
            raise ValueError(f'member escapes the extraction root: {info.filename}')
        target.parent.mkdir(parents=True, exist_ok=True)
        with z.open(info) as src, open(target, 'wb') as dst:
            shutil.copyfileobj(src, dst)


def _safe_tar_extract(t, dest):
    for member in t.getmembers():
        if not member.isfile():
            continue
        target = _inside(dest, member.name)
        if target is None:
            raise ValueError(f'member escapes the extraction root: {member.name}')
        target.parent.mkdir(parents=True, exist_ok=True)
        src = t.extractfile(member)
        if src is None:
            continue
        with src, open(target, 'wb') as dst:
            shutil.copyfileobj(src, dst)


def pages_in(root):
    """Every image under `root`, sorted by its path, as (relative_path, absolute)."""
    found = []
    for p in sorted(root.rglob('*')):
        if p.is_file() and p.suffix.lower() in gen.PAGE_EXTS:
            found.append((p.relative_to(root), p))
    return found


# Files that are not pages but are worth keeping. ComicInfo.xml is the series,
# issue and creator metadata readers and Komga/Kavita index on; dropping it
# silently loses data the user had. Thumbs.db, .DS_Store and .sfv are
# leftovers from whoever packed the archive and are not.
KEEP_ALONGSIDE = {'comicinfo.xml'}


def extras_in(root):
    """Non-page members worth carrying across, as (relative_path, absolute)."""
    return [(p.relative_to(root), p) for p in sorted(root.rglob('*'))
            if p.is_file() and p.name.lower() in KEEP_ALONGSIDE]


# ---------------------------------------------------------------- writing


def to_jpeg(src, quality=95):
    """Re-encode one page as JPEG beside itself. Returns the new path.

    Quality 95 with 4:4:4 chroma — line art and flat colour are exactly what
    chroma subsampling smears. The ICC profile is carried across so the colours
    do not shift. This is lossy and cannot be undone, which is why the caller
    has to ask for it.
    """
    from PIL import Image

    dst = src.with_suffix('.jpg')
    with Image.open(src) as im:
        if getattr(im, 'n_frames', 1) > 1:
            im.seek(0)  # an animated WebP page is a still page plus noise
        icc = im.info.get('icc_profile')
        if im.mode in ('RGBA', 'LA', 'P'):
            im = im.convert('RGBA')
            flat = Image.new('RGB', im.size, (255, 255, 255))
            flat.paste(im, mask=im.split()[-1])
            im = flat
        elif im.mode != 'RGB':
            im = im.convert('RGB')
        im.save(dst, 'JPEG', quality=quality, subsampling=0,
                optimize=True, icc_profile=icc)
    if dst != src:
        src.unlink()
    return dst


def write_cbz(entries, dest):
    """Zip `entries` — (name_in_archive, source_path) — with no compression.

    Stored, not deflated: every page is already a compressed image, so deflate
    spends CPU on both ends to save nothing, and stored members are what the
    slower readers are happiest with.
    """
    with zipfile.ZipFile(dest, 'w', zipfile.ZIP_STORED) as z:
        for name, src in entries:
            z.write(src, arcname=name)


def verify(new_path, expected_pages):
    """The new file must read back as the same number of pages, through the
    same counter the sweep used. A repack that loses a page is a repack that
    failed, and the original must stay where it is."""
    gen._PAGE_COUNTS.clear()
    got = gen.page_count(new_path)
    if got != expected_pages:
        raise RuntimeError(f'page count changed: {expected_pages} in, {got} out')
    with zipfile.ZipFile(new_path) as z:
        bad = z.testzip()
    if bad is not None:
        raise RuntimeError(f'zip member is corrupt: {bad}')
    return got


def _rel(original):
    try:
        return original.relative_to(LIBRARY)
    except ValueError:
        return Path(original.name)


def quarantine_path(original):
    """Where an original goes, keeping its place in the library visible."""
    return QUARANTINE / _rel(original)


def staging_path(original):
    """Where an original waits while its replacement is built."""
    return STAGING / _rel(original)


def stage(original, final):
    """Move the original out of the library, after checking it can come back.

    Every refusal happens here, before anything moves, because a check that
    fires half-way through leaves the library short a file and the caller
    holding a rollback it should not have needed.
    """
    staged = staging_path(original)
    quarantine = quarantine_path(original)
    for slot, what in ((staged, 'staging'), (quarantine, 'quarantine')):
        if slot.exists():
            raise FileExistsError(
                f'Destination already occupied, refusing to overwrite: {slot} ({what})')
    # final is usually the original's own path, which is about to be vacated.
    if final.exists() and final != original:
        raise FileExistsError(
            f'Destination already occupied, refusing to overwrite: {final}')
    staged.parent.mkdir(parents=True, exist_ok=True)
    shutil.move(str(original), str(staged))
    return staged


def unstage(staged, original):
    """Put it back exactly where it came from. Called when a repack fails."""
    original.parent.mkdir(parents=True, exist_ok=True)
    shutil.move(str(staged), str(original))


def _finish(staged, original, new_file, final):
    """Replacement into the library, original on to quarantine — in that order.

    If the move into the library fails there is still a good original in
    staging, so the failure costs a temp file and nothing else.
    """
    if final.exists():
        raise FileExistsError(
            f'Destination already occupied, refusing to overwrite: {final}')
    final.parent.mkdir(parents=True, exist_ok=True)
    shutil.move(str(new_file), str(final))
    q = quarantine_path(original)
    q.parent.mkdir(parents=True, exist_ok=True)
    shutil.move(str(staged), str(q))


# ---------------------------------------------------------------- the jobs


def plan_repack(path, convert):
    """Describe what would happen to one mis-packaged comic."""
    gen._PAGE_COUNTS.clear()
    pages = gen.page_count(path)
    fmt = detect_format(path)
    # Already a zip named .cbz, and no page is being re-encoded: there is
    # nothing this would change. Say so rather than rewriting 300 MB to
    # produce the same file, and rather than failing on a quarantine slot
    # that a previous run already filled.
    done = (fmt == 'zip' and path.suffix.lower() == '.cbz' and not convert)
    return {'kind': 'repack', 'path': str(path), 'format': fmt,
            'pages_before': pages, 'size': path.stat().st_size,
            'convert': convert, 'nothing_to_do': done,
            'dest': str(path.with_suffix('.cbz'))}


def do_repack(path, convert, work):
    """Extract, optionally re-encode, repack as a stored zip, verify, swap."""
    expected = gen.page_count(path)
    if not expected:
        raise RuntimeError(f'nothing to repack: page count is {expected}')

    final = path.with_suffix('.cbz')
    staged = stage(path, final)
    try:
        extracted = work / 'in'
        extract(staged, extracted)
        found = pages_in(extracted)
        if len(found) != expected:
            raise RuntimeError(
                f'extracted {len(found)} pages, archive reported {expected}')

        converted = 0
        entries = []
        for rel, abs_path in found:
            if convert and abs_path.suffix.lower() not in JPEG_EXTS:
                abs_path = to_jpeg(abs_path)
                rel = rel.with_suffix('.jpg')
                converted += 1
            entries.append((str(rel), abs_path))
        entries += [(str(rel), abs_path) for rel, abs_path in extras_in(extracted)]
        # Only the extension can have changed, so the order the pages were found
        # in still holds; sorting again guards against .png and .webp of the same
        # page number landing differently.
        entries.sort(key=lambda e: e[0])

        new_file = work / 'out.cbz'
        write_cbz(entries, new_file)
        verify(new_file, expected)
    except BaseException:
        unstage(staged, path)
        raise

    _finish(staged, path, new_file, final)
    return {'pages_after': expected, 'converted': converted,
            'new_size': final.stat().st_size, 'final': str(final)}


def plan_omnibus(path):
    inner = gen.list_members(path) or []
    return {'kind': 'omnibus', 'path': str(path), 'format': detect_format(path),
            'inner': sorted(inner), 'size': path.stat().st_size,
            'dest': str(path.with_suffix('.cbz'))}


def do_omnibus(path, convert, work):
    """Five comics inside one .cbz become one book of continuously numbered pages.

    Issue order comes from the inner filenames, which carry 001..005, not from
    whatever order the zip happens to store them in.
    """
    final = path.with_suffix('.cbz')
    staged = stage(path, final)
    try:
        holder = work / 'holder'
        extract(staged, holder)
        issues = sorted(p for p in holder.rglob('*')
                        if p.is_file() and p.suffix.lower() in {'.cbr', '.cbz', '.cb7'})
        if not issues:
            raise RuntimeError('no inner comics found')

        entries, converted = [], 0
        for n, issue in enumerate(issues):
            unpacked = work / f'issue_{n:03d}'
            extract(issue, unpacked)
            for rel, abs_path in pages_in(unpacked):
                if convert and abs_path.suffix.lower() not in JPEG_EXTS:
                    abs_path = to_jpeg(abs_path)
                    converted += 1
                entries.append(abs_path)

        numbered = [(f'{i:03d}{p.suffix.lower()}', p)
                    for i, p in enumerate(entries, 1)]
        new_file = work / 'out.cbz'
        write_cbz(numbered, new_file)
        verify(new_file, len(numbered))
    except BaseException:
        unstage(staged, path)
        raise

    _finish(staged, path, new_file, final)
    return {'pages_after': len(numbered), 'issues': len(issues),
            'converted': converted, 'new_size': final.stat().st_size,
            'final': str(final)}


def _issue_entries(sources, convert, work, label):
    """Pages from several comics, prefixed with a padded issue number.

    The prefix is the whole design. `0007/whatever the scanner called it.jpg`
    puts the issues in order for any reader that sorts by name, while leaving
    the page names inside an issue exactly as they were — so a page sequence
    that read correctly as a single issue still reads correctly in the volume.

    Four digits, not one. An unpadded index is what put issue 10 before issue 2
    in every volume this tool exists to repair.
    """
    entries, converted, total = [], 0, 0
    for n, src in enumerate(sources, 1):
        expected = gen.page_count(src)
        if not expected:
            raise RuntimeError(f'{Path(src).name} holds no pages')
        unpacked = work / f'{label}_{n:04d}'
        extract(src, unpacked)
        found = pages_in(unpacked)
        if len(found) != expected:
            raise RuntimeError(f'{Path(src).name}: extracted {len(found)} pages, '
                               f'archive reported {expected}')
        for rel, abs_path in found:
            if convert and abs_path.suffix.lower() not in JPEG_EXTS:
                abs_path = to_jpeg(abs_path)
                rel = rel.with_suffix('.jpg')
                converted += 1
            entries.append((f'{n:04d}/{rel}', abs_path))
        entries += [(f'{n:04d}/{rel}', abs_path)
                    for rel, abs_path in extras_in(unpacked)]
        total += expected
    return entries, converted, total


def plan_merge(sources, output, convert):
    ordered = sorted(sources, key=natural_key)
    pages = []
    for s in ordered:
        gen._PAGE_COUNTS.clear()
        pages.append(gen.page_count(s))
    return {'kind': 'merge', 'path': str(output), 'format': 'merge',
            'sources': [str(s) for s in ordered], 'source_pages': pages,
            'pages_before': sum(p or 0 for p in pages),
            'size': sum(Path(s).stat().st_size for s in ordered),
            'convert': convert, 'dest': str(output)}


def do_merge(sources, output, convert, work):
    """Several issues into one volume. The issues are ordered by their own
    filenames, read naturally, so 'v 2' precedes 'v 10'."""
    ordered = sorted(sources, key=natural_key)
    if output.exists():
        raise FileExistsError(
            f'Destination already occupied, refusing to overwrite: {output}')

    entries, converted, total = _issue_entries(ordered, convert, work, 'issue')
    entries.sort(key=lambda e: e[0])
    new_file = work / 'merged.cbz'
    write_cbz(entries, new_file)
    verify(new_file, total)

    output.parent.mkdir(parents=True, exist_ok=True)
    shutil.move(str(new_file), str(output))
    # The sources are kept, exactly like a repacked original: a merge that read
    # the wrong pages is only correctable while the issues still exist.
    for s in ordered:
        q = quarantine_path(Path(s))
        q.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(s), str(q))
    return {'pages_after': total, 'issues': len(ordered), 'converted': converted,
            'new_size': output.stat().st_size, 'final': str(output)}


def misordered_report(path):
    """Is this volume one makecbz.py built, and did it come out in order?

    Returns (issue_count, highest_index) or None. A volume is mis-ordered when
    an index of 10 or more exists, because that is the point at which the
    unpadded name sorts ahead of single-digit ones.
    """
    members = gen.list_members(path)
    if not members:
        return None
    indices = set()
    for m in members:
        top = m.split('/')[0]
        idx = temp_extract_index(top)
        if idx is not None:
            indices.add(idx)
    if not indices:
        return None
    return len(indices), max(indices)


def plan_repair(path):
    gen._PAGE_COUNTS.clear()
    found = misordered_report(path)
    if found is None:
        return {'kind': 'repair', 'path': str(path),
                'error': 'not a makecbz.py volume — no temp_extract_ folders'}
    issues, highest = found
    return {'kind': 'repair', 'path': str(path), 'format': 'makecbz volume',
            'issues': issues, 'highest_index': highest,
            'misordered': highest >= 10,
            'pages_before': gen.page_count(path),
            'size': path.stat().st_size, 'convert': False,
            'dest': str(path.with_suffix('.cbz'))}


def do_repair(path, convert, work):
    """Rebuild a makecbz.py volume with its issues in the right order.

    Nothing was lost when it was built wrong: `temp_extract_7_...` still names
    issue 7. Re-prefixing each page with that index, padded, puts the volume
    back in reading order without needing the original issue files.
    """
    expected = gen.page_count(path)
    final = path.with_suffix('.cbz')
    staged = stage(path, final)
    try:
        extracted = work / 'in'
        extract(staged, extracted)

        found, converted = [], 0
        for rel, abs_path in pages_in(extracted):
            idx = temp_extract_index(rel.parts[0])
            if idx is None:
                # A page outside the extraction folders means this volume is
                # not the shape we think it is. Guessing where it belongs in
                # the reading order would be worse than refusing.
                raise RuntimeError(f'page outside any temp_extract_ folder: {rel}')
            inner = Path(*rel.parts[1:])
            if convert and abs_path.suffix.lower() not in JPEG_EXTS:
                abs_path = to_jpeg(abs_path)
                inner = inner.with_suffix('.jpg')
                converted += 1
            found.append((idx, inner, abs_path))

        if len(found) != expected:
            raise RuntimeError(f'rebuilt {len(found)} pages, volume held {expected}')

        # makecbz.py numbered its folders from zero, and an issue that yielded
        # no pages leaves a gap. Renumber by rank so a repaired volume always
        # comes out 0001..N, the same layout --merge writes.
        issue_no = {idx: n for n, idx
                    in enumerate(sorted({i for i, _, _ in found}), 1)}
        entries = [(f'{issue_no[idx]:04d}/{inner}', abs_path)
                   for idx, inner, abs_path in found]

        # The per-issue ComicInfo.xml rides along with the issue it describes.
        # One at the volume root belongs to the volume and stays at the root.
        # Never converted — it is metadata, not a page.
        for rel, abs_path in extras_in(extracted):
            idx = temp_extract_index(rel.parts[0])
            if idx is None:
                entries.append((str(rel), abs_path))
            elif idx in issue_no:
                entries.append((f'{issue_no[idx]:04d}/{Path(*rel.parts[1:])}',
                                abs_path))
        entries.sort(key=lambda e: e[0])
        new_file = work / 'out.cbz'
        write_cbz(entries, new_file)
        verify(new_file, expected)
    except BaseException:
        unstage(staged, path)
        raise

    _finish(staged, path, new_file, final)
    return {'pages_after': expected, 'converted': converted,
            'new_size': final.stat().st_size, 'final': str(final)}


def do_junk(path):
    q = quarantine_path(path)
    if q.exists():
        raise FileExistsError(f'Destination already occupied, refusing to overwrite: {q}')
    # Recorded before the move, because the re-download list reports how much
    # disk the error page was occupying and the path is about to change.
    size = path.stat().st_size
    q.parent.mkdir(parents=True, exist_ok=True)
    shutil.move(str(path), str(q))
    return {'quarantined': str(q), 'size': size}


# ---------------------------------------------------------------- reports


def mb(n):
    return f'{n / 1e6:.0f} MB'


def file_url(p):
    from urllib.parse import quote
    return 'file://' + quote(str(p))


def link_label(name):
    """Square brackets are common in scan-group filenames and they end a
    markdown link label early, so the link renders as broken text."""
    return name.replace('[', '\\[').replace(']', '\\]')


def write_report(results, convert):
    lines = ['# Repacked comics — please open each one',
             '',
             'Two different faults, fixed the same way: extract, then write a',
             'plain stored zip. The links open the files themselves.',
             '']
    if not convert:
        lines += ['Page images were copied byte for byte. Nothing was re-encoded and',
                  'no quality was lost — including the WebP books, which QComicBook',
                  'turned out to be perfectly happy with once they were out of 7z.',
                  '']
    else:
        lines += ['Non-JPEG pages were re-encoded to JPEG at quality 95, 4:4:4.', '']

    ok = sorted((r for r in results
                 if r.get('status') == 'ok' and r['kind'] != 'junk'),
                key=lambda r: -(r.get('pages_after') or 0))
    failed = [r for r in results if r.get('status') == 'failed']
    junk = [r for r in results if r.get('status') == 'ok' and r['kind'] == 'junk']

    # Repairs and container fixes are not the same complaint, and one heading
    # over both said the wrong thing about each. A repaired volume always
    # opened; it just read in the wrong order.
    groups = [
        ('repair', 'read in the wrong order, now rebuilt',
         ['These opened perfectly well already. The issues inside them were',
          'merged in the wrong order, so they read 1, 11, 12, 2, 3 ... Every',
          'page is byte for byte the one that was there before; only the name',
          'it is stored under changed.']),
        (None, 'would not open in QComicBook, now repacked',
         ['These were 7z or tar wearing a `.cbr`/`.cbz` name, plus one zip that',
          'held whole comics instead of pages. The container was the entire',
          'objection — QComicBook reads the pages themselves fine.']),
    ]
    for kind, heading, blurb in groups:
        rows = [r for r in ok
                if (r['kind'] == 'repair') == (kind == 'repair')]
        if not rows:
            continue
        lines += [f'## {len(rows)} {heading}', ''] + blurb + ['']
        lines += ['| pages | was | size | open it |', '|---|---|---|---|']
        for r in rows:
            p = Path(r['final'])
            was = r['format'] + (' wrapper' if r['kind'] == 'omnibus' else '')
            lines.append(f'| {r.get("pages_after")} | {was} | {mb(r["new_size"])} | '
                         f'[{link_label(p.name)}]({file_url(p)}) |')
        lines.append('')

    if ok:
        lines += ['The originals are in `/mnt/extramedia/_quarantine/`, under the',
                  'same relative path they had in the library. Nothing was deleted.',
                  '']

    if failed:
        lines += ['## Failed — the original is untouched', '',
                  '| file | why |', '|---|---|']
        for r in failed:
            lines.append(f'| `{Path(r["path"]).name}` | {r["error"]} |')
        lines.append('')

    if junk:
        lines += [f'## {len(junk)} error pages moved out of the library', '',
                  'These were `429 Too Many Requests` HTML, not comics. See',
                  '`LIBRARY_REDOWNLOAD.md` for the list to fetch again.', '']

    REPORT.write_text('\n'.join(lines) + '\n')
    print(f'\nreport -> {REPORT}')


def write_redownload(moved):
    """A checklist of comics to fetch again, each with the path it belongs at.

    The full path rather than the bare name: the name alone does not say which
    series folder the replacement should land in, and several of these sit two
    levels down.
    """
    lines = ['# Comics to download again',
             '',
             'Each of these was saved as a `429 Too Many Requests` HTML page',
             'instead of the comic. The server was rate-limiting and the',
             'downloader wrote the refusal to disk under the comic\'s name, so',
             'the names are right even though the bytes never were.',
             '',
             'The path shown is where the file was, and where the replacement',
             'should go. The error page itself is now at the same relative path',
             'under `/mnt/extramedia/_quarantine/`.',
             '']
    total = 0
    for r in sorted(moved, key=lambda r: r['path']):
        original = Path(r['path'])
        size = r.get('size') or 0
        if not size and r.get('quarantined'):
            # Runs before the size was recorded still have the file itself.
            q = Path(r['quarantined'])
            size = q.stat().st_size if q.exists() else 0
        total += size
        lines.append(f'- [ ] **{original.name}** — {mb(size)} of HTML')
        lines.append(f'  - belongs at `{original}`')
        if r.get('quarantined'):
            lines.append(f'  - error page now at `{r["quarantined"]}`')
    lines += ['', f'{len(moved)} files, {mb(total)} of disk that was never a comic.']
    REDOWNLOAD.write_text('\n'.join(lines) + '\n')
    print(f'redownload list -> {REDOWNLOAD}')


def save_log(results):
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().isoformat()
    REPACK_LOG.write_text(json.dumps(
        {'timestamp': stamp, 'results': results}, indent=2))
    with open(REPACK_HISTORY, 'a') as f:
        for r in results:
            f.write(json.dumps({**r, 'timestamp': stamp}) + '\n')
    print(f'execution log -> {REPACK_LOG}')


def load_history():
    """Every result so far, newest wins where a file was repacked twice."""
    if not REPACK_HISTORY.exists():
        return []
    by_path = {}
    for line in REPACK_HISTORY.read_text().splitlines():
        if not line.strip():
            continue
        try:
            r = json.loads(line)
        except ValueError:
            continue
        by_path[r.get('path')] = r
    return list(by_path.values())


# ---------------------------------------------------------------- driver


MISORDERED = Path(__file__).resolve().parent / 'LIBRARY_MISORDERED.md'


def find_misordered(root):
    """Walk the library for volumes makecbz.py built, and say which read wrong.

    Only .cbz is worth opening: makecbz.py always wrote zip, whatever the
    sources were. Reading the member list of a zip is cheap, so this is minutes
    rather than the hours a full archive sweep costs.
    """
    files = sorted(p for p in root.rglob('*.cbz') if p.is_file())
    print(f'{len(files)} .cbz to check under {root}', flush=True)
    hits, started = [], time.time()
    for i, p in enumerate(files, 1):
        try:
            found = misordered_report(p)
        except OSError:
            continue
        if found:
            issues, highest = found
            hits.append({'path': str(p), 'issues': issues, 'highest': highest,
                         'misordered': highest >= 10,
                         'size': p.stat().st_size})
        if i % 2000 == 0:
            rate = i / (time.time() - started)
            print(f'  {i}/{len(files)}  {rate:.0f}/s  '
                  f'eta {(len(files) - i) / rate / 60:.0f}m  hits={len(hits)}',
                  flush=True)
    return hits


def write_misordered(hits, root):
    bad = sorted((h for h in hits if h['misordered']), key=lambda h: -h['issues'])
    ok = [h for h in hits if not h['misordered']]
    lines = ['# Volumes merged in the wrong page order',
             '',
             'Every volume below was built by `makecbz.py`, which is detectable',
             'because it leaves its `temp_extract_` folders inside the archive.',
             '',
             'It numbered those folders without zero-padding, so `temp_extract_10_`',
             'sorts *before* `temp_extract_1_` — `0` is 48 and `_` is 95. A volume',
             'is therefore fine up to ten issues and scrambled from eleven, which',
             'is why this went unnoticed for so long.',
             '',
             'Nothing was lost. The folder name still carries the issue number, so',
             'the reading order can be rebuilt from inside the volume itself —',
             'the original issue files are not needed.',
             '']
    if bad:
        lines += [f'## {len(bad)} read in the wrong order', '',
                  '| issues | pages out of order | file |', '|---|---|---|']
        for h in bad:
            n = h['issues']
            # 1, then 11..n, then 2, 3 ... — everything from 2 up is displaced.
            lines.append(f'| {n} | issues 2–{n} | `{Path(h["path"]).relative_to(root)}` |')
        lines += ['', 'Repair them with:', '',
                  '```', 'python3 repack_comics.py --repair --execute FILE...', '```', '']
    if ok:
        lines += [f'## {len(ok)} built by the same tool but still in order', '',
                  'Ten issues or fewer, so the unpadded index never overtook itself.',
                  'They carry the `temp_extract_` folders but read correctly.', '']
    MISORDERED.write_text('\n'.join(lines) + '\n')
    print(f'\n{len(bad)} mis-ordered, {len(ok)} fine -> {MISORDERED}')


def free_gb(path):
    st = shutil.disk_usage(path)
    return st.free / 1e9


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('files', nargs='*',
                    help='comics to repack; default is the built-in Phase 1 list')
    ap.add_argument('--execute', action='store_true',
                    help='actually do it; without this nothing is written')
    ap.add_argument('--convert-nonjpeg', action='store_true',
                    help='re-encode WebP/PNG pages as JPEG (lossy, irreversible)')
    ap.add_argument('--only', metavar='SUBSTR',
                    help='restrict to files whose path contains SUBSTR')
    ap.add_argument('--skip-junk', action='store_true',
                    help='leave the 429 HTML files alone')
    ap.add_argument('--rebuild-reports', action='store_true',
                    help='re-render both markdown reports from the run history '
                         'and exit, touching no comic')
    ap.add_argument('--merge', nargs='?', const='', metavar='OUTPUT.cbz',
                    help='merge the given issues into one volume; with no name, '
                         'every comic in --dir, named after that folder')
    ap.add_argument('--pattern', metavar='GLOB',
                    help='with --merge, which files in --dir to take; quoted, '
                         'and expanded here rather than by the shell '
                         f'(default: {MERGE_PATTERNS})')
    ap.add_argument('--dir', default='.', metavar='DIR',
                    help='with --merge and --pattern, where to look (default: .)')
    ap.add_argument('--repair', action='store_true',
                    help='rebuild makecbz.py volumes in the right issue order')
    ap.add_argument('--find-misordered', nargs='?', const=str(LIBRARY),
                    metavar='ROOT',
                    help='scan for volumes that read in the wrong order and exit')
    args = ap.parse_args()

    if args.find_misordered:
        root = Path(args.find_misordered)
        write_misordered(find_misordered(root), root)
        return 0

    if args.rebuild_reports:
        history = load_history()
        if not history:
            print(f'No history at {REPACK_HISTORY}; nothing to render.')
            return 1
        write_report(history, args.convert_nonjpeg)
        moved = [r for r in history if r['kind'] == 'junk' and r['status'] == 'ok']
        if moved:
            write_redownload(moved)
        return 0

    if args.merge is not None:
        # The pattern arrives as a string and is expanded here. A shell that
        # expanded it first would hand over a list this script cannot tell from
        # explicitly chosen files, and an unquoted pattern matching nothing
        # would arrive as the literal pattern.
        where = Path(args.dir).resolve()
        patterns = [args.pattern] if args.pattern else MERGE_PATTERNS
        if args.files and not args.pattern:
            sources = [Path(f) for f in args.files]
        else:
            sources = [p for p in sorted(where.iterdir()) if p.is_file()
                       and any(fnmatch.fnmatch(p.name, g) for g in patterns)]
        # Named after the folder, the way makecbz.py did it, so the common
        # case is `--merge` on its own inside a series directory.
        output = Path(args.merge) if args.merge else where / f'{where.name}.cbz'
        sources = [p for p in sources if p.resolve() != output.resolve()]
        if not sources:
            print(f'No issues to merge in {where} '
                  f'matching {" ".join(patterns)}.')
            return 1
        return run_merge(sources, output, args)

    if args.files:
        targets = [Path(f) for f in args.files]
        junk = []
    else:
        targets = [LIBRARY / r for r in PHASE1]
        junk = [] if args.skip_junk else [LIBRARY / r for r in HTML_JUNK]

    if args.only:
        targets = [p for p in targets if args.only.lower() in str(p).lower()]
        junk = [p for p in junk if args.only.lower() in str(p).lower()]

    missing = [p for p in targets + junk if not p.exists()]
    if missing:
        print('These are not where the report said they were:')
        for p in missing:
            print(f'  {p}')
        return 1
    targets = [p for p in targets if p.exists()]

    if not targets and not junk:
        print('Nothing selected.')
        return 1

    print(f'{len(targets)} to repack, {len(junk)} error pages to quarantine')
    print(f'{"EXECUTING" if args.execute else "DRY RUN — nothing will be written"}')
    print(f'convert non-JPEG pages: {"yes" if args.convert_nonjpeg else "no, pages copied as-is"}')
    print()

    # Plan first, and print it, whether or not we are going to run it.
    plans = []
    for p in targets:
        try:
            if args.repair:
                plan = plan_repair(p)
            elif _is_wrapper(p):
                plan = plan_omnibus(p)
            else:
                plan = plan_repack(p, args.convert_nonjpeg)
        except Exception as e:
            plan = {'kind': 'repair' if args.repair else 'repack',
                    'path': str(p), 'error': str(e)}
        plans.append(plan)
        _print_plan(plan)
    for p in junk:
        kind = 'HTML error page' if looks_like_html(p) else 'NOT HTML — check before moving'
        print(f'  quarantine  {mb(p.stat().st_size):>8}  {kind}  {p.name}')
    print()

    if not args.execute:
        print('Dry run complete. Re-run with --execute to carry this out.')
        return 0

    have = free_gb(TEMP_ROOT)
    if have < MIN_FREE_GB:
        print(f'Only {have:.1f} GB free on {TEMP_ROOT}, need {MIN_FREE_GB} GB to work in.')
        return 1

    QUARANTINE.mkdir(parents=True, exist_ok=True)
    STAGING.mkdir(parents=True, exist_ok=True)
    left = sorted(p for p in STAGING.rglob('*') if p.is_file())
    if left:
        print(f'{len(left)} file(s) left in {STAGING} by an earlier run:')
        for p in left:
            print(f'  {p}')
        print('Put them back in the library, or move them aside, before re-running.')
        return 1
    results = []
    started = time.time()

    for plan in plans:
        p = Path(plan['path'])
        if 'error' in plan:
            print(f'SKIP  {p.name}: {plan["error"]}')
            results.append({**plan, 'status': 'failed', 'error': plan['error']})
            continue
        if plan.get('nothing_to_do'):
            print(f'  {p.name}: already a zip .cbz, left alone')
            continue
        print(f'  {p.name} ...', end='', flush=True)
        try:
            with tempfile.TemporaryDirectory(dir=TEMP_ROOT, prefix='repack_') as tmp:
                work = Path(tmp)
                op = {'omnibus': do_omnibus, 'repair': do_repair}.get(
                    plan['kind'], do_repack)
                out = op(p, args.convert_nonjpeg, work)
            results.append({**plan, **out, 'status': 'ok'})
            print(f' {out["pages_after"]} pages, {mb(out["new_size"])}'
                  + (f', {out["converted"]} converted' if out['converted'] else ''))
        except Exception as e:
            results.append({**plan, 'status': 'failed', 'error': str(e)})
            print(f' FAILED: {e}')

    for p in junk:
        try:
            out = do_junk(p)
            results.append({'kind': 'junk', 'path': str(p), 'status': 'ok', **out})
        except Exception as e:
            results.append({'kind': 'junk', 'path': str(p), 'status': 'failed',
                            'error': str(e)})
            print(f'  FAILED to quarantine {p.name}: {e}')

    good = sum(1 for r in results if r['status'] == 'ok' and r['kind'] != 'junk')
    bad = sum(1 for r in results if r['status'] == 'failed')
    print(f'\n{good} repacked, {bad} failed, in {(time.time() - started) / 60:.1f}m')

    save_log(results)
    history = load_history()
    write_report(history, args.convert_nonjpeg)
    moved = [r for r in history if r['kind'] == 'junk' and r['status'] == 'ok']
    if moved:
        write_redownload(moved)
    return 1 if bad else 0


def run_merge(sources, output, args):
    """Several issues into one volume — the makecbz.py job, done safely."""
    missing = [p for p in sources if not p.exists()]
    if missing:
        for p in missing:
            print(f'  not found: {p}')
        return 1

    plan = plan_merge(sources, output, args.convert_nonjpeg)
    print(f'{len(sources)} issues -> {output}')
    print(f'{"EXECUTING" if args.execute else "DRY RUN — nothing will be written"}')
    print()
    for n, (s, pages) in enumerate(zip(plan['sources'], plan['source_pages']), 1):
        print(f'  {n:04d}/  {str(pages):>4} pages  {Path(s).name}')
    print(f'\n  {plan["pages_before"]} pages in total, {mb(plan["size"])}')
    if any(p is None for p in plan['source_pages']):
        print('\n  One of these could not be read. Refusing to merge a volume '
              'that would silently be missing an issue.')
        return 1
    print()

    if not args.execute:
        print('Dry run complete. Re-run with --execute to carry this out.')
        return 0

    QUARANTINE.mkdir(parents=True, exist_ok=True)
    try:
        with tempfile.TemporaryDirectory(dir=TEMP_ROOT, prefix='merge_') as tmp:
            out = do_merge(sources, output, args.convert_nonjpeg, Path(tmp))
    except Exception as e:
        print(f'FAILED: {e}')
        return 1
    print(f'{out["pages_after"]} pages from {out["issues"]} issues, '
          f'{mb(out["new_size"])} -> {output}')
    print(f'The issues are in {QUARANTINE}, not deleted.')
    save_log([{**plan, **out, 'status': 'ok'}])
    write_report(load_history(), args.convert_nonjpeg)
    return 0


def _is_wrapper(path):
    """True when the archive holds whole comics instead of pages."""
    members = gen.list_members(path) or []
    return any(Path(m).suffix.lower() in {'.cbr', '.cbz', '.cb7'} for m in members)


def _print_plan(plan):
    p = Path(plan['path'])
    if 'error' in plan:
        print(f'  ERROR       {p.name}: {plan["error"]}')
        return
    if plan['kind'] == 'repair':
        state = ('reads WRONG from issue 2' if plan['misordered']
                 else 'reads correctly, 10 issues or fewer')
        print(f'  repair      {mb(plan["size"]):>8}  {plan["issues"]} issues, '
              f'{plan["pages_before"]} pages — {state}  {p.name}')
    elif plan['kind'] == 'omnibus':
        print(f'  omnibus     {mb(plan["size"]):>8}  {plan["format"]} holding '
              f'{len(plan["inner"])} comics  {p.name}')
        for m in plan['inner']:
            print(f'                          + {m}')
    elif plan.get('nothing_to_do'):
        print(f'  nothing     {mb(plan["size"]):>8}  already a zip .cbz, '
              f'{plan["pages_before"]} pages  {p.name}')
    else:
        print(f'  repack      {mb(plan["size"]):>8}  {plan["format"]} -> zip, '
              f'{plan["pages_before"]} pages  {p.name}')


if __name__ == '__main__':
    sys.exit(main())
