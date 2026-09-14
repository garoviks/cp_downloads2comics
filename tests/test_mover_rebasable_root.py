#!/usr/bin/env python3
"""O17 — the folder pair chosen in the UI must reach the mover, not just the scan.

Both source and destination are pickable (REQUIREMENTS FR:132, "Folder picker
modals for source and destination paths"). Before this, those pickers reached
matching_analysis_generator.py via --src/--dest but stopped there: serve_v2.py
launched comic_mover.py with neither, so the mover fell back to the hardcoded
constants at comic_mover.py:26-28. Two consequences, both silent:

  * Pick a different DESTINATION -> the scan analysed library B while the move
    wrote into library A. The CSV's 'Has Existing Folder: YES' described a folder
    in a library the files never reached.
  * Pick a different SOURCE -> the generator wrote the CSV into the new source
    folder (matching_analysis_generator.py:883), while the mover kept reading the
    old one. A stale CSV, or none at all.

The subprocess boundary is what hid this: nothing fails when an argument is
simply never passed.

Run:  python3 -m unittest discover tests
"""
import os
import subprocess
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import paths

mover = paths.load_mover()

CSV_COLUMNS = [
    "Left Folder", "File Count", "Left Panel File", "Series Name", "Action Type",
    "Suggested Folder Name", "Right Panel Matches (Count)", "Has Existing Folder",
    "Has Existing Files", "Consolidation Strategy", "Move Source", "Files Details",
    "Right Loose Files", "Proposed Filename", "Proposed Files Details",
]


