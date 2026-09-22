#!/usr/bin/env python3
"""A block of NUL bytes is a valid empty tar, and must not be called a container.

A tar archive legitimately *ends* in two 512-byte blocks of NUL, so a file that
is nothing but NULs satisfies every structural test `tarfile.is_tarfile()`
makes. Sixteen NUL-headed damaged comics were classified `tar` on that basis and
printed into LIBRARY_REPACK_CANDIDATES.md under "repack as zip" — work that
would have produced sixteen empty .cbz files wearing full issue names.

This is the fourth time in this codebase that a stdlib detector was believed
without asking it for contents: `zipfile.is_zipfile` scans backwards from EOF
and mislabels archives holding a nested .zip; `unrar` as the sole RAR reader
reported files unreadable that `7z` opens; and a lister's page count after the
damage point was read as the book's page count. The shared lesson is that a
format test answers "could this be parsed as X", not "is this an X".

Run:  python3 -m unittest discover tests
"""
import os
import sys
import tarfile
import tempfile
import unittest
import zipfile
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import paths

sw = paths.load_sweep()


class TarDetection(unittest.TestCase):

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.dir = Path(self.tmp.name)
        self.addCleanup(self.tmp.cleanup)

    def test_a_file_of_nulls_is_not_a_tar_container(self):
        """The exact shape of the sixteen. is_tarfile() says yes; it is not one."""
        path = self.dir / 'nulled.cbr'
        path.write_bytes(b'\0' * (512 * 20))
        self.assertTrue(tarfile.is_tarfile(path),
                        'premise gone: the stdlib no longer accepts this')
        self.assertFalse(sw.tar_has_members(path))
        self.assertIsNone(sw.detect_container(path))

    def test_a_real_tar_is_still_detected(self):
        """The false positive must not be closed by refusing tar altogether."""
        page = self.dir / '001.jpg'
        page.write_bytes(b'\xff\xd8\xff\xe0' + b'x' * 100)
        path = self.dir / 'real.cbr'
        with tarfile.open(path, 'w') as tar:
            tar.add(page, arcname='001.jpg')
        self.assertTrue(sw.tar_has_members(path))
        self.assertEqual(sw.detect_container(path), 'tar')

    def test_a_folder_named_like_an_archive_is_not_a_nested_archive(self):
        """Eight of the sixteen nested-archive candidates were folders.

        A member's name is not its type. Comic archives routinely hold a folder
        named after the release — `Herogasm 06 (of 06) (2009).cbz/` — and a
        suffix test alone books the file as carrying a nested archive and as
        needing work.
        """
        path = self.dir / 'foldered.cbz'
        with zipfile.ZipFile(path, 'w') as z:
            z.writestr('Herogasm 06 (of 06) (2009).cbz/', b'')
            z.writestr('Herogasm 06 (of 06) (2009).cbz/001.jpg', b'\xff\xd8x')
        names = [n for n in sw.gen.list_members(path)
                 if Path(n).suffix.lower() in sw.NESTED_EXTS]
        self.assertTrue(names, 'premise gone: the folder no longer looks nested')
        self.assertEqual(sw.drop_directories(path, names), [])
        self.assertEqual(sw.inspect(path)['nested'], [])

    def test_a_real_nested_archive_survives_the_filter(self):
        """The over-correction to avoid: dropping everything that looks nested."""
        inner = self.dir / 'inner.cbz'
        with zipfile.ZipFile(inner, 'w') as z:
            z.writestr('001.jpg', b'\xff\xd8x')
        path = self.dir / 'wrapper.cbz'
        with zipfile.ZipFile(path, 'w') as z:
            z.writestr('Issue 01.cbz', inner.read_bytes())
        self.assertEqual(sw.drop_directories(path, ['Issue 01.cbz']),
                         ['Issue 01.cbz'])
        self.assertEqual(sw.inspect(path)['nested'], ['Issue 01.cbz'])

    def test_a_non_tar_does_not_raise(self):
        """tarfile.open() raises ReadError, which is not an OSError subclass in
        every case — detect_container's `except OSError` would not have caught
        it, so the helper has to swallow TarError itself."""
        path = self.dir / 'junk.cbr'
        path.write_bytes(os.urandom(4096))
        self.assertFalse(sw.tar_has_members(path))


if __name__ == '__main__':
    unittest.main()
