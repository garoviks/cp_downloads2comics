#!/usr/bin/env python3
"""Snapshot what the Volume Builder sees, so migration step 6 can be verified.

Step 6 switches the Builder's series derivation to `parse_release()`. The series
string it derives is load-bearing three times over: it is the GROUPING KEY that
decides which loose issues count as one run, it becomes the proposed output
volume's FILENAME, and `/api/create` deletes the source issues after merging. So
"it still starts" is not the bar. The bar is a before/after diff of every group
the Builder would show you.

WHY IT IMPORTS THE REAL MODULE. §10.3 records two harness bugs of mine that each
produced a confident, wrong number, and both had the same cause: the harness
re-implemented part of the code path instead of calling it. This one calls
`scan_root()` itself, so there is nothing to get subtly out of step.

WHY IT IS STILL READ-ONLY. `scan_root()` is not: at :593 it calls
`write_exclusions()` to persist the skipped-folder list, rewriting
`.comic_exclusions.md` in your library whenever that set changes. That is correct
for the app and unacceptable for a measurement, so the function is replaced with
a recording no-op for the duration. The snapshot reports whether the real app
WOULD have written, which is itself worth knowing, without doing it.

Importing the module is safe: `comic_volume_creator_server.py` guards its server
behind `if __name__ == '__main__'` and touches no filesystem at import.

WHAT IS CAPTURED, and what is deliberately not. Sizes and mtimes are excluded —
they change on their own and would bury the signal in noise. `invisible` is
captured even though the UI never shows it, because the verification for step 6
is "visible-file count before/after" and a file going missing is the exact
failure mode: `is_numbered_issue()` returns False and the file silently ceases
to exist as far as the Builder is concerned.

Run:  python3 builder_scan_snapshot.py before.json
      python3 builder_scan_snapshot.py after.json
      python3 builder_scan_snapshot.py --diff before.json after.json
"""
import importlib.util
import json
import os
import sys

BUILDER = '/home/nesha/scripts/comic_volume_creator/comic_volume_creator_server.py'


def load_builder():
    spec = importlib.util.spec_from_file_location('cvc_server', BUILDER)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def snapshot(mod):
    """Run the Builder's own scan, with its one write neutralised."""
    would_have_written = []

    def no_write(root_path, always, temp, skipped=None):
        would_have_written.append({'root': root_path, 'skipped': list(skipped or [])})

    real_write = mod.write_exclusions
    mod.write_exclusions = no_write
    try:
        results, skipped, exclusions = mod.scan_root(mod.ALLOWED_ROOT)
    finally:
        mod.write_exclusions = real_write

    rows = [{
        'folder':  r['folder'],
        'series':  r['series'],
        'outname': r['outname'],
        'flag':    r['flag'],
        'status':  r['status'],
        'files':   r['files'],
    } for r in results]
    rows.sort(key=lambda r: (r['folder'], r['series']))

    # Every comic the Builder walked past but did NOT group, and why. Recomputed
    # over the same folders scan_root() actually processed, so the two halves of
    # the snapshot cannot disagree about which folders were in scope.
    invisible = {}
    for folder in sorted({r['folder'] for r in results} | _processed_folders(mod)):
        hidden = []
        try:
            entries = [e.name for e in os.scandir(folder) if e.is_file()]
        except OSError:
            continue
        for name in sorted(entries):
            if os.path.splitext(name)[1].lower() not in mod.COMIC_EXTS:
                continue
            if not mod.is_numbered_issue(name):
                hidden.append({'file': name,
                               'is_volume': mod.is_volume(name)})
        if hidden:
            invisible[folder] = hidden

    return {
        'rows': rows,
        'skipped': sorted(s['path'] for s in skipped),
        'invisible': invisible,
        'totals': {
            'groups': len(rows),
            'grouped_files': sum(len(r['files']) for r in rows),
            'invisible_files': sum(len(v) for v in invisible.values()),
            'folders_with_groups': len({r['folder'] for r in rows}),
            'skipped_folders': len(skipped),
            'exclusions_rewrite_suppressed': len(would_have_written),
        },
    }


