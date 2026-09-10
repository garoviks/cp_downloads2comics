#!/usr/bin/env python3
"""Every write the mover performs must land inside the library root.

'Suggested Folder Name' and 'Proposed Filename' are not trusted strings: the
server copies them out of the overrides JSON with no validation
(comic_mover.py:489-494), and the only guard was `.strip('/')`. That neutralises
an absolute path but does nothing about '..', so before this suite existed:

    '../../../tmp/pwned'  ->  /tmp/pwned

and mkdir(parents=True, exist_ok=True) created it silently.

This is a single-user tool bound to loopback, so the realistic cause is a typo or
a malformed CSV cell rather than an attacker. The consequence is the same either
way: directories created outside the library, with no error.

Run:  python3 -m unittest discover tests
"""
import os
import pathlib
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import paths

mover = paths.load_mover()


class TestResolveUnderDest(unittest.TestCase):
    def test_plain_name_resolves_inside(self):
        got = mover.resolve_under_dest('Sandman')
        self.assertIsNotNone(got)
        self.assertEqual(got.name, 'Sandman')
        self.assertEqual(got.parent, mover.DEST_DIR.resolve())

    def test_absolute_path_is_neutralised_not_rejected(self):
        """Documents existing behaviour: '/etc/cron.d' becomes a relative name.

        `.strip('/')` turns it into 'etc/cron.d' under the library, which is
        harmless. The guard does not need to reject it, only to keep it inside.
        """
        got = mover.resolve_under_dest('/etc/cron.d')
        self.assertIsNotNone(got)
        self.assertTrue(str(got).startswith(str(mover.DEST_DIR.resolve()) + os.sep))

    def test_dotdot_escape_is_rejected(self):
        """The case that motivated the guard."""
        self.assertIsNone(mover.resolve_under_dest('../../../tmp/pwned'))

    def test_shallow_dotdot_escape_is_rejected(self):
        self.assertIsNone(mover.resolve_under_dest('..'))

    def test_dotdot_that_stays_inside_is_allowed(self):
        """'A/../B' resolves to 'B', which is inside — no reason to reject it."""
        got = mover.resolve_under_dest('A/../B')
        self.assertIsNotNone(got)
        self.assertEqual(got.name, 'B')

    def test_empty_is_rejected(self):
        self.assertIsNone(mover.resolve_under_dest(''))

    def test_sibling_prefix_directory_is_rejected(self):
        """A bare startswith() would accept '/mnt/extramedia/ComicsOld'.

        Reached via '..' back out and into the sibling, which is exactly the
        near-miss the trailing os.sep in the comparison exists to catch.
        """
        sibling = os.path.basename(str(mover.DEST_DIR.resolve())) + 'Old'
        self.assertIsNone(mover.resolve_under_dest(f'../{sibling}'))


class TestIsPlainName(unittest.TestCase):
    def test_accepts_real_comic_filenames(self):
        for name in ('Feral 019 (2024).cbr',
                     'Die - Loaded v01 - Zero Sessions (2026).cbz',
                     'T.H.U.N.D.E.R. Agents v02.cbz'):
            self.assertTrue(mover.is_plain_name(name), name)

    def test_rejects_path_components(self):
        for name in ('', '.', '..', '/etc/passwd', 'a/b', '../x.cbz', 'a/'):
            self.assertFalse(mover.is_plain_name(name), name)


class TestPlanSkipsEscapingRows(unittest.TestCase):
    """The guard has to be reachable from the CSV, not just unit-testable.

    A real source file is required. plan_moves() checks the SOURCE exists before
    it ever resolves the destination, so a row naming a nonexistent file is
    skipped for that reason and never reaches the guard at all — the test would
    pass while proving nothing. SRC_DIR is redirected at a tempdir so the row
    gets far enough to matter.
    """

    def setUp(self):
        self._real_src = mover.SRC_DIR
        self._tmp = tempfile.TemporaryDirectory()
        mover.SRC_DIR = pathlib.Path(self._tmp.name)
        (mover.SRC_DIR / 'Whatever 001 (2024).cbz').write_text('x')

    def tearDown(self):
        mover.SRC_DIR = self._real_src
        self._tmp.cleanup()

    def _row(self, dest):
        return {
            'Left Panel File': 'Whatever 001 (2024).cbz',
            'Series Name': 'Whatever',
            'Suggested Folder Name': dest,
            'Action Type': 'CONSOLIDATE',
        }

    def test_escaping_destination_is_skipped_for_the_right_reason(self):
        ops = mover.plan_moves([self._row('../../../tmp/pwned')])
        self.assertTrue(ops)
        for op in ops:
            self.assertEqual(op.moves, [], 'an escaping row planned a move')
            self.assertIn('escapes the library', op.skipped_reason or '')

    def test_ordinary_destination_still_plans_a_move(self):
        """The guard must not reject good rows — the failure mode that matters."""
        ops = mover.plan_moves([self._row('Sandman')])
        self.assertEqual(sum(len(op.moves) for op in ops), 1)

    def test_proposed_filename_with_a_path_is_not_used(self):
        """A bad 'Proposed Filename' falls back to the original name."""
        row = self._row('Sandman')
        row['Proposed Filename'] = '../../../tmp/pwned.cbz'
        moves = [mv for op in mover.plan_moves([row]) for mv in op.moves]
        self.assertEqual(len(moves), 1)
        self.assertEqual(moves[0].dst.name, 'Whatever 001 (2024).cbz')


if __name__ == '__main__':
    unittest.main()
