#!/usr/bin/env python3
"""Regression suite for how the mover selects loose library-root files.

This is the highest-consequence code path in either app: it decides which
already-filed comics get swept into a folder alongside the incoming one.

find_loose_right_files() searched the library root with

    if search_term in item.name.lower()

a bare substring test, so a folder named 'Sleep' collected 'Sleeper Book 01',
'Flow' collected 'Sunflower', 'Odin' collected 'A. Rodin'. An audit of the real
library found 18 files misfiled exactly this way.

The generator already computes the correct answer into the CSV column
'Right Loose Files' (matching_analysis_generator.py:987). The mover now reads
that column instead of re-deriving it, so there is one producer and one consumer
rather than two disagreeing implementations.

Run:  python3 -m unittest discover tests
"""
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import paths

mover = paths.load_mover()


class TestBuggyFunctionIsGone(unittest.TestCase):
    def test_find_loose_right_files_removed(self):
        """Guard against it being reintroduced."""
        self.assertFalse(
            hasattr(mover, 'find_loose_right_files'),
            'find_loose_right_files() is back — it selects loose files by bare '
            'substring and misfiles comics. Read the CSV column instead.')


class TestLooseRightFiles(unittest.TestCase):
    """The replacement reads the generator's column verbatim."""

    def test_empty_column_selects_nothing(self):
        self.assertEqual(mover.loose_right_files({}), [])
        self.assertEqual(mover.loose_right_files({'Right Loose Files': ''}), [])
        self.assertEqual(mover.loose_right_files({'Right Loose Files': '   '}), [])

    def test_single_file(self):
        got = mover.loose_right_files({'Right Loose Files': 'Feral 019.cbr'})
        self.assertEqual([p.name for p in got], ['Feral 019.cbr'])
        self.assertEqual(got[0].parent, mover.DEST_DIR)

    def test_pipe_separated_and_trimmed(self):
        row = {'Right Loose Files': 'A 001.cbz | B 002.cbr |  C 003.cbz  '}
        self.assertEqual([p.name for p in mover.loose_right_files(row)],
                         ['A 001.cbz', 'B 002.cbr', 'C 003.cbz'])

    def test_empty_segments_ignored(self):
        row = {'Right Loose Files': 'A 001.cbz || | B 002.cbr'}
        self.assertEqual([p.name for p in mover.loose_right_files(row)],
                         ['A 001.cbz', 'B 002.cbr'])

    def test_names_are_never_reinterpreted(self):
        """The column is authoritative — no substring logic may creep back in.

        These are the exact filenames the old function wrongly collected. The
        mover must now take only what it is given, verbatim.
        """
        row = {'Right Loose Files': 'Sleeper Book 01 (2018).cbr'}
        self.assertEqual([p.name for p in mover.loose_right_files(row)],
                         ['Sleeper Book 01 (2018).cbr'])

        # A row that names nothing must move nothing, even though the library
        # root contains files whose names contain 'Sleep'.
        self.assertEqual(mover.loose_right_files({'Right Loose Files': ''}), [])

    def test_filenames_with_pipes_are_not_expected(self):
        """Documents the format's one limitation: '|' is the separator."""
        row = {'Right Loose Files': 'Weird|Name.cbz'}
        self.assertEqual([p.name for p in mover.loose_right_files(row)],
                         ['Weird', 'Name.cbz'])


if __name__ == '__main__':
    unittest.main()
