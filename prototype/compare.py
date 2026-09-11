#!/usr/bin/env python3
"""Compare the parse_release() prototype against the live derivation, over the
whole real library. Read-only: opens nothing, moves nothing, writes nothing.

The question this answers is NOT "are they identical" — they are deliberately
not. It is the Phase 1 safety question:

    Does any pair of series that are DISTINCT today MERGE under the prototype?

Splitting is safe (it is un-corruption). Merging silently files comics into the
wrong folder, so a single merge is a blocker.

NOTE: what this calls "the prototype" is now `../release.py` — promoted after this
script reported a clean verdict. It is kept, unrenamed, because it is the evidence
that promotion rested on and must still reproduce that verdict on demand.

Run:  python3 compare.py
"""
import collections
import re
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
sys.path.insert(0, HERE)

import matching_analysis_generator as live      # noqa: E402
import release as proto                        # noqa: E402

ROOT = '/mnt/extramedia/Comics'
EXTS = {'.cbz', '.cbr', '.zip', '.rar'}


def collect():
    files, folders = [], []
    for e in os.scandir(ROOT):
        if e.is_file() and os.path.splitext(e.name)[1].lower() in EXTS:
            files.append(e.name)
        elif e.is_dir():
            folders.append(e.name)
            try:
                for f in os.listdir(e.path):
                    if os.path.splitext(f)[1].lower() in EXTS:
                        files.append(f)
            except OSError:
                pass
    return files, folders


def main():
    if not os.path.isdir(ROOT):
        print(f'library not mounted at {ROOT} — nothing to compare')
        return 0

    files, folders = collect()
    print(f'library: {len(files)} comic files, {len(folders)} top-level folders\n')

    # Library key set the prototype resolves against, derived by the prototype
    # itself so both sides are self-consistent.
    lib_keys = {proto.normalize(proto.parse_release(f + '.cbz').series)
                for f in folders}
    # Real folder names under the live normaliser, for judging merges below.
    folder_keys = {live.normalize_name(live.extract_folder_series_name(f))
                   for f in folders}

    # Both sides go through the SAME normaliser (the live one). Otherwise we
    # would be measuring two things at once: live's normalize_name strips
    # leading articles and apostrophes, so "cult of the lamb" vs "cult of lamb"
    # would register as a conflict when only the derivation is under test.
    live_of, proto_of = {}, {}
    for name in files:
        stem = os.path.splitext(name)[0]
        live_of[name] = live.normalize_name(live.extract_series_name(stem))
        chosen, _ = proto.resolve(name, lib_keys)
        proto_of[name] = live.normalize_name(chosen)

    # ---- the invariant --------------------------------------------------
    live2proto = collections.defaultdict(set)
    proto2live = collections.defaultdict(set)
    for name in files:
        a, b = live_of[name], proto_of[name]
        if not a or not b:
            continue
        live2proto[a].add(b)
        proto2live[b].add(a)

    raw_merges = {k: v for k, v in proto2live.items() if len(v) > 1}
    splits = {k: v for k, v in live2proto.items() if len(v) > 1}

    print(f'distinct series keys  live: {len(live2proto)}   prototype: {len(proto2live)}')
    print(f'splits  (same today -> distinct under prototype): {len(splits)}')

    # A raw merge is only DANGEROUS if the live keys were genuinely different
    # series. Most are not: live fails to strip issue numbers, so it invents one
    # key per issue ('2000ad prog 0001', '0002', ...). Collapsing those is the
    # prototype being right, not a regression.
    def stem(k):
        k = re.sub(r'\b\d+\b', ' ', k)               # drop bare numbers
        return ' '.join(k.split())

    buckets = collections.Counter()
    dangerous = {}
    for k, v in raw_merges.items():
        stems = {stem(x) for x in v}
        # The decisive test: is the prototype's key a WORD-PREFIX of every live
        # key it absorbs? If so the prototype only truncated at a common point —
        # 'brass sun' <- 'brass sun diamond age', 'brass sun engine summer' are
        # volume subtitles of one series, not two series. Only when the live keys
        # diverge BEFORE the prototype's key is anything genuinely conflated.
        kw = k.split()
        prefix_of_all = all(x.split()[:len(kw)] == kw for x in v)
        # The other direction: the prototype's key is LONGER than a live key and
        # names a folder that really exists. That is not conflation — it is the
        # prototype telling apart two folders live conflates. Real example:
        # 'Die' and 'Die - Loaded' both exist; live derives 'die' for
        # 'Die - Loaded v01', filing a spin-off into the parent.
        more_precise = k in folder_keys and any(k.startswith(x + ' ') for x in v)
        if len(stems) == 1:
            buckets['live over-split by issue/volume number'] += 1
        elif len({re.sub(r'[^a-z0-9]', '', x) for x in v}) == 1:
            buckets['punctuation/diacritics only'] += 1
        elif more_precise:
            buckets['prototype MORE precise — real folder live conflates'] += 1
        elif prefix_of_all:
            buckets['volume/arc subtitle collapsed into parent (Q2)'] += 1
        else:
            buckets['DANGEROUS — genuinely different series'] += 1
            dangerous[k] = v

    print(f'\nraw merges: {len(raw_merges)} — classified:')
    for c, n in buckets.most_common():
        print(f'  {n:6}  {c}')

    if dangerous:
        print('\n!! DANGEROUS merges — these would file different series together:')
        for k, v in sorted(dangerous.items())[:30]:
            print(f'   {k!r:38} <- {sorted(v)[:6]}')
    merges = dangerous

    # ---- categorise the disagreements ----------------------------------
    changed = [n for n in files if live_of[n] != proto_of[n]]
    print(f'\nfiles whose key changes: {len(changed)} of {len(files)} '
          f'({100 * len(changed) / len(files):.1f}%)')

    cats = collections.Counter()
    samples = collections.defaultdict(list)
    for n in changed:
        a, b = live_of[n], proto_of[n]
        if not a:
            c = 'live produced nothing'
        elif b.startswith(a + ' ') or b == a:
            c = 'prototype keeps MORE of the title (un-truncation)'
        elif a.startswith(b + ' '):
            c = 'prototype keeps LESS (trims trailing metadata live kept)'
        elif a.replace(' ', '') == b.replace(' ', ''):
            c = 'whitespace only'
        else:
            c = 'genuinely different'
        cats[c] += 1
        if len(samples[c]) < 6:
            samples[c].append((n, a, b))

    print()
    for c, n in cats.most_common():
        print(f'  {n:6}  {c}')
    for c, _ in cats.most_common():
        print(f'\n-- {c} --')
        for n, a, b in samples[c]:
            print(f'   {n[:56]}\n       live      {a!r}\n       prototype {b!r}')

    print('\n' + '=' * 70)
    print('VERDICT:', 'BLOCKER — merges present' if merges
          else 'safe on the merge invariant (splits only)')
    return 1 if merges else 0


if __name__ == '__main__':
    sys.exit(main())
