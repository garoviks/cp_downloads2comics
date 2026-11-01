#!/usr/bin/env python3
"""Duplicate warnings, renamed-series grouping, and publisher-home series.

Five things the user asked for after re-scanning 390 real downloads, tested here
against temp copies of a library and a downloads folder — never the real ones:

  A. A download already ANYWHERE in the library is reported, not only one sitting
     in the folder it is headed for. The real miss: 'The Cloven - Book Three'
     was in 'Fantagraphics (Europe)/' while the row was going to '/The Cloven/'.
  B. Two downloads that are the same book are reported on both rows (Kidz v01
     twice, The Cloven twice, the two Bonerest folders) and look-alikes are not
     (Revolution 9 006 / 009, Trekker Book 13 / 14).
  D. Renaming several rows to one new series gives ONE new folder for all of
     them, not eleven COPY_TO_BASE rows.
  E. A '## Publisher home' list in the rules file sends a series to its publisher
     folder ahead of the series-folder rule — 'The Cloven' lives in
     'Fantagraphics (Europe)' although a '/The Cloven/' folder exists.

These are warnings and routing. Nothing here unticks, skips or deletes anything.

Run:  python3 -m unittest discover tests
"""
import contextlib
import csv
import io
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path
from unittest import mock

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import paths

g = paths.load_generator()
mover = paths.load_mover()
srv = paths.load_serve_v2()

HTML = Path(paths.GENERATOR_DIR) / 'comic_organizer_v2.html'

CLOVEN_LIB = 'The Cloven - Book Three (2025) (Graphic Novel) (Fantagraphics) (Digital-HD) (LeDuch).cbz'
CLOVEN_CBR = 'The Cloven - Book Three (2025) (digital) (Mr Norrell-Empire).cbr'
CLOVEN_CBZ = 'The Cloven - Book Three (2025) (Graphic Novel) (Fantagraphics) (Digital-HD) (LeDuch).cbz'


def cbz(path: Path, pages: int = 3) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(path, 'w') as z:
        for i in range(pages):
            z.writestr(f'{i:03d}.jpg', b'x' * 10)
    return path


class Temp(unittest.TestCase):
    """A temp library and downloads folder, wired into the generator's globals."""

    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix='dupw-'))
        self.src, self.dest = self.tmp / 'src', self.tmp / 'dest'
        self.src.mkdir()
        self.dest.mkdir()
        self.saved = (g.SRC_DIR, g.DEST_DIR, g.OUTPUT_FILE)
        g.SRC_DIR, g.DEST_DIR = self.src, self.dest
        g.OUTPUT_FILE = self.src / 'matching_analysis_consolidated.csv'
        self.clear()

    def tearDown(self):
        g.SRC_DIR, g.DEST_DIR, g.OUTPUT_FILE = self.saved
        self.clear()
        shutil.rmtree(self.tmp, ignore_errors=True)

    def clear(self):
        for name in ('_DEST_FOLDER_INDEX', '_LIBRARY_INDEX', '_PAGE_COUNTS',
                     '_RULES_CACHE', '_CONTAINERS_CACHE', '_PUBLISHER_HOME_CACHE'):
            getattr(g, name, {}).clear()
        if hasattr(g, '_PUBLISHER_HOME_REPORTED'):
            g._PUBLISHER_HOME_REPORTED.clear()

    def lib(self, rel, pages=3):
        return cbz(self.dest / rel, pages)

    def down(self, rel, pages=3):
        return cbz(self.src / rel, pages)

    def scan(self):
        """Run the real generator over the temp folders and return its CSV rows."""
        self.clear()
        argv = ['generator', '--src', str(self.src), '--dest', str(self.dest)]
        with mock.patch.object(sys, 'argv', argv), contextlib.redirect_stdout(io.StringIO()):
            g.main()
        with open(g.OUTPUT_FILE, newline='', encoding='utf-8') as f:
            return list(csv.DictReader(f))

    def write_rules(self, *lines):
        (self.dest / '.comic_matching_rules.md').write_text(
            '# rules\n\n## Publisher home\n\n' + '\n'.join(lines) + '\n', encoding='utf-8')
        self.clear()


def by_file(rows):
    return {r['Left Panel File']: r for r in rows}


# ═══════════════════════════════════════════════════════════════════════════
# A. a copy anywhere in the library
# ═══════════════════════════════════════════════════════════════════════════

