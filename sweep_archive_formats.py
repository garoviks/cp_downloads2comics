#!/usr/bin/env python3
"""Find comics the library's own reader can open but QComicBook cannot.

Three defects, and a file can carry more than one:

  container   packed as 7z or tar while wearing a .cbr/.cbz name. Readable
              here, unopenable in QComicBook.
  pages       pages stored as something other than JPEG or PNG. WebP is the
              one that matters; avif, jxl, gif, bmp and tif are reported too
              because we may as well know.
  nested      the archive holds .cbr/.cbz/.cb7/.zip/.rar/.7z members. A
              wrapper around other comics, which no reader opens as a book.

Read-only. Converts nothing, moves nothing, writes only its own report.

The three answers of gen.list_members are kept apart throughout. A list is
evidence about the contents. An empty list is evidence there are no contents.
None is the absence of evidence — the file claims to be an archive and would
not open — and folding it into the empty case is exactly what produced the
false alarms this sweep exists to avoid.

Usage:  python3 sweep_archive_formats.py [library_root] [report_path]
"""
import json
import sys
import tarfile
import time
import zipfile
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / 'tests'))
import paths

gen = paths.load_generator()

ARCHIVE_EXTS = {'.cbr', '.cbz', '.cb7'}

# Containers QComicBook will not open, so a comic packed this way needs
# repacking as zip even though it reads perfectly well here.
REPACK_CONTAINERS = {'7z', 'tar'}

# Page formats every reader handles. Everything else in gen.PAGE_EXTS is a
# real image and a real page, and still worth flagging.
SAFE_PAGE_FORMATS = {'jpeg', 'png'}

# Four spellings of one format. Counting them separately would make a KissManga
# rip look like a mixed-format book when every page in it is a JPEG.
JPEG_EXTS = {'.jpg', '.jpeg', '.jpe', '.jfif'}

NESTED_EXTS = {'.cbr', '.cbz', '.cb7', '.zip', '.rar', '.7z'}

# Where the raw per-file findings are streamed as they are made. The walk takes
# hours, and losing all of it to a crash in the last minute would be silly; this
# also lets the report be rebuilt without re-reading 29k archives.
SCRATCH = Path('/tmp/archive_format_sweep.jsonl')


def detect_container(path: Path):
    """Which archive format this file actually is, read from its bytes.

    Same tests in the same order as gen.list_members, for the same reasons: a
    zip is settled by its central directory at the end, three magic numbers sit
    at or near the front, and tar's `ustar` mark is 257 bytes in so it can only
    be found by opening the file — which is why it goes last.

    Returns a format name, or None for a file that matches nothing we can name.
    The name is what the file *claims*; whether it opens is list_members' answer
    and is tracked separately.
    """
    try:
        if zipfile.is_zipfile(path):
            return 'zip'
        with open(path, 'rb') as f:
            head = f.read(len(gen.ACE_MAGIC) + 7)
        if head.startswith(gen.ZIP_MAGIC):
            # Opens as neither, yet starts as a zip: a damaged or truncated one.
            # Still a zip by intent, so it is not a repack candidate.
            return 'zip'
        if head.startswith(gen.RAR_MAGIC):
            return 'rar'
        if head.startswith(gen.SEVENZ_MAGIC):
            return '7z'
        if head[7:].startswith(gen.ACE_MAGIC):
            return 'ace'
        if tarfile.is_tarfile(path):
            return 'tar'
    except OSError:
        return None
    return None


def page_format(suffix: str) -> str:
    """The format a page extension denotes, with JPEG's four spellings merged."""
    return 'jpeg' if suffix in JPEG_EXTS else suffix.lstrip('.')


def inspect(path: Path) -> dict:
    """Everything this sweep wants to know about one file, in one read."""
    try:
        size = path.stat().st_size
    except OSError:
        size = 0
    container = detect_container(path)
    names = gen.list_members(path)

    if names is None:
        # It claims to be an archive and would not open. We know its container
        # only by its magic bytes and know nothing whatever about its contents,
        # so no page or nesting claim is made about it.
        return {'path': str(path), 'size': size, 'status': 'unreadable',
                'container': container or 'unknown', 'pages': 0,
                'formats': {}, 'nested': []}

    if not names and container is None:
        # Opened nothing because there was nothing to open: no format we can
        # name, so it is not an archive at all. Definite, not assumed.
        return {'path': str(path), 'size': size, 'status': 'not-an-archive',
                'container': 'not-an-archive', 'pages': 0,
                'formats': {}, 'nested': []}

    formats = Counter()
    nested = []
    for name in names:
        suffix = Path(name).suffix.lower()
        if suffix in gen.PAGE_EXTS:
            formats[page_format(suffix)] += 1
        elif suffix in NESTED_EXTS:
            nested.append(name)
    return {'path': str(path), 'size': size, 'status': 'read',
            'container': container or 'unknown', 'pages': sum(formats.values()),
            'formats': dict(formats), 'nested': nested}


