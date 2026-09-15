#!/usr/bin/env python3
"""Filing a book the destination folder already holds, and the decision that stops it.

The generator names the copies already in the folder a download is headed for;
the mover refuses to execute until each one has been answered. Three things have
to line up for that to work, and none of them is visible from either end alone:

  * the KEY. The mover plans moves for a file row from 'Left Panel File', which
    can carry a subfolder, while the column names the file bare. Key on the bare
    name and the skip silently never fires — and, worse, the gate keeps asking
    about a file no decision can ever settle.
  * the ANSWER. Skipping is opt-in. Doing nothing must not file the copy, and
    must not quietly drop the file either.
  * the REFUSAL. serve_v2.py runs the mover with --no-confirm, so a warning is
    printed to nobody. Only exiting non-zero stops a second copy landing.

Run:  python3 -m unittest discover tests
"""
import csv
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import paths

mover = paths.load_mover()
gen = paths.load_generator()

CSV_COLUMNS = gen.CSV_COLUMNS


def row(**kw):
    r = {c: '' for c in CSV_COLUMNS}
    r.update(kw)
    return r


class TestWhichFileWasFlagged(unittest.TestCase):
    """flagged_duplicates() must name files the way plan_moves() looks them up."""

    def test_a_file_row_is_named_by_its_full_source_path(self):
        # The column's left half is a bare name; the move is planned from
        # 'Left Panel File'. A source subfolder lives in one and not the other.
        got = mover.flagged_duplicates(row(
            **{'Action Type': 'CONSOLIDATE',
               'Left Panel File': 'Sha 01-03/Sha 01.cbr',
               'Existing Copies': 'Sha 01.cbr => Shakara/Sha 01.cbz'}))
        self.assertEqual(got, ['Sha 01-03/Sha 01.cbr'])

    def test_a_folder_row_names_each_colliding_file_under_its_folder(self):
        got = mover.flagged_duplicates(row(
            **{'Action Type': 'CONSOLIDATE_FOLDER', 'Left Folder': 'Saga v1-3',
               'Existing Copies': 'Saga 01.cbr => Saga/Saga 01.cbz'
                                  ' | Saga 03.cbr => Saga/Saga 03.cbz'}))
        self.assertEqual(got, ['Saga v1-3/Saga 01.cbr', 'Saga v1-3/Saga 03.cbr'])

    def test_a_row_with_nothing_already_in_the_folder_flags_nothing(self):
        self.assertEqual(mover.flagged_duplicates(row(
            **{'Action Type': 'CONSOLIDATE', 'Left Panel File': 'Saga 01.cbr'})), [])


class TestWhatIsStillUndecided(unittest.TestCase):

    def setUp(self):
        mover.DUPLICATE_DECISIONS.clear()

    tearDown = setUp

    def test_one_file_matching_two_copies_is_one_question(self):
        """Blood Type collided with two rips already on the shelf. One decision."""
        rows = [row(**{'Action Type': 'CONSOLIDATE', 'Left Panel File': 'Blood Type v01.cbr',
                       'Existing Copies': 'Blood Type v01.cbr => Blood Type/a.cbz'
                                          ' | Blood Type v01.cbr => Blood Type/b.cbr'})]
        self.assertEqual(mover.undecided_duplicates(rows), ['Blood Type v01.cbr'])

    def test_both_answers_settle_it(self):
        """'File it anyway' has to count as answered, or the gate never opens."""
        rows = [row(**{'Action Type': 'CONSOLIDATE', 'Left Panel File': 'A.cbr',
                       'Existing Copies': 'A.cbr => X/A.cbz'}),
                row(**{'Action Type': 'CONSOLIDATE', 'Left Panel File': 'B.cbr',
                       'Existing Copies': 'B.cbr => X/B.cbz'})]
        mover.DUPLICATE_DECISIONS.update({'A.cbr': 'skip', 'B.cbr': 'keep'})
        self.assertEqual(mover.undecided_duplicates(rows), [])