class TestCopiesAnywhereInTheLibrary(Temp):

    def setUp(self):
        super().setUp()
        self.lib('Fantagraphics (Europe)/' + CLOVEN_LIB, pages=4)
        self.lib('The Cloven/The Cloven - Book One (2023) (digital).cbz')
        self.down(CLOVEN_CBR, pages=4)
        self.folder = self.dest / 'The Cloven'

    def test_the_cloven_copy_in_the_publisher_folder_is_found(self):
        got = g.find_existing_copies(CLOVEN_CBR, self.folder)
        self.assertEqual([c.relative_to(self.dest).as_posix() for c in got],
                         ['Fantagraphics (Europe)/' + CLOVEN_LIB])

    def test_the_destination_folders_own_copy_is_still_found_and_listed_first(self):
        self.lib('The Cloven/The Cloven - Book Three (2025).cbz')
        got = [c.relative_to(self.dest).as_posix()
               for c in g.find_existing_copies(CLOVEN_CBR, self.folder)]
        self.assertEqual(got, ['The Cloven/The Cloven - Book Three (2025).cbz',
                               'Fantagraphics (Europe)/' + CLOVEN_LIB])

    def test_an_unrelated_volume_of_the_same_series_is_not(self):
        self.down('The Cloven - Book Two (2024) (digital).cbr')
        self.assertEqual(g.find_existing_copies(
            'The Cloven - Book Two (2024) (digital).cbr', self.folder), [])

    def test_a_copy_in_a_subfolder_one_level_down_is_found(self):
        self.lib('2000AD - Collections/PSI Division/Psi-Division v01 (2019) (digital).cbz')
        got = g.find_existing_copies('Psi-Division v01 (2024) (digital-Empire).cbr',
                                     self.dest / 'Psi-Division')
        self.assertEqual([c.relative_to(self.dest).as_posix() for c in got],
                         ['2000AD - Collections/PSI Division/Psi-Division v01 (2019) (digital).cbz'])

    def test_a_copy_in_a_loose_file_at_the_library_root_is_found(self):
        self.lib('Saga v01 (2012).cbz')
        got = g.find_existing_copies('Saga v01 (2013) (digital).cbr', self.dest / 'Saga')
        self.assertEqual([c.name for c in got], ['Saga v01 (2012).cbz'])

    def test_the_library_index_stops_one_level_below_a_top_level_folder(self):
        """Depth is a cost decision: the walk stays at root, folder, subfolder."""
        self.lib('Shelf/Sub/Deeper/Hidden v01 (2019).cbz')
        got = g.find_existing_copies('Hidden v01 (2024) (digital).cbr', self.dest / 'Hidden')
        self.assertEqual(got, [])

    def test_the_index_is_built_once_per_library(self):
        first = g.index_library()
        self.assertIs(first, g.index_library())

    def test_describe_reports_path_size_and_pages_in_the_three_parallel_columns(self):
        names, sizes, pages = g.describe_existing_copies([CLOVEN_CBR], '/The Cloven/')
        self.assertEqual(names, f'{CLOVEN_CBR} => Fantagraphics (Europe)/{CLOVEN_LIB}')
        self.assertEqual(pages, '4p => 4p')
        self.assertEqual(sizes.count('=>'), 1)

    def test_a_row_that_files_nowhere_in_particular_still_hears_about_a_copy(self):
        """COPY_TO_BASE has no folder; the library is the only place to look."""
        names, _, _ = g.describe_existing_copies([CLOVEN_CBR], '/')
        self.assertIn('Fantagraphics (Europe)/', names)

    def test_a_scan_puts_the_copy_on_the_row(self):
        rows = by_file(self.scan())
        self.assertIn('Fantagraphics (Europe)/', rows[CLOVEN_CBR]['Existing Copies'])


class TestTheMoverGateAsksAboutBoth(Temp):

    def test_a_copy_in_the_folder_and_a_copy_elsewhere_are_two_questions(self):
        self.lib('The Cloven/The Cloven - Book Three (2025).cbz')
        self.lib('Fantagraphics (Europe)/' + CLOVEN_LIB)
        self.lib('Elsewhere/Saga v01 (2012).cbz')
        self.lib('Saga/Saga v02 (2013).cbz')
        self.down(CLOVEN_CBR)
        self.down('Saga v01 (2013) (digital).cbr')
        rows = self.scan()
        mover.DUPLICATE_DECISIONS.clear()
        try:
            self.assertEqual(sorted(mover.undecided_duplicates(rows)),
                             sorted([CLOVEN_CBR, 'Saga v01 (2013) (digital).cbr']))
            mover.DUPLICATE_DECISIONS.update({CLOVEN_CBR: 'skip'})
            self.assertEqual(mover.undecided_duplicates(rows),
                             ['Saga v01 (2013) (digital).cbr'])
        finally:
            mover.DUPLICATE_DECISIONS.clear()

    def test_skip_still_means_dont_file_this_download(self):
        self.lib('Fantagraphics (Europe)/' + CLOVEN_LIB)
        self.lib('The Cloven/The Cloven - Book One (2023).cbz')
        self.down(CLOVEN_CBR)
        rows = self.scan()
        with open(g.OUTPUT_FILE, newline='') as f:
            self.assertIn('Existing Copies', f.readline())
        decisions = self.tmp / 'd.json'
        decisions.write_text(json.dumps({CLOVEN_CBR: 'skip'}))
        out = subprocess.run(
            [sys.executable, 'comic_mover.py', '--execute', '--no-confirm',
             '--src', str(self.src), '--dest', str(self.dest),
             '--duplicate-decisions', str(decisions)],
            cwd=paths.GENERATOR_DIR, capture_output=True, text=True, timeout=60)
        self.assertEqual(out.returncode, 0, out.stdout + out.stderr)
        self.assertTrue((self.src / CLOVEN_CBR).exists())
        self.assertTrue(rows)