def _write_fixture(tmp):
    """A source holding one file and a CSV, plus two candidate destinations."""
    import csv
    src = os.path.join(tmp, 'src')
    dest_a = os.path.join(tmp, 'destA')
    dest_b = os.path.join(tmp, 'destB')
    for d in (src, dest_a, dest_b):
        os.makedirs(d)
    os.makedirs(os.path.join(dest_a, 'Saga (2012)'))
    os.makedirs(os.path.join(dest_b, 'Saga (2012)'))
    open(os.path.join(src, 'Saga 025.cbr'), 'w').close()

    row = {c: '' for c in CSV_COLUMNS}
    row.update({'Left Panel File': 'Saga 025.cbr', 'Series Name': 'Saga',
                'Action Type': 'CONSOLIDATE', 'Suggested Folder Name': 'Saga (2012)',
                'Has Existing Folder': 'YES', 'Move Source': 'Saga 025.cbr'})
    with open(os.path.join(src, 'matching_analysis_consolidated.csv'),
              'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=CSV_COLUMNS)
        w.writeheader()
        w.writerow(row)
    return src, dest_a, dest_b


def _dry_run(src, dest):
    """Run the real script as a subprocess — the boundary where the bug lived.

    Importing main() and calling it would not reproduce the defect: the argument
    was missing from the command line, not from the parsing.
    """
    out = subprocess.run(
        [sys.executable, 'comic_mover.py', '--dry-run', '--src', src, '--dest', dest],
        cwd=paths.GENERATOR_DIR, capture_output=True, text=True, timeout=60)
    return out.stdout + out.stderr


class TestFoldersReachTheMover(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp(prefix='o17-')
        self.src, self.dest_a, self.dest_b = _write_fixture(self.tmp)

    def tearDown(self):
        import shutil
        shutil.rmtree(self.tmp, ignore_errors=True)

    def test_dest_steers_where_files_would_go(self):
        """The same CSV must target whichever destination was passed."""
        self.assertIn(os.path.join(self.dest_a, 'Saga (2012)'), _dry_run(self.src, self.dest_a))

    def test_a_different_dest_moves_the_target(self):
        out = _dry_run(self.src, self.dest_b)
        self.assertIn(os.path.join(self.dest_b, 'Saga (2012)'), out)
        self.assertNotIn(self.dest_a, out)

    def test_src_steers_which_csv_is_read(self):
        self.assertIn(os.path.join(self.src, 'matching_analysis_consolidated.csv'),
                      _dry_run(self.src, self.dest_a))

    def test_the_real_library_is_never_touched_when_folders_are_given(self):
        """The whole point: passing folders must fully displace the defaults."""
        out = _dry_run(self.src, self.dest_a)
        self.assertNotIn(paths.LIBRARY_ROOT, out)


class TestConfinementFollowsTheNewRoot(unittest.TestCase):
    """Rebasing must not weaken resolve_under_dest — it must re-aim it.

    A guard that still confines to the OLD root after the root changes is worse
    than no guard, because it reads as protection while permitting every write
    into the newly-selected library to escape.
    """

    def setUp(self):
        self.original = mover.DEST_DIR
        self.tmp = tempfile.mkdtemp(prefix='o17-conf-')
        mover.DEST_DIR = __import__('pathlib').Path(self.tmp)

    def tearDown(self):
        mover.DEST_DIR = self.original
        import shutil
        shutil.rmtree(self.tmp, ignore_errors=True)

    def test_plain_name_lands_under_the_new_root(self):
        got = mover.resolve_under_dest('Sandman')
        self.assertIsNotNone(got)
        self.assertEqual(got.parent, mover.DEST_DIR.resolve())

    def test_dotdot_escape_from_the_new_root_is_still_rejected(self):
        self.assertIsNone(mover.resolve_under_dest('../../../tmp/pwned'))

    def test_escape_is_measured_against_the_new_root_not_the_old(self):
        """Naming the ORIGINAL library from the new root must be refused.

        This is the assertion that would fail if resolve_under_dest kept a
        reference to the startup root instead of reading DEST_DIR at call time.
        """
        depth = len(mover.DEST_DIR.resolve().parts) - 1
        escape = os.path.join(*(['..'] * depth), paths.LIBRARY_ROOT.lstrip('/'))
        self.assertIsNone(mover.resolve_under_dest(escape))


class TestServerPassesTheFoldersOn(unittest.TestCase):
    """The defect's actual location: serve_v2.py built the command without them.

    comic_mover.py accepting --src/--dest fixes nothing on its own if the server
    never sends them, and that omission is invisible — a subprocess launched
    without an optional argument exits 0 and does the wrong thing quietly.
    """

    def setUp(self):
        self.serve = paths.load_serve_v2()

    def test_dry_run_command_carries_both_folders(self):
        cmd = self.serve.mover_cmd('dry-run', '/tmp/S', '/tmp/D')
        self.assertIn('--src', cmd)
        self.assertEqual(cmd[cmd.index('--src') + 1], '/tmp/S')
        self.assertIn('--dest', cmd)
        self.assertEqual(cmd[cmd.index('--dest') + 1], '/tmp/D')

    def test_execute_command_carries_both_folders(self):
        cmd = self.serve.mover_cmd('execute', '/tmp/S', '/tmp/D')
        self.assertIn('--execute', cmd)
        self.assertEqual(cmd[cmd.index('--src') + 1], '/tmp/S')
        self.assertEqual(cmd[cmd.index('--dest') + 1], '/tmp/D')

    def test_dry_run_never_executes(self):
        """A mode mix-up here moves files for real instead of previewing them."""
        cmd = self.serve.mover_cmd('dry-run', '/tmp/S', '/tmp/D')
        self.assertIn('--dry-run', cmd)
        self.assertNotIn('--execute', cmd)

    def test_optional_arguments_are_omitted_not_blanked(self):
        cmd = self.serve.mover_cmd('dry-run', '/tmp/S', '/tmp/D')
        self.assertNotIn('--overrides', cmd)
        self.assertNotIn('--selected-ids', cmd)

    def test_optional_arguments_survive_alongside_the_folders(self):
        cmd = self.serve.mover_cmd('execute', '/tmp/S', '/tmp/D',
                                   overrides_file='/tmp/o.json', selected_ids=[3, 1])
        self.assertEqual(cmd[cmd.index('--overrides') + 1], '/tmp/o.json')
        self.assertEqual(cmd[cmd.index('--selected-ids') + 1], '3,1')
        self.assertEqual(cmd[cmd.index('--dest') + 1], '/tmp/D')


class TestFolderPairDefaults(unittest.TestCase):
    """An absent or blank folder must fall back to the constant, not to ''."""

    def setUp(self):
        self.serve = paths.load_serve_v2()
        self.handler = self.serve.ComicOrganizerV2Handler.__new__(
            self.serve.ComicOrganizerV2Handler)

    def test_missing_keys_fall_back_to_the_constants(self):
        src, dest = self.handler.folder_pair({})
        self.assertEqual(src, str(self.serve.SRC_DIR))
        self.assertEqual(dest, str(self.serve.DEST_DIR))

    def test_blank_strings_fall_back_too(self):
        """'' would otherwise reach the mover and resolve to the process cwd."""
        src, dest = self.handler.folder_pair({'src_dir': '  ', 'dest_dir': ''})
        self.assertEqual(src, str(self.serve.SRC_DIR))
        self.assertEqual(dest, str(self.serve.DEST_DIR))

    def test_supplied_values_win(self):
        src, dest = self.handler.folder_pair({'src_dir': '/tmp/S', 'dest_dir': '/tmp/D'})
        self.assertEqual((src, dest), ('/tmp/S', '/tmp/D'))


if __name__ == '__main__':
    unittest.main(verbosity=2)