def gb(n: int) -> float:
    return n / 1_000_000_000


def human_size(n: int) -> str:
    return f'{n / 1e9:.2f} GB' if n >= 1e9 else f'{n / 1e6:.0f} MB'


def table(rows, root: Path, limit: int = 50, extra: str = '') -> list:
    """A size-ordered markdown table of findings, capped so the report stays
    readable. The cap is stated in the caller's heading, never silently applied.

    `extra` names one optional middle column, whose per-row value each caller
    has already put in `_extra`.
    """
    if not rows:
        return ['_None._', '']
    cols = ['Size', 'Pages'] + ([extra] if extra else []) + ['Path']
    lines = ['| ' + ' | '.join(cols) + ' |',
             '|' + '|'.join(['---:', '---:'] + (['---'] if extra else []) + ['---']) + '|']
    for r in rows[:limit]:
        cells = [human_size(r['size']), str(r['pages'])]
        if extra:
            cells.append(str(r.get('_extra', '')))
        cells.append(f'`{Path(r["path"]).relative_to(root)}`')
        lines.append('| ' + ' | '.join(cells) + ' |')
    if len(rows) > limit:
        filler = ['…'] * (len(cols) - 1)
        lines.append('| ' + ' | '.join(
            filler + [f'_…and {len(rows) - limit} more, see the total above_']) + ' |')
    lines.append('')
    return lines


def totals(rows) -> str:
    return (f'{len(rows)} files, {gb(sum(r["size"] for r in rows)):.1f} GB, '
            f'{sum(r["pages"] for r in rows):,} pages')