# ═══════════════════════════════════════════════════════════════════════════
# B. two downloads that are the same book
# ═══════════════════════════════════════════════════════════════════════════

KIDZ_A = 'Kidz v01 (2020) (Digital) (DR & Quinch-Empire).cbr'
KIDZ_B = 'Kidz v01 (2020) (digital) (Dr.Vink).cbz'
REV_6 = 'Revolution 9 006 (2026) (digital) (Knight Ripper-Empire).cbr'
REV_9 = 'Revolution 9 009 (2026) (digital) (Knight Ripper-Empire).cbr'
TREK_13 = 'Trekker (Book 13) - Chapeltown (2018) (digital) (Son of Ultron-Empire).cbr'
TREK_14 = 'Trekker (Book 14) - The Darkstar Zephyr (2019) (digital) (Son of Ultron-Empire).cbr'
GW_GN = 'Graveyard Wars (2020) (Graphic Novel) (Ablaze) (Digital-HD) (LeDuch).cbz'
GW_V1 = 'Graveyard Wars v01 (2020) (Digital) (DR & Quinch-Empire).cbr'
BONE_A = "Bonerest - A World's End 001-008 (2005-2006) (Darthscanner-DCP)"
BONE_B = "Bonerest - A World's End 01-08 (2005-2006)"


class TestTwinsInDownloads(Temp):

    def setUp(self):
        super().setUp()
        self.lib('Placeholder/Placeholder 001 (2020).cbz')
        self.down(KIDZ_A, pages=10)
        self.down(KIDZ_B, pages=10)
        self.down(CLOVEN_CBR, pages=4)
        self.down(CLOVEN_CBZ, pages=6)
        self.down(REV_6)
        self.down(REV_9)
        self.down(TREK_13)
        self.down(TREK_14)
        self.down(GW_GN)
        self.down(GW_V1)
        for i in range(1, 4):
            self.down(f"{BONE_A}/Bonerest - A World's End 00{i} (2005) (DarthScanner-DCP).cbr")
            self.down(f"{BONE_B}/Bonerest - A World's End 0{i} (2005).cbz")
        self.rows = self.scan()
        self.row = by_file(self.rows)

    def test_the_csv_has_the_new_column(self):
        self.assertIn('Also In Downloads', self.rows[0])

    def test_kidz_is_found_on_both_rows_with_size_and_pages(self):
        a, b = self.row[KIDZ_A]['Also In Downloads'], self.row[KIDZ_B]['Also In Downloads']
        self.assertTrue(a.startswith(f'{KIDZ_B} => '), a)
        self.assertTrue(b.startswith(f'{KIDZ_A} => '), b)
        self.assertIn('10p', a)

    def test_the_cloven_pair_is_found_on_both_rows(self):
        self.assertIn(CLOVEN_CBZ, self.row[CLOVEN_CBR]['Also In Downloads'])
        self.assertIn(CLOVEN_CBR, self.row[CLOVEN_CBZ]['Also In Downloads'])

    def test_two_volumes_of_one_series_are_not_twins(self):
        for name in (REV_6, REV_9, TREK_13, TREK_14):
            self.assertEqual(self.row[name]['Also In Downloads'], '', name)

    def test_the_graveyard_wars_graphic_novel_and_v01_are_not_paired(self):
        """The user's call; duplicates.looks_like_one_book() says they are not.

        'v01' is a token the graphic-novel filename does not carry, so the title
        signatures differ. Recorded here so a change to the judge shows up as a
        failing test rather than as a surprise on the page.
        """
        for name in (GW_GN, GW_V1):
            self.assertEqual(self.row[name]['Also In Downloads'], '', name)

    def test_the_two_bonerest_folders_are_reported_as_the_same_set_on_both_rows(self):
        a = [r for r in self.rows if r['Left Folder'] == BONE_A][0]
        b = [r for r in self.rows if r['Left Folder'] == BONE_B][0]
        self.assertEqual(a['Also In Downloads'], f'same 3 books as {BONE_B}')
        self.assertEqual(b['Also In Downloads'], f'same 3 books as {BONE_A}')

    def test_a_row_with_no_twin_says_nothing(self):
        self.assertEqual(self.row['Placeholder 001 (2020).cbz']['Also In Downloads']
                         if 'Placeholder 001 (2020).cbz' in self.row else '', '')


class TestFoldersThatOnlyHalfOverlapAreNotTheSameSet(Temp):

    def test_one_shared_book_is_a_file_twin_not_a_set(self):
        self.lib('Placeholder/Placeholder 001 (2020).cbz')
        for i in (1, 2, 3):
            self.down(f'Aaa Set/Aaa {i:02d} (2020).cbz')
        for i in (3, 4, 5):
            self.down(f'Aaa Other/Aaa {i:02d} (2021).cbr')
        rows = self.scan()
        notes = [r['Also In Downloads'] for r in rows if r['Left Folder'].startswith('Aaa')]
        self.assertTrue(notes)
        self.assertFalse(any(n.startswith('same ') for n in notes), notes)
        self.assertTrue(all(n for n in notes))


