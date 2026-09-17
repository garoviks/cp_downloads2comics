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
import json
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


def do_junk(path):
    q = quarantine_path(path)
    if q.exists():
        raise FileExistsError(f'Destination already occupied, refusing to overwrite: {q}')
    q.parent.mkdir(parents=True, exist_ok=True)
    shutil.move(str(path), str(q))
    return {'quarantined': str(q)}


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
             'Every file below is now a plain stored zip with a `.cbz` name. The',
             'links open the file itself; the point of the exercise is whether',
             '**QComicBook** will read them, since YACReader already would.',
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

    if ok:
        lines += [f'## {len(ok)} repacked', '',
                  '| pages | was | size | open it |', '|---|---|---|---|']
        for r in ok:
            p = Path(r['final'])
            pages = r.get('pages_after')
            was = r['format'] + (' wrapper' if r['kind'] == 'omnibus' else '')
            lines.append(f'| {pages} | {was} | {mb(r["new_size"])} | '
                         f'[{link_label(p.name)}]({file_url(p)}) |')
        lines.append('')
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


def write_redownload(names):
    lines = ['# Comics to download again',
             '',
             'Each of these was saved as a `429 Too Many Requests` HTML page',
             'instead of the comic. The server was rate-limiting and the',
             'downloader wrote the refusal to disk under the comic\'s name, so',
             'the names are right even though the bytes never were.',
             '',
             'The files have been moved to `/mnt/extramedia/_quarantine/`.',
             '']
    for n in names:
        lines.append(f'- [ ] {n}')
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
    args = ap.parse_args()

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
            plan = (plan_omnibus(p) if _is_wrapper(p)
                    else plan_repack(p, args.convert_nonjpeg))
        except Exception as e:
            plan = {'kind': 'repack', 'path': str(p), 'error': str(e)}
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
                out = (do_omnibus(p, args.convert_nonjpeg, work)
                       if plan['kind'] == 'omnibus'
                       else do_repack(p, args.convert_nonjpeg, work))
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
        write_redownload(sorted(Path(r['path']).stem for r in moved))
    return 1 if bad else 0


def _is_wrapper(path):
    """True when the archive holds whole comics instead of pages."""
    members = gen.list_members(path) or []
    return any(Path(m).suffix.lower() in {'.cbr', '.cbz', '.cb7'} for m in members)


def _print_plan(plan):
    p = Path(plan['path'])
    if 'error' in plan:
        print(f'  ERROR       {p.name}: {plan["error"]}')
        return
    if plan['kind'] == 'omnibus':
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
