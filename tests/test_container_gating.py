#!/usr/bin/env python3
"""O16 — a shelf must not collect everything that shares its opening words.

Some folders hold many unrelated series: a publisher shelf, an anthology, a
creator shelf, an event's tie-ins, or a character/universe shelf. Both apps
otherwise assume one folder is one series, and `parse_release` offers SHORTENED
forms of a title as fallback candidates — so `Star Trek - Deviations - Evermore`
also answers to `Star Trek`, and the shortened form reaches the shelf.

The gate is a single distinction: a container accepts the file's OWN series and
refuses a shortened form of it. Publisher shelves are exempt because routing a
Humanoids release to `Humanoids (Europe)` is requirement O6 working as designed;
creator and event shelves refuse everything, because neither authorship nor
crossover membership is derivable from a filename.

The classification lives in `.comic_containers.md` in the library root, not in
this repo — it describes a library, and the library root is rebasable (O17).

Run:  python3 -m unittest discover tests
"""
import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import paths

g = paths.load_generator()

CONTAINERS_MD = """# Container Folders

## Publisher (1)
- Humanoids (Europe)

## Anthology (1)
- 2000AD prog

## Franchise (2)
- Star Trek
- Rick and Morty

## Creator (1)
- Mark Millar

## Event (1)
- Civil War II (Story Arc) (2016-2017)
"""


class ContainerFixture(unittest.TestCase):
    """A temp library root holding a containers file. Never the real library.

    The gate reads DEST_DIR at call time, so pointing it at a temp directory is
    enough — and it must be, since a test that needed the real library would be
    measuring the classification rather than the rule.
    """

    md = CONTAINERS_MD
    rules_md = None

    def setUp(self):
        self.original = g.DEST_DIR
        self.tmp = tempfile.mkdtemp(prefix='o16-')
        if self.md is not None:
            with open(os.path.join(self.tmp, g.CONTAINERS_FILE), 'w') as f:
                f.write(self.md)
        if self.rules_md is not None:
            with open(os.path.join(self.tmp, g.MATCHING_RULES_FILE), 'w') as f:
                f.write(self.rules_md)
        g.DEST_DIR = __import__('pathlib').Path(self.tmp)
        g._CONTAINERS_CACHE.pop(self.tmp, None)
        g._RULES_CACHE.pop(self.tmp, None)
        self._saved_shape = dict(g.FOLDER_SERIES)
        g.FOLDER_SERIES.clear()

    def tearDown(self):
        g.DEST_DIR = self.original
        g._CONTAINERS_CACHE.pop(self.tmp, None)
        g._RULES_CACHE.pop(self.tmp, None)
        g.FOLDER_SERIES.clear()
        g.FOLDER_SERIES.update(self._saved_shape)
        import shutil
        shutil.rmtree(self.tmp, ignore_errors=True)


class TestTheListIsRead(ContainerFixture):
    def test_every_section_becomes_a_kind(self):
        self.assertEqual(
            {g.container_kind(n) for n in
             ('Humanoids (Europe)', '2000AD prog', 'Star Trek', 'Mark Millar',
              'Civil War II (Story Arc) (2016-2017)')},
            {'publisher', 'anthology', 'franchise', 'creator', 'event'})

    def test_an_unlisted_folder_is_not_a_container(self):
        self.assertIsNone(g.container_kind('Lumberjanes'))

    def test_names_match_regardless_of_surrounding_space(self):
        """Two real library folders end in a space; identity is stored stripped."""
        self.assertEqual(g.container_kind('Rick and Morty '), 'franchise')
        self.assertEqual(g.container_kind('  Star Trek'), 'franchise')

    def test_matching_ignores_case(self):
        self.assertEqual(g.container_kind('sTaR tReK'), 'franchise')

    def test_the_heading_count_is_not_part_of_the_kind(self):
        """'## Franchise (57)' must yield 'franchise', not 'franchise (57)'."""
        self.assertNotIn('(', g.container_kind('Star Trek') or '')


