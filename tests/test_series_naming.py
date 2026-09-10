#!/usr/bin/env python3
"""Regression suite for series-name derivation.

Two layers:

1. Golden cases — small, exact, hand-checked. They pin the behaviour of the four
   generator entry points that turn a filename into a series name, plus the
   creator's is_volume() detector. These are the cases a human can reason about.

2. Whole-library no-merge invariant — the layer that actually protects files.
   A series name is not cosmetic: it becomes a dict key and then a folder name on
   disk. Two items that derive the *same* key get filed together. So the failure
   that matters is a MERGE: two items that used to derive different keys starting
   to derive the same one, silently moving files into the wrong folder. Splitting
   is allowed and expected — repairing a corrupted key makes it split away from
   whatever it was wrongly grouped with.

Run:  python3 -m unittest discover tests
"""
import json
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import paths

gen = paths.load_generator()
creator = paths.load_creator()


# ═══════════════════════════════════════════════════════════════════════════
# Golden cases
# ═══════════════════════════════════════════════════════════════════════════

class TestMidWordCorruption(unittest.TestCase):
    """Real titles that the unanchored VOLUME_PATTERN ate letters out of.

    `\\b` binds only to the FIRST alternative of an alternation, so every keyword
    after the first `|` used to match mid-word: 'GN' inside 'Signal', 'HC' inside
    'Bytchcraft'. All 50 library items affected by this are represented here by
    one example of each distinct cause.
    """

    def check(self, name, expected):
        self.assertEqual(gen.extract_series_name(name), expected)
        self.assertEqual(gen.extract_folder_series_name(name), expected)

    def test_gn_inside_word(self):
        self.check('Signal to Noise', 'Signal to Noise')
        self.check('Charlamagne tha God', 'Charlamagne tha God')

    def test_hc_inside_word(self):
        self.check('Bytchcraft', 'Bytchcraft')
        self.check('Ashcan', 'Ashcan')
        self.check('Koshchei in Hell', 'Koshchei in Hell')

    def test_gn_inside_word_after_separator(self):
        # extract_series_name splits on ' - ' first, so the corruption only ever
        # showed up downstream — assert on the two call sites that see it.
        self.assertEqual(gen.extract_folder_series_name('Black Canary - Ignite'),
                         'Black Canary - Ignite')
        self.assertEqual(gen.normalize_name('Black Canary - Ignite'),
                         'black canary ignite')

    def test_gn_as_suffix_of_ogn(self):
        # 'OGN' is a packaging word we do NOT strip; 'O' + 'GN' must not be split.
        self.check('Camp Midnight OGN', 'Camp Midnight OGN')

    def test_volume_number_still_stripped_alongside(self):
        self.check('Camp Midnight v01 OGN', 'Camp Midnight OGN')

    def test_vol_dot_n(self):
        self.check('Tales Designed to Thrizzle Vol. 1', 'Tales Designed to Thrizzle')


class TestUnderscoreBoundaries(unittest.TestCase):
    """Why the anchors are (?<![A-Za-z0-9])/(?![A-Za-z0-9]) and not \\b.

    `\\b` treats '_' as a word character, so it would refuse to match a keyword
    that is underscore-delimited. Release filenames are full of underscores.
    """

    def test_keyword_between_underscores_is_stripped(self):
        # Plain \b anchors would leave 'Complete' in place here.
        self.assertEqual(gen.extract_series_name('Nancy_In_Hell_Complete_Minutemen'),
                         'Nancy_In_Hell__Minutemen')

    def test_volume_number_followed_by_underscore_is_stripped(self):
        # The stray trailing '_' is a pre-existing cosmetic artefact of the
        # underscore-separated form, unrelated to anchoring and deliberately not
        # in scope here. What this pins is that 'v01' is still removed.
        self.assertEqual(gen.extract_series_name('Dead Irons v01_(2009)'),
                         'Dead Irons _')


class TestPackagingWordsStillStrip(unittest.TestCase):
    """The word list must NOT shrink.

    A Special or an Annual is an issue OF its parent series and belongs in the
    parent's folder — stripping the word is what routes it there. Separately,
    NO_RENAME_KEYWORDS makes propose_filename() leave such a file's own name
    alone. The two halves are complementary, not contradictory.
    """

    def test_special_routes_to_parent(self):
        self.assertEqual(gen.extract_series_name('Misty Special'), 'Misty')
        self.assertEqual(gen.extract_series_name('Wytches - Bad Egg Halloween Special'),
                         'Wytches')
        self.assertEqual(gen.extract_series_name('Taboo 001-009 + Special'), 'Taboo')

    def test_collected_edition_words(self):
        self.assertEqual(gen.extract_series_name('Bone Parish Complete Collection'),
                         'Bone Parish')
        self.assertEqual(gen.extract_series_name('Behemoth v01 (2025) (Collection)'),
                         'Behemoth')

    def test_keyword_still_matches_at_string_edges(self):
        # No neighbouring character on one side — the lookarounds must not
        # require one.
        self.assertEqual(gen.extract_folder_series_name('Omnibus'), '')
        self.assertEqual(gen.extract_folder_series_name('Saga TPB'), 'Saga')


