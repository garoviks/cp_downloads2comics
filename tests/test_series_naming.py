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
        # What this guards is that 'OGN' is never SPLIT into 'O' + 'GN' — the
        # Phase 1 bug, which produced 'Camp Midnight O'.
        #
        # The two call sites now answer differently, and both are right.
        # extract_series_name() parses a RELEASE, where OGN (Original Graphic
        # Novel) is packaging, so it is consumed whole and 'Camp Midnight' is the
        # series — which is also the real folder name in the library.
        # extract_folder_series_name() reads a FOLDER, whose name you chose, so it
        # keeps what you wrote.
        self.assertEqual(gen.extract_series_name('Camp Midnight OGN'), 'Camp Midnight')
        self.assertEqual(gen.extract_folder_series_name('Camp Midnight OGN'),
                         'Camp Midnight OGN')

    def test_volume_number_still_stripped_alongside(self):
        self.assertEqual(gen.extract_series_name('Camp Midnight v01 OGN'), 'Camp Midnight')
        self.assertEqual(gen.extract_folder_series_name('Camp Midnight v01 OGN'),
                         'Camp Midnight OGN')

    def test_vol_dot_n(self):
        self.check('Tales Designed to Thrizzle Vol. 1', 'Tales Designed to Thrizzle')


class TestUnderscoreBoundaries(unittest.TestCase):
    """Underscore-separated releases — the form `\\b` gets wrong.

    `\\b` treats '_' as a word character, so it refuses to match a keyword that is
    underscore-delimited. Release filenames are full of underscores, which is why
    VOLUME_PATTERN uses (?<![A-Za-z0-9])/(?![A-Za-z0-9]) instead, and why
    release.py tokenises on '_' rather than relying on boundaries at all.
    """

    def test_underscores_become_word_separators(self):
        # Both parsers see 'Complete' as a word here; neither leaves it glued.
        # The old subtraction left the debris 'Nancy_In_Hell__Minutemen' — the
        # double underscore is where the word was cut out of the middle.
        #
        # 'Minutemen' is a scanlation group, not part of the title, but it is
        # underscore-joined and so indistinguishable from a title word. Recorded
        # as a known limitation in tests/test_release.py, not a defect.
        self.assertEqual(gen.extract_series_name('Nancy_In_Hell_Complete_Minutemen'),
                         'Nancy In Hell Complete Minutemen')

    def test_volume_number_followed_by_underscore_is_stripped(self):
        # The old code left a stray ' _' behind ('Dead Irons _') because it cut
        # 'v01' out of the middle and the underscore that followed it survived.
        # Consuming a suffix instead of subtracting a substring removes the whole
        # class of artefact.
        self.assertEqual(gen.extract_series_name('Dead Irons v01_(2009)'), 'Dead Irons')


class TestPackagingWordsStillStrip(unittest.TestCase):
    """The word list must NOT shrink.

    A Special or an Annual is an issue OF its parent series and belongs in the
    parent's folder — stripping the word is what routes it there. Separately,
    NO_RENAME_KEYWORDS makes propose_filename() leave such a file's own name
    alone. The two halves are complementary, not contradictory.
    """

    def test_special_routes_to_parent(self):
        self.assertEqual(gen.extract_series_name('Misty Special'), 'Misty')
        self.assertEqual(gen.extract_series_name('Taboo 001-009 + Special'), 'Taboo')

    def test_arc_special_offers_the_parent_as_a_candidate(self):
        # 'Wytches - Bad Egg Halloween Special' used to derive 'Wytches' outright.
        # It now offers both, most specific first, and the LIBRARY chooses: the
        # arc folder if you made one, the parent otherwise. That is the whole
        # point of returning candidates — the filename cannot know which exists.
        self.assertEqual(
            gen.extract_series_candidates('Wytches - Bad Egg Halloween Special'),
            ('Wytches - Bad Egg Halloween', 'Wytches'))

        # No 'Wytches - Bad Egg Halloween' folder -> falls through to the parent,
        # i.e. exactly the old behaviour, but now for a stated reason.
        dest = {'Wytches': {'folders': ['Wytches 001-006 (2014)'],
                            'loose_files': [], 'files_in_folders': []}}
        matched, _data, how, _blocked = gen.find_matches(
            'Wytches - Bad Egg Halloween Special (2015).cbz',
            'Wytches - Bad Egg Halloween', dest)
        # EXACT_SHORTENED, not EXACT: the destination was reached through the
        # fallback candidate, which is the one worth a second look in the UI.
        self.assertEqual((matched, how), ('Wytches', 'EXACT_SHORTENED'))

    def test_arc_folder_beats_the_parent_when_it_exists(self):
        dest = {
            'Die': {'folders': ['Die 001-020'], 'loose_files': [], 'files_in_folders': []},
            'Die - Loaded': {'folders': ['Die - Loaded'], 'loose_files': [],
                             'files_in_folders': []},
        }
        matched, _data, how, _blocked = gen.find_matches(
            'Die - Loaded v01 - Zero Sessions (2026).cbz', 'Die - Loaded', dest)
        self.assertEqual((matched, how), ('Die - Loaded', 'EXACT'))

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


