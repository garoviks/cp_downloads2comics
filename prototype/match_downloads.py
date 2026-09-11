#!/usr/bin/env python3
"""Run the LIVE matcher and the PROTOTYPE resolver over the real download folder.

Read-only: opens nothing, moves nothing, writes nothing.

compare.py already answered "does the prototype merge distinct series" across the
whole library. This answers the different question the library cannot: given the
files actually waiting to be filed, where does each one GO, and do the two
implementations disagree about it?

It also tests the two rules settled in COMIC_TOOLS_ARCHITECTURE.md 8.4 against
real data rather than invented examples:

  Q2  arcs go to the most specific EXISTING folder, else the parent
  Q3  publisher/anthology containers may receive files; creator/event ones may not

FAIRNESS. The first version of this script built the prototype's library from
top-level folder names only, while live's find_exact_match() accepts a match
against a folder *or* a loose file in the library root. That made the prototype
look 20 matches worse than it is. Both sides now resolve against exactly the
same universe: every dest_map key that live itself would accept.

The destination scan walks 43k items, so it is cached in /tmp. Delete the cache
or pass --rescan after the library changes.

NOTE: "the prototype" here is now `../release.py`. This script keeps comparing it
against live's own derivation, which is exactly what migration step 5 is replacing —
so it stays useful until the generator has fully switched over, and becomes a
live-vs-live tautology afterwards.

Run:  python3 match_downloads.py [--rescan]
"""
import collections
import os
import pickle
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
sys.path.insert(0, HERE)

import matching_analysis_generator as live      # noqa: E402
import release as proto                        # noqa: E402

CACHE = '/tmp/comic_dest_map.pickle'

# Containers that may NOT receive auto-filed comics (Q3). Publisher shelves and
# anthologies are deliberately absent — routing into those is requirement O6.
CREATOR_OR_EVENT = {
    'Mark Millar',
    'Jodorowsky and Moebius',
    'Neil Gaiman Library',
    'Civil War II (Story Arc) (2016-2017)',
}


def dest_map(rescan=False):
    if not rescan and os.path.exists(CACHE):
        with open(CACHE, 'rb') as f:
            return pickle.load(f)
    dm = live.scan_destination_directory()
    with open(CACHE, 'wb') as f:
        pickle.dump(dm, f)
    return dm


def main():
    if not live.SRC_DIR.is_dir():
        print(f'no download folder at {live.SRC_DIR}')
        return 0
    if not live.DEST_DIR.is_dir():
        print(f'library not mounted at {live.DEST_DIR}')
        return 0

    files = sorted(f.name for f in live.SRC_DIR.iterdir()
                   if f.is_file() and f.suffix.lower() in live.COMIC_EXTS)

    dm = dest_map('--rescan' in sys.argv)

    # The universe live matches against: a dest entry counts only if it has a
    # real folder or a loose file in the base dir (find_exact_match:604).
    matchable = {k: v for k, v in dm.items()
                 if v.get('folders') or v.get('loose_files')}

    # SELF-CONSISTENCY. The prototype must derive the library key set with its
    # OWN parser, from the real folder and file names — not from live's keys.
    # Reusing live's keys mixes normalisers and manufactures fake disagreements:
    # live corrupts the loose file 'Giant Robot Hellboy Returns 01.cbr' to
    # 'Robot Hellboy Returns' on BOTH sides so it matches itself, while the
    # prototype reads the incoming file correctly and then finds no such key.
    # That is the harness being wrong, not the parser.
    # A FOLDER indexes under its full name only. The folder name is a deliberate
    # choice by the user, so 'Ghost Machine - The Official Guidebook' must not
    # also answer to 'Ghost Machine' — an unrelated 'Ghost Machine 001' would be
    # swept into the guidebook.
    #
    # A LOOSE FILE indexes under every candidate, because no folder exists yet and
    # grouping is the whole point: the loose
    # 'Cindy and Biscuit - We Love Trouble.cbz' has to be findable as
    # 'Cindy and Biscuit' so an incoming issue can join it.
    proto_keys, key_to_real = set(), {}

    def index(real, keys, is_folder):
        for nk in keys:
            if not nk:
                continue
            proto_keys.add(nk)
            if nk not in key_to_real or is_folder:
                key_to_real[nk] = real

    for entry in matchable.values():
        for real in entry.get('folders', []):
            index(real, [proto.normalize(proto.parse_release(real).series)], True)
        for real in entry.get('loose_files', []):
            cands = proto.parse_release(real).series_candidates
            index(real, [proto.normalize(c) for c in cands], False)

    print(f'{len(files)} comic files in {live.SRC_DIR}')
    print(f'{len(dm)} dest series keys, {len(matchable)} matchable '
          f'(have a folder or a loose file)')
    print(f'prototype library keys, self-derived: {len(proto_keys)}\n')

    rows = []
    for name in files:
        stem = os.path.splitext(name)[0]
        live_series = live.extract_series_name(stem)
        matched_key, _data, how = live.find_matches(name, live_series, dm)

        chosen, ok = proto.resolve(name, proto_keys)
        proto_key = key_to_real.get(proto.normalize(chosen)) if ok else None
        # Compare on the SERIES each side settled on, not on the display name:
        # live reports a series key while the prototype reports the real folder
        # or loose file it landed on, so comparing those directly invents
        # disagreements that are only formatting.
        rows.append((name, live_series, matched_key, how,
                     chosen if ok else None, proto_key))

    hows = collections.Counter(r[3] for r in rows)
    print('LIVE match type:')
    for h, n in hows.most_common():
        print(f'  {n:4}  {h}')

    live_hit = sum(1 for r in rows if r[2])
    proto_hit = sum(1 for r in rows if r[5])
    print(f'\nmatched to an existing series — live {live_hit}, prototype {proto_hit}')

    same = [r for r in rows if r_eq(r[2], r[4])]
    print(f'agree on the series: {len(same)} of {len(rows)}')

    diff = [r for r in rows if not r_eq(r[2], r[4])]
    print(f'\n{"=" * 72}\nDISAGREEMENTS: {len(diff)}\n{"=" * 72}')
    for name, ls, lk, how, ps, pk in diff:
        print(f'\n  {name[:68]}')
        print(f'     live       series {lk!r} via {how}')
        print(f'     prototype  series {ps!r}')
        print(f'                lands on {pk!r}')

    bad = [r for r in rows if r[2] in CREATOR_OR_EVENT or r[5] in CREATOR_OR_EVENT]
    print(f'\n{"=" * 72}\nQ3 — routed into a creator/event container: {len(bad)}')
    for name, ls, lk, how, ps, pk in bad:
        print(f'   {name[:60]}\n      live {lk!r} / proto {pk!r}')

    print(f'\n{"=" * 72}\nQ2 — releases with an arc separator:')
    for name, ls, lk, how, ps, pk in rows:
        if ' - ' in os.path.splitext(name)[0].split('(')[0]:
            flag = '' if r_eq(lk, ps) else '   <-- DIFFERS'
            print(f'   {name[:58]}\n      live {lk!r} / proto {pk!r}{flag}')

    return 0


def r_eq(a, b):
    return live.normalize_name(a or '') == live.normalize_name(b or '')


if __name__ == '__main__':
    sys.exit(main())
