#!/usr/bin/env python3
"""Deciding whether two comic files are the same book.

Two files are candidates for the same book when release.parse_release() makes the
same series, volume, issue and kind of them. That grouping is cheap and it is also
far too generous to act on, because the parser discards information: two files land
on one key precisely when the thing that told them apart is the thing it dropped.

    Harley Quinn v02 - Keepsake      -> (harley quinn, vol 2, issue None)
    Harley Quinn v02 - Power Outage  -> (harley quinn, vol 2, issue None)

subtitles go outright, and

    Starhenge Book Two - a Kiss for Atticus 03   -> (starhenge, vol 2, issue None)
    Starhenge Book Two - A Kiss For Atticus 01   -> (starhenge, vol 2, issue None)

a 'Book N' marker sets kind='volume' and takes the issue number with it.

So a shared key opens the question and looks_like_one_book() answers it, by reading
back the evidence the parser threw away. Every rule below was written for a case
found in the real library, and the asymmetry is deliberate throughout: a true
duplicate wrongly rejected costs a minute of reading, a false duplicate accepted
costs a book.

Both callers share this module rather than each carrying its own copy —
library_duplicates.py reports on the library, matching_analysis_generator.py warns
about an incoming download. Two implementations of one rule is how the Organiser
and the Builder drifted apart in the first place.
"""
import re
from pathlib import Path

import release

COMIC_EXTS = {'.cbz', '.cbr'}

# Parenthesised text is where the year and the packer's tags live ('(2026)',
# '(Digital Rip)', '(Son of Ultron-Empire)'). Those differ between two rips of
# one book, which is exactly what a duplicate check is looking for, so they are cut.
_PARENS = re.compile(r'\([^)]*\)')
_WORD = re.compile(r'[a-z0-9]+')

# 'v01' is one token, not 'v' then '01', so stripping format words and leading
# zeros separately never makes it agree with 'Vol 1' or 'Book 1'. Split the
# marker off the number and only the number survives, which is the whole point.
_GLUED = re.compile(r'^([a-z]+)(\d+)$')

# Words that describe the packaging rather than the book. 'Omnibus v01' and
# 'Vol 1' of the same collection are the same reading material, so these must not
# be what keeps two files apart. Subtitles are deliberately NOT in this set: they
# are the only thing distinguishing 'Harley Quinn v02 - Keepsake' from
# 'Harley Quinn v02 - Power Outage', which are different books that happen to
# share a volume number.
_FORMAT_WORDS = {
    'v', 'vol', 'volume', 'book', 't', 'omnibus', 'tpb', 'hc', 'gn',
    'c2c', 'hybrid', 'digital', 'webrip', 'scanlation', 'the', 'a', 'an',
}

# These words live inside the parentheses that get cut, so without a separate
# check a 1 MB 'New Avengers 001 (Cover ONLY)' is indistinguishable from the
# 42 MB issue it was scanned from. They mark a partial or alternate scan, never
# the book itself.
_VARIANT = re.compile(r'\b(variants?|covers?\s+only|printing)\b', re.I)

# A folder can carry the volume number that the filenames inside it leave out,
# which is the only thing separating 'Terra Obscura Volume 1/#003' from
# 'Terra Obscura Volume 2/#003'.
_FOLDER_VOL = re.compile(r'\b(?:v|vol|volume|book)\.?\s*(\d{1,3})\b', re.I)


def book_key(filename: str, series_key: str) -> tuple:
    """The parse that opens the question. Series arrives already normalised.

    The caller supplies the normalised series rather than this module reaching for
    a normaliser, so that the report and the generator can each key on the same
    series vocabulary they use everywhere else.
    """
    r = release.parse_release(Path(filename).name)
    # '001' and '01' are one issue. Packers pad differently, and the two
    # 'Bonerest - A World's End' folders in Downloads differed in nothing else,
    # so the unpadded form is what two copies are grouped on.
    issue = re.sub(r'^0+(?=\d)', '', r.issue) if r.issue else r.issue
    return (series_key, r.volume, issue, r.issue_range, r.kind)


def title_signature(filename: str) -> frozenset:
    """What is left of a filename once packaging is removed: the book itself.

    Format words go so a re-release under a different label still matches, and a
    marker glued to its number ('v01') is split so only the number survives.
    Everything else — including every word of a subtitle — is kept, because the
    parser has already discarded the subtitle by this point and it is the only
    remaining evidence that two files carrying the same series and volume number
    are not the same book.
    """
    bare = _PARENS.sub(' ', Path(filename).stem).lower()
    words = set()
    for w in _WORD.findall(bare):
        if w in _FORMAT_WORDS:
            continue
        if w.isdigit():
            words.add(str(int(w)))
            continue
        glued = _GLUED.match(w)
        if glued and glued.group(1) in _FORMAT_WORDS:
            words.add(str(int(glued.group(2))))
        else:
            words.add(w)
    return frozenset(words)


def folder_volumes(rel_path) -> frozenset:
    """Volume numbers the folders above a file claim for it.

    Takes a path relative to whichever root it was found under, so a download and
    a library file can be compared without a root they do not share.

    A folder naming more than one volume is a shelf holding a range — 'Shakara
    (v01-v02)' contains both books and so identifies neither. Only a folder that
    names exactly one volume is read as a statement about the file inside it.
    """
    out = set()
    for part in Path(rel_path).parent.parts:
        found = {int(m) for m in _FOLDER_VOL.findall(part)}
        if len(found) == 1:
            out |= found
    return frozenset(out)


def looks_like_one_book(rel_paths) -> bool:
    """Whether every path given is plausibly the same book. Paths are relative.

    Three ways they can be shown not to be, all of them evidence the parser threw
    away: the filenames disagree once packaging is stripped, one is a variant or
    cover-only scan and another is not, or their folders claim different volumes.
    An absent volume folder is silence rather than disagreement, so it is dropped
    before comparing — otherwise 'v1 (1999)/The Authority v1 #10' and a copy filed
    without that folder would read as two different books.
    """
    paths = [Path(p) for p in rel_paths]
    if len({title_signature(p.name) for p in paths}) > 1:
        return False
    if len({bool(_VARIANT.search(p.name)) for p in paths}) > 1:
        return False
    claimed = {folder_volumes(p) for p in paths}
    claimed.discard(frozenset())
    return len(claimed) <= 1
