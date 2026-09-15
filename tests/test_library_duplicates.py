#!/usr/bin/env python3
"""A duplicate report that is wrong in the generous direction deletes a book.

duplicates.py groups files by what release.parse_release() makes of them,
which means two files land together whenever the thing that told them apart is
the thing the parser discards. It discards a lot: issue numbers under a 'Book N'
marker, subtitles, and anything the folder above knew that the filename did not.

So the report never presents a group as a duplicate on the strength of the parse
alone. It re-reads the filenames for evidence the parser threw away, and any
disagreement demotes the group to 'check these by hand'. Every case below is one
that was actually found in the library at /mnt/extramedia/Comics and would have
been listed as a likely duplicate without the check that follows it.

The asymmetry is deliberate and these tests pin it: a true duplicate wrongly sent
to the review pile costs a minute of reading, and a false duplicate left in the
likely pile costs a book.

Run:  python3 -m unittest discover tests
"""
import os
import sys
import unittest
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import paths

dup = paths.load_duplicates()

def files(*rel):
    """Paths relative to whatever root they were found under, as the rules take."""
    return [Path(r) for r in rel]


class TestTitleSignature(unittest.TestCase):
    """What survives a filename once the packaging is stripped off."""

    def test_the_same_volume_spelled_three_ways_agrees(self):
        # Found as 'batman by grant morrison v1'. 'v01' is a single token, so
        # stripping format words and leading zeros as separate steps left it
        # unequal to 'Vol 1' and a real duplicate was demoted.
        spellings = [
            'Batman by Grant Morrison Omnibus v01 (2018) (hybrid) (Marika-Empire).cbz',
            'BATMAN BY GRANT MORRISON, BOOK 1 (DC) (MiracleScans Ltd).cbr',
            'Batman by Grant Morrison Vol 1.cbz',
        ]
        self.assertEqual(len({dup.title_signature(s) for s in spellings}), 1)

    def test_the_year_and_the_packer_do_not_tell_two_copies_apart(self):
        """The whole point: same book, two rips, listed together."""
        self.assertEqual(
            dup.title_signature('Shakara v02 - The Destroyer (2012) (digital-SD) (Torquemada).cbr'),
            dup.title_signature('Shakara v02 - The Destroyer (2012) (digital SD) (Torquemada).cbr'))

    def test_a_subtitle_keeps_two_collected_editions_apart(self):
        # parse_release() drops subtitles, so six different Harley Quinn v02s
        # collapsed to one key and the report called them duplicates.
        self.assertNotEqual(
            dup.title_signature('Harley Quinn v02 - Keepsake (2022) (digital).cbz'),
            dup.title_signature('Harley Quinn v02 - Power Outage (2015).cbz'))

    def test_an_issue_number_under_a_book_marker_still_counts(self):
        # 'Book Two' sets kind=volume and discards the issue, so #01 and #03 of
        # Starhenge parsed identically.
        self.assertNotEqual(
            dup.title_signature('Starhenge Book Two - a Kiss for Atticus 03.cbz'),
            dup.title_signature('Starhenge Book Two - A Kiss For Atticus 01.cbz'))


class TestFolderVolumes(unittest.TestCase):
    """A folder can carry the volume number the filenames inside it leave out."""

    def test_a_folder_naming_one_volume_speaks_for_the_file(self):
        self.assertEqual(
            dup.folder_volumes(Path('Terra Obscura Volume 2/Terra Obscura #003.cbr')),
            frozenset({2}))

    def test_a_folder_naming_a_range_speaks_for_none_of_them(self):
        """'Shakara (v01-v02)' holds both books, so it identifies neither."""
        self.assertEqual(
            dup.folder_volumes(Path(
                'Shakara (v01-v02)(2008-2012)(digital-SD)(Torquemada)/'
                'Shakara v02 - The Destroyer (2012) (digital-SD) (Torquemada).cbr')),
            frozenset())


class TestLooksLikeOneBook(unittest.TestCase):

    def test_two_rips_of_one_book_are_one_book(self):
        self.assertTrue(dup.looks_like_one_book(files(
            'Insurrection/Insurrection v02 - Liberty (2015) (digital) (Torquemada).cbr',
            '2000AD - Collections/Insurrection/Insurrection v02 - Liberty (2015) (digital) (Torquemada).cbr',
        )))

    def test_a_cover_only_scan_is_not_the_issue_it_came_from(self):
        # 1 MB of covers and the 42 MB issue parsed to the same key because the
        # tag that says so lives in parentheses, which get cut.
        self.assertFalse(dup.looks_like_one_book(files(
            'New Avengers (2010)/New Avengers 001 (5 covers) (c2c) (2010) (Minutemen-Danger&Darth).cbr',
            'New Avengers (2010)/New Avengers 001 (2010) (2nd Printing Variant) (Cover ONLY) (ScanDog).cbr',
        )))

    def test_two_volumes_of_one_series_are_not_one_book(self):
        """Identical filenames; only the folder above knows they differ."""
        self.assertFalse(dup.looks_like_one_book(files(
            'Terra Obscura/Terra Obscura Volume 1/Terra Obscura #003.cbr',
            'Terra Obscura/Terra Obscura Volume 2/Terra Obscura #003.cbr',
        )))

    def test_a_missing_volume_folder_is_silence_not_disagreement(self):
        # Both are The Authority v1 #10. One copy is filed under a 'v1 (1999)'
        # folder and the other is not; reading that absence as 'volume none'
        # would demote a real duplicate.
        self.assertTrue(dup.looks_like_one_book(files(
            'Warren Ellis/1999/1999 The Authority/The Authority v1 #10.cbr',
            'Warren Ellis/The Authority/v1 (1999)/The Authority v1 #10.cbr',
        )))


if __name__ == '__main__':
    unittest.main()
