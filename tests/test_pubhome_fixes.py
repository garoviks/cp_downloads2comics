#!/usr/bin/env python3
"""The 'File this series in its publisher folder' button, after the first real use.

Three things the user hit:
  1. The button never said WHICH folder. It now reads 'File The Cloven in
     Fantagraphics (Europe)', from a read-only question to the server, and is not
     offered when no folder would be picked.
  2. After saving, the page looked unchanged until a rescan AND an F5. It now
     rescans and reloads its rows itself, and says so; a failed rescan is said
     plainly and points at Scan Folders.
  3. Every save of the rules file left one more blank line at the end.

Temp dirs only. The page is exercised in node with a stubbed DOM and fetch.

Run:  python3 -m unittest discover tests
"""
import json
import os
import shutil
import subprocess
import sys
import tempfile
import threading
import unittest
import urllib.request
from http.server import ThreadingHTTPServer
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import paths

srv = paths.load_serve_v2()
HTML = Path(paths.GENERATOR_DIR) / 'comic_organizer_v2.html'


def page_functions(*names):
    """Source of the named top-level functions in the page (async ones too), for running in node."""
    html = HTML.read_text(encoding='utf-8')
    out = []
    for name in names:
        start = html.index(f'function {name}(')
        if html[start - 6:start] == 'async ':
            start -= 6
        depth, i = 0, html.index('{', start)
        for j in range(i, len(html)):
            depth += (html[j] == '{') - (html[j] == '}')
            if depth == 0:
                out.append(html[start:j + 1])
                break
    return '\n'.join(out)

CLOVEN = 'The Cloven - Book Three (2025) (Graphic Novel) (Fantagraphics) (Digital-HD) (LeDuch).cbz'
HAVE_NODE = shutil.which('node') is not None


def node(js, stdin=''):
    out = subprocess.run(['node', '-e', js], input=stdin, capture_output=True, text=True, timeout=30)
    if out.returncode:
        raise AssertionError(out.stderr)
    return json.loads(out.stdout)


PREAMBLE = (
    'const PUBLISHER_KEYWORDS = ["Cinebook", "Fantagraphics", "Humanoids", "Soleil", "SAF"];\n'
    + page_functions('basename', 'esc', 'publisherKeywordIn', 'publisherHomeButtonHtml')
)


@unittest.skipUnless(HAVE_NODE, 'node not installed')
class TestTheButtonNamesItsFolder(unittest.TestCase):

    def button(self, row, folder):
        js = (PREAMBLE + '\nconst r = JSON.parse(process.argv[1]);'
              + '\nconsole.log(JSON.stringify(publisherHomeButtonHtml(r.row, r.folder)));')
        out = subprocess.run(['node', '-e', js, json.dumps({'row': row, 'folder': folder})],
                             capture_output=True, text=True, timeout=30)
        self.assertEqual(out.returncode, 0, out.stderr)
        return json.loads(out.stdout)

    def test_the_text_names_series_and_folder(self):
        html = self.button({'id': 3, 'leftFile': CLOVEN, 'series': 'The Cloven'}, 'Fantagraphics (Europe)')
        self.assertIn('File The Cloven in Fantagraphics (Europe)', html)
        self.assertNotIn('its publisher folder', html)

    def test_no_folder_found_means_no_button(self):
        self.assertEqual(self.button({'id': 3, 'leftFile': CLOVEN, 'series': 'The Cloven'}, None), '')
        self.assertEqual(self.button({'id': 3, 'leftFile': CLOVEN, 'series': 'The Cloven'}, ''), '')

    def test_no_publisher_keyword_in_the_name_means_no_button(self):
        self.assertEqual(self.button({'id': 3, 'leftFile': 'Saga 001 (2020) (digital).cbz', 'series': 'Saga'},
                                     'Fantagraphics (Europe)'), '')

    def test_names_are_escaped(self):
        html = self.button({'id': 1, 'leftFile': CLOVEN, 'series': 'A <b> & C'}, 'F "x"')
        self.assertNotIn('<b>', html)


class TestTheServerAnswersWithoutWriting(unittest.TestCase):

    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix='pubhome-'))
        (self.tmp / 'Fantagraphics (Europe)').mkdir()
        (self.tmp / 'The Cloven').mkdir()
        self.addCleanup(shutil.rmtree, self.tmp, ignore_errors=True)
        self.httpd = ThreadingHTTPServer(('127.0.0.1', 0), srv.ComicOrganizerV2Handler)
        threading.Thread(target=self.httpd.serve_forever, daemon=True).start()
        self.addCleanup(self.httpd.shutdown)

    def ask(self, file):
        req = urllib.request.Request(
            f'http://127.0.0.1:{self.httpd.server_address[1]}/api/publisher-home-folder',
            json.dumps({'file': file, 'dest_dir': str(self.tmp)}).encode(),
            {'Content-Type': 'application/json'})
        return json.load(urllib.request.urlopen(req, timeout=10))

    def test_it_names_the_folder_the_save_would_use(self):
        self.assertEqual(self.ask(CLOVEN), {'folder': 'Fantagraphics (Europe)'})

    def test_no_folder_is_null(self):
        self.assertEqual(self.ask('Saga 001 (2020).cbz'), {'folder': None})
        self.assertEqual(self.ask('Foo (Cinebook).cbz'), {'folder': None})     # keyword, but no Cinebook folder

    def test_asking_writes_nothing(self):
        self.ask(CLOVEN)
        self.assertEqual(sorted(p.name for p in self.tmp.iterdir()), ['Fantagraphics (Europe)', 'The Cloven'])


