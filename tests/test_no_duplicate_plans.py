#!/usr/bin/env python3
"""Every source file must be planned exactly once.

The CSV is a move plan, and the mover executes it row by row without checking
whether two rows name the same file. So a file appearing twice is not a cosmetic
duplicate — it is two moves of one file to two destinations. Whichever runs first
wins and the second fails with "Source not found", leaving an empty folder behind
under the name that lost.

This shipped. A real run planned the three Nameless Kingdom volumes both as a
folder op and as three standalone files, and the library ended up with an empty
/The Nameless Kingdom/ next to the populated folder that actually got them.

Cause: STEP 1 recorded processed files by bare name while STEP 2 identifies them
by path relative to the source directory. The two forms coincide for a loose
file, so the de-duplication appeared to work everywhere except the one case it
existed for.

Run:  python3 -m unittest discover tests
"""
import csv
import io
import os
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import paths

gen = paths.load_generator()


def plan(tree):
    """Build `tree` under a temp source dir, run the generator, return CSV rows.

    `tree` maps a path relative to the source directory to its file content.
    The destination is an empty temp directory, so every row is a create/copy —
    which is what we want: the question here is how many rows a file gets, not
    where it goes.
    """
    with tempfile.TemporaryDirectory() as src, tempfile.TemporaryDirectory() as dest:
        for rel in tree:
            p = Path(src) / rel
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_bytes(b'x')

        argv, sd, dd, out = sys.argv, gen.SRC_DIR, gen.DEST_DIR, gen.OUTPUT_FILE
        sys.argv = ['gen', '--src', src, '--dest', dest]
        try:
            with redirect_stdout(io.StringIO()):
                gen.main()
            with open(Path(src) / 'matching_analysis_consolidated.csv',
                      newline='', encoding='utf-8') as f:
                return list(csv.DictReader(f))
        finally:
            sys.argv = argv
            gen.SRC_DIR, gen.DEST_DIR, gen.OUTPUT_FILE = sd, dd, out


def planned_sources(rows):
    """Every source file each row claims, as paths relative to the source dir.

    Mirrors how comic_mover.plan_moves() reads a row: a folder row moves the
    names in Files Details out of Left Folder, any other row moves the single
    file named in Left Panel File.
    """
    out = []
    for r in rows:
        if r['Action Type'] in ('CONSOLIDATE_FOLDER', 'CREATE_FOLDER_FROM_FOLDER'):
            folder = r['Left Folder']
            out += [str(Path(folder) / n.strip())
                    for n in r['Files Details'].split('|') if n.strip()]
        elif r['Left Panel File'].strip():
            out.append(r['Left Panel File'].strip())
    return out


class TestEachFileIsPlannedOnce(unittest.TestCase):

    def test_files_in_a_subfolder_are_not_planned_twice(self):
        """The shipped bug, reduced to its smallest form."""
        rows = plan({
            'The Nameless Kingdom Vol. 1 - 3 (2026) (digital)/The Nameless Kingdom v01 (2026) (digital).cbz': 1,
            'The Nameless Kingdom Vol. 1 - 3 (2026) (digital)/The Nameless Kingdom v02 (2026) (digital).cbz': 1,
            'The Nameless Kingdom Vol. 1 - 3 (2026) (digital)/The Nameless Kingdom v03 (2026) (digital).cbz': 1,
        })
        got = planned_sources(rows)
        self.assertEqual(sorted(got), sorted(set(got)),
                         f'a file is planned more than once:\n  ' +
                         '\n  '.join(sorted(x for x in got if got.count(x) > 1)))
        self.assertEqual(len(got), 3)

    def test_a_subfolder_and_loose_files_together(self):
        """Loose files were never affected; prove the fix did not break them."""
        rows = plan({
            'Sha 01-03/Sha 01 (2024).cbz': 1,
            'Sha 01-03/Sha 02 (2024).cbz': 1,
            'Bone Parish 001 (2018).cbr': 1,
            'Behemoth 002 (2025).cbr': 1,
        })
        got = planned_sources(rows)
        self.assertEqual(sorted(got), sorted(set(got)))
        self.assertEqual(len(got), 4)

    def test_a_nested_file_is_planned_once_and_still_planned(self):
        """The trap in fixing this: the duplicate was masking a second defect.

        A folder row flattens by joining a bare name onto Left Folder, so it can
        only move direct children — a nested file listed there resolves to a path
        that does not exist. Before the fix the nested file was moved only by its
        duplicate standalone row. De-duplicating by suppressing that row would
        have turned a double-move into no move at all: silent data loss.
        """
        rows = plan({
            'Cruel Kingdom 01-02/Cruel Kingdom 01 (2026).cbz': 1,
            'Cruel Kingdom 01-02/extras/Cruel Kingdom 02 (2026).cbz': 1,
        })
        got = planned_sources(rows)
        self.assertEqual(sorted(got), sorted(set(got)))
        self.assertIn('Cruel Kingdom 01-02/extras/Cruel Kingdom 02 (2026).cbz', got,
                      'the nested file was dropped from the plan entirely')
        self.assertIn('Cruel Kingdom 01-02/Cruel Kingdom 01 (2026).cbz', got)

    def test_every_planned_source_actually_exists(self):
        """A row naming a file that is not there is a move that cannot run.

        This is what the folder row did for nested files: it listed a bare name
        the mover then looked for as a direct child.
        """
        tree = {
            'Cruel Kingdom 01-02/Cruel Kingdom 01 (2026).cbz': 1,
            'Cruel Kingdom 01-02/extras/Cruel Kingdom 02 (2026).cbz': 1,
            'Behemoth 002 (2025).cbr': 1,
        }
        rows = plan(tree)
        for src in planned_sources(rows):
            self.assertIn(src, tree, f'plan names a file that does not exist: {src}')


if __name__ == '__main__':
    unittest.main()