class TestThePlanHonoursTheAnswer(unittest.TestCase):

    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix='dup-'))
        (self.tmp / 'src').mkdir()
        (self.tmp / 'dest' / 'Saga').mkdir(parents=True)
        (self.tmp / 'src' / 'Saga 01.cbr').touch()
        self.src, self.dest = mover.SRC_DIR, mover.DEST_DIR
        mover.SRC_DIR, mover.DEST_DIR = self.tmp / 'src', self.tmp / 'dest'
        mover.DUPLICATE_DECISIONS.clear()
        self.row = row(**{'Action Type': 'CONSOLIDATE', 'Left Panel File': 'Saga 01.cbr',
                          'Series Name': 'Saga', 'Suggested Folder Name': 'Saga',
                          'Existing Copies': 'Saga 01.cbr => Saga/Saga 01.cbz'})

    def tearDown(self):
        mover.SRC_DIR, mover.DEST_DIR = self.src, self.dest
        mover.DUPLICATE_DECISIONS.clear()
        shutil.rmtree(self.tmp, ignore_errors=True)

    def test_a_skipped_file_plans_no_move_and_says_why(self):
        # Recorded as a skipped operation rather than dropped: a file that
        # vanishes from the plan looks like a bug in the plan.
        mover.DUPLICATE_DECISIONS['Saga 01.cbr'] = 'skip'
        op, = mover.plan_moves([self.row])
        self.assertEqual(op.moves, [])
        self.assertIn('left where it is', op.skipped_reason)

    def test_filing_it_anyway_moves_it(self):
        mover.DUPLICATE_DECISIONS['Saga 01.cbr'] = 'keep'
        op, = mover.plan_moves([self.row])
        self.assertEqual(len(op.moves), 1)

    def test_an_undecided_flag_does_not_by_itself_stop_the_move(self):
        """The refusal is the gate; plan_moves() is not it.

        Two guards would mean a dry run that could not show you what you were
        deciding about.
        """
        op, = mover.plan_moves([self.row])
        self.assertEqual(len(op.moves), 1)


class TestWhatTheGeneratorReports(unittest.TestCase):
    """Only the destination folder is searched, and the demotion rules still apply."""

    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix='dup-gen-'))
        self.src, self.dest = self.tmp / 'src', self.tmp / 'dest'
        self.src.mkdir()
        self.folder = self.dest / 'Harley Quinn'
        self.folder.mkdir(parents=True)
        (self.folder / 'Harley Quinn v02 - Power Outage (2015).cbz').write_text('x' * 10)
        (self.dest / 'Elsewhere').mkdir()
        (self.dest / 'Elsewhere' / 'Harley Quinn v02 - Power Outage (2015).cbz').write_text('x')
        self.saved = (gen.SRC_DIR, gen.DEST_DIR)
        gen.SRC_DIR, gen.DEST_DIR = self.src, self.dest
        gen._DEST_FOLDER_INDEX.clear()

    def tearDown(self):
        gen.SRC_DIR, gen.DEST_DIR = self.saved
        gen._DEST_FOLDER_INDEX.clear()
        shutil.rmtree(self.tmp, ignore_errors=True)

    def _incoming(self, name):
        (self.src / name).write_text('y' * 20)
        return name

    def test_another_rip_of_the_same_book_is_found(self):
        got = gen.find_existing_copies(
            self._incoming('Harley Quinn v02 - Power Outage (2016) (digital-Empire).cbz'),
            self.folder)
        self.assertEqual([p.name for p in got],
                         ['Harley Quinn v02 - Power Outage (2015).cbz'])

    def test_a_different_volume_two_is_not(self):
        """Six Harley Quinn v02s parse alike; the subtitle is what tells them apart."""
        self.assertEqual(gen.find_existing_copies(
            self._incoming('Harley Quinn v02 - Keepsake (2022) (digital).cbz'),
            self.folder), [])

    def test_a_copy_elsewhere_in_the_library_is_not_the_folder_this_is_headed_for(self):
        """Scope is the destination folder — the whole-library view is its own report."""
        names, _ = gen.describe_existing_copies(
            [self._incoming('Harley Quinn v02 - Power Outage (2016).cbz')], '/Elsewhere/')
        self.assertEqual(names.count('=>'), 1)
        self.assertIn('Elsewhere', names)

    def test_the_two_columns_are_parallel_and_name_both_halves(self):
        """The UI zips these back together by position, so the shape is a contract."""
        names, sizes = gen.describe_existing_copies(
            [self._incoming('Harley Quinn v02 - Power Outage (2016).cbz')], '/Harley Quinn/')
        self.assertEqual(
            names,
            'Harley Quinn v02 - Power Outage (2016).cbz'
            ' => Harley Quinn/Harley Quinn v02 - Power Outage (2015).cbz')
        self.assertEqual(sizes.count('=>'), names.count('=>'))
        self.assertEqual(sizes, '0 MB => 0 MB')

    def test_a_row_with_no_destination_folder_asks_nothing(self):
        """A blank folder name is not the library root.

        'Suggested Folder Name' is empty on rows that file nothing anywhere.
        Joined onto the library path it resolves to the library itself, which
        would flag every copy anywhere in it — the whole-library view, asked for
        on a row that has no destination to compare against.
        """
        self.assertEqual(gen.describe_existing_copies(
            [self._incoming('Harley Quinn v02 - Power Outage (2016).cbz')], ''), ('', ''))


