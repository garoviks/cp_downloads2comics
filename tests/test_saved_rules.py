#!/usr/bin/env python3
"""Writing `.comic_matching_rules.md` — the other half of O16.

The container gate can only ever be a default, because the distinction it needs
is not in the filename. `Star Trek - Deviations` genuinely belongs on the
`Star Trek` shelf; `Supernatural - Wayward Special` genuinely does not belong on
`Supernatural (2025)`. A person can tell; a parser cannot. So the UI asks once
and writes the answer down.

This file is about the WRITER. That it is a module-level function rather than a
method on the request handler is deliberate, following mover_cmd(): a writer
reachable only by booting a server and POSTing to it is a writer whose edge
cases never get tested, and the edge cases are the whole difficulty — flipping
an earlier answer, keeping the prose, and refusing a folder name that would
forge extra rules.

Run:  python3 -m unittest discover tests
"""
import os
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import paths

srv = paths.load_serve_v2()
g = paths.load_generator()


class RulesFileFixture(unittest.TestCase):
    """A temp library root. Never the real one — this test WRITES."""

    def setUp(self):
        self.tmp = tempfile.mkdtemp(prefix='o16-rules-')
        self.path = Path(self.tmp) / srv.MATCHING_RULES_FILE

    def tearDown(self):
        import shutil
        shutil.rmtree(self.tmp, ignore_errors=True)

    def entries(self):
        """What the GENERATOR makes of the file we just wrote.

        Reading it back with the real reader rather than a regex here, because
        the only thing that matters about this file is what the matcher sees. A
        writer that produces something only this test can parse is broken.
        """
        saved_root, saved_file = g.DEST_DIR, g.MATCHING_RULES_FILE
        g.DEST_DIR = Path(self.tmp)
        g._RULES_CACHE.pop(self.tmp, None)
        try:
            return dict(g.load_matching_rules())
        finally:
            g._RULES_CACHE.pop(self.tmp, None)
            g.DEST_DIR = saved_root


class TestTheFirstRule(RulesFileFixture):
    def test_a_rule_saved_into_thin_air_creates_the_file(self):
        """The library root may never have been ruled on before."""
        self.assertFalse(self.path.exists())
        srv.save_matching_rule(self.path, 'Star Trek', 'accept')
        self.assertEqual(self.entries(), {'star trek': 'accept'})

    def test_the_generator_then_honours_it(self):
        """End to end: the button changes what the matcher does.

        Written because every other assertion here is about file CONTENT, and a
        file the matcher ignores would pass all of them.
        """
        srv.save_matching_rule(self.path, 'Star Trek', 'accept')
        saved = g.DEST_DIR
        g.DEST_DIR = Path(self.tmp)
        g._RULES_CACHE.pop(self.tmp, None)
        g._CONTAINERS_CACHE.pop(self.tmp, None)
        try:
            self.assertTrue(g.container_allows('Star Trek', is_primary=False))
        finally:
            g._RULES_CACHE.pop(self.tmp, None)
            g._CONTAINERS_CACHE.pop(self.tmp, None)
            g.DEST_DIR = saved

    def test_both_sections_exist_from_the_start(self):
        srv.save_matching_rule(self.path, 'Star Trek', 'accept')
        srv.save_matching_rule(self.path, 'Supernatural (2025)', 'refuse')
        self.assertEqual(self.entries(),
                         {'star trek': 'accept', 'supernatural (2025)': 'refuse'})


class TestChangingYourMind(RulesFileFixture):
    """The case that makes appending wrong.

    You click accept, then look at the actual books and decide no. If the old
    line survives, the folder is listed twice with opposite meanings and which
    one wins is an accident of dict ordering.
    """

    def test_a_reversal_replaces_the_earlier_answer(self):
        srv.save_matching_rule(self.path, 'Star Trek', 'accept')
        srv.save_matching_rule(self.path, 'Star Trek', 'refuse')
        self.assertEqual(self.entries(), {'star trek': 'refuse'})

    def test_the_old_line_is_gone_not_merely_outvoted(self):
        srv.save_matching_rule(self.path, 'Star Trek', 'accept')
        srv.save_matching_rule(self.path, 'Star Trek', 'refuse')
        self.assertEqual(self.path.read_text().count('- Star Trek'), 1)

    def test_saving_the_same_answer_twice_is_not_two_entries(self):
        srv.save_matching_rule(self.path, 'Star Trek', 'accept')
        srv.save_matching_rule(self.path, 'Star Trek', 'accept')
        self.assertEqual(self.path.read_text().count('- Star Trek'), 1)

    def test_a_reversal_matches_regardless_of_how_you_typed_it(self):
        srv.save_matching_rule(self.path, 'Rick and Morty ', 'accept')
        srv.save_matching_rule(self.path, 'rick and morty', 'refuse')
        self.assertEqual(self.entries(), {'rick and morty': 'refuse'})