class TestVolumeRangeLeavesNoDanglingSeparator(unittest.TestCase):
    """A folder name is a folder name: 'X-Men Vol 1 - 5' must not become 'X-Men -'.

    Removing the volume keyword and the trailing issue number takes both ends of
    a range and leaves the dash that joined them. This shipped: a real run created
    /mnt/extramedia/Comics/'The Nameless Kingdom -'/ as a sibling of the correct
    folder, so the same series existed twice under names differing by a hyphen.
    """

    def test_range_folder_keeps_only_the_title(self):
        self.assertEqual(
            gen.extract_folder_series_name('The Nameless Kingdom Vol. 1 - 3 (2026) (digital)'),
            'The Nameless Kingdom')
        self.assertEqual(gen.extract_folder_series_name('X-Men Vol 1 - 5'), 'X-Men')

    def test_a_hyphen_inside_the_title_survives(self):
        # The strip is anchored to the end, so an internal hyphen is not a
        # candidate. Without the anchor these lose their tail.
        self.assertEqual(gen.extract_folder_series_name('Spider-Man'), 'Spider-Man')
        self.assertEqual(gen.extract_folder_series_name('A-Force Vol. 2 - 4'), 'A-Force')

    def test_a_title_ending_in_a_word_is_untouched(self):
        self.assertEqual(gen.extract_folder_series_name('Sha 01-03'), 'Sha')
        self.assertEqual(gen.extract_folder_series_name('Hellboy Vol. 1 (2020)'), 'Hellboy')


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


class TestPickDestinationFolder(unittest.TestCase):
    """Ten destination keys hold more than one folder. This decides between them.

    'Sleeper' is the worst case and the reason the function exists: three real
    folders, all deriving the key 'Sleeper', so before this the winner was
    whichever one os.scandir returned first.
    """

    SLEEPER = [
        'Sleeper 001-012 (2003-2004) (digital-Empire)',
        'Sleeper - Season One 01-12 (2003) (digital) (Minutemen-Annika)',
        'Sleeper - Season Two 001-012 (2004-2005) (digital-Empire)',
    ]

    def test_plain_issue_goes_to_the_plain_folder(self):
        self.assertEqual(gen.pick_destination_folder('Sleeper 013 (2004).cbz', self.SLEEPER),
                         'Sleeper 001-012 (2003-2004) (digital-Empire)')

    def test_season_issue_goes_to_its_season(self):
        for season in ('One', 'Two'):
            with self.subTest(season=season):
                got = gen.pick_destination_folder(
                    f'Sleeper - Season {season} 013 (2004).cbz', self.SLEEPER)
                self.assertIn(f'Season {season}', got)

    def test_no_folder_is_named_so_the_choice_is_reproducible(self):
        # Reachable through a PUBLISHER match, where the folder is not expected
        # to appear in the filename. Arbitrary is fine; unstable is not — this
        # string becomes a path.
        pick = lambda: gen.pick_destination_folder('Totally Unrelated 001.cbz', self.SLEEPER)
        self.assertEqual(pick(), sorted(self.SLEEPER)[0])
        self.assertEqual(pick(), gen.pick_destination_folder(
            'Totally Unrelated 001.cbz', list(reversed(self.SLEEPER))))

    def test_substring_is_not_enough(self):
        folders = ['Sleeper 001-012', 'Sleepers 001-004']
        self.assertEqual(gen.pick_destination_folder('Sleepers 005.cbz', folders),
                         'Sleepers 001-004')