def _run(args, tmp):
    return subprocess.run([sys.executable, 'comic_mover.py', *args],
                          cwd=paths.GENERATOR_DIR, capture_output=True,
                          text=True, timeout=60)


class TestTheMoverRefusesToExecuteUndecided(unittest.TestCase):
    """--no-confirm is how the UI runs it, so nobody is there to read a warning."""

    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix='dup-exec-'))
        src, dest = self.tmp / 'src', self.tmp / 'dest'
        (dest / 'Saga').mkdir(parents=True)
        src.mkdir()
        (src / 'Saga 01.cbr').write_text('incoming')
        (dest / 'Saga' / 'Saga 01.cbz').write_text('already here')
        with open(src / 'matching_analysis_consolidated.csv', 'w', newline='') as f:
            w = csv.DictWriter(f, fieldnames=CSV_COLUMNS)
            w.writeheader()
            w.writerow(row(**{'Action Type': 'CONSOLIDATE', 'Left Panel File': 'Saga 01.cbr',
                              'Series Name': 'Saga', 'Suggested Folder Name': 'Saga',
                              'Has Existing Folder': 'YES',
                              'Existing Copies': 'Saga 01.cbr => Saga/Saga 01.cbz'}))
        self.src, self.dest = str(src), str(dest)

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def _decisions(self, mapping):
        import json
        p = self.tmp / 'decisions.json'
        p.write_text(json.dumps(mapping))
        return str(p)

    def test_execute_stops_rather_than_warns(self):
        out = _run(['--execute', '--no-confirm', '--src', self.src, '--dest', self.dest],
                   self.tmp)
        self.assertNotEqual(out.returncode, 0)
        self.assertIn('Refusing to execute', out.stdout + out.stderr)
        self.assertTrue((Path(self.src) / 'Saga 01.cbr').exists(),
                        'refusing must mean nothing moved')

    def test_a_dry_run_still_shows_what_is_being_asked(self):
        out = _run(['--dry-run', '--src', self.src, '--dest', self.dest], self.tmp)
        self.assertEqual(out.returncode, 0)
        self.assertIn('Saga 01.cbr', out.stdout)

    def test_deciding_opens_the_gate(self):
        out = _run(['--execute', '--no-confirm', '--src', self.src, '--dest', self.dest,
                    '--duplicate-decisions', self._decisions({'Saga 01.cbr': 'skip'})],
                   self.tmp)
        self.assertEqual(out.returncode, 0, out.stdout + out.stderr)
        self.assertTrue((Path(self.src) / 'Saga 01.cbr').exists(),
                        'skip means the file stays in the source folder')
        self.assertEqual((Path(self.dest) / 'Saga' / 'Saga 01.cbz').read_text(),
                         'already here')


if __name__ == '__main__':
    unittest.main()