# ═══════════════════════════════════════════════════════════════════════════
# D. renamed rows that share a new series
# ═══════════════════════════════════════════════════════════════════════════

class TestRenamedRowsShareAFolder(Temp):

    FILES = ['Aaa One 001 (2020).cbr', 'Bbb Two 001 (2020).cbr', 'Ccc Three 001 (2020).cbr']

    def setUp(self):
        super().setUp()
        self.lib('Existing Series (2019)/Existing Series 001 (2019).cbz')
        for n in self.FILES:
            self.down(n)

    def rescan(self, renames):
        return g.rescan_renamed(renames, g.scan_destination_directory())

    def test_three_renamed_to_a_new_series_all_get_one_new_folder(self):
        out = self.rescan([{'left_file': n, 'new_series': 'Trekker'} for n in self.FILES])
        self.assertEqual({r['Action Type'] for r in out}, {'CREATE_FOLDER_WITH_FILES'})
        self.assertEqual({r['Suggested Folder Name'] for r in out}, {'/Trekker/'})
        self.assertEqual([r['left_file'] for r in out], self.FILES)

    def test_renaming_one_alone_is_as_today(self):
        out = self.rescan([{'left_file': self.FILES[0], 'new_series': 'Trekker'}])
        self.assertEqual(out[0]['Action Type'], 'COPY_TO_BASE')
        self.assertEqual(out[0]['Suggested Folder Name'], '/')

    def test_renaming_to_a_series_the_library_has_consolidates_as_today(self):
        out = self.rescan([{'left_file': n, 'new_series': 'Existing Series'} for n in self.FILES])
        self.assertEqual({r['Action Type'] for r in out}, {'CONSOLIDATE'})
        self.assertEqual({r['Suggested Folder Name'] for r in out}, {'/Existing Series (2019)/'})

    def test_two_different_new_series_are_two_groups(self):
        out = self.rescan([
            {'left_file': self.FILES[0], 'new_series': 'Trekker'},
            {'left_file': self.FILES[1], 'new_series': 'trekker'},
            {'left_file': self.FILES[2], 'new_series': 'Other'}])
        self.assertEqual([r['Action Type'] for r in out],
                         ['CREATE_FOLDER_WITH_FILES', 'CREATE_FOLDER_WITH_FILES', 'COPY_TO_BASE'])
        self.assertEqual(out[0]['Suggested Folder Name'], out[1]['Suggested Folder Name'])

    def test_the_server_runs_the_same_rescan_for_the_page(self):
        out = srv.run_rescan([{'left_file': n, 'new_series': 'Trekker'} for n in self.FILES],
                             str(self.dest))
        self.assertEqual({r['Suggested Folder Name'] for r in out}, {'/Trekker/'})
        self.assertEqual({r['Action Type'] for r in out}, {'CREATE_FOLDER_WITH_FILES'})

    def test_the_overrides_reach_the_mover_and_a_dry_run_moves_all_three_into_trekker(self):
        self.scan()
        out = srv.run_rescan([{'left_file': n, 'new_series': 'Trekker'} for n in self.FILES],
                             str(self.dest))
        overrides = self.tmp / 'o.json'
        overrides.write_text(json.dumps([
            {'left_file': r['left_file'], 'series_name': 'Trekker',
             'dest_folder': r['Suggested Folder Name']} for r in out]))
        run = subprocess.run(
            [sys.executable, 'comic_mover.py', '--dry-run', '--src', str(self.src),
             '--dest', str(self.dest), '--overrides', str(overrides)],
            cwd=paths.GENERATOR_DIR, capture_output=True, text=True, timeout=60)
        self.assertEqual(run.returncode, 0, run.stdout + run.stderr)
        for n in self.FILES:
            self.assertIn(n, run.stdout)
        for n in self.FILES:
            self.assertIn('→ ' + str(self.dest / 'Trekker' / n), run.stdout)
        self.assertIn('Destination folders to ensure exist: 1', run.stdout)
        self.assertFalse((self.dest / 'Trekker').exists(), 'a dry run creates nothing')

    def test_the_page_sends_every_renamed_row_and_updates_the_others(self):
        html = HTML.read_text(encoding='utf-8')
        self.assertIn('renamed', html)
        self.assertIn("'/api/rescan-series'", html)
        # The multi-select path used to say 'no rescan'.
        self.assertNotIn('Option B: apply series override to all selected rows, no rescan', html)


# ═══════════════════════════════════════════════════════════════════════════
# E. series that live in their publisher folder
# ═══════════════════════════════════════════════════════════════════════════