class TestAcceptedMerges(unittest.TestCase):
    """The 13 key merges that migration step 5 deliberately introduced.

    The no-merge invariant below is measured against a baseline, and that baseline
    was regenerated when the parser changed. Regenerating hides whatever merged at
    that moment, so the merges are pinned HERE instead: each one is a pair of
    library items that used to derive different keys and now derive the same one,
    with the reason it is correct. If a future change re-splits them, this fails.
    """

    CASES = [
        # (item A, item B, shared key, why the merge is right)
        ('Camp Midnight v01 OGN (2016) (Digital) (TheArchivist-Empire).cbr',
         'Camp Midnight v02 - Camp Midnight Vs. Camp Daybright (2019) (Digital) (DrDoom-Empire).cbz',
         'Camp Midnight', 'OGN is packaging, not part of the title'),
        ('King of the Flies v01 Hallorave HC (2010) (Minutemen Nweako).cbz',
         'King of the Flies v02 - The Origin of the World HC (2011) (c2c) (fylgja).cbz',
         'King of the Flies', 'Hallorave is a volume subtitle'),
        ('Not Drunk Enough Book One (2017) (Digital-Empire).cbz',
         'Not Drunk Enough Book Two (2020) (Digital-Empire).cbz',
         'Not Drunk Enough', 'spelled-out book numbers are volume markers'),
        ('One Path v01 (2025) (Graphic Novel) (Mad Cave Studios) (Digital) (LeDuch-DCP).cbz',
         'One Path v02 The White King (2026) (Graphic Novel) (Mad Cave Studios) (Digital) (LeDuch-DCP).cbz',
         'One Path', 'volume subtitle without a dash'),
        ('Side-Kicked v01 (2015) (Digital) (danke-Empire).cbz',
         'Side-Kicked v01.5 (2017) (Digital) (danke-Empire).cbz',
         'Side-Kicked', "old code left the debris 'Side-Kicked .5'"),
        ('Sleeper 001-012 (2003-2004) (digital-Empire)',
         'Sleeper - Season One 01-12 (2003) (digital) (Minutemen-Annika)',
         'Sleeper', 'Season N is a run marker; folders re-separated by '
                    'pick_destination_folder'),
        ('Starhenge Book One - The Dragon & The Boar (2023) (Digital-Empire).cbr',
         'Starhenge Book Two - A Kiss For Atticus 01 (of 04) (2026) (Limited Series) '
         '(Image Comics) (Digital) (LeDuch-DCP).cbz',
         'Starhenge', 'spelled-out book numbers again'),
        ('The Cursed Library 01 (of 03) - Part One - Alpha (2024) (digital) (Salem-Empire).cbr',
         'The Cursed Library Part Two - Omega #002 (2024) (Series) (Digital-HD) (LeDuch).cbz',
         'The Cursed Library', 'Part N is a run marker'),
        ('The Last Session v01 - Roll for Initiative (2022) (digital-SD) (Empire).cbr',
         'The Last Session v02 Rerolled (2025) (Collection) (Mad Cave Studios) '
         '(Digital-HD) (LeDuch).cbz',
         'The Last Session', 'volume subtitle without a dash'),
        ("Tim Burton's The Nightmare Before Christmas - The Shiver of Christmas Town",
         "Tim Burton's The Nightmare Before Christmas - The Shiver of Christmas Town "
         "004 (2026) (4 covers) (digital) (Salem-Empire).cbr",
         "Tim Burton's The Nightmare Before Christmas - The Shiver of Christmas Town",
         'a folder and an issue of it; the old code truncated one of the two'),
        ('Total THB',
         'Total_THB_v2.cbz',
         'Total THB', "underscore debris — old code produced 'Total_THB_', so the "
                      'loose file never found its own folder'),
        ('Where Does the Rainbow End',
         'Where Does the Rainbow End_ (2026) (Collection) (Mad Cave Studios) '
         '(Digital) (LeDuch-DCP).cbz',
         'Where Does the Rainbow End', 'trailing underscore debris, same cause'),
        ('The Hobbit (Graphic Novel) (2012 New Edition) [English].cbr',
         'The Hobbit - A Graphic Novel (2024) (Digital Rip) (Hourman-DCP).cbr',
         'The Hobbit', "dangling-article debris — 'Graphic Novel' is packaging, "
                       "and removing it must take the orphaned 'A' with it"),
    ]

    def test_each_accepted_merge_still_holds(self):
        for a, b, key, why in self.CASES:
            with self.subTest(key=key):
                self.assertEqual(gen.extract_series_name(a), key, why)
                self.assertEqual(gen.extract_series_name(b), key, why)


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

    It HAS been regenerated once, at migration step 5, when release.parse_release()
    replaced the subtraction parser. That deliberately merged 13 groups. Because
    regenerating hides whatever merged at that moment, all 13 are pinned above in
    TestAcceptedMerges with the reason each is correct — so the judgement is a test,
    not a note in a commit message.
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
