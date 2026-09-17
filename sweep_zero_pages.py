#!/usr/bin/env python3
"""Find files in the library that are not comics, by counting the pages inside them.

Zero pages means the archive opened and held no images. That is how the 238 MB
`429 Too Many Requests` HTML page wearing a .cbr extension looked from the
outside, and nothing else in the pipeline would ever have noticed it.

Read-only. Writes a report and touches nothing.

Usage:  python3 sweep_zero_pages.py [library_root] [report_path]
"""
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / 'tests'))
import paths

gen = paths.load_generator()

ARCHIVE_EXTS = {'.cbr', '.cbz', '.cb7'}


def main():
    root = Path(sys.argv[1] if len(sys.argv) > 1 else '/mnt/extramedia/Comics')
    report = Path(sys.argv[2] if len(sys.argv) > 2 else '/tmp/zero_page_sweep.txt')

    files = sorted(p for p in root.rglob('*')
                   if p.is_file() and p.suffix.lower() in ARCHIVE_EXTS)
    total = len(files)
    print(f'{total} archives under {root}', flush=True)

    empty, unreadable, ok = [], [], 0
    started = time.time()
    for i, p in enumerate(files, 1):
        try:
            n = gen.page_count(p)
            size = p.stat().st_size
        except OSError:
            unreadable.append((p, 0))
            continue
        if n is None:
            unreadable.append((p, size))
        elif n == 0:
            empty.append((p, size))
        else:
            ok += 1
        # The cache is per-path and this walk never revisits one, so it would
        # only grow for the length of the run.
        gen._PAGE_COUNTS.clear()
        if i % 500 == 0:
            rate = i / (time.time() - started)
            print(f'{i}/{total}  {rate:.0f}/s  eta {(total - i) / rate / 60:.0f}m  '
                  f'empty={len(empty)} unreadable={len(unreadable)}', flush=True)

    lines = [f'Zero-page sweep of {root}',
             f'{total} archives, {ok} hold images',
             '',
             f'=== {len(empty)} opened fine but hold no images ===']
    for p, size in sorted(empty, key=lambda x: -x[1]):
        lines.append(f'{size / 1048576:9.0f} MB  {p.relative_to(root)}')
    lines += ['', f'=== {len(unreadable)} could not be read ===']
    for p, size in sorted(unreadable, key=lambda x: -x[1]):
        lines.append(f'{size / 1048576:9.0f} MB  {p.relative_to(root)}')

    report.write_text('\n'.join(lines) + '\n')
    print(f'\ndone in {(time.time() - started) / 60:.0f}m: '
          f'{len(empty)} empty, {len(unreadable)} unreadable -> {report}', flush=True)


if __name__ == '__main__':
    main()
