#!/usr/bin/env python3
"""Golden cases for release.parse_release().

Part of the production suite. It was not, when written: this covered
`prototype/parse_release.py`, which nothing imported. The parser is now what
`matching_analysis_generator.py` derives every series name with, so these cases
guard live behaviour and the "FIXES" comments record what the OLD subtraction
code produced — kept deliberately, so a regression back to it is recognisable.
"""
import unittest

from paths import load_release

_release = load_release()
parse_release, resolve, normalize = (
    _release.parse_release, _release.resolve, _release.normalize)


class TestSeriesIsAPrefix(unittest.TestCase):
    """Nothing is ever deleted from the middle of a title."""

    def test_no_truncation_at_ordinal(self):
        # FIXES: live -> 'Star Trek - Red Shirts - Ghost of the'
        # ISSUE_PATTERN matches ' 21' inside '21st'.
        r = parse_release('Star Trek - Red Shirts - Ghost of the 21st Century (2013).cbz')
        self.assertEqual(r.series, 'Star Trek - Red Shirts - Ghost of the 21st Century')

    def test_no_dangling_separator(self):
        # FIXES: live -> 'The Wicked + The Divine -'
        r = parse_release('The Wicked + The Divine - Book 02 (2015).cbz')
        self.assertEqual(r.series, 'The Wicked + The Divine')
        self.assertEqual(r.volume, 2)

    def test_no_underscore_debris(self):
        # FIXES: live -> 'Dead Irons _'
        r = parse_release('Dead Irons v01_(2009).cbr')
        self.assertEqual(r.series, 'Dead Irons')
        self.assertEqual(r.volume, 1)


class TestPackagingWordsThatAreRealWords(unittest.TestCase):
    """Packaging words are consumed only as a SUFFIX, so no exception list."""

    def test_giant_days_survives(self):
        # FIXES: live -> 'Days'
        self.assertEqual(parse_release('Giant Days Vol. 05 (2017).cbr').series, 'Giant Days')

    def test_the_complete_peanuts_survives(self):
        # FIXES: live -> 'The Peanuts'
        self.assertEqual(
            parse_release('The Complete Peanuts v01 (2015).cbz').series,
            'The Complete Peanuts')

    def test_comic_book_history_survives(self):
        # 'Book' is only a volume marker when a number follows it.
        self.assertEqual(
            parse_release('Comic Book History of Animation 001 (2020).cbz').series,
            'Comic Book History of Animation')

    def test_signal_to_noise_survives(self):
        self.assertEqual(parse_release('Signal to Noise (2007).cbz').series, 'Signal to Noise')

    def test_trailing_packaging_still_strips(self):
        self.assertEqual(
            parse_release('Bone Parish Complete Collection (2020).cbz').series,
            'Bone Parish')

    def test_special_strips_and_is_recorded_as_kind(self):
        r = parse_release('Misty Special (1980).cbz')
        self.assertEqual(r.series, 'Misty')
        self.assertEqual(r.kind, 'special')


class TestSpelledOutAndNumericVolumes(unittest.TestCase):
    def test_spelled_out_book_number(self):
        r = parse_release('High Strangeness Book Five (2019).cbz')
        self.assertEqual((r.series, r.volume), ('High Strangeness', 5))

    def test_season_is_absorbed_not_kept(self):
        # The outstanding 'Heartthrob Season 3 001' -> want 'Heartthrob'.
        r = parse_release('Heartthrob Season 3 001 (2019).cbz')
        self.assertEqual(r.series, 'Heartthrob')
        self.assertEqual(r.issue, '001')

    def test_decimal_volume(self):
        self.assertEqual(parse_release('Side-Kicked v01.5 (2017).cbz').volume, 1.5)

    def test_issue_keeps_zero_padding(self):
        self.assertEqual(parse_release('Feral 019 (2024).cbr').issue, '019')


class TestAcronymsAreNotShredded(unittest.TestCase):
    def test_dotted_acronyms(self):
        for name, want in [
            ('T.H.U.N.D.E.R. Agents v02 (2014).cbz', 'T.H.U.N.D.E.R. Agents'),
            ('M.A.S.K. 03 (2026).cbz', 'M.A.S.K.'),
            ('Ghosted in L.A. (2020).cbz', 'Ghosted in L.A.'),
        ]:
            self.assertEqual(parse_release(name).series, want, name)

    def test_dot_before_digit_still_splits(self):
        self.assertEqual(parse_release('Giant Days Vol.05 (2017).cbr').volume, 5)


class TestLibraryResolvesAmbiguity(unittest.TestCase):
    """The point of returning candidates instead of one guess.

    'Revolution 9 006' and 'Cruel Kingdom 2 001' are structurally identical, so
    no filename rule can separate them. The library can.
    """

    def test_trailing_numeral_kept_when_the_folder_exists(self):
        keys = {normalize('Revolution 9')}
        self.assertEqual(resolve('Revolution 9 006 (2018).cbz', keys), ('Revolution 9', True))

    def test_trailing_numeral_dropped_when_it_does_not(self):
        keys = {normalize('Cruel Kingdom')}
        self.assertEqual(resolve('Cruel Kingdom 2 001 (2024).cbz', keys), ('Cruel Kingdom', True))

    def test_spinoff_folder_wins_over_parent(self):
        # Both 'Die' and 'Die - Loaded' are real folders in the library.
        # FIXES: live derives 'die', filing the spin-off into the parent.
        keys = {normalize('Die'), normalize('Die - Loaded')}
        self.assertEqual(
            resolve('Die - Loaded v01 - Zero Sessions (2026).cbz', keys),
            ('Die - Loaded', True))

    def test_parent_used_when_no_spinoff_folder(self):
        keys = {normalize('Die')}
        self.assertEqual(resolve('Die - Loaded v01 (2025).cbz', keys), ('Die', True))

    def test_unmatched_falls_back_to_best_guess(self):
        chosen, matched = resolve('Something Entirely New 001 (2026).cbz', set())
        self.assertEqual((chosen, matched), ('Something Entirely New', False))


class TestKnownLimitations(unittest.TestCase):
    """Documented, not fixed — so nobody mistakes them for oversights."""

    def test_scanlation_group_glued_by_underscores_is_kept(self):
        # The release group is normally in brackets; here it is underscore-joined
        # and indistinguishable from title words. Live is no better:
        # it yields 'Nancy_In_Hell__Minutemen'.
        self.assertEqual(
            parse_release('Nancy_In_Hell_Complete_Minutemen.cbr').series,
            'Nancy In Hell Complete Minutemen')


if __name__ == '__main__':
    unittest.main(verbosity=2)
