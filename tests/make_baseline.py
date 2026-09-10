#!/usr/bin/env python3
"""Regenerate the whole-library key baseline.

The baseline records, for every base-level item in the library, the series key the
current code derives for it. test_series_naming.py then asserts that a change never
causes two items with *different* baseline keys to share a key — i.e. never merges two
distinct series, which is what silently moves files into the wrong folder.

Splitting is allowed and expected: repairing a corrupted key makes it split away from
whatever it was wrongly grouped with.

Run this ONLY to establish a new intentional baseline, never to paper over a failure:

    python3 tests/make_baseline.py
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import paths


def main():
    if not os.path.isdir(paths.LIBRARY_ROOT):
        sys.exit(f'Library not mounted: {paths.LIBRARY_ROOT}')

    gen = paths.load_generator()
    items = paths.library_items()
    keys = {name: gen.extract_series_name(name) for name in items}

    payload = {
        'library_root': paths.LIBRARY_ROOT,
        'item_count': len(items),
        'distinct_keys': len(set(keys.values())),
        'keys': keys,
    }
    with open(paths.BASELINE_FILE, 'w', encoding='utf-8') as f:
        json.dump(payload, f, indent=1, ensure_ascii=False, sort_keys=True)
        f.write('\n')

    print(f'{len(items)} items, {payload["distinct_keys"]} distinct keys')
    print(f'written to {paths.BASELINE_FILE}')


if __name__ == '__main__':
    main()
