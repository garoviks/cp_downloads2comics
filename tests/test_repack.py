#!/usr/bin/env python3
"""Repacking a comic must not lose a page, and must not lose the original.

Everything here turns on one asymmetry: the new file is disposable and the old
file is not. So the order is always extract, build, *verify*, and only then
move the original aside. A repack that cannot prove the page count survived has
to leave the library exactly as it found it — a comic that no reader opens is
still better than a comic that is gone.

The other half is that the originals go to quarantine rather than to nothing.
`test_the_original_is_moved_not_deleted` is the one that would catch a future
`unlink` creeping in, and it asserts on the bytes, not just the path.

Run:  python3 -m unittest discover tests
"""
import io
import os
import shutil
import subprocess
import sys
import tarfile
import tempfile
import unittest
import zipfile
from pathlib import Path
from unittest import mock

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import paths

sys.path.insert(0, paths.GENERATOR_DIR)
import repack_comics as rp

gen = paths.load_generator()


def jpeg_bytes(colour=(200, 30, 30), size=(40, 60)):
    from PIL import Image
    buf = io.BytesIO()
    Image.new('RGB', size, colour).save(buf, 'JPEG')
    return buf.getvalue()


def webp_bytes(colour=(30, 200, 30), size=(40, 60)):
    from PIL import Image
    buf = io.BytesIO()
    Image.new('RGB', size, colour).save(buf, 'WEBP')
    return buf.getvalue()


def page_colour(i, issue=0):
    """A colour per page, and a different one per issue, so that two pages are
    never byte-identical and a mis-ordered merge cannot pass unnoticed."""
    return (i * 7 % 256, 100, 40 + issue * 30)


def make_pages(folder, count, ext='.jpg', issue=0):
    """`count` distinct pages, each a different colour so order is provable."""
    folder.mkdir(parents=True, exist_ok=True)
    for i in range(1, count + 1):
        colour = page_colour(i, issue)
        data = webp_bytes(colour) if ext == '.webp' else jpeg_bytes(colour)
        (folder / f'{i:03d}{ext}').write_bytes(data)