class TestTheListSurvivesHandEditing(ContainerFixture):
    """This file is meant to be edited by hand, so its parsing must be forgiving.

    Written because a mutation that dropped the strip() on the entry text killed
    no test: every fixture entry happened to be perfectly formatted. An extra
    space after the bullet is the obvious way to mistype one of these, and
    silently dropping the entry would open a shelf without saying so.
    """
    md = "##   Franchise  (2)  \n-  Star Trek   \n\n- \n"

    def test_extra_space_after_the_bullet_still_registers(self):
        self.assertEqual(g.container_kind('Star Trek'), 'franchise')

    def test_a_padded_heading_still_names_the_kind(self):
        self.assertEqual(g.container_kind('Star Trek'), 'franchise')

    def test_an_empty_bullet_is_skipped_not_stored(self):
        """'- ' must not register the empty string and classify every folder."""
        self.assertNotIn('', g.load_containers())
        self.assertIsNone(g.container_kind('Lumberjanes'))


class TestTheListIsOptional(ContainerFixture):
    """No file means no classification — the pre-O16 behaviour, not a crash.

    A library that has never been classified must keep working; failing closed
    on an absent file would refuse every destination in it.
    """
    md = None

    def test_a_missing_file_classifies_nothing(self):
        self.assertEqual(g.load_containers(), {})

    def test_and_therefore_blocks_nothing(self):
        self.assertTrue(g.container_allows('Star Trek', is_primary=False))


class TestTheGateByKind(ContainerFixture):
    def test_a_publisher_shelf_accepts_a_shortened_name(self):
        """Requirement O6: publisher routing is the feature, not the bug."""
        self.assertTrue(g.container_allows('Humanoids (Europe)', is_primary=False))

    def test_a_franchise_shelf_accepts_only_the_files_own_series(self):
        self.assertTrue(g.container_allows('Star Trek', is_primary=True))
        self.assertFalse(g.container_allows('Star Trek', is_primary=False))

    def test_an_anthology_accepts_only_the_files_own_series(self):
        self.assertTrue(g.container_allows('2000AD prog', is_primary=True))
        self.assertFalse(g.container_allows('2000AD prog', is_primary=False))

    def test_a_creator_shelf_accepts_nothing(self):
        """Not even an exact hit: no comic is a series called 'Mark Millar'."""
        self.assertFalse(g.container_allows('Mark Millar', is_primary=True))
        self.assertFalse(g.container_allows('Mark Millar', is_primary=False))

    def test_an_event_accepts_nothing(self):
        folder = 'Civil War II (Story Arc) (2016-2017)'
        self.assertFalse(g.container_allows(folder, is_primary=True))
        self.assertFalse(g.container_allows(folder, is_primary=False))

    def test_an_ordinary_folder_is_untouched(self):
        self.assertTrue(g.container_allows('Lumberjanes', is_primary=True))
        self.assertTrue(g.container_allows('Lumberjanes', is_primary=False))


class TestAnUnknownKindFailsClosed(ContainerFixture):
    """A typo in a heading must not silently open a shelf.

    'Creater' is not a kind. Treating an unrecognised heading as permissive
    would turn a spelling mistake into an invisible loss of the whole gate.
    """
    md = "## Creater (1)\n- Mark Millar\n"

    def test_an_unrecognised_heading_blocks(self):
        self.assertEqual(g.container_kind('Mark Millar'), 'creater')
        self.assertFalse(g.container_allows('Mark Millar', is_primary=True))