class TestPublisherHome(Temp):

    def setUp(self):
        super().setUp()
        self.lib('The Cloven/The Cloven - Book One (2023) (digital).cbz')
        self.lib('Fantagraphics (Europe)/Some Other Book (2020).cbz')
        self.lib('Adventures of Blake & Mortimer/Blake & Mortimer 01 (2020).cbz')
        self.down(CLOVEN_CBR)
        self.down('Adventures of Blake & Mortimer 02 (2021) (Cinebook).cbz')
        self.lib('Cinebook (Europe)/Lucky Luke 01 (2020) (Cinebook).cbz')

    def folder_for(self, name):
        return by_file(self.scan())[name]['Suggested Folder Name']

    def test_without_the_list_the_series_folder_wins(self):
        self.assertEqual(self.folder_for(CLOVEN_CBR), '/The Cloven/')

    def test_with_the_line_the_publisher_folder_wins_even_though_the_series_folder_exists(self):
        self.write_rules('- The Cloven => Fantagraphics (Europe)')
        row = by_file(self.scan())[CLOVEN_CBR]
        self.assertEqual(row['Suggested Folder Name'], '/Fantagraphics (Europe)/')
        self.assertEqual(row['Action Type'], 'CONSOLIDATE')
        self.assertEqual(row['Confidence'], 'PUBLISHER_HOME')
        self.assertEqual(row['Proposed Filename'], '', 'a publisher folder never renames a file')

    def test_blake_and_mortimer_still_goes_to_its_own_folder(self):
        self.write_rules('- The Cloven => Fantagraphics (Europe)')
        self.assertEqual(self.folder_for('Adventures of Blake & Mortimer 02 (2021) (Cinebook).cbz'),
                         '/Adventures of Blake & Mortimer/')

    def test_the_series_match_is_on_the_series_key_not_the_spelling(self):
        self.write_rules('- the cloven => Fantagraphics (Europe)')
        self.assertEqual(self.folder_for(CLOVEN_CBR), '/Fantagraphics (Europe)/')
        self.write_rules('- Cloven => Fantagraphics (Europe)')
        self.assertEqual(self.folder_for(CLOVEN_CBR), '/Fantagraphics (Europe)/')
        self.write_rules('- The Cloven Saga => Fantagraphics (Europe)')
        self.assertEqual(self.folder_for(CLOVEN_CBR), '/The Cloven/')

    def test_a_bad_target_is_ignored_and_reported_once(self):
        self.write_rules('- The Cloven => No Such Folder')
        self.down('The Cloven - Book Four (2026) (digital).cbr')
        log = io.StringIO()
        with contextlib.redirect_stdout(log):
            self.clear()
            self.write_rules('- The Cloven => No Such Folder')
            dest_map = g.scan_destination_directory()
            a = g.find_matches(CLOVEN_CBR, 'The Cloven', dest_map)
            b = g.find_matches('The Cloven - Book Four (2026) (digital).cbr', 'The Cloven', dest_map)
        self.assertEqual(a[0], 'The Cloven')
        self.assertEqual(b[0], 'The Cloven')
        self.assertEqual(log.getvalue().count('No Such Folder'), 1, log.getvalue())

    def test_a_missing_section_or_file_has_no_effect(self):
        self.assertEqual(self.folder_for(CLOVEN_CBR), '/The Cloven/')
        (self.dest / '.comic_matching_rules.md').write_text('# rules\n\n## Accept (0)\n')
        self.clear()
        self.assertEqual(self.folder_for(CLOVEN_CBR), '/The Cloven/')

    def test_the_writer_adds_the_line_in_its_own_section_and_the_matcher_reads_it(self):
        path = self.dest / '.comic_matching_rules.md'
        msg = srv.save_publisher_home(path, 'The Cloven', 'Fantagraphics (Europe)')
        self.assertIn('Fantagraphics (Europe)', msg)
        self.assertIn('- The Cloven => Fantagraphics (Europe)', path.read_text())
        self.clear()
        self.assertEqual(self.folder_for(CLOVEN_CBR), '/Fantagraphics (Europe)/')

    def test_the_writer_replaces_an_earlier_line_for_the_same_series(self):
        path = self.dest / '.comic_matching_rules.md'
        srv.save_publisher_home(path, 'The Cloven', 'Cinebook (Europe)')
        srv.save_publisher_home(path, 'the cloven', 'Fantagraphics (Europe)')
        text = path.read_text()
        self.assertEqual(text.lower().count('the cloven =>'), 1)
        self.assertIn('Fantagraphics (Europe)', text)

    def test_the_writer_keeps_accept_and_refuse_rules_and_counts_honest(self):
        path = self.dest / '.comic_matching_rules.md'
        srv.save_matching_rule(path, 'Star Trek', 'accept')
        srv.save_publisher_home(path, 'The Cloven', 'Fantagraphics (Europe)')
        text = path.read_text()
        self.assertIn('- Star Trek', text)
        self.assertIn('## Publisher home (1)', text)
        self.assertIn('## Accept (1)', text)

    def test_the_writer_refuses_text_that_could_forge_rules(self):
        path = self.dest / '.comic_matching_rules.md'
        for series, folder in [('A\n## Accept', 'X'), ('A', 'B\n- C'), ('A => B', 'X'),
                               ('', 'X'), ('A', ''), ('A', 'a/b')]:
            with self.assertRaises(ValueError, msg=(series, folder)):
                srv.save_publisher_home(path, series, folder)

    def test_the_button_is_on_the_page_and_the_keywords_are_the_matchers(self):
        html = HTML.read_text(encoding='utf-8')
        self.assertIn('/api/publisher-home-folder', html)       # the button names its folder (was a fixed label)
        self.assertIn('>File ${esc(row.series)} in ${esc(folder)}<', html)
        m = re.search(r'PUBLISHER_KEYWORDS\s*=\s*\[([^\]]*)\]', html)
        self.assertTrue(m, 'the page needs the keyword list')
        self.assertEqual(set(re.findall(r'"([^"]+)"', m.group(1))), set(g.PUBLISHER_KEYWORDS))


