#!/usr/bin/env python3
"""Regression suite for folder matching.

find_specific_series_match() and find_publisher_match() decide which existing
folder an incoming file is moved into. A wrong answer here does not corrupt a
name — it physically relocates a file. That makes these the highest-consequence
functions in the generator.

Both used a bare `keyword.lower() in filename.lower()` substring test, so
'Soleil' matched 'Beausoleil' and 'SAF' matched 'Failsafe'.

These tests use a small hand-built dest_map, so they run without the library.

Run:  python3 -m unittest discover tests
"""
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import paths

gen = paths.load_generator()


def fake_dest_map(*folders):
    """dest_map is {folder_name: {...data...}}; matching only reads the key."""
    return {f: {'folder': f, 'loose_files': [], 'files_in_folders': []}
            for f in folders}


PUBLISHER_MAP = fake_dest_map(
    'Cinebook (Europe)',
    'Fantagraphics (Europe)',
    'Humanoids (Europe)',
    'SAF Comics (Europe Collection) (2019)',
    'Soleil (Europe)',
    'Failsafe (2017)',
)


class TestPublisherMatchWholeWords(unittest.TestCase):
    """A publisher name must match as a WORD, never as a substring."""

    def match(self, filename):
        r = gen.find_publisher_match(filename, PUBLISHER_MAP)
        return r[0] if r else None

    def test_soleil_does_not_match_beausoleil(self):
        # The real file that exposed this, sitting in the download folder.
        self.assertIsNone(self.match(
            'The Demon of Beausoleil (2026) (Graphic Novel) (Oni Press) '
            '(Digital) (LeDuch-DCP).cbz'))

    def test_saf_does_not_match_failsafe(self):
        # 'SAF' is a three-letter keyword — the worst substring offender.
        self.assertIsNone(self.match('Failsafe 001 (2017) (digital).cbz'))
        self.assertIsNone(self.match('Safe Havens 003 (2020).cbz'))
        self.assertIsNone(self.match('Safari Honeymoon (2014).cbr'))

    def test_real_publishers_still_match(self):
        self.assertEqual(
            self.match('Amazonia 04 (Cinebook 2025) (digital).cbr'),
            'Cinebook (Europe)')
        self.assertEqual(
            self.match('Some Album 01 (Soleil) (2019).cbr'),
            'Soleil (Europe)')
        self.assertEqual(
            self.match('Another Album (SAF) (2019).cbr'),
            'SAF Comics (Europe Collection) (2019)')

    def test_publisher_in_underscore_separated_name(self):
        # Underscores must act as separators, not swallow the boundary.
        self.assertEqual(
            self.match('Superman_Isnt_Jewish_(But_I_Am...Kinda)_(2018)_'
                       '(Humanoids)_(Digital-Empire).cbr'),
            'Humanoids (Europe)')

    def test_publisher_adjacent_to_punctuation(self):
        self.assertEqual(
            self.match('Title 01 [Fantagraphics] (2005).cbr'),
            'Fantagraphics (Europe)')


class TestSpecificSeriesMatchWholeWords(unittest.TestCase):
    """Same rule for the specific-series list."""

    SERIES_MAP = fake_dest_map(
        'Billy & Buddy 001-008 (2009-2019)',
        'Gomer Goof 001-010',
    )

    def match(self, filename):
        r = gen.find_specific_series_match(filename, self.SERIES_MAP)
        return r[0] if r else None

    def test_known_series_matches(self):
        self.assertEqual(self.match('Billy & Buddy v10 (2020) (digital).cbr'),
                         'Billy & Buddy 001-008 (2009-2019)')

    def test_punctuation_normalised_between_words(self):
        # '&' is dropped by tokenising, so these spellings all agree.
        self.assertEqual(self.match('Billy and Buddy v10.cbr'), None)
        self.assertEqual(self.match('Billy   &   Buddy v10.cbr'),
                         'Billy & Buddy 001-008 (2009-2019)')

    def test_unrelated_file_does_not_match(self):
        self.assertIsNone(self.match('Gomer Pyle 001 (1966).cbr'))
        self.assertIsNone(self.match('Billy the Kid 003.cbr'))


class TestContainsWords(unittest.TestCase):
    """The shared primitive both matchers now use, tested directly."""

    def test_whole_word_only(self):
        self.assertFalse(gen.contains_words('The Demon of Beausoleil', 'Soleil'))
        self.assertFalse(gen.contains_words('Failsafe', 'SAF'))
        self.assertTrue(gen.contains_words('Soleil (Europe)', 'Soleil'))

    def test_case_insensitive(self):
        self.assertTrue(gen.contains_words('SOLEIL (europe)', 'soleil'))

    def test_separators_are_equivalent(self):
        for sep in (' ', '_', '-', '.', '(', ')'):
            with self.subTest(sep=sep):
                self.assertTrue(
                    gen.contains_words(f'A{sep}Humanoids{sep}B', 'Humanoids'))

    def test_multi_word_phrase_requires_order(self):
        self.assertTrue(gen.contains_words('Billy & Buddy v10', 'Billy Buddy'))
        self.assertFalse(gen.contains_words('Buddy and Billy', 'Billy Buddy'))

    def test_empty_inputs(self):
        self.assertFalse(gen.contains_words('', 'Soleil'))
        self.assertFalse(gen.contains_words('Soleil', ''))


if __name__ == '__main__':
    unittest.main()