class TestTheFailSafeForUnlistedShelves(ContainerFixture):
    """A shelf added after the list was written is refused until classified."""

    def test_enough_distinct_series_makes_an_unlisted_folder_a_container(self):
        g.FOLDER_SERIES['new shelf'] = {
            f'series {i}' for i in range(g.UNCLASSIFIED_CONTAINER_SERIES)}
        self.assertEqual(g.container_kind('New Shelf'), 'unknown')
        self.assertFalse(g.container_allows('New Shelf', is_primary=True))

    def test_one_series_short_of_the_threshold_is_still_ordinary(self):
        g.FOLDER_SERIES['new shelf'] = {
            f'series {i}' for i in range(g.UNCLASSIFIED_CONTAINER_SERIES - 1)}
        self.assertIsNone(g.container_kind('New Shelf'))

    def test_the_curated_list_wins_over_the_shape(self):
        """Shape is the fallback, not an override — publisher must stay open.

        `Europe Comics (Collection)` holds 350 distinct series. If shape were
        checked first it would be 'unknown' and O6 routing into every publisher
        shelf would stop working.
        """
        g.FOLDER_SERIES['humanoids (europe)'] = {
            f'series {i}' for i in range(500)}
        self.assertEqual(g.container_kind('Humanoids (Europe)'), 'publisher')
        self.assertTrue(g.container_allows('Humanoids (Europe)', is_primary=False))

    def test_the_threshold_clears_real_series_folders(self):
        """'Lumberjanes' parses as 12 series and must not trip the fail-safe.

        The number that matters is the gap between the largest ordinary series
        folder in the library and the threshold. If this ever fails, the
        threshold has drifted down into real folders.
        """
        self.assertGreater(g.UNCLASSIFIED_CONTAINER_SERIES, 13)


class TestTheGateInsideTheMatcher(ContainerFixture):
    """The rule reaching find_matches(), which is where it has to bite.

    container_allows() being correct proves nothing on its own — the defect is
    that the SECOND candidate reaches the shelf, and only find_matches() knows
    which candidate is which.
    """

    def _dest(self, *folders):
        return {g.extract_series_name(f): {'folders': [f], 'files_in_folders': [],
                                           'loose_files': []}
                for f in folders}

    def test_a_shortened_title_no_longer_reaches_the_shelf(self):
        dest = self._dest('Star Trek')
        fn = 'Star Trek - Deviations - Evermore (2026) (digital).cbr'
        folder, _, conf, blocked = g.find_matches(
            fn, 'Star Trek - Deviations - Evermore', dest)
        self.assertIsNone(folder)
        self.assertEqual(conf, 'BLOCKED_CONTAINER')
        self.assertEqual(blocked, 'Star Trek')

    def test_the_shelfs_own_series_still_reaches_it(self):
        dest = self._dest('Star Trek')
        folder, _, conf, blocked = g.find_matches(
            'Star Trek 025 (2024) (Digital).cbz', 'Star Trek', dest)
        self.assertEqual(folder, 'Star Trek')
        self.assertEqual(conf, 'EXACT')
        self.assertIsNone(blocked)

    def test_a_refused_candidate_does_not_end_the_search(self):
        """Falling through matters: a more specific folder may still be there.

        If the gate returned NONE instead of trying the next candidate, adding
        a real 'Star Trek - Deviations' folder would not help.
        """
        dest = self._dest('Star Trek', 'Star Trek - Deviations')
        folder, _, _, _ = g.find_matches(
            'Star Trek - Deviations 001 (2026) (digital).cbr',
            'Star Trek - Deviations', dest)
        self.assertEqual(folder, 'Star Trek - Deviations')

    def test_an_ordinary_folder_still_takes_a_shortened_title(self):
        """The gate must not become a blanket ban on the fallback candidate."""
        dest = self._dest('The Wicked + The Divine')
        folder, _, _, _ = g.find_matches(
            'The Wicked + The Divine - Christmas Annual (2017) (Digital).cbr',
            'The Wicked + The Divine - Christmas', dest)
        self.assertEqual(folder, 'The Wicked + The Divine')

    def test_a_key_holding_several_folders_is_refused_only_if_all_refuse(self):
        """Ten destination keys hold more than one folder.

        pick_destination_folder() chooses between them later, so refusing the
        whole key because one of its folders is a container would discard a
        perfectly good destination.
        """
        data = {'folders': ['Star Trek', 'Star Trek Annuals'],
                'files_in_folders': [], 'loose_files': []}
        self.assertTrue(g._match_is_allowed(data, is_primary=False))

    def test_a_key_backed_only_by_loose_files_is_allowed(self):
        """Loose base-directory files are not folders and cannot be containers."""
        data = {'folders': [], 'files_in_folders': [],
                'loose_files': ['Star Trek - Something.cbz']}
        self.assertTrue(g._match_is_allowed(data, is_primary=False))