# ═══════════════════════════════════════════════════════════════════════════
# C. the page
# ═══════════════════════════════════════════════════════════════════════════

class TestThePage(unittest.TestCase):

    def setUp(self):
        self.html = HTML.read_text(encoding='utf-8')

    def test_there_is_a_duplicates_chip_and_a_warning_badge(self):
        self.assertIn('Duplicates', self.html)
        self.assertIn('already in library:', self.html)
        self.assertIn('also in Downloads:', self.html)
        self.assertIn('identical', self.html)

    def test_the_page_reads_the_new_column(self):
        self.assertIn('Also In Downloads', self.html)


def page_functions(*names):
    """Source of the named top-level functions in the page, for running in node."""
    html = HTML.read_text(encoding='utf-8')
    out = []
    for name in names:
        start = html.index(f'function {name}(')
        depth, i = 0, html.index('{', start)
        for j in range(i, len(html)):
            depth += (html[j] == '{') - (html[j] == '}')
            if depth == 0:
                out.append(html[start:j + 1])
                break
    return '\n'.join(out)


def page_counts(rows):
    """What the page's own warningCounts() and bar text make of these CSV rows."""
    js = (page_functions('existingCopies', 'isIdentical', 'alsoInDownloads',
                         'warningOf', 'warningCounts', 'warningBarText')
          + '\nconst rows = JSON.parse(require("fs").readFileSync(0, "utf8"));'
          + '\nconst c = warningCounts(rows);'
          + '\nconsole.log(JSON.stringify({c, text: warningBarText(c)}));')
    out = subprocess.run(['node', '-e', js], input=json.dumps(rows), capture_output=True,
                         text=True, timeout=30)
    if out.returncode:
        raise AssertionError(out.stderr)
    return json.loads(out.stdout)


# ═══════════════════════════════════════════════════════════════════════════
# journey: scan -> Duplicates chip rows -> rename Trekker rows -> one folder -> dry run
# ═══════════════════════════════════════════════════════════════════════════

class TestJourney(Temp):

    def test_scan_then_rename_then_dry_run(self):
        self.lib('Fantagraphics (Europe)/' + CLOVEN_LIB, pages=4)
        self.lib('The Cloven/The Cloven - Book One (2023).cbz')
        self.down(CLOVEN_CBR)
        self.down(KIDZ_A)
        self.down(KIDZ_B)
        self.down(REV_6)
        self.down(REV_9)
        trek = ['Zzz Alpha 001 (2020).cbr', 'Yyy Beta 001 (2020).cbr', 'Xxx Gamma 001 (2020).cbr']
        for n in trek:
            self.down(n)
        rows = self.scan()

        flagged = {r['Left Panel File'] for r in rows
                   if r['Existing Copies'] or r['Also In Downloads']}
        self.assertEqual(flagged, {CLOVEN_CBR, KIDZ_A, KIDZ_B})

        # The summary bar: its numbers are the rows' numbers, in Python and in
        # the page's own JavaScript.
        counts = g.warning_counts(rows)
        self.assertEqual(counts, {'library': 1, 'identical': 0, 'downloads': 2, 'total': 3})
        if shutil.which('node'):
            shown = page_counts(rows)
            self.assertEqual(shown['c'], counts)
            self.assertEqual(shown['text'], 'You have 3 warnings: 1 already in library '
                                            '(0 identical), 2 also in Downloads')
            self.assertEqual(page_counts([])['text'], '')

        out = srv.run_rescan([{'left_file': n, 'new_series': 'Trekker'} for n in trek],
                             str(self.dest))
        self.assertEqual({r['Suggested Folder Name'] for r in out}, {'/Trekker/'})

        overrides = self.tmp / 'o.json'
        overrides.write_text(json.dumps([
            {'left_file': r['left_file'], 'series_name': 'Trekker',
             'dest_folder': r['Suggested Folder Name']} for r in out]))
        run = subprocess.run(
            [sys.executable, 'comic_mover.py', '--dry-run', '--src', str(self.src),
             '--dest', str(self.dest), '--overrides', str(overrides)],
            cwd=paths.GENERATOR_DIR, capture_output=True, text=True, timeout=60)
        self.assertEqual(run.returncode, 0, run.stdout + run.stderr)
        for n in trek:
            self.assertIn('→ ' + str(self.dest / 'Trekker' / n), run.stdout)
        # ... and the Cloven copy elsewhere in the library is asked about.
        self.assertIn(CLOVEN_CBR, run.stdout.split('Planning moves')[0])