class TestProposeFilename(unittest.TestCase):
    """propose_filename() is the only call site that writes a *file* name."""

    def test_no_rename_keyword_passes_through(self):
        self.assertEqual(gen.propose_filename('Misty Special 001 (1978).cbz', 'Misty'),
                         'Misty Special 001 (1978).cbz')

    def test_rename_to_canonical(self):
        self.assertEqual(gen.propose_filename('The Feral 021 (2024).cbz', 'Feral'),
                         'Feral 021 (2024).cbz')

    def test_mid_word_corruption_no_longer_blocks_rename(self):
        # Before anchoring, src_series was 'Sial to Noise', which normalised
        # differently from the canonical name and aborted the rename.
        self.assertEqual(gen.extract_series_name('Signal to Noise 001 (2020).cbz'),
                         'Signal to Noise')


@unittest.skipIf(creator is None, 'comic_volume_creator not present')
class TestCreatorIsVolume(unittest.TestCase):
    """is_volume() uses the same regex as a boolean DETECTOR, not a stripper.

    A false positive there makes a file vanish from the volume-creator UI
    entirely, so the mid-word bug was worse in this app than in the generator.
    """

    def test_false_positives_from_mid_word_matches(self):
        for name in ('Signal to Noise', 'Bytchcraft', 'Ashcan',
                     'Koshchei in Hell', 'Black Canary - Ignite'):
            with self.subTest(name=name):
                self.assertFalse(creator.is_volume(name))

    def test_true_positives_preserved(self):
        for name in ('Saga TPB', 'Hellboy Omnibus v01', 'Bone Parish Complete Collection',
                     'Some Series Graphic Novel', 'Preacher Book 1'):
            with self.subTest(name=name):
                self.assertTrue(creator.is_volume(name))


# ═══════════════════════════════════════════════════════════════════════════
# Whole-library invariant
# ═══════════════════════════════════════════════════════════════════════════

class TestNoSeriesMerge(unittest.TestCase):
    """No change may cause two previously-distinct series keys to merge.

    Skips itself when the library is unmounted or the baseline is missing, so the
    suite still runs anywhere. Items added to or removed from the library since
    the baseline was taken are ignored rather than failing the run.

    Regenerate the baseline with `python3 tests/make_baseline.py` ONLY to record a
    new intentional baseline — never to paper over a failure here.
    """

    @classmethod
    def setUpClass(cls):
        if not os.path.isdir(paths.LIBRARY_ROOT):
            raise unittest.SkipTest(f'library not mounted: {paths.LIBRARY_ROOT}')
        if not os.path.isfile(paths.BASELINE_FILE):
            raise unittest.SkipTest('no baseline; run tests/make_baseline.py')
        with open(paths.BASELINE_FILE, encoding='utf-8') as f:
            cls.baseline = json.load(f)['keys']

    def test_no_two_distinct_keys_merge(self):
        old = self.baseline
        # Only items that exist both in the baseline and on disk today.
        names = [n for n in paths.library_items() if n in old]

        groups = {}
        for name in names:
            groups.setdefault(gen.extract_series_name(name), []).append(name)

        merges = []
        for new_key, members in groups.items():
            old_keys = {old[n] for n in members}
            if len(old_keys) > 1:
                merges.append((new_key, sorted(old_keys), sorted(members)))

        if merges:
            lines = [f'{len(merges)} merged group(s) — files would move into the '
                     f'wrong folder:']
            for new_key, old_keys, members in merges[:10]:
                lines.append(f'  {old_keys!r} -> {new_key!r}')
                for m in members[:6]:
                    lines.append(f'      {m}')
            self.fail('\n'.join(lines))

    def test_coverage_is_meaningful(self):
        """Guard against the invariant silently passing on an empty set."""
        names = [n for n in paths.library_items() if n in self.baseline]
        self.assertGreater(len(names), 0.9 * len(self.baseline),
                           'baseline no longer describes this library; '
                           'regenerate it deliberately')


if __name__ == '__main__':
    unittest.main()
