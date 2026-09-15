#!/usr/bin/env python3
"""Report comics that appear more than once in the library.

Two files are candidates for the same book when they parse to the same series,
volume, issue and kind. That is the same rule the Organiser uses to warn about an
incoming download, applied to the library against itself.

That key is too generous to act on by itself — duplicates.py explains why and holds
the checks that decide it. This module is the report around them: walk the library,
group, split the groups into the ones worth acting on and the ones worth reading,
and write it down.

Nothing here deletes or moves anything. It writes a markdown file.

Usage:  python3 library_duplicates.py [--dest DIR] [--out FILE]
"""
import argparse
from collections import defaultdict
from pathlib import Path

import duplicates
import matching_analysis_generator as g
import release

COMIC_EXTS = duplicates.COMIC_EXTS


def scan(dest_dir: Path):
    groups = defaultdict(list)
    total = 0
    for path in dest_dir.rglob('*'):
        if path.is_file() and path.suffix.lower() in COMIC_EXTS:
            total += 1
            key = duplicates.book_key(path.name, g.normalize_name(
                release.parse_release(path.name).series))
            groups[key].append(path)
    return total, {k: v for k, v in groups.items() if len(v) > 1}


def human(n: int) -> str:
    return f'{n / 1e9:.2f} GB' if n >= 1e9 else f'{n / 1e6:.0f} MB'


def render_group(key, files, dest_dir) -> str:
    series, volume, issue, _range, kind = key
    label = series or '(no series)'
    if volume is not None:
        label += f' — v{volume:g}'
    if issue:
        label += f' — #{issue}'
    sized = sorted(((f.stat().st_size, f) for f in files), reverse=True)
    # Two rips of one book by different packers never come out the same length,
    # so an exact match means one file filed in two places rather than a judgement
    # call. Said out loud because it is the difference between reading the names
    # and not having to.
    if len({s for s, _ in sized}) == 1:
        label += '  — identical size'
    lines = [f'### {label}  *({kind})*', '']
    for size, f in sized:
        lines.append(f'- `{human(size):>8}`  {f.relative_to(dest_dir)}')
    lines.append('')
    return '\n'.join(lines)


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--dest', default='/mnt/extramedia/Comics')
    ap.add_argument('--out', default='LIBRARY_DUPLICATES.md')
    args = ap.parse_args()

    dest_dir = Path(args.dest)
    print(f'Scanning {dest_dir} ...')
    total, dupes = scan(dest_dir)

    likely, review = {}, {}
    for key, files in dupes.items():
        one_book = duplicates.looks_like_one_book(
            [f.relative_to(dest_dir) for f in files])
        (likely if one_book else review)[key] = files

    def reclaim(d):
        return sum(sum(f.stat().st_size for f in sorted(v, key=lambda p: -p.stat().st_size)[1:])
                   for v in d.values())

    out = [
        '# Duplicate comics in the library',
        '',
        f'- Library: `{dest_dir}`',
        f'- Comic files scanned: **{total:,}**',
        f'- Groups where one book appears more than once: **{len(dupes):,}**',
        f'- Extra copies: **{sum(len(v) - 1 for v in dupes.values()):,}**',
        '',
        '## How a duplicate was decided',
        '',
        'Two files are the same book when they parse to the same series, volume, issue',
        'and kind. Year and packer tags are ignored, so `(2014)` and `(2016)`, or',
        '`(digital-Empire)` and `(DR & Quinch-Empire)`, are treated as the same book —',
        'which is the case this report exists to find. Sizes differ between packers and',
        'are shown so you can judge, not used to decide. Where every copy is the same',
        'length the heading says so: that is one file filed in two folders, not a',
        'judgement call.',
        '',
        'Read a heading with no `v` and no `#` more carefully. It means the parser found',
        'a series name and nothing else, so `Strange Adventures (2000)` and',
        '`Strange Adventures (DC 2022)` — different series two decades apart — land in',
        'one group. The years in the filenames are the giveaway.',
        '',
        '**Nothing here has been deleted or moved.** Regenerate with',
        '`python3 library_duplicates.py`.',
        '',
        '---',
        '',
        f'## Likely duplicates — {len(likely):,} groups, {human(reclaim(likely))} recoverable',
        '',
        'Every file in these groups agrees on everything the parser discarded: issue',
        'numbers, subtitles, whether it is a variant or cover-only scan, and any volume',
        'number claimed by the folders above it. That leaves only the year and the',
        "packer's tag to tell the copies apart. The largest copy is listed first.",
        '',
    ]
    for key, files in sorted(likely.items(),
                             key=lambda kv: -sum(f.stat().st_size for f in kv[1])):
        out.append(render_group(key, files, dest_dir))

    out += [
        '---',
        '',
        f'## Check these by hand — {len(review):,} groups, {human(reclaim(review))}',
        '',
        'Something here disagrees that the parser could not see: an issue number, a',
        'subtitle, a `(Cover ONLY)` tag, or a folder claiming a different volume. That',
        'usually means these are **different books that parse to the same key**, not',
        'duplicates — `Terra Obscura Volume 1/#003` and `Volume 2/#003`, or',
        '`Starhenge Book Two ... 01` and `... 03`. Read the names before touching',
        'anything.',
        '',
    ]
    for key, files in sorted(review.items(),
                             key=lambda kv: -sum(f.stat().st_size for f in kv[1])):
        out.append(render_group(key, files, dest_dir))

    Path(args.out).write_text('\n'.join(out), encoding='utf-8')
    print(f'likely duplicates : {len(likely):,} groups, {human(reclaim(likely))}')
    print(f'needs a look      : {len(review):,} groups, {human(reclaim(review))}')
    print(f'written to        : {args.out}')


if __name__ == '__main__':
    main()