class RepackTests(unittest.TestCase):

    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.library = self.tmp / 'Comics'
        self.quarantine = self.tmp / '_quarantine'
        self.staging = self.tmp / '_repack_staging'
        self.library.mkdir()
        # The real paths point at a 3.6 TB library. Everything below has to
        # happen inside the temp dir or the test is not a test.
        #
        # The log and report paths matter as much as the library ones: any test
        # that goes through main() calls save_log(), and an unpatched LOG_DIR
        # writes a /tmp fixture into the repo's real run history, which then
        # shows up as a row in the report. That happened once.
        logs = self.tmp / 'logs'
        self.patches = [
            mock.patch.object(rp, 'LIBRARY', self.library),
            mock.patch.object(rp, 'QUARANTINE', self.quarantine),
            mock.patch.object(rp, 'STAGING', self.staging),
            mock.patch.object(rp, 'TEMP_ROOT', self.tmp),
            mock.patch.object(rp, 'LOG_DIR', logs),
            mock.patch.object(rp, 'REPACK_LOG', logs / 'last_repack.json'),
            mock.patch.object(rp, 'REPACK_HISTORY', logs / 'repacks.jsonl'),
            mock.patch.object(rp, 'REPORT', self.tmp / 'report.md'),
            mock.patch.object(rp, 'REDOWNLOAD', self.tmp / 'redownload.md'),
            mock.patch.object(rp, 'MISORDERED', self.tmp / 'misordered.md'),
        ]
        for p in self.patches:
            p.start()

    def tearDown(self):
        for p in self.patches:
            p.stop()
        shutil.rmtree(self.tmp, ignore_errors=True)

    def _work(self):
        w = self.tmp / 'work'
        w.mkdir(exist_ok=True)
        return w

    def _seven_zip(self, name, pages=5, ext='.jpg'):
        src = self.tmp / 'src'
        shutil.rmtree(src, ignore_errors=True)
        make_pages(src, pages, ext)
        out = self.library / name
        rc = subprocess.run(['7z', 'a', '-t7z', str(out), str(src / '*')],
                            capture_output=True).returncode
        self.assertEqual(rc, 0, '7z is needed for this test')
        return out

    def _tar(self, name, pages=4):
        src = self.tmp / 'src_tar'
        shutil.rmtree(src, ignore_errors=True)
        make_pages(src, pages)
        out = self.library / name
        with tarfile.open(out, 'w') as t:
            for f in sorted(src.iterdir()):
                t.add(f, arcname=f.name)
        return out

    # ------------------------------------------------ count in == count out

    def test_a_7z_wearing_a_cbr_name_survives_the_round_trip(self):
        original = self._seven_zip('book.cbr', pages=5)
        self.assertEqual(rp.detect_format(original), '7z')
        before = gen.page_count(original)

        rp.do_repack(original, convert=False, work=self._work())

        new = self.library / 'book.cbz'
        self.assertTrue(zipfile.is_zipfile(new))
        gen._PAGE_COUNTS.clear()
        self.assertEqual(gen.page_count(new), before)
        self.assertFalse(original.exists(), 'the .cbr name should be gone')

    def test_a_tar_wearing_a_cbr_name_survives_the_round_trip(self):
        original = self._tar('firefly.cbr', pages=4)
        self.assertEqual(rp.detect_format(original), 'tar')
        before = gen.page_count(original)

        rp.do_repack(original, convert=False, work=self._work())

        gen._PAGE_COUNTS.clear()
        self.assertEqual(gen.page_count(self.library / 'firefly.cbz'), before)

    def test_pages_are_stored_not_deflated(self):
        """Every page is already a compressed image. Deflating one again costs
        CPU at both ends to save nothing, and stored is what the slow readers
        are happiest with."""
        rp.do_repack(self._seven_zip('stored.cbr'), convert=False, work=self._work())
        with zipfile.ZipFile(self.library / 'stored.cbz') as z:
            kinds = {i.compress_type for i in z.infolist()}
        self.assertEqual(kinds, {zipfile.ZIP_STORED})

    # ------------------------------------------------ the conversion is opt-in

    def test_webp_pages_are_left_alone_unless_asked(self):
        """Re-encoding is lossy and cannot be undone, so it does not happen by
        default. Repacking the container first is what tells us whether the
        image format was ever the reader's problem."""
        original = self._seven_zip('webp.cbr', pages=4, ext='.webp')
        rp.do_repack(original, convert=False, work=self._work())
        with zipfile.ZipFile(self.library / 'webp.cbz') as z:
            names = z.namelist()
            first = z.read(sorted(names)[0])
        self.assertTrue(all(n.endswith('.webp') for n in names), names)
        self.assertTrue(first.startswith(b'RIFF'), 'page is no longer WebP')

    def test_converting_turns_webp_into_jpeg_and_keeps_the_order(self):
        original = self._seven_zip('webp2.cbr', pages=6, ext='.webp')
        before = gen.page_count(original)

        rp.do_repack(original, convert=True, work=self._work())

        with zipfile.ZipFile(self.library / 'webp2.cbz') as z:
            names = z.namelist()
        self.assertEqual(len(names), before)
        self.assertTrue(all(n.endswith('.jpg') for n in names), names)
        # Only the extension changed, so the page numbers still sort the way
        # they did — that is the whole reason the extension is all we touch.
        self.assertEqual(names, sorted(names))
        self.assertEqual([Path(n).stem for n in sorted(names)],
                         [f'{i:03d}' for i in range(1, before + 1)])

    def test_a_transparent_page_is_flattened_onto_white(self):
        """RGBA has no meaning in a JPEG. Left to Pillow it raises; flattened
        onto black the page reads as a dark smear."""
        from PIL import Image
        src = self.tmp / 'rgba.png'
        Image.new('RGBA', (20, 20), (255, 0, 0, 0)).save(src)
        out = rp.to_jpeg(src)
        with Image.open(out) as im:
            self.assertEqual(im.mode, 'RGB')
            self.assertEqual(im.getpixel((10, 10)), (255, 255, 255))

    # ------------------------------------------------ failure leaves no mark

    def test_a_failed_verification_leaves_the_original_in_place(self):
        original = self._seven_zip('fragile.cbr', pages=5)
        before = original.read_bytes()

        with mock.patch.object(rp, 'verify',
                               side_effect=RuntimeError('page count changed')):
            with self.assertRaises(RuntimeError):
                rp.do_repack(original, convert=False, work=self._work())

        self.assertTrue(original.exists(), 'the original was not put back')
        self.assertEqual(original.read_bytes(), before)
        self.assertFalse((self.library / 'fragile.cbz').exists())
        self.assertFalse(self.quarantine.exists(),
                         'nothing should have reached quarantine')
        self.assertEqual(list(self.staging.rglob('*.cbr')), [],
                         'staging must be empty again after a failure')

    def test_verify_rejects_a_short_repack(self):
        """The guard itself, rather than a caller that happens to trip it."""
        good = self.tmp / 'four.cbz'
        with zipfile.ZipFile(good, 'w') as z:
            for i in range(4):
                z.writestr(f'{i:03d}.jpg', jpeg_bytes())
        self.assertEqual(rp.verify(good, 4), 4)
        with self.assertRaises(RuntimeError):
            rp.verify(good, 5)

    def test_it_refuses_to_overwrite_an_occupied_quarantine_slot(self):
        original = self._seven_zip('twice.cbr', pages=3)
        slot = rp.quarantine_path(original)
        slot.parent.mkdir(parents=True, exist_ok=True)
        slot.write_bytes(b'an earlier run put something here')

        with self.assertRaises(FileExistsError):
            rp.do_repack(original, convert=False, work=self._work())

        self.assertTrue(original.exists())
        self.assertEqual(slot.read_bytes(), b'an earlier run put something here')

    def test_it_refuses_to_overwrite_an_occupied_destination(self):
        """A .cbr repacking to .cbz can land on a .cbz that already exists —
        a different book, or the same book from a different scanner."""
        original = self._seven_zip('collision.cbr', pages=3)
        squatter = self.library / 'collision.cbz'
        squatter.write_bytes(b'someone else lives here')

        with self.assertRaises(FileExistsError):
            rp.do_repack(original, convert=False, work=self._work())

        self.assertTrue(original.exists(), 'the original must be put back')
        self.assertEqual(squatter.read_bytes(), b'someone else lives here')

    # ------------------------------------------------ the original is kept

    def test_the_original_is_moved_not_deleted(self):
        original = self._seven_zip('keepme.cbr', pages=3)
        before = original.read_bytes()

        rp.do_repack(original, convert=False, work=self._work())

        kept = self.quarantine / 'keepme.cbr'
        self.assertTrue(kept.exists(), 'the original is nowhere')
        self.assertEqual(kept.read_bytes(), before, 'quarantine holds a copy, '
                                                    'but not the same bytes')

    def test_quarantine_keeps_the_place_the_file_had_in_the_library(self):
        (self.library / 'Firefly').mkdir()
        original = self._seven_zip('Firefly/special.cbr', pages=3)
        rp.do_repack(original, convert=False, work=self._work())
        self.assertTrue((self.quarantine / 'Firefly' / 'special.cbr').exists())

    # ------------------------------------------------ staging

    def test_the_original_leaves_the_library_before_it_is_read(self):
        """The window where a half-written file could sit next to a good one is
        the window this closes: while the replacement is being built, the
        original is out of the library entirely."""
        original = self._seven_zip('moved.cbr', pages=3)
        seen = {}

        real_extract = rp.extract

        def watch(path, dest):
            seen['original_gone'] = not original.exists()
            seen['in_staging'] = rp.staging_path(original).exists()
            seen['reading'] = Path(path)
            return real_extract(path, dest)

        with mock.patch.object(rp, 'extract', watch):
            rp.do_repack(original, convert=False, work=self._work())

        self.assertTrue(seen['original_gone'])
        self.assertTrue(seen['in_staging'])
        self.assertEqual(seen['reading'], rp.staging_path(original),
                         'the staged copy is what gets extracted')

    def test_staging_is_empty_once_a_repack_succeeds(self):
        rp.do_repack(self._seven_zip('clean.cbr', pages=3),
                     convert=False, work=self._work())
        self.assertEqual([p for p in self.staging.rglob('*') if p.is_file()], [])

    def test_an_occupied_staging_slot_stops_the_repack_before_anything_moves(self):
        original = self._seven_zip('busy.cbr', pages=3)
        slot = rp.staging_path(original)
        slot.parent.mkdir(parents=True, exist_ok=True)
        slot.write_bytes(b'an earlier run died holding this')

        with self.assertRaises(FileExistsError):
            rp.do_repack(original, convert=False, work=self._work())

        self.assertTrue(original.exists())
        self.assertEqual(slot.read_bytes(), b'an earlier run died holding this')

    def test_a_run_refuses_to_start_on_a_dirty_staging_folder(self):
        """Leftovers mean a previous run died mid-flight. Carrying on would
        repack around a file the library is still missing."""
        self.staging.mkdir(parents=True, exist_ok=True)
        (self.staging / 'orphan.cbr').write_bytes(b'left behind')
        self._seven_zip('next.cbr', pages=2)

        with mock.patch.object(rp, 'PHASE1', ['next.cbr']), \
             mock.patch.object(rp, 'HTML_JUNK', []), \
             mock.patch.object(sys, 'argv', ['repack_comics.py', '--execute']):
            rc = rp.main()

        self.assertEqual(rc, 1)
        self.assertTrue((self.library / 'next.cbr').exists())
        self.assertFalse((self.library / 'next.cbz').exists())

    # ------------------------------------------------ the wrapper

    def _wrapper(self, name, issue_pages):
        """A .cbz holding whole .cbr comics instead of pages."""
        holder = self.tmp / 'holder'
        shutil.rmtree(holder, ignore_errors=True)
        holder.mkdir()
        for n, count in enumerate(issue_pages, 1):
            pages = self.tmp / f'iss{n}'
            shutil.rmtree(pages, ignore_errors=True)
            make_pages(pages, count, issue=n)
            inner = holder / f'Series {n:03d} (2018).cbz'
            with zipfile.ZipFile(inner, 'w', zipfile.ZIP_STORED) as z:
                for f in sorted(pages.iterdir()):
                    z.write(f, arcname=f.name)
        out = self.library / name
        with zipfile.ZipFile(out, 'w', zipfile.ZIP_STORED) as z:
            # Written back to front on purpose: issue order must come from the
            # names, not from the order the zip happens to store them in.
            for f in sorted(holder.iterdir(), reverse=True):
                z.write(f, arcname=f.name)
        return out

    def test_the_omnibus_totals_every_page_from_every_issue(self):
        original = self._wrapper('omni.cbz', [31, 26, 30, 30, 29])
        self.assertEqual(gen.page_count(original), 0,
                         'a wrapper holds no pages of its own — that is why no '
                         'reader opens it')

        rp.do_omnibus(original, convert=False, work=self._work())

        gen._PAGE_COUNTS.clear()
        self.assertEqual(gen.page_count(self.library / 'omni.cbz'), 146)

    def test_the_omnibus_runs_the_issues_in_number_order(self):
        """Page 1 of issue 2 must follow the last page of issue 1, whatever
        order the members came out of the wrapper in."""
        original = self._wrapper('order.cbz', [3, 3, 3])
        rp.do_omnibus(original, convert=False, work=self._work())

        with zipfile.ZipFile(self.library / 'order.cbz') as z:
            names = z.namelist()
            pages = [z.read(n) for n in names]

        self.assertEqual(names, [f'{i:03d}.jpg' for i in range(1, 10)])
        # Each source page was given a distinct colour, so identical bytes at
        # two positions would mean an issue was read twice.
        self.assertEqual(len(set(pages)), 9)
        # Issue 1 pages 1..3, then issue 2 pages 1..3, then issue 3.
        expected = [jpeg_bytes(page_colour(i, issue))
                    for issue in (1, 2, 3) for i in range(1, 4)]
        self.assertEqual(pages, expected)

    def test_a_wrapper_is_recognised_without_being_told(self):
        wrapper = self._wrapper('w.cbz', [2, 2])
        plain = self._seven_zip('p.cbr', pages=2)
        self.assertTrue(rp._is_wrapper(wrapper))
        self.assertFalse(rp._is_wrapper(plain))

    # ------------------------------------------------ merging issues

    def _issue(self, name, pages, issue, ext='.jpg'):
        """One issue as a .cbz, pages named the way a scanner would."""
        src = self.tmp / f'mk_{issue}'
        shutil.rmtree(src, ignore_errors=True)
        make_pages(src, pages, ext, issue=issue)
        out = self.library / name
        out.parent.mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(out, 'w', zipfile.ZIP_STORED) as z:
            for f in sorted(src.iterdir()):
                z.write(f, arcname=f.name)
        return out

    def test_merge_orders_issue_2_before_issue_10(self):
        """The bug this replaces, stated as a test.

        makecbz.py numbered its folders without padding, so `temp_extract_10_`
        sorted ahead of `temp_extract_1_` and every volume of eleven or more
        issues read 1, 11, 12, 2, 3. Unpadded issue *filenames* are the same
        trap one level up, which is why the sources are sorted naturally.
        """
        sources = [self._issue(f'Series {i}.cbz', 2, issue=i)
                   for i in range(1, 13)]
        out = self.library / 'Series v01.cbz'

        with tempfile.TemporaryDirectory() as tmp:
            rp.do_merge(sources, out, convert=False, work=Path(tmp))

        with zipfile.ZipFile(out) as z:
            names = sorted(z.namelist())
            pages = [z.read(n) for n in names]

        self.assertEqual(len(names), 24)
        self.assertEqual([n.split('/')[0] for n in names],
                         [f'{i:04d}' for i in range(1, 13) for _ in range(2)])
        expected = [jpeg_bytes(page_colour(p, i))
                    for i in range(1, 13) for p in (1, 2)]
        self.assertEqual(pages, expected, 'issues are not in reading order')

    def test_merge_keeps_the_page_names_inside_an_issue(self):
        """Only the prefix is added. A page sequence that read correctly as a
        single issue still reads correctly inside the volume."""
        sources = [self._issue('One.cbz', 3, issue=1)]
        out = self.library / 'vol.cbz'
        with tempfile.TemporaryDirectory() as tmp:
            rp.do_merge(sources, out, convert=False, work=Path(tmp))
        with zipfile.ZipFile(out) as z:
            self.assertEqual(sorted(z.namelist()),
                             ['0001/001.jpg', '0001/002.jpg', '0001/003.jpg'])

    def test_merge_keeps_the_issues(self):
        """makecbz.py called os.remove on them. A merge that read the wrong
        pages is only correctable while the issues still exist."""
        sources = [self._issue('Keep 1.cbz', 2, issue=1),
                   self._issue('Keep 2.cbz', 2, issue=2)]
        with tempfile.TemporaryDirectory() as tmp:
            rp.do_merge(sources, self.library / 'kept.cbz', False, Path(tmp))
        for s in sources:
            self.assertFalse(s.exists())
            self.assertTrue((self.quarantine / s.name).exists(), s.name)

    def test_merge_refuses_to_overwrite(self):
        sources = [self._issue('A 1.cbz', 2, issue=1)]
        out = self.library / 'taken.cbz'
        out.write_bytes(b'already here')
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(FileExistsError):
                rp.do_merge(sources, out, False, Path(tmp))
        self.assertEqual(out.read_bytes(), b'already here')

    def test_bare_merge_takes_the_whole_folder_and_names_it_after_it(self):
        """How makecbz.py was actually run: from inside a series folder with
        no arguments. The replacement has to answer to the same gesture."""
        folder = self.library / 'Some Series (2019)'
        folder.mkdir(parents=True)
        for n in (1, 2, 10):
            self._issue(f'Some Series (2019)/Some Series {n:03d}.cbz', 2, issue=n)
        (folder / 'notes.txt').write_text('not a comic')

        with mock.patch.object(sys, 'argv', ['repack_comics.py', '--merge',
                                             '--dir', str(folder), '--execute']):
            self.assertEqual(rp.main(), 0)

        out = folder / 'Some Series (2019).cbz'
        self.assertTrue(out.exists(), 'volume not named after its folder')
        with zipfile.ZipFile(out) as z:
            names = sorted(z.namelist())
        self.assertEqual([n.split('/')[0] for n in names],
                         ['0001', '0001', '0002', '0002', '0003', '0003'])
        self.assertEqual(len(names), 6, 'notes.txt should not have been swept in')

    def test_a_test_run_never_touches_the_real_run_history(self):
        """Guards the harness, not the tool. Every path the script writes to
        has to be redirected into the temp dir, or a test leaves a fixture in
        the repo's history and the next report renders it as a real comic."""
        real = Path(rp.__file__).resolve().parent
        for name in ('LOG_DIR', 'REPACK_LOG', 'REPACK_HISTORY',
                     'REPORT', 'REDOWNLOAD', 'MISORDERED'):
            value = Path(getattr(rp, name))
            self.assertFalse(value.is_relative_to(real),
                             f'{name} still points into the repo: {value}')
            self.assertTrue(value.is_relative_to(self.tmp), name)

    def test_bare_merge_does_not_eat_its_own_output(self):
        """Re-running in a folder that already holds the volume must not fold
        the volume back into itself."""
        folder = self.library / 'Twice (2020)'
        folder.mkdir(parents=True)
        self._issue('Twice (2020)/Twice 001.cbz', 2, issue=1)
        volume = folder / 'Twice (2020).cbz'
        volume.write_bytes(b'the volume from last time')

        with mock.patch.object(sys, 'argv', ['repack_comics.py', '--merge',
                                             '--dir', str(folder), '--execute']):
            rc = rp.main()

        self.assertEqual(rc, 1, 'should refuse rather than overwrite')
        self.assertEqual(volume.read_bytes(), b'the volume from last time')

    def test_bare_merge_on_an_empty_folder_says_so_and_writes_nothing(self):
        folder = self.library / 'Nothing Here'
        folder.mkdir(parents=True)
        with mock.patch.object(sys, 'argv', ['repack_comics.py', '--merge',
                                             '--dir', str(folder), '--execute']):
            self.assertEqual(rp.main(), 1)
        self.assertEqual(list(folder.iterdir()), [])

    def test_natural_key_puts_2_before_10(self):
        names = ['Issue 10.cbz', 'Issue 2.cbz', 'Issue 1.cbz']
        self.assertEqual(sorted(names, key=rp.natural_key),
                         ['Issue 1.cbz', 'Issue 2.cbz', 'Issue 10.cbz'])
        self.assertEqual(sorted(names),
                         ['Issue 1.cbz', 'Issue 10.cbz', 'Issue 2.cbz'])

    # ------------------------------------------------ repairing old volumes

    def _makecbz_volume(self, name, issue_pages):
        """A volume shaped exactly as makecbz.py left it: pages under unpadded
        `temp_extract_{i}_{stem}` folders, stored in scrambled order."""
        entries = []
        for i, count in enumerate(issue_pages):
            folder = f'temp_extract_{i}_Series {i + 1:03d}'
            for p in range(1, count + 1):
                entries.append((f'{folder}/{p:03d}.jpg',
                                jpeg_bytes(page_colour(p, i + 1))))
        out = self.library / name
        # zip -r stored these in readdir order, which is arbitrary. Reversing
        # is a stand-in for arbitrary and proves the repair does not lean on it.
        with zipfile.ZipFile(out, 'w', zipfile.ZIP_STORED) as z:
            for n, data in reversed(entries):
                z.writestr(n, data)
        return out

    def test_a_makecbz_volume_is_recognised_and_its_order_judged(self):
        fine = self._makecbz_volume('small.cbz', [2] * 9)
        broken = self._makecbz_volume('big.cbz', [2] * 12)
        self.assertEqual(rp.misordered_report(fine), (9, 8))
        self.assertEqual(rp.misordered_report(broken), (12, 11))
        self.assertIsNone(rp.misordered_report(self._seven_zip('plain.cbr', 2)))

    def test_repair_puts_a_scrambled_volume_back_in_reading_order(self):
        """The whole point. Twelve issues that displayed 1, 11, 12, 2, 3 ...
        have to come back as 1, 2, 3 ... 12, rebuilt from inside the volume
        with no access to the original issue files."""
        volume = self._makecbz_volume('scrambled.cbz', [2] * 12)

        before = sorted(zipfile.ZipFile(volume).namelist())
        displayed = [n.split('_')[2].split('/')[0] for n in before]
        self.assertEqual(displayed[:6], ['0', '0', '10', '10', '11', '11'],
                         'the fixture does not reproduce the bug')

        with tempfile.TemporaryDirectory() as tmp:
            rp.do_repair(volume, convert=False, work=Path(tmp))

        with zipfile.ZipFile(self.library / 'scrambled.cbz') as z:
            names = sorted(z.namelist())
            pages = [z.read(n) for n in names]

        self.assertEqual([n.split('/')[0] for n in names],
                         [f'{i:04d}' for i in range(1, 13) for _ in range(2)])
        expected = [jpeg_bytes(page_colour(p, i))
                    for i in range(1, 13) for p in (1, 2)]
        self.assertEqual(pages, expected, 'still not in reading order')

    def test_repair_keeps_every_page(self):
        volume = self._makecbz_volume('count.cbz', [3, 5, 2, 7] + [1] * 8)
        before = gen.page_count(volume)
        self.assertEqual(before, 25)
        with tempfile.TemporaryDirectory() as tmp:
            rp.do_repair(volume, convert=False, work=Path(tmp))
        gen._PAGE_COUNTS.clear()
        self.assertEqual(gen.page_count(self.library / 'count.cbz'), 25)

    def test_repair_quarantines_the_volume_it_replaces(self):
        volume = self._makecbz_volume('kept.cbz', [2] * 11)
        before = volume.read_bytes()
        with tempfile.TemporaryDirectory() as tmp:
            rp.do_repair(volume, convert=False, work=Path(tmp))
        self.assertEqual((self.quarantine / 'kept.cbz').read_bytes(), before)

    def test_repair_keeps_the_comicinfo_and_drops_the_junk(self):
        """ComicInfo.xml is the metadata readers index on. Dropping it loses
        something the user had. Thumbs.db and .sfv are the packer's leftovers."""
        volume = self.library / 'meta.cbz'
        with zipfile.ZipFile(volume, 'w', zipfile.ZIP_STORED) as z:
            for i in range(11):
                folder = f'temp_extract_{i}_Series {i + 1:03d}'
                z.writestr(f'{folder}/001.jpg', jpeg_bytes(page_colour(1, i + 1)))
                z.writestr(f'{folder}/ComicInfo.xml',
                           f'<ComicInfo><Number>{i + 1}</Number></ComicInfo>')
                z.writestr(f'{folder}/Thumbs.db', b'\x00junk')
            z.writestr('ComicInfo.xml', '<ComicInfo><Series>Whole</Series></ComicInfo>')

        with tempfile.TemporaryDirectory() as tmp:
            rp.do_repair(volume, convert=False, work=Path(tmp))

        with zipfile.ZipFile(self.library / 'meta.cbz') as z:
            names = z.namelist()
            # each issue keeps its own metadata, under its new number
            self.assertIn('0001/ComicInfo.xml', names)
            self.assertIn('0011/ComicInfo.xml', names)
            self.assertIn('<Number>11</Number>', z.read('0011/ComicInfo.xml').decode())
            # the volume's own metadata stays at the root
            self.assertIn('ComicInfo.xml', names)
            self.assertIn('<Series>Whole</Series>', z.read('ComicInfo.xml').decode())
        self.assertFalse([n for n in names if 'Thumbs.db' in n], 'junk carried over')
        gen._PAGE_COUNTS.clear()
        self.assertEqual(gen.page_count(self.library / 'meta.cbz'), 11,
                         'metadata must not be counted as pages')

    def test_repair_never_re_encodes_the_comicinfo(self):
        """--convert-nonjpeg must not treat an .xml as a page to re-encode."""
        volume = self.library / 'conv.cbz'
        with zipfile.ZipFile(volume, 'w', zipfile.ZIP_STORED) as z:
            z.writestr('temp_extract_0_A/001.jpg', jpeg_bytes())
            z.writestr('temp_extract_0_A/ComicInfo.xml', '<ComicInfo/>')
        with tempfile.TemporaryDirectory() as tmp:
            rp.do_repair(volume, convert=True, work=Path(tmp))
        with zipfile.ZipFile(self.library / 'conv.cbz') as z:
            self.assertEqual(z.read('0001/ComicInfo.xml'), b'<ComicInfo/>')

    def test_repair_refuses_a_volume_it_does_not_understand(self):
        """A page outside the extraction folders means this is not the shape we
        think it is. Guessing where it belongs would be worse than refusing."""
        odd = self.library / 'odd.cbz'
        with zipfile.ZipFile(odd, 'w') as z:
            z.writestr('temp_extract_0_A/001.jpg', jpeg_bytes())
            z.writestr('loose page.jpg', jpeg_bytes())
        before = odd.read_bytes()
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(RuntimeError):
                rp.do_repair(odd, convert=False, work=Path(tmp))
        self.assertEqual(odd.read_bytes(), before)
        self.assertFalse(self.quarantine.exists())

    def test_temp_extract_index_reads_the_issue_number_back(self):
        self.assertEqual(rp.temp_extract_index('temp_extract_7_Some Comic 008'), 7)
        self.assertEqual(rp.temp_extract_index('temp_extract_0_A'), 0)
        self.assertEqual(rp.temp_extract_index('temp_extract_12_B_C_D'), 12)
        self.assertIsNone(rp.temp_extract_index('pages'))
        self.assertIsNone(rp.temp_extract_index('temp_extract_x_A'))

    # ------------------------------------------------ the dry run

    def test_without_execute_nothing_is_written(self):
        original = self._seven_zip('untouched.cbr', pages=3)
        before = sorted(p.name for p in self.library.rglob('*'))

        with mock.patch.object(rp.shutil, 'move') as moved, \
             mock.patch.object(rp, 'PHASE1', ['untouched.cbr']), \
             mock.patch.object(rp, 'HTML_JUNK', []), \
             mock.patch.object(sys, 'argv', ['repack_comics.py']):
            rc = rp.main()

        self.assertEqual(rc, 0)
        moved.assert_not_called()
        self.assertTrue(original.exists())
        self.assertEqual(sorted(p.name for p in self.library.rglob('*')), before)
        self.assertFalse(self.quarantine.exists())

    def test_an_html_error_page_is_recognised_by_its_bytes(self):
        p = self.library / 'looks like a comic.cbr'
        p.write_bytes(b'<html>\r\n<head><title>429 Too Many Requests</title></head>\r\n'
                      + b'<body>nginx</body></html>' + b'\0' * 4096)
        self.assertTrue(rp.looks_like_html(p))
        self.assertIsNone(rp.detect_format(p))

        rp.do_junk(p)
        self.assertFalse(p.exists())
        self.assertTrue((self.quarantine / 'looks like a comic.cbr').exists())

    def test_the_redownload_list_says_where_each_file_belongs(self):
        """A bare filename does not say which series folder the replacement
        goes in, and several of these sit two levels down."""
        folder = self.library / 'Murder Drones'
        folder.mkdir()
        p = folder / 'Murder Drones 05 (of 06).cbr'
        p.write_bytes(b'<html><title>429 Too Many Requests</title></html>')
        original = str(p)

        with mock.patch.object(rp, 'REDOWNLOAD', self.tmp / 'redl.md'):
            rp.write_redownload([{'kind': 'junk', 'path': original, 'status': 'ok',
                                  **rp.do_junk(p)}])
            text = (self.tmp / 'redl.md').read_text()

        self.assertIn(original, text, 'the path it belongs at is missing')
        self.assertIn(str(self.quarantine / 'Murder Drones'), text,
                      'the path it was moved to is missing')
        self.assertIn('- [ ]', text, 'it should be a checklist')

    def test_the_size_is_recorded_before_the_file_moves(self):
        """Reporting it afterwards would mean stat-ing a path that no longer
        holds the file."""
        p = self.library / 'big.cbr'
        p.write_bytes(b'<html>429</html>' + b'x' * 5000)
        out = rp.do_junk(p)
        self.assertEqual(out['size'], 5016)

    def test_a_real_comic_is_not_mistaken_for_an_error_page(self):
        self.assertFalse(rp.looks_like_html(self._seven_zip('real.cbr', pages=2)))

    # ------------------------------------------------ extraction safety

    def test_a_member_that_escapes_the_extraction_root_is_refused(self):
        """Python 3.11's tarfile has no `filter=`, so the guard is ours to get
        right. A comic has no reason to name a path outside itself."""
        nasty = self.tmp / 'nasty.cbz'
        with zipfile.ZipFile(nasty, 'w') as z:
            z.writestr('../../escaped.jpg', jpeg_bytes())
        with self.assertRaises(ValueError):
            rp.extract(nasty, self.tmp / 'out')
        self.assertFalse((self.tmp.parent / 'escaped.jpg').exists())


if __name__ == '__main__':
    unittest.main()
