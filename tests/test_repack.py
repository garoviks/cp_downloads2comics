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
        self.patches = [
            mock.patch.object(rp, 'LIBRARY', self.library),
            mock.patch.object(rp, 'QUARANTINE', self.quarantine),
            mock.patch.object(rp, 'STAGING', self.staging),
            mock.patch.object(rp, 'TEMP_ROOT', self.tmp),
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