def _processed_folders(mod):
    """The folders scan_root() would call process() on: the root if it has no
    subdirs, plus every non-excluded top-level folder that has no sub-subdirs.
    Mirrors scan_root():561-579 so 'invisible' covers folders that produced no
    group at all — which is precisely where a vanished file would hide."""
    root = mod.ALLOWED_ROOT
    exclusions = mod.read_exclusions(root)
    blocked = {p.strip() for p in exclusions['always']} | {p.strip() for p in exclusions['temp']}
    folders = set()
    if not mod.has_subdirs(root):
        folders.add(root)
    try:
        for entry in os.scandir(root):
            if not entry.is_dir() or entry.path.strip() in blocked:
                continue
            if not mod.has_subdirs(entry.path):
                folders.add(entry.path)
    except OSError:
        pass
    return folders


def diff(before, after):
    b = {(r['folder'], r['series']): r for r in before['rows']}
    a = {(r['folder'], r['series']): r for r in after['rows']}

    print('=== TOTALS ===')
    for k in before['totals']:
        bv, av = before['totals'][k], after['totals'].get(k)
        mark = '' if bv == av else '   <-- CHANGED'
        print(f'  {k:34} {bv:>7} -> {av:>7}{mark}')

    gone, new = sorted(set(b) - set(a)), sorted(set(a) - set(b))
    print(f'\n=== GROUPS THAT DISAPPEARED: {len(gone)} ===')
    for k in gone:
        print(f'  {k[0]}\n     series {k[1]!r}  {len(b[k]["files"])} files  {b[k]["status"]}')
    print(f'\n=== GROUPS THAT APPEARED: {len(new)} ===')
    for k in new:
        print(f'  {k[0]}\n     series {k[1]!r}  {len(a[k]["files"])} files  {a[k]["status"]}')

    changed = [k for k in sorted(set(b) & set(a)) if b[k] != a[k]]
    print(f'\n=== GROUPS THAT CHANGED: {len(changed)} ===')
    for k in changed:
        print(f'  {k[0]}  ({k[1]!r})')
        for f in ('outname', 'flag', 'status'):
            if b[k][f] != a[k][f]:
                print(f'     {f}: {b[k][f]!r} -> {a[k][f]!r}')
        if b[k]['files'] != a[k]['files']:
            lost = set(b[k]['files']) - set(a[k]['files'])
            got = set(a[k]['files']) - set(b[k]['files'])
            if lost:
                print(f'     lost {len(lost)}: {sorted(lost)[:3]}')
            if got:
                print(f'     gained {len(got)}: {sorted(got)[:3]}')

    # THE headline number for step 6. A file that was grouped and now is not has
    # vanished from the UI; that is the regression the step must not ship.
    bf = {(r['folder'], f) for r in before['rows'] for f in r['files']}
    af = {(r['folder'], f) for r in after['rows'] for f in r['files']}
    vanished, arrived = sorted(bf - af), sorted(af - bf)
    print(f'\n{"=" * 72}\nFILES VISIBLE BEFORE BUT NOT AFTER: {len(vanished)}')
    for folder, f in vanished[:40]:
        print(f'   {f}\n      in {folder}')
    if len(vanished) > 40:
        print(f'   ... and {len(vanished) - 40} more')
    print(f'\nFILES VISIBLE AFTER BUT NOT BEFORE: {len(arrived)}')
    for folder, f in arrived[:40]:
        print(f'   {f}\n      in {folder}')
    return 1 if vanished else 0


def main():
    if '--diff' in sys.argv:
        i = sys.argv.index('--diff')
        with open(sys.argv[i + 1]) as f:
            before = json.load(f)
        with open(sys.argv[i + 2]) as f:
            after = json.load(f)
        return diff(before, after)

    out = sys.argv[1] if len(sys.argv) > 1 else 'builder_snapshot.json'
    mod = load_builder()
    if not os.path.isdir(mod.ALLOWED_ROOT):
        print(f'library not mounted at {mod.ALLOWED_ROOT}')
        return 0
    snap = snapshot(mod)
    with open(out, 'w') as f:
        json.dump(snap, f, indent=1, sort_keys=True)
    print(f'wrote {out}')
    for k, v in snap['totals'].items():
        print(f'  {k:34} {v}')
    if snap['totals']['exclusions_rewrite_suppressed']:
        print('\n  NOTE: the real app would have rewritten .comic_exclusions.md on this\n'
              '  scan. Suppressed — nothing was written.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
