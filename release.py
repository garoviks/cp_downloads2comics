#!/usr/bin/env python3
"""Parse a comic filename once, into a record.

LIVE. `matching_analysis_generator.py` derives every series name through this.
It began as `prototype/parse_release.py` and was promoted only after being
measured against the real library — COMIC_TOOLS_ARCHITECTURE.md §10.3: 92 real
releases, 56 matched against the old code's 55, and **zero** files that the old
code placed became homeless.

`comic_volume_creator` does NOT use this yet — that is migration step 6. Until
then the two apps still derive series names differently, which is the drift
recorded in §7.

─────────────────────────────────────────────────────────────────────────────
Why this exists
─────────────────────────────────────────────────────────────────────────────
Both apps today derive a series name by SUBTRACTION: take the filename and
`.sub('')` away anything resembling packaging, then hope the residue is a title.
Subtraction has no model of what the name IS, only of what survived, so it
leaves debris and destroys real words:

    Star Trek - Red Shirts - Ghost of the 21st Century
        -> 'Star Trek - Red Shirts - Ghost of the'
        ISSUE_PATTERN (:46) is r'\\s+#?\\d{1,3}(?!\\d)...' and matches ' 21'
        inside '21st' — 't' is not a digit, so the negative lookahead passes.

    The Wicked + The Divine - Book 02   -> 'The Wicked + The Divine -'   (dangling dash)
    Giant Days                          -> 'Days'                        (real title word)
    Signal to Noise                     -> 'Sial to Noise'               (fixed in Phase 1)

─────────────────────────────────────────────────────────────────────────────
The two ideas
─────────────────────────────────────────────────────────────────────────────
1. A SERIES IS A PREFIX. Release filenames put the title first and the metadata
   after it. So find where the metadata starts and keep everything to its left,
   instead of carving pieces out of the middle. Nothing mid-string is ever
   deleted, which removes the whole truncation class of bug.

2. AMBIGUITY IS RESOLVED BY THE LIBRARY, NOT THE FILENAME. 'Revolution 9 006'
   and 'Cruel Kingdom 2 001' are structurally identical, yet you want
   'Revolution 9' from one and 'Cruel Kingdom' from the other. No filename rule
   can tell them apart, because the difference is not in the filename — it is in
   which folder exists. So this returns ORDERED CANDIDATES and lets the matcher
   pick the one the library actually has. That is why no hand-maintained
   "protected titles" list is needed here.

Tokenising rather than boundary-matching also sidesteps the bug Phase 1 fixed:
there are no \\b semantics to get wrong, because words are split once and then
compared as words.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field

COMIC_EXTS = {'.cbz', '.cbr', '.zip', '.rar'}

# Packaging words, consumed ONLY as a trailing suffix. Because they are never
# removed from the middle or the start, 'Giant Days', 'The Complete Peanuts' and
# 'Special Forces' survive intact with no exception list.
PACKAGING = {
    'tpb', 'omnibus', 'collection', 'collected', 'gn', 'ogn', 'hc', 'sc',
    'graphic', 'novel', 'scanlation', 'complete', 'digital', 'webrip',
}
# The subset of PACKAGING that means "this file IS a collected edition", as
# opposed to packaging that only describes where the file came from. A digital
# scan of issue 5 is still issue 5, so 'digital'/'webrip'/'scanlation' are
# deliberately absent: they are trimmed from the title but must not set `kind`.
COLLECTION_WORDS = {
    'tpb', 'omnibus', 'collection', 'collected', 'gn', 'ogn', 'hc', 'sc',
    'graphic', 'novel', 'complete',
}
# Words that make the file an issue of a parent series rather than its own thing.
KIND_WORDS = {'annual': 'annual', 'special': 'special', 'giant': 'special',
              'yearbook': 'annual', 'oneshot': 'one-shot'}
# 'Season 3', 'Series 2', 'Part 4' — a run marker, not part of the title.
RUN_WORDS = {'season', 'series', 'part', 'cycle', 'saga'}
VOL_WORDS = {'v', 'vol', 'volume', 'book', 't'}
# 'Book' / 'Season' only mark a volume when a NUMBER follows. Without this,
# 'Comic Book History of Animation' cuts at 'Book' and becomes 'Comic'.
# Spelled-out numbers count: 'High Strangeness Book Five' must still cut.
NUMBER_WORDS = {
    'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7,
    'eight': 8, 'nine': 9, 'ten': 10, 'eleven': 11, 'twelve': 12,
    'thirteen': 13, 'fourteen': 14, 'fifteen': 15, 'sixteen': 16,
    'seventeen': 17, 'eighteen': 18, 'nineteen': 19, 'twenty': 20,
}

_YEAR = re.compile(r'^(19|20)\d{2}$')
_VOL_ATTACHED = re.compile(r'^(v|vol|volume|book|t)\.?\s*(\d+(?:\.\d+)?)$', re.I)
_NUM = re.compile(r'^#?(\d+(?:\.\d+)?)$')
_RANGE = re.compile(r'^#?(\d+)\s*[-–]\s*(\d+)$')


@dataclass(frozen=True)
class Release:
    """What a comic filename means. Fields, not leftovers."""
    series_candidates: tuple[str, ...]   # most specific first; never empty
    volume: float | None = None
    issue: str | None = None             # str: keeps '015' padding and '1.5'
    issue_range: tuple[int, int] | None = None
    year: int | None = None
    kind: str = 'issue'                  # issue|volume|special|annual|one-shot|unknown
    tags: tuple[str, ...] = ()
    original: str = ''
    subtitle: str | None = None
    trace: tuple[str, ...] = field(default=(), compare=False)

    @property
    def series(self) -> str:
        """The single best guess, when the caller cannot consult the library."""
        return self.series_candidates[0]


def _strip_ext(name: str) -> str:
    low = name.lower()
    for ext in COMIC_EXTS:
        if low.endswith(ext):
            return name[:-len(ext)]
    return name


def _split_tags(text: str) -> tuple[str, list[str]]:
    """Pull out every (...) and [...] group. Series names never live in brackets."""
    tags: list[str] = []

    def take(m: re.Match) -> str:
        inner = m.group(1).strip()
        if inner:
            tags.append(inner)
        return ' '
    text = re.sub(r'\(([^()]*)\)', take, text)
    text = re.sub(r'\[([^\[\]]*)\]', take, text)
    return text, tags


def _tokenise(text: str) -> list[str]:
    """Split on separators, keeping words. '_' and '.' are separators here,
    which is exactly what \\b gets wrong on release filenames."""
    text = re.sub(r'[_]+', ' ', text)
    # Split 'Vol.05' -> 'Vol. 05', but ONLY before a digit. Splitting on every
    # '.' shreds acronyms: 'T.H.U.N.D.E.R. Agents', 'M.A.S.K.', 'Ghosted in L.A.'
    # Not between digits either, or 'v01.5' loses its decimal.
    text = re.sub(r'(?<!\d)\.(?=\d)', '. ', text)
    return [t for t in re.split(r'\s+', text.strip()) if t]


def _classify(tok: str) -> str:
    """What kind of token is this, on its own?"""
    bare = tok.strip('.,#').lower()
    if _VOL_ATTACHED.match(tok.strip('.,')):
        return 'vol'                                 # v01, Vol.5, T01, Book02
    if bare in VOL_WORDS:
        return 'volword'                             # 'Vol' with the number split off
    if bare in RUN_WORDS:
        return 'runword'
    if bare in KIND_WORDS:
        return 'kindword'
    if bare in PACKAGING:
        return 'packaging'
    if _RANGE.match(tok):
        return 'range'
    if _YEAR.match(tok.strip('.,()')):
        return 'year'
    if _NUM.match(tok):
        return 'num'
    return 'word'


def _numeric(tok: str | None) -> float | None:
    """Value of a token that stands for a number, digits or spelled out."""
    if tok is None:
        return None
    m = _NUM.match(tok)
    if m:
        return float(m.group(1))
    return NUMBER_WORDS.get(tok.strip('.,').lower())


def _is_strong(tok: str) -> bool:
    """A number that is unambiguously an issue number rather than part of a title.

    '006' and '01-04' are issue numbers. A bare '2' or '9' might be either
    ('Revolution 9', 'Megaghost 2'), so it is weak and only used as a fallback.
    """
    if _RANGE.match(tok):
        return True
    m = _NUM.match(tok)
    if not m:
        return False
    digits = m.group(1).split('.')[0]
    return len(digits) >= 3 or (len(digits) > 1 and digits[0] == '0') or tok.startswith('#')


def parse_release(filename: str) -> Release:
    original = filename
    text = _strip_ext(filename)
    text, tags = _split_tags(text)

    year = None
    for t in tags:                                   # year lives in a tag: '(2016)'
        m = re.search(r'\b((?:19|20)\d{2})\b', t)
        if m:
            year = int(m.group(1))
            break

    tokens = _tokenise(text)
    kinds = [_classify(t) for t in tokens]
    trace: list[str] = []

    # ---- locate where the metadata starts (never index 0: a title cannot be empty)
    cut = None
    for i in range(1, len(tokens)):
        k = kinds[i]
        nxt = tokens[i + 1] if i + 1 < len(tokens) else None
        if k in ('volword', 'runword') and _numeric(nxt) is None:
            continue          # 'Book'/'Season' with no number is an ordinary word
        if k in ('vol', 'volword', 'runword', 'kindword'):
            cut = i
            trace.append(f'cut at {tokens[i]!r} ({k})')
            break
        if k in ('num', 'range') and _is_strong(tokens[i]):
            cut = i
            trace.append(f'cut at {tokens[i]!r} (strong number)')
            break
    if cut is None:                                  # fall back to a weak number
        for i in range(1, len(tokens)):
            if kinds[i] in ('num', 'range'):
                cut = i
                trace.append(f'cut at {tokens[i]!r} (weak number)')
                break

    head = tokens[:cut] if cut is not None else list(tokens)
    tail = tokens[cut:] if cut is not None else []

    # ---- read the metadata off the tail
    volume = issue = None
    issue_range = None
    kind = 'issue'
    j = 0
    while j < len(tail):
        tok, k = tail[j], _classify(tail[j])
        if k == 'vol':
            m = _VOL_ATTACHED.match(tok.strip('.,'))
            volume = float(m.group(2))
            kind = 'volume'
        elif k == 'volword' and _numeric(tail[j + 1] if j + 1 < len(tail) else None) is not None:
            volume = _numeric(tail[j + 1])
            kind = 'volume'
            j += 1
        elif k == 'runword' and _numeric(tail[j + 1] if j + 1 < len(tail) else None) is not None:
            j += 1                                   # 'Season 3' — absorbed, not a volume
        elif k == 'kindword':
            kind = KIND_WORDS[tok.strip('.,#').lower()]
        elif k == 'range':
            m = _RANGE.match(tok)
            issue_range = (int(m.group(1)), int(m.group(2)))
        elif k == 'num' and issue is None:
            issue = _NUM.match(tok).group(1)
        elif k == 'year' and year is None:
            year = int(tok.strip('.,()'))
        elif k == 'word':
            break                                    # subtitle starts here
        j += 1

    rest = tail[j:]
    subtitle = ' '.join(rest).lstrip('-–— ').strip() or None

    # ---- trim trailing packaging from the head ('Bone Parish Complete Collection')
    trimmed = False
    while head and _classify(head[-1]) in ('packaging', 'kindword'):
        last = head[-1].strip('.,#').lower()
        if last in KIND_WORDS:
            kind = KIND_WORDS[last]
        elif last in COLLECTION_WORDS and kind == 'issue':
            # 'Y - The Last Man Omnibus' is a collected edition even though no
            # volume number follows. Guarded on kind=='issue' so a 'special' or
            # 'annual' already read off the tail is not overwritten.
            kind = 'volume'
        trace.append(f'trailing {head[-1]!r} removed')
        head.pop()
        trimmed = True
    # An article the trim left hanging is debris, not a title:
    # 'Invincible Iron Man by Gerry Duggan - The Complete Collection'
    #     -> '...Gerry Duggan - The'   without this
    # Guarded on `trimmed`, so a title that genuinely ends in an article keeps it.
    while trimmed and head and head[-1].strip('.,').lower() in {'the', 'a', 'an'}:
        trace.append(f'dangling article {head[-1]!r} removed')
        head.pop()
    while head and head[-1] in {'-', '–', '—', '+', ','}:
        head.pop()                                   # the dangling-dash debris

    if not head:                                     # never return nothing
        head = tokens[:1] or [_strip_ext(original)]

    # ---- candidates, most specific first
    primary = ' '.join(head).strip(' -–—,')
    cands = [primary]
    if len(head) > 1 and _classify(head[-1]) in ('num', 'range'):
        shorter = ' '.join(head[:-1]).strip(' -–—,')
        if shorter:
            cands.append(shorter)                    # 'Revolution 9' | 'Revolution'
    if ' - ' in primary:                             # arc/spin-off, see Q2
        cands.append(primary.split(' - ')[0].strip())

    seen, ordered = set(), []
    for c in cands:
        if c and c.lower() not in seen:
            seen.add(c.lower())
            ordered.append(c)

    return Release(
        series_candidates=tuple(ordered), volume=volume, issue=issue,
        issue_range=issue_range, year=year, kind=kind, tags=tuple(tags),
        original=original, subtitle=subtitle, trace=tuple(trace),
    )


def resolve(filename: str, library_keys) -> tuple[str, bool]:
    """Pick the candidate the library actually has. This is idea 2 in practice.

    library_keys: a set of already-normalised folder keys.
    Returns (chosen_series, matched_library).
    """
    r = parse_release(filename)
    for cand in r.series_candidates:
        if normalize(cand) in library_keys:
            return cand, True
    return r.series, False


def normalize(name: str) -> str:
    """Matching key. Deliberately does NOT strip leading articles — see compare.py."""
    return ' '.join(re.findall(r'[a-z0-9]+', name.lower()))


if __name__ == '__main__':
    for s in ['Giant Days Vol. 05 (2017) (digital) (Son of Ultron-Empire).cbr',
              'Star Trek - Red Shirts - Ghost of the 21st Century (2013).cbz',
              'The Wicked + The Divine - Book 02 (2015).cbz',
              'Revolution 9 006 (2018).cbz',
              'Cruel Kingdom 2 001 (2024).cbz',
              'Heartthrob Season 3 001 (2019).cbz',
              'Feral v04 - Pet City (2026) (Digital).cbr',
              'Misty Special (1980).cbz',
              'Bone Parish Complete Collection (2020).cbz',
              'Signal to Noise (2007).cbz',
              'Dead Irons v01_(2009).cbr',
              'Camp Midnight v01 OGN (2016).cbz']:
        r = parse_release(s)
        print(f'{s[:52]:54} {r.series_candidates}  vol={r.volume} '
              f'issue={r.issue} year={r.year} kind={r.kind}')
