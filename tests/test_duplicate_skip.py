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
from unittest import mock

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import paths

mover = paths.load_mover()
gen = paths.load_generator()

CSV_COLUMNS = gen.CSV_COLUMNS


def row(**kw):
    r = {c: '' for c in CSV_COLUMNS}
    r.update(kw)
    return r


def cbz(path: Path, pages: int, extra=()):
    """A real comic archive holding `pages` images, plus any other names given."""
    import zipfile
    with zipfile.ZipFile(path, 'w') as z:
        for i in range(pages):
            z.writestr(f'{i:03d}.jpg', b'not really a jpeg')
        for name in extra:
            z.writestr(name, b'x')
    return path


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


class TestHowManyPages(unittest.TestCase):
    """The evidence the file size was standing in for.

    Two packers disagree about bytes but rarely about how many pages a book has,
    so this is the number that tells two rips of one edition from two different
    editions. It decides nothing on its own — same rule as the sizes.
    """

    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix='pages-'))
        gen._PAGE_COUNTS.clear()

    def tearDown(self):
        gen._PAGE_COUNTS.clear()
        shutil.rmtree(self.tmp, ignore_errors=True)

    def test_images_are_counted_and_everything_else_is_not(self):
        p = cbz(self.tmp / 'twelve-pages.cbz', 12, extra=('ComicInfo.xml', 'readme.txt'))
        self.assertEqual(gen.page_count(p), 12)

    def test_the_rarer_jpeg_spellings_are_still_pages(self):
        """.jpe is a JPEG. Not knowing that cost 159 false alarms.

        The first sweep of the library reported whole manga series as holding no
        images, because every KissManga rip names its pages `001 - proxy..jpe`.
        An allowlist that is missing a spelling does not under-report quietly —
        it accuses a perfectly good comic of not being one.
        """
        p = self.tmp / 'kissmanga-style.cbz'
        import zipfile
        with zipfile.ZipFile(p, 'w') as z:
            for i in range(5):
                z.writestr(f'{i:03d} - proxy..jpe.jpe', b'x')
            z.writestr('006.jfif', b'x')
            z.writestr('007.tiff', b'x')
        self.assertEqual(gen.page_count(p), 7)

    def test_an_archive_too_damaged_to_open_claims_nothing(self):
        """Says zip in its first four bytes, then will not open.

        A truncated download looks exactly like this. It must not read as
        'holds no pages' — that is the alarm reserved for files which opened
        fine and turned out not to be comics, and this one never opened at all.
        """
        p = self.tmp / 'truncated.cbz'
        p.write_bytes(gen.ZIP_MAGIC + b'\x14\x00' + b'\x00' * 200)
        self.assertIsNone(gen.page_count(p))
        self.assertEqual(gen.human_pages(p), '')

    def test_the_other_archive_formats_hiding_under_cbr_are_read(self):
        """A .cbr holding 7z, and a .cbr holding tar. Both are real comics.

        Knowing only zip and rar was the PAGE_EXTS mistake in a second place:
        an unrecognised format fell through to zero, so the sweep accused five
        good books — 234, 161, 50, 42 and 20 pages — of not being comics.
        """
        import subprocess
        import tarfile
        src = self.tmp / 'pages'
        src.mkdir()
        for i in range(4):
            (src / f'{i:03d}.jpg').write_bytes(b'x')
        (src / 'notes.txt').write_bytes(b'x')

        seven = self.tmp / 'packed-as-7z.cbr'
        rc = subprocess.run(['7z', 'a', '-t7z', str(seven), str(src / '*')],
                            capture_output=True).returncode
        self.assertEqual(rc, 0, '7z is needed for this test')
        self.assertTrue(seven.read_bytes().startswith(gen.SEVENZ_MAGIC))
        self.assertEqual(gen.page_count(seven), 4)

        tar = self.tmp / 'packed-as-tar.cbr'
        with tarfile.open(tar, 'w') as t:
            for f in sorted(src.iterdir()):
                t.add(f, arcname=f.name)
        self.assertEqual(gen.page_count(tar), 4)

    def test_an_ace_archive_claims_nothing(self):
        """ACE is a real archive format with no reader installed here.

        Neither 7z nor unrar will open one, so we cannot see inside. That is
        'could not read it', not 'holds no pages' — the same distinction the
        truncated zip above turns on, reached by a different route.
        """
        p = self.tmp / 'old-scanlation.cbr'
        p.write_bytes(b'\xd6\x9d1\x00\x00\x00\x90' + gen.ACE_MAGIC + b'\x00' * 64)
        self.assertIsNone(gen.page_count(p))
        self.assertEqual(gen.human_pages(p), '')

    def test_a_download_that_is_not_an_archive_at_all_counts_zero(self):
        """The file that motivated this: 238 MB of HTML named .cbr.

        Zero is a finding, not a failure. It is how 'this is not a comic' looks
        from the outside, and the UI colours it accordingly.
        """
        p = self.tmp / 'html-error-page.cbr'
        p.write_text('<html><head><title>429 Too Many Requests</title>')
        self.assertEqual(gen.page_count(p), 0)
        self.assertEqual(gen.human_pages(p), '0p')

    def test_a_file_that_is_not_an_archive_is_settled_without_asking_unrar(self):
        """The signature check is the answer, not a shortcut to one.

        The zero above is only trustworthy because we read the magic bytes
        ourselves. Asking unrar instead looks like it works — this build exits 0
        and prints nothing for anything that is not a RAR, which counts as zero
        by accident — but that makes 'holds no pages' and 'could not read it'
        the same answer, and leaves the distinction resting on a behaviour no
        version of unrar promises.
        """
        p = self.tmp / 'not-an-archive.cbr'
        p.write_bytes(b'this is not an archive')
        with mock.patch('subprocess.run',
                        side_effect=AssertionError('unrar was asked about a non-archive')):
            self.assertEqual(gen.page_count(p), 0)

    def test_an_archive_holding_no_images_counts_zero(self):
        p = cbz(self.tmp / 'no-images.cbz', 0, extra=('index.html',))
        self.assertEqual(gen.page_count(p), 0)

    def test_a_rar_that_cannot_be_opened_claims_nothing(self):
        """Says it is a RAR and then is not one. Unreadable is not the same as empty.

        `unrar lb` exits 0 with no output for a file that is not a RAR at all,
        so trusting its exit code alone would report this as a confident zero.
        """
        p = self.tmp / 'truncated.cbr'
        p.write_bytes(gen.RAR_MAGIC + b'\x00 truncated nonsense')
        self.assertIsNone(gen.page_count(p))
        self.assertEqual(gen.human_pages(p), '')

    def test_the_extension_does_not_decide_the_format(self):
        """.cbr files are routinely zips, and the other way round."""
        p = cbz(self.tmp / 'zip-named-cbr.cbr', 7)
        self.assertEqual(gen.page_count(p), 7)

    def test_a_missing_file_is_silence_rather_than_an_error(self):
        self.assertIsNone(gen.page_count(self.tmp / 'gone.cbz'))