class TestASavedRuleOverridesTheClassification(ContainerFixture):
    """`.comic_matching_rules.md` — the answers you already gave.

    The gate can only ever be a default. `Star Trek - Deviations` really does
    belong on the `Star Trek` shelf and `Supernatural - Wayward Special` really
    does not belong on `Supernatural (2025)`, and no rule derivable from the
    filenames tells those apart. So the UI asks, once, and the answer is kept
    here — keyed on the FOLDER, because next month's issue will have a different
    filename but the same destination.
    """

    rules_md = ("## Accept (1)\n- Star Trek\n\n"
                "## Refuse (1)\n- Supernatural (2025)\n")

    def test_accept_reopens_a_container_shelf(self):
        self.assertTrue(g.container_allows('Star Trek', is_primary=False))

    def test_refuse_closes_an_ordinary_folder(self):
        """'Supernatural (2025)' holds one series, so nothing else would stop it."""
        self.assertIsNone(g.container_kind('Supernatural (2025)'))
        self.assertFalse(g.container_allows('Supernatural (2025)', is_primary=False))

    def test_refuse_still_admits_the_folders_own_series(self):
        """Otherwise saying 'not this one' would orphan the whole folder."""
        self.assertTrue(g.container_allows('Supernatural (2025)', is_primary=True))

    def test_an_unruled_folder_is_unaffected(self):
        self.assertFalse(g.container_allows('Mark Millar', is_primary=True))
        self.assertTrue(g.container_allows('Lumberjanes', is_primary=False))

    def test_the_rule_reaches_find_matches(self):
        dest = {g.extract_series_name(f): {'folders': [f], 'files_in_folders': [],
                                           'loose_files': []}
                for f in ('Star Trek',)}
        folder, _, conf, _ = g.find_matches(
            'Star Trek - Deviations - Evermore (2026) (digital).cbr',
            'Star Trek - Deviations - Evermore', dest)
        self.assertEqual(folder, 'Star Trek')
        # Not EXACT_SHORTENED: the shelf took it because the user said so, and a
        # settled question must not be reported as an open one.
        self.assertEqual(conf, 'RULED_ACCEPT')

    def test_a_refusal_by_rule_is_told_apart_from_one_by_classification(self):
        """Both create a new folder; only one is a decision already made.

        'Supernatural (2025)' is an ordinary single-series folder — the
        container gate would wave this through. The refusal can only have come
        from the rules file, and the row must say so or it will ask again.
        """
        dest = {g.extract_series_name(f): {'folders': [f], 'files_in_folders': [],
                                           'loose_files': []}
                for f in ('Supernatural (2025)',)}
        folder, _, conf, blocked = g.find_matches(
            'Supernatural - Wayward Special 001 (2026) (digital).cbr',
            'Supernatural - Wayward Special', dest)
        self.assertIsNone(folder)
        self.assertEqual(conf, 'RULED_REFUSE')
        # Still named, or the UI cannot offer to reverse the decision.
        self.assertEqual(blocked, 'Supernatural (2025)')

    def test_an_accepted_rule_still_counts_as_matching_a_series(self):
        """The new confidence must not fall out of the lists that mean 'matched'.

        Two places ask 'did this match a series key?' — one names the new folder
        after the matched series rather than the parsed guess, the other counts
        matches for the summary. RULED_ACCEPT is an EXACT_SHORTENED match that
        someone authorised, so both must say yes. Adding a confidence and missing
        these is silent: the run completes and quietly names folders wrongly.
        """
        self.assertIn('RULED_ACCEPT', g.SERIES_KEY_MATCHES)
        self.assertIn('EXACT_SHORTENED', g.SERIES_KEY_MATCHES)
        self.assertIn('EXACT', g.SERIES_KEY_MATCHES)
        # A refusal matched nothing, so it must NOT be in there.
        self.assertNotIn('RULED_REFUSE', g.SERIES_KEY_MATCHES)
        self.assertNotIn('BLOCKED_CONTAINER', g.SERIES_KEY_MATCHES)
        # PUBLISHER is excluded deliberately — it would name the folder after
        # the publisher instead of the series.
        self.assertNotIn('PUBLISHER', g.SERIES_KEY_MATCHES)