# ═══════════════════════════════════════════════════════════════════════════
# follow-up fixes (Opus review of 4419a9d)
# ═══════════════════════════════════════════════════════════════════════════

import duplicates  # noqa: E402  (paths puts the app directory on sys.path)

COSMO_1 = 'Cosmoknights (Book 01) (2019) (digital) (Son of Ultron-Empire).cbz'
COSMO_2 = 'Cosmoknights (Book 02) (2023) (digital) (Son of Ultron-Empire).cbz'


class TestVolumeMarkerInsideBrackets(unittest.TestCase):
    """'(Book 01)' is the book, not packaging, even though it sits in brackets."""

    def one_book(self, a, b):
        return duplicates.looks_like_one_book([a, b])

    def test_cosmoknights_book_01_and_02_are_two_books(self):
        self.assertFalse(self.one_book(COSMO_1, COSMO_2))

    def test_a_bracketed_marker_equals_the_bare_one(self):
        self.assertTrue(self.one_book('X (Book 01) (2019).cbz', 'X Book 01 (2020).cbz'))

    def test_every_marker_form_counts(self):
        for a, b in (('X (Vol 1) (2019).cbz', 'X (Vol 2) (2019).cbz'),
                     ('X (Vol. 1) (2019).cbz', 'X (Vol. 2) (2019).cbz'),
                     ('X (Volume 1) (2019).cbz', 'X (Volume 2) (2019).cbz'),
                     ('X (v1) (2019).cbz', 'X (v2) (2019).cbz'),
                     ('X (Part 1) (2019).cbz', 'X (Part 2) (2019).cbz')):
            self.assertFalse(self.one_book(a, b), (a, b))

    def test_the_same_bracketed_marker_with_other_padding_is_one_book(self):
        self.assertTrue(self.one_book('X (Vol 1) (2019).cbz', 'X (Vol 01) (2020).cbz'))

    def test_a_bracketed_part_equals_a_bare_part(self):
        self.assertTrue(self.one_book('X (Part 2) (2019).cbz', 'X Part 2 (2020).cbz'))

    def test_years_and_packer_tags_are_still_ignored(self):
        self.assertTrue(self.one_book('Hound (2022) (digital) (Empire).cbz',
                                      'Hound (2024) (digital) (Other).cbz'))
        self.assertTrue(self.one_book(REV_6, REV_6.replace('2026', '2027')))

    def test_trekker_13_and_14_stay_apart_and_the_pairs_still_pair(self):
        self.assertFalse(self.one_book(TREK_13, TREK_14))
        self.assertTrue(self.one_book(KIDZ_A, KIDZ_B))
        self.assertTrue(self.one_book(CLOVEN_CBR, CLOVEN_CBZ))
        self.assertTrue(self.one_book(f"{BONE_A}/Bonerest - A World's End 001 (2005).cbr",
                                      f"{BONE_B}/Bonerest - A World's End 01 (2005).cbz"))


class TestCosmoknightsAreNotTwinsOnTheScan(Temp):
    def test_two_books_of_one_series_are_not_reported_as_twins(self):
        self.down(COSMO_1)
        self.down(COSMO_2)
        rows = by_file(self.scan())
        self.assertEqual(rows[COSMO_1]['Also In Downloads'], '')
        self.assertEqual(rows[COSMO_2]['Also In Downloads'], '')


# 2. 'identical' means the same bytes, decided in the generator ----------------

def cbz_payload(path: Path, pages: int, payload: bytes) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(path, 'w') as z:
        for i in range(pages):
            z.writestr(f'{i:03d}.jpg', payload)
    return path