class TestTheFileStaysReadable(RulesFileFixture):
    """It is documentation as much as data, and a person edits it by hand."""

    PROSE = """# Saved Matching Rules

Some paragraph a human wrote.

## Accept (1)

Why you would accept.

- Aardvark

## Refuse (0)

Why you would refuse.
"""

    def setUp(self):
        super().setUp()
        self.path.write_text(self.PROSE, encoding='utf-8')

    def test_the_explanations_survive_a_save(self):
        srv.save_matching_rule(self.path, 'Star Trek', 'accept')
        text = self.path.read_text()
        self.assertIn('Why you would accept.', text)
        self.assertIn('Why you would refuse.', text)
        self.assertIn('Some paragraph a human wrote.', text)

    def test_entries_are_filed_alphabetically(self):
        for name in ('Zatanna', 'Batman'):
            srv.save_matching_rule(self.path, name, 'accept')
        accept = self.path.read_text().split('## Refuse')[0]
        self.assertLess(accept.index('- Aardvark'), accept.index('- Batman'))
        self.assertLess(accept.index('- Batman'), accept.index('- Zatanna'))

    def test_the_heading_count_is_kept_true(self):
        srv.save_matching_rule(self.path, 'Batman', 'accept')
        srv.save_matching_rule(self.path, 'Joker', 'refuse')
        text = self.path.read_text()
        self.assertIn('## Accept (2)', text)
        self.assertIn('## Refuse (1)', text)

    def test_an_entry_lands_in_the_section_it_was_meant_for(self):
        srv.save_matching_rule(self.path, 'Joker', 'refuse')
        self.assertEqual(self.entries()['joker'], 'refuse')


class TestAHandEditedFileThatLostASection(RulesFileFixture):
    """Rather than a button that appears to work and does nothing."""

    def setUp(self):
        super().setUp()
        self.path.write_text("# Rules\n\n## Accept (0)\n", encoding='utf-8')

    def test_the_missing_section_is_recreated(self):
        srv.save_matching_rule(self.path, 'Supernatural (2025)', 'refuse')
        self.assertEqual(self.entries(), {'supernatural (2025)': 'refuse'})


class TestWhatAFolderNameMayNotBe(RulesFileFixture):
    """Every line of this file means something, so the name becomes a line.

    The value arrives in a POST body. A name carrying a newline could write its
    own '## ' heading or its own '- ' bullets, which is a folder granting itself
    permissions in a section the user never opened.
    """

    def test_a_newline_cannot_forge_extra_rules(self):
        with self.assertRaises(ValueError):
            srv.save_matching_rule(
                self.path, 'Harmless\n- Star Trek\n- Mark Millar', 'accept')
        self.assertEqual(self.entries(), {})

    def test_a_newline_cannot_forge_a_section(self):
        with self.assertRaises(ValueError):
            srv.save_matching_rule(self.path, 'X\n\n## Accept (1)\n- Batman', 'refuse')

    def test_a_carriage_return_counts_as_a_newline(self):
        """splitlines() breaks on \\r too, so checking only for \\n would miss it."""
        with self.assertRaises(ValueError):
            srv.save_matching_rule(self.path, 'X\r- Star Trek', 'accept')

    def test_a_path_is_not_a_folder_name(self):
        """The matcher only ever compares top-level names."""
        with self.assertRaises(ValueError):
            srv.save_matching_rule(self.path, '../../etc/passwd', 'accept')

    def test_an_empty_name_is_refused(self):
        """'' would otherwise register and classify every folder at once."""
        for name in ('', '   '):
            with self.assertRaises(ValueError):
                srv.save_matching_rule(self.path, name, 'accept')

    def test_only_the_two_decisions_are_writable(self):
        """Otherwise a typo'd decision invents a section that means nothing."""
        for bad in ('', 'maybe', 'Publisher', 'accept ; rm -rf'):
            with self.assertRaises(ValueError):
                srv.save_matching_rule(self.path, 'Star Trek', bad)
        self.assertEqual(self.entries(), {})

    def test_the_decision_is_not_case_sensitive(self):
        srv.save_matching_rule(self.path, 'Star Trek', 'ACCEPT')
        self.assertEqual(self.entries(), {'star trek': 'accept'})

    def test_an_ordinary_name_with_brackets_is_fine(self):
        """Most real folders carry a year, so this must not be over-tightened."""
        srv.save_matching_rule(self.path, 'GG Studio (Collection) (2010-2012)', 'refuse')
        self.assertIn('gg studio (collection) (2010-2012)', self.entries())


if __name__ == '__main__':
    unittest.main(verbosity=2)