class TestTheRulesFileIsOptionalAndForgiving(ContainerFixture):
    rules_md = None

    def test_no_rules_file_changes_nothing(self):
        self.assertEqual(g.load_matching_rules(), {})
        self.assertFalse(g.container_allows('Star Trek', is_primary=False))


class TestAMistypedRuleFailsClosed(ContainerFixture):
    """A section that is neither 'Accept' nor 'Refuse' must not grant permission.

    Same stance as a mistyped container heading: the cost of wrongly refusing is
    a folder you file by hand, the cost of wrongly accepting is a misfiled book
    you may not notice.
    """
    rules_md = "## Acept (1)\n- Lumberjanes\n"

    def test_an_unrecognised_section_does_not_accept(self):
        self.assertFalse(g.container_allows('Lumberjanes', is_primary=False))
        self.assertTrue(g.container_allows('Lumberjanes', is_primary=True))


class TestRulesAreKeyedLikeEveryOtherFolderList(ContainerFixture):
    """Same identity rules as the containers file, because it is the same parser."""
    rules_md = "## Accept (1)\n-  rick and morty   \n"

    def test_case_and_surrounding_space_do_not_matter(self):
        self.assertTrue(g.container_allows('Rick and Morty ', is_primary=False))


class TestTheReportSaysHowItMatched(ContainerFixture):
    """Provenance, so the UI can ask rather than guess.

    Every destination in the report is created either way; what differs is
    whether you would want to reverse it. A match found through a SHORTENED
    candidate might be a spin-off filed under its parent, and a shelf the gate
    REFUSED is a decision worth offering back with one click. Collapsing both
    into 'EXACT' and 'NONE' throws away exactly the rows a human should see.
    """

    def _dest(self, *folders):
        return {g.extract_series_name(f): {'folders': [f], 'files_in_folders': [],
                                           'loose_files': []}
                for f in folders}

    def test_a_fallback_match_is_marked_apart_from_a_direct_one(self):
        dest = self._dest('The Wicked + The Divine')
        _, _, conf, _ = g.find_matches(
            'The Wicked + The Divine - Christmas Annual (2017) (Digital).cbr',
            'The Wicked + The Divine - Christmas', dest)
        self.assertEqual(conf, 'EXACT_SHORTENED')

    def test_finding_nothing_is_not_the_same_as_being_refused(self):
        """Both create a new folder; only one of them had somewhere to go."""
        _, _, conf, blocked = g.find_matches(
            'Lumberjanes 001 (2015) (digital).cbr', 'Lumberjanes', {})
        self.assertEqual(conf, 'NONE')
        self.assertIsNone(blocked)

    def test_the_refused_shelf_is_named_as_it_sits_on_disk(self):
        """The UI has to offer the real folder back, not the parsed key.

        'Rick and Morty ' ends in a space in the library. Reporting the key
        would hand the UI a path that does not exist.
        """
        dest = self._dest('Rick and Morty ')
        _, _, conf, blocked = g.find_matches(
            'Rick and Morty - Corporate Assets 001 (2021).cbr',
            'Rick and Morty - Corporate Assets', dest)
        self.assertEqual(conf, 'BLOCKED_CONTAINER')
        self.assertEqual(blocked, 'Rick and Morty ')

    def test_a_publisher_shelf_reached_by_a_short_name_is_still_flagged(self):
        """O6 allows it, but it is still a fallback match and still worth a look."""
        dest = self._dest('Humanoids (Europe)')
        folder, _, conf, blocked = g.find_matches(
            'Humanoids - The Incal 001 (2020).cbr', 'Humanoids - The Incal', dest)
        self.assertEqual(folder, 'Humanoids')
        self.assertEqual(conf, 'EXACT_SHORTENED')
        self.assertIsNone(blocked)


if __name__ == '__main__':
    unittest.main(verbosity=2)
