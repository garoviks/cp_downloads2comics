#!/usr/bin/env python3
"""What format a file is gets decided at byte 0, not by whoever opens it first.

`zipfile.is_zipfile()` does not look at the start of the file. It scans
*backwards* from the end for an end-of-central-directory record, because a zip
is allowed to carry a prefix — a self-extracting stub, say. That makes it the
wrong question to ask first: any archive that happens to carry a `.zip` inside
it answers yes, and then gets read as that inner zip.

A real file in the library did exactly this. `Luis Royo - Subversive Beauty &
Portfolio.cbr` is a RAR holding 97 JPEGs and one nested zip. The counter asked
is_zipfile first, got yes, listed the inner zip's five members — a DOS utility,
`PICCHECK.exe` and friends — found no images among them, and reported a 97-page
art book as holding no pages. It was listed as damaged on that basis.

So the order matters, and these tests pin it: magic bytes first, is_zipfile only
as a last resort once no signature matched.

Run:  python3 -m unittest discover tests
"""
import io
import os
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import paths

gen = paths.load_generator()


def zip_bytes(names):
    """A valid zip archive, in memory."""
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, 'w') as z:
        for n in names:
            z.writestr(n, b'x')
    return buf.getvalue()


class TestFormatIsDecidedAtByteZero(unittest.TestCase):

    def setUp(self):
        self.dir = tempfile.TemporaryDirectory()
        self.tmp = Path(self.dir.name)
        self.addCleanup(self.dir.cleanup)
        gen._PAGE_COUNTS.clear()
        self.addCleanup(gen._PAGE_COUNTS.clear)

    def test_a_rar_carrying_a_zip_is_not_read_as_that_zip(self):
        """The Luis Royo shape. A RAR with a zip inside it must not be
        described by the inner zip's contents — that inner zip held a DOS
        utility, and believing it condemned 97 real pages."""
        path = self.tmp / 'royo.cbr'
        path.write_bytes(gen.RAR_MAGIC + b'\x00' * 64
                         + zip_bytes(['PICCHECK.exe', 'INI2REG.exe']))

        # is_zipfile is happy to read it, which is the whole trap.
        self.assertTrue(zipfile.is_zipfile(path))

        self.assertNotIn('PICCHECK.exe', gen.list_members(path) or [],
                         'read the nested zip instead of the RAR')

    def test_and_so_it_is_not_reported_as_holding_no_pages(self):
        """The consequence that mattered: `None` says we could not read it.
        `0` would accuse it of being empty, which is what happened."""
        path = self.tmp / 'royo.cbr'
        path.write_bytes(gen.RAR_MAGIC + b'\x00' * 64
                         + zip_bytes(['PICCHECK.exe']))
        self.assertIsNone(gen.page_count(path),
                          'claimed to know the page count of an unreadable RAR')

    def test_an_ordinary_zip_is_still_read(self):
        """The fix must not cost us the common case."""
        path = self.tmp / 'plain.cbz'
        path.write_bytes(zip_bytes(['001.jpg', '002.jpg', 'ComicInfo.xml']))
        self.assertEqual(gen.page_count(path), 2)

    def test_a_zip_behind_a_stub_is_still_found(self):
        """This is why is_zipfile exists, and why it is kept as a fallback:
        a zip may legitimately carry a prefix. With no signature at byte 0 to
        contradict it, scanning backwards is the right thing to do."""
        path = self.tmp / 'stub.cbz'
        path.write_bytes(b'MZ not any archive magic we know' + b'\x00' * 32
                         + zip_bytes(['001.jpg', '002.jpg', '003.jpg']))
        self.assertEqual(gen.page_count(path), 3)

    def test_a_truncated_zip_says_it_could_not_be_read(self):
        """Starts like a zip, has no central directory left. Not the same as
        being empty, and must not be rounded to zero."""
        path = self.tmp / 'cut.cbz'
        path.write_bytes(zip_bytes(['001.jpg', '002.jpg'])[:40])
        self.assertIsNone(gen.page_count(path))

    def test_a_file_of_no_known_format_holds_nothing_and_says_so(self):
        """Zero, not None: we looked, and there is provably nothing to find."""
        path = self.tmp / 'junk.cbr'
        path.write_bytes(os.urandom(4096))
        self.assertEqual(gen.page_count(path), 0)


if __name__ == '__main__':
    unittest.main()