def build_report(results, root: Path, report: Path, elapsed: float):
    by_size = lambda rows: sorted(rows, key=lambda r: -r['size'])

    read = [r for r in results if r['status'] == 'read']
    unreadable = [r for r in results if r['status'] == 'unreadable']
    not_archive = [r for r in results if r['status'] == 'not-an-archive']

    repack = by_size([r for r in read if r['container'] in REPACK_CONTAINERS])
    oddpages = by_size([r for r in read if r['formats']
                        and set(r['formats']) - SAFE_PAGE_FORMATS])
    nested = by_size([r for r in read if r['nested']])

    flagged = {r['path'] for r in repack} | {r['path'] for r in oddpages} \
        | {r['path'] for r in nested}
    affected = [r for r in results if r['path'] in flagged]

    containers = Counter(r['container'] for r in results)
    fmt_files = Counter()
    fmt_pages = Counter()
    for r in oddpages:
        for f, n in r['formats'].items():
            if f not in SAFE_PAGE_FORMATS:
                fmt_files[f] += 1
                fmt_pages[f] += n

    L = [f'# Library repack candidates',
         '',
         f'Read-only sweep of `{root}` — {len(results):,} archives, '
         f'{gb(sum(r["size"] for r in results)):.1f} GB, '
         f'{sum(r["pages"] for r in results):,} pages, '
         f'{elapsed / 60:.0f} minutes.',
         '',
         'Every comic in the library should open in QComicBook. These are the '
         'ones that will not, or may not. Nothing here has been changed.',
         '',
         '## How much work is this',
         '',
         '| Defect | Files | Size | Pages | Why it matters |',
         '|---|---:|---:|---:|---|',
         f'| 7z or tar container | {len(repack)} | {gb(sum(r["size"] for r in repack)):.1f} GB '
         f'| {sum(r["pages"] for r in repack):,} | QComicBook will not open these. Repack as zip. |',
         f'| Non-JPEG/PNG pages | {len(oddpages)} | {gb(sum(r["size"] for r in oddpages)):.1f} GB '
         f'| {sum(r["pages"] for r in oddpages):,} | WebP especially may not render. Re-encode pages. |',
         f'| Nested archives | {len(nested)} | {gb(sum(r["size"] for r in nested)):.1f} GB '
         f'| {sum(r["pages"] for r in nested):,} | A wrapper, not a book. Unpack one level. |',
         f'| **Distinct files affected** | **{len(affected)}** '
         f'| **{gb(sum(r["size"] for r in affected)):.1f} GB** '
         f'| **{sum(r["pages"] for r in affected):,}** | A file can carry more than one defect. |',
         '',
         f'That is {len(affected) / len(results) * 100:.2f}% of the library by count '
         f'and {sum(r["size"] for r in affected) / max(sum(r["size"] for r in results), 1) * 100:.2f}% by size.'
         if results else '',
         '',
         '## Container formats across the whole library',
         '',
         '| Container | Files | Size |',
         '|---|---:|---:|']
    for name, count in containers.most_common():
        size = sum(r['size'] for r in results if r['container'] == name)
        L.append(f'| {name} | {count:,} | {gb(size):.1f} GB |')
    L += ['',
          f'`unreadable` means the file claims to be an archive and would not open, '
          f'so nothing is asserted about what is inside it — that is not the same as '
          f'being empty. `not-an-archive` means no archive format was found at all, '
          f'which is a definite answer.',
          '']

    # ---- Class 1 -----------------------------------------------------------
    L += ['## 1. 7z and tar containers — repack as zip',
          '',
          f'**{totals(repack)}**',
          '']
    if repack:
        c = Counter(r['container'] for r in repack)
        L += ['| Format | Files |', '|---|---:|']
        L += [f'| {k} | {v} |' for k, v in c.most_common()]
        L.append('')
    for r in repack:
        r['_extra'] = r['container']
    L += [f'Largest first{f", top 50 of {len(repack)}" if len(repack) > 50 else ""}.', '']
    L += table(repack, root, extra='Container')

    # ---- Class 2 -----------------------------------------------------------
    L += ['## 2. Pages that are not JPEG or PNG',
          '',
          f'**{totals(oddpages)}**',
          '',
          'Broken down by the format found. A file with pages in two formats is '
          'counted under each, so these rows sum to more than the file count above.',
          '',
          '| Page format | Files | Pages in that format |',
          '|---|---:|---:|']
    for f, n in fmt_files.most_common():
        L.append(f'| {f} | {n} | {fmt_pages[f]:,} |')
    L.append('')
    for r in oddpages:
        r['_extra'] = ', '.join(sorted(set(r['formats']) - SAFE_PAGE_FORMATS))
    L += [f'Largest first{f", top 50 of {len(oddpages)}" if len(oddpages) > 50 else ""}.', '']
    L += table(oddpages, root, extra='Page formats')

    # ---- Class 3 -----------------------------------------------------------
    L += ['## 3. Nested archives — a wrapper, not a book',
          '',
          f'**{totals(nested)}**',
          '',
          'These hold other comic archives as members. A reader opening one sees '
          'no pages. Note the page count column: where it is 0 the file is purely '
          'a wrapper, and where it is not the archive is a mixture.',
          '']
    for r in nested:
        r['_extra'] = str(len(r['nested']))
    L += [f'Largest first{f", top 50 of {len(nested)}" if len(nested) > 50 else ""}.', '']
    L += table(nested, root, extra='Archive members')
    if nested:
        L += ['### What the largest wrappers contain', '']
        for r in nested[:10]:
            L.append(f'- `{Path(r["path"]).relative_to(root)}` — '
                     f'{len(r["nested"])} archive members, {r["pages"]} loose pages')
            for name in sorted(r['nested'])[:8]:
                L.append(f'  - `{name}`')
            if len(r['nested']) > 8:
                L.append(f'  - _…and {len(r["nested"]) - 8} more_')
        L.append('')

    # ---- Context -----------------------------------------------------------
    L += ['## Not repack candidates, but worth knowing',
          '',
          f'### {len(unreadable)} unreadable',
          '',
          'These claim to be archives and would not open. Nothing is claimed '
          'about their contents. They are a separate problem from repacking.',
          '']
    L += table(by_size(unreadable), root, limit=50)
    L += [f'### {len(not_archive)} not archives at all', '',
          'No archive format found. Definitely holds no comic.', '']
    L += table(by_size(not_archive), root, limit=50)

    report.write_text('\n'.join(L) + '\n')


def main():
    root = Path(sys.argv[1] if len(sys.argv) > 1 else '/mnt/extramedia/Comics')
    report = Path(sys.argv[2] if len(sys.argv) > 2
                  else Path(__file__).resolve().parent / 'LIBRARY_REPACK_CANDIDATES.md')

    files = sorted(p for p in root.rglob('*')
                   if p.is_file() and p.suffix.lower() in ARCHIVE_EXTS)
    total = len(files)
    print(f'{total} archives under {root}', flush=True)

    results = []
    started = time.time()
    with SCRATCH.open('w') as scratch:
        for i, p in enumerate(files, 1):
            r = inspect(p)
            results.append(r)
            scratch.write(json.dumps(r) + '\n')
            # The cache is per-path and this walk never revisits one, so it
            # would only ever grow for the length of the run.
            gen._PAGE_COUNTS.clear()
            if i % 500 == 0:
                scratch.flush()
                rate = i / (time.time() - started)
                n7z = sum(1 for x in results if x['container'] in REPACK_CONTAINERS)
                nodd = sum(1 for x in results if x['formats']
                           and set(x['formats']) - SAFE_PAGE_FORMATS)
                nnest = sum(1 for x in results if x['nested'])
                print(f'{i}/{total}  {rate:.1f}/s  eta {(total - i) / rate / 60:.0f}m  '
                      f'repack={n7z} oddpages={nodd} nested={nnest}', flush=True)

    elapsed = time.time() - started
    build_report(results, root, report, elapsed)
    print(f'\ndone in {elapsed / 60:.0f}m -> {report}', flush=True)


if __name__ == '__main__':
    main()
