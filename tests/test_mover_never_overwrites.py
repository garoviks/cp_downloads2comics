#!/usr/bin/env python3
"""A move must never destroy the file already at its destination.

shutil.move() overwrites an existing path silently and returns normally, so a
plan containing two moves to one destination loses a file and reports success
for both. The execution log then records both as executed, which makes the loss
invisible to --rollback too: it restores whichever file survived and reports the
other as merely "not where we left it".

This happened. A real run planned an incoming download and an identically named
loose file already in the library root into the same folder — same basename, so
the same destination path. One overwrote the other. Two files, both irreplaceable
from the log, and the run reported 0 failures.

The guard belongs in the mover rather than only in the planner: the planner is
one of several things that can produce a colliding pair, and the mover is the
single point where a file is actually at risk. rollback() has always refused to
overwrite; this pins the forward direction to the same rule.

Run:  python3 -m unittest discover tests
"""
import os
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import paths

mover = paths.load_mover()


class TestMoveRefusesToClobber(unittest.TestCase):

    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.tmp, True)
        self.src_dir = Path(self.tmp) / 'src'
        self.dest_dir = Path(self.tmp) / 'dest'
        self.src_dir.mkdir()
        self.dest_dir.mkdir()
        # execute_moves() writes the rollback log as a side effect. Left
        # pointing at the real one, running the suite would overwrite the undo
        # record for whatever the user last did for real.
        self._saved = (mover.SRC_DIR, mover.DEST_DIR,
                       mover.LOG_DIR, mover.ROLLBACK_FILE)
        mover.SRC_DIR, mover.DEST_DIR = self.src_dir, self.dest_dir
        mover.LOG_DIR = Path(self.tmp) / 'logs'
        mover.ROLLBACK_FILE = mover.LOG_DIR / 'last_execution.json'
        self.addCleanup(self._restore)

    def _restore(self):
        (mover.SRC_DIR, mover.DEST_DIR,
         mover.LOG_DIR, mover.ROLLBACK_FILE) = self._saved

    def _op(self, moves, dest_folder='Shelf'):
        op = mover.MoveOperation({}, 'Shelf', dest_folder)
        for src, dst in moves:
            op.add_move(src, dst, 'FILE')
        return op

    def test_two_files_to_one_path_does_not_destroy_either(self):
        """The shipped case, reduced: two distinct files, one destination."""
        a = self.src_dir / 'Wizard.cbz'
        b = self.dest_dir / 'Wizard.cbz'
        a.write_bytes(b'incoming download')
        b.write_bytes(b'already in the library')
        target = self.dest_dir / 'Shelf' / 'Wizard.cbz'

        op = self._op([(a, target), (b, target)])
        mover.execute_moves([op], dry_run=False)

        survivors = {p.read_bytes() for p in
                     (list(self.src_dir.rglob('*.cbz')) + list(self.dest_dir.rglob('*.cbz')))}
        self.assertIn(b'incoming download', survivors)
        self.assertIn(b'already in the library', survivors,
                      'the library copy was overwritten and is gone')

    def test_the_colliding_move_is_reported_as_an_error(self):
        """Silent success is what made the loss invisible; it must be loud."""
        a = self.src_dir / 'Wizard.cbz'
        b = self.dest_dir / 'Wizard.cbz'
        a.write_bytes(b'incoming download')
        b.write_bytes(b'already in the library')
        target = self.dest_dir / 'Shelf' / 'Wizard.cbz'

        op = self._op([(a, target), (b, target)])
        mover.execute_moves([op], dry_run=False)

        executed = [m for m in op.moves if m.executed]
        failed = [m for m in op.moves if m.error]
        self.assertEqual(len(executed), 1, 'exactly one move can legitimately succeed')
        self.assertEqual(len(failed), 1, 'the colliding move must record an error')
        self.assertIn('refusing to overwrite', failed[0].error)

    def test_an_ordinary_move_still_works(self):
        """The guard must not block the normal case of an empty destination."""
        a = self.src_dir / 'Wizard.cbz'
        a.write_bytes(b'incoming download')
        target = self.dest_dir / 'Shelf' / 'Wizard.cbz'

        op = self._op([(a, target)])
        mover.execute_moves([op], dry_run=False)

        self.assertTrue(target.exists())
        self.assertEqual(target.read_bytes(), b'incoming download')
        self.assertFalse(a.exists())
        self.assertTrue(op.moves[0].executed)


if __name__ == '__main__':
    unittest.main()