class TestIdenticalMeansTheSameBytes(Temp):

    def test_same_megabyte_and_pages_but_different_bytes_is_not_identical(self):
        self.lib('Saga/Saga 001 (2020).cbz', pages=3)
        cbz_payload(self.src / 'Saga 001 (2020) (digital).cbz', 3, b'y' * 11)
        row = by_file(self.scan())['Saga 001 (2020) (digital).cbz']
        # Both read '0 MB' and '3p', which is what the old test called identical.
        self.assertEqual(row['Existing Copy Sizes'], '0 MB => 0 MB')
        self.assertEqual(row['Existing Copy Pages'], '3p => 3p')
        self.assertEqual(row['Existing Copy Identical'], 'no')
        self.assertEqual(g.warning_counts([row])['identical'], 0)

    def test_the_same_bytes_and_pages_is_identical(self):
        shutil.copy(self.lib('Saga/Saga 001 (2020).cbz'), self.src / 'Saga 001 (2020) (digital).cbz')
        row = by_file(self.scan())['Saga 001 (2020) (digital).cbz']
        self.assertEqual(row['Existing Copy Identical'], 'yes')
        self.assertEqual(g.warning_counts([row])['identical'], 1)

    def test_one_identical_copy_among_two_does_not_make_the_row_identical(self):
        orig = self.lib('Saga/Saga 001 (2020).cbz')
        shutil.copy(orig, self.src / 'Saga 001 (2020) (digital).cbz')
        cbz_payload(self.dest / 'Other' / 'Saga 001 (2021).cbz', 3, b'z' * 12)
        row = by_file(self.scan())['Saga 001 (2020) (digital).cbz']
        self.assertEqual(row['Existing Copy Identical'], 'yes | no')
        self.assertEqual(g.warning_counts([row])['identical'], 0)

    def test_twins_get_the_same_verdict(self):
        shutil.copy(self.down(KIDZ_A, pages=4), self.src / KIDZ_B)
        row = by_file(self.scan())
        self.assertEqual(row[KIDZ_A]['Also In Downloads Identical'], 'yes')
        self.assertEqual(row[KIDZ_B]['Also In Downloads Identical'], 'yes')
        # The bar's '(Y identical)' belongs to 'already in library' only.
        self.assertEqual(g.warning_counts(list(row.values()))['identical'], 0)

    def test_twins_with_different_bytes_are_not_identical(self):
        self.down(KIDZ_A, pages=4)
        cbz_payload(self.src / KIDZ_B, 4, b'q' * 13)
        row = by_file(self.scan())
        self.assertEqual(row[KIDZ_A]['Also In Downloads Identical'], 'no')

    def test_a_folder_set_is_never_called_identical(self):
        for i in range(1, 3):
            self.down(f"{BONE_A}/Bonerest - A World's End 00{i} (2005).cbr")
            self.down(f"{BONE_B}/Bonerest - A World's End 0{i} (2005).cbz")
        rows = self.scan()
        a = [r for r in rows if r['Left Folder'] == BONE_A][0]
        self.assertTrue(a['Also In Downloads'].startswith('same 2 books'))
        self.assertEqual(a['Also In Downloads Identical'], 'no')

    def test_the_bar_matches_the_rows_in_python_and_in_the_page(self):
        shutil.copy(self.lib('Saga/Saga 001 (2020).cbz'), self.src / 'Saga 001 (2020) (digital).cbz')
        self.lib('Saga/Saga 002 (2020).cbz')
        cbz_payload(self.src / 'Saga 002 (2020) (digital).cbz', 3, b'y' * 11)
        shutil.copy(self.down(KIDZ_A, pages=4), self.src / KIDZ_B)
        rows = self.scan()
        counts = g.warning_counts(rows)
        self.assertEqual(counts, {'library': 2, 'identical': 1, 'downloads': 2, 'total': 4})
        if shutil.which('node'):
            self.assertEqual(page_counts(rows)['c'], counts)

    def test_an_old_csv_without_the_columns_shows_no_identical(self):
        old = [{'Left Panel File': 'a.cbz', 'Existing Copies': 'a.cbz => X/a.cbz',
                'Existing Copy Sizes': '5 MB => 5 MB', 'Existing Copy Pages': '3p => 3p',
                'Also In Downloads': 'b.cbz => 5 MB, 3p (this: 5 MB, 3p)'}]
        self.assertEqual(g.warning_counts(old)['identical'], 0)
        if shutil.which('node'):
            self.assertEqual(page_counts(old)['c']['identical'], 0)

    def test_the_page_comment_no_longer_claims_size_to_the_mb(self):
        self.assertNotIn('size shown AND the page count', HTML.read_text(encoding='utf-8'))


# 3. a backup before every rules-file write -----------------------------------

class TestRulesFileBackup(unittest.TestCase):

    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix='dupw-rules-'))
        self.rules = self.tmp / '.comic_matching_rules.md'
        self.bak = self.tmp / '.comic_matching_rules.md.bak'
        self.addCleanup(shutil.rmtree, self.tmp, ignore_errors=True)

    def writers(self):
        return (lambda: srv.save_matching_rule(self.rules, 'Some Folder', 'accept'),
                lambda: srv.save_publisher_home(self.rules, 'The Cloven', 'Fantagraphics (Europe)'))

    def test_no_file_yet_means_no_backup(self):
        for write in self.writers():
            self.rules.unlink(missing_ok=True)
            self.bak.unlink(missing_ok=True)
            write()
            self.assertTrue(self.rules.exists())
            self.assertFalse(self.bak.exists())

    def test_the_old_file_is_copied_before_it_is_rewritten(self):
        for write in self.writers():
            self.rules.write_text('# mine\n\n## Accept (0)\n\n## Refuse (0)\n\n## Publisher home (0)\n',
                                  encoding='utf-8')
            before = self.rules.read_text(encoding='utf-8')
            write()
            self.assertEqual(self.bak.read_text(encoding='utf-8'), before)
            self.assertNotEqual(self.rules.read_text(encoding='utf-8'), before)

    def test_a_second_write_replaces_the_previous_backup(self):
        write_rule, write_home = self.writers()
        write_rule()
        after_first = self.rules.read_text(encoding='utf-8')
        write_home()
        self.assertEqual(self.bak.read_text(encoding='utf-8'), after_first)


if __name__ == '__main__':
    unittest.main()