@unittest.skipUnless(HAVE_NODE, 'node not installed')
class TestSavingRefreshesThePage(unittest.TestCase):
    """savePublisherHome() -> rescan -> rows reloaded, without a manual F5."""

    def run_flow(self, scan_ok):
        js = (PREAMBLE + '\n'
              + page_functions('savePublisherHome', 'scanFolders') + r'''
const toasts = [], logs = []; let renders = 0;
const data = [{ id: 0, leftFile: %(f)s, series: 'The Cloven', folder: '/The Cloven/', action: 'CONSOLIDATE' }];
const els = {};
const document = { getElementById: id => els[id] || (els[id] = { textContent: '/x', innerHTML: '', disabled: true }) };
const closeConsole = () => {}, showConsole = () => {}, closeModal = () => {}, renderAll = () => { renders++; };
const addLog = m => logs.push(m), toast = m => toasts.push(m);
const currentFolders = () => ({ srcDir: '/src', destDir: '/dest' });
const SCAN_OK = %(ok)s;
const fetch = async (url) => {
  if (url === '/api/save-publisher-home') return { ok: true, json: async () => ({ saved: 'Publisher home: The Cloven => Fantagraphics (Europe)' }) };
  if (url === '/api/scan') {
    if (!SCAN_OK) return { ok: false, status: 500 };
    let sent = false;
    return { ok: true, body: { getReader: () => ({ read: async () => sent ? { done: true } : (sent = true, { done: false, value: new TextEncoder().encode('done\n') }) }) } };
  }
  if (url === '/api/csv') return { ok: true, json: async () => ([{ 'Left Panel File': %(f)s, 'Series Name': 'The Cloven',
      'Action Type': 'CONSOLIDATE', 'Suggested Folder Name': '/Fantagraphics (Europe)/', 'Right Panel Matches (Count)': '1' }]) };
  throw new Error('unexpected ' + url);
};
(async () => {
  await savePublisherHome(0);
  console.log(JSON.stringify({ folder: data[0] && data[0].folder, toasts, renders }));
})();
''' % {'f': json.dumps(CLOVEN), 'ok': 'true' if scan_ok else 'false'})
        return node(js)

    def test_the_cloven_row_changes_in_place_and_the_note_says_so(self):
        got = self.run_flow(True)
        self.assertEqual(got['folder'], '/Fantagraphics (Europe)/')
        self.assertGreaterEqual(got['renders'], 1)
        self.assertEqual(got['toasts'][-1], 'Saved: Publisher home: The Cloven => Fantagraphics (Europe). Rescanned.')

    def test_a_failed_rescan_is_said_plainly(self):
        got = self.run_flow(False)
        self.assertEqual(got['folder'], '/The Cloven/')
        last = got['toasts'][-1]
        self.assertIn('Saved', last)
        self.assertIn('rescan failed', last.lower())
        self.assertIn('Scan Folders', last)
        self.assertNotIn('Rescanned.', last)


class TestSavesDoNotGrowBlankLines(unittest.TestCase):

    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix='pubhome-rules-'))
        self.rules = self.tmp / '.comic_matching_rules.md'
        self.addCleanup(shutil.rmtree, self.tmp, ignore_errors=True)
        # The user's real file: a Publisher home section with a line and a blank tail.
        self.base = ('# rules\n\n## Accept (0)\n\nprose\n\n## Refuse (0)\n\nprose\n\n'
                     '## Publisher home (1)\n\n- The Cloven => Fantagraphics (Europe)\n\n')

    def fresh(self):
        self.rules.write_text(self.base, encoding='utf-8')

    def test_three_publisher_home_saves_equal_one(self):
        self.fresh()
        srv.save_publisher_home(self.rules, 'The Cloven', 'Fantagraphics (Europe)')
        once = self.rules.read_text(encoding='utf-8')
        for _ in range(2):
            srv.save_publisher_home(self.rules, 'The Cloven', 'Fantagraphics (Europe)')
        self.assertEqual(self.rules.read_text(encoding='utf-8'), once)
        self.assertTrue(once.endswith('Fantagraphics (Europe)\n'), repr(once[-40:]))

    def test_three_accept_saves_equal_one(self):
        self.fresh()
        srv.save_matching_rule(self.rules, 'Zed', 'accept')
        once = self.rules.read_text(encoding='utf-8')
        for _ in range(2):
            srv.save_matching_rule(self.rules, 'Zed', 'accept')
        self.assertEqual(self.rules.read_text(encoding='utf-8'), once)

    def test_mixed_saves_in_a_row_keep_one_trailing_newline(self):
        self.fresh()
        for i in range(3):
            srv.save_matching_rule(self.rules, f'F{i}', 'refuse')
            srv.save_publisher_home(self.rules, f'S{i}', 'Fantagraphics (Europe)')
        text = self.rules.read_text(encoding='utf-8')
        self.assertTrue(text.endswith('\n') and not text.endswith('\n\n'), repr(text[-40:]))
        self.assertNotIn('\n\n\n', text)

    def test_the_backup_still_holds_the_file_before_the_save(self):
        self.fresh()
        srv.save_publisher_home(self.rules, 'The Cloven', 'Fantagraphics (Europe)')
        self.assertEqual((self.tmp / '.comic_matching_rules.md.bak').read_text(encoding='utf-8'), self.base)

    def test_prose_and_entries_are_kept(self):
        self.fresh()
        srv.save_publisher_home(self.rules, 'Other', 'Fantagraphics (Europe)')
        text = self.rules.read_text(encoding='utf-8')
        for want in ('prose', '- The Cloven => Fantagraphics (Europe)', '- Other => Fantagraphics (Europe)'):
            self.assertIn(want, text)


if __name__ == '__main__':
    unittest.main()