class TestWhatTheGeneratorReports(unittest.TestCase):
    """The destination folder is searched first, then the library; the demotion rules still apply."""

    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix='dup-gen-'))
        self.src, self.dest = self.tmp / 'src', self.tmp / 'dest'
        self.src.mkdir()
        self.folder = self.dest / 'Harley Quinn'
        self.folder.mkdir(parents=True)
        cbz(self.folder / 'Harley Quinn v02 - Power Outage (2015).cbz', 5)
        (self.dest / 'Elsewhere').mkdir()
        cbz(self.dest / 'Elsewhere' / 'Harley Quinn v02 - Power Outage (2015).cbz', 5)
        self.saved = (gen.SRC_DIR, gen.DEST_DIR)
        gen.SRC_DIR, gen.DEST_DIR = self.src, self.dest
        gen._DEST_FOLDER_INDEX.clear()
        gen._LIBRARY_INDEX.clear()
        gen._PAGE_COUNTS.clear()

    def tearDown(self):
        gen.SRC_DIR, gen.DEST_DIR = self.saved
        gen._DEST_FOLDER_INDEX.clear()
        gen._LIBRARY_INDEX.clear()
        gen._PAGE_COUNTS.clear()
        shutil.rmtree(self.tmp, ignore_errors=True)

    def _incoming(self, name, pages=3):
        cbz(self.src / name, pages)
        return name

    def test_another_rip_of_the_same_book_is_found(self):
        got = gen.find_existing_copies(
            self._incoming('Harley Quinn v02 - Power Outage (2016) (digital-Empire).cbz'),
            self.folder)
        # The fixture also keeps the same book in 'Elsewhere/'; the library-wide
        # search reports it after the destination folder's own copy.
        self.assertEqual([p.relative_to(self.dest).as_posix() for p in got],
                         ['Harley Quinn/Harley Quinn v02 - Power Outage (2015).cbz',
                          'Elsewhere/Harley Quinn v02 - Power Outage (2015).cbz'])

    def test_a_different_volume_two_is_not(self):
        """Six Harley Quinn v02s parse alike; the subtitle is what tells them apart."""
        self.assertEqual(gen.find_existing_copies(
            self._incoming('Harley Quinn v02 - Keepsake (2022) (digital).cbz'),
            self.folder), [])

    def test_a_copy_elsewhere_in_the_library_is_reported_after_the_folders_own(self):
        """Scope is the whole library, destination folder first (dup-warnings A)."""
        names, _, _ = gen.describe_existing_copies(
            [self._incoming('Harley Quinn v02 - Power Outage (2016).cbz')], '/Elsewhere/')
        self.assertEqual(names.count('=>'), 2)
        self.assertLess(names.index('Elsewhere/'), names.index('Harley Quinn/'))

    def test_the_three_columns_are_parallel_and_name_both_halves(self):
        """The UI zips these back together by position, so the shape is a contract."""
        names, sizes, pages = gen.describe_existing_copies(
            [self._incoming('Harley Quinn v02 - Power Outage (2016).cbz', pages=3)],
            '/Harley Quinn/')
        self.assertEqual(
            names,
            'Harley Quinn v02 - Power Outage (2016).cbz'
            ' => Harley Quinn/Harley Quinn v02 - Power Outage (2015).cbz'
            ' | Harley Quinn v02 - Power Outage (2016).cbz'
            ' => Elsewhere/Harley Quinn v02 - Power Outage (2015).cbz')
        self.assertEqual(sizes.count('=>'), names.count('=>'))
        self.assertEqual(pages.count('=>'), names.count('=>'))
        self.assertEqual(sizes, '0 MB => 0 MB | 0 MB => 0 MB')
        self.assertEqual(pages, '3p => 5p | 3p => 5p')

    def test_a_row_with_no_destination_folder_searches_the_library_not_the_root_as_a_folder(self):
        """A blank folder name is COPY_TO_BASE: no folder of its own to look in.

        It used to ask nothing, because the root as a "destination folder" would
        have flagged every copy anywhere. Now every copy anywhere is the point,
        so the library index answers, once per copy — not once more for the root
        walked as if it were a folder.
        """
        names, _, _ = gen.describe_existing_copies(
            [self._incoming('Harley Quinn v02 - Power Outage (2016).cbz')], '')
        self.assertEqual(names.count('=>'), 2)


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
