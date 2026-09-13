#!/usr/bin/env python3
"""
Comic File Organizer — Matching Analysis Generator

Reads source and destination directories, extracts series names,
performs exact matching, and generates consolidation strategies.

Output: matching_analysis_consolidated.csv

Usage:
    python3 matching_analysis_generator.py [--src SOURCE_DIR] [--dest DEST_DIR]
"""

import csv
import re
import sys
import argparse
from pathlib import Path
from collections import defaultdict, Counter
from typing import Dict, List, Tuple, Optional

import release

# ═══════════════════════════════════════════════════════════════════════════
# REGEX PATTERNS
# ═══════════════════════════════════════════════════════════════════════════

COMIC_EXTS = {'.cbz', '.cbr'}    # unified with release.py and the Builder (step 7)

# Anchors are (?<![A-Za-z0-9]) / (?![A-Za-z0-9]) rather than \b, because \b counts
# '_' as a word character and release filenames are full of underscores
# (e.g. 'Nancy_In_Hell_Complete_Minutemen' — \b would refuse to strip 'Complete').
#
# NOTE: \b binds only to the FIRST alternative. The previous single-\b form left
# every later keyword unanchored, so 'GN'/'HC' matched mid-word:
# 'Signal' -> 'Sial', 'Bytchcraft' -> 'Bytcraft', 'Ashcan' -> 'Asan'.
# Every alternative must carry its own anchors.
#
# comic_volume_creator_server.py has its own copy of this pattern with a shorter
# keyword list. The drift is known and deliberately not resolved here — whether
# these should be shared at all is an architecture question, not a bug fix.
_NB, _NA = r'(?<![A-Za-z0-9])', r'(?![A-Za-z0-9])'
_VOL_NUM = rf'{_NB}(?:v|vol|book|t)\.?\s*\d+{_NA}'
_VOL_WORDS = (r'(?:TPB|Omnibus|Collection|Graphic\s*Novel|GN|HC|Scanlation'
              r'|Complete|Annual|Special|Giant)')
VOLUME_PATTERN = re.compile(rf'{_VOL_NUM}|{_NB}{_VOL_WORDS}{_NA}', re.IGNORECASE)

ISSUE_PATTERN = re.compile(
    r'\s+#?\d{1,3}(?!\d)(?:\s*\(of\s*\d+\))?|\s+\(\d{1,3}\)'
)

NO_RENAME_KEYWORDS = {"annual", "special", "giant", "one-shot"}

YEAR_PATTERN = re.compile(r'\((\d{4})[^)]*\)')

# ═══════════════════════════════════════════════════════════════════════════
# CONFIG
# ═══════════════════════════════════════════════════════════════════════════

SRC_DIR = Path("/home/nesha/Downloads/comics_download/")
DEST_DIR = Path("/mnt/extramedia/Comics")
OUTPUT_FILE = SRC_DIR / "matching_analysis_consolidated.csv"  # Save CSV to left folder

# Files to skip in source directory (loose files only, not folders)
SKIP_PATTERNS = {
    "comics_download.txt",
    "sha 01",  # More specific: loose "Sha 01" files (not folders)
    "the bank",  # Loose "The Bank" files (not folders)
    "the owl",  # Loose "The Owl" files (not folders)
}

# Known folder names for exact matching (rule 1 priority)
SPECIFIC_SERIES_FOLDERS = {
    "Billy & Buddy",
    "Gomer Goof",
}

# ═══════════════════════════════════════════════════════════════════════════
# FILENAME PARSING
# ═══════════════════════════════════════════════════════════════════════════

# REMOVED: parse_filename(). It derived a series name by SUBTRACTION — cut at the
# year, then .sub('') away every parenthetical, then VOLUME_PATTERN, then split at
# ISSUE_PATTERN and keep the residue. Its 'subtitle' and 'year' outputs were read
# by nothing; extract_series_name() was the only caller and used only 'series'.
#
# Subtraction has no model of what a name IS, only of what survived, so it left
# debris and cut real titles in half:
#
#   'Star Trek - Red Shirts - Ghost of the 21st Century'
#       -> 'Star Trek - Red Shirts - Ghost of the'   (ISSUE_PATTERN matched ' 21'
#                                                     inside '21st')
#   'The Wicked + The Divine - Book 02'  -> 'The Wicked + The Divine -'
#   'Giant Days Vol. 05'                 -> 'Days'
#
# release.parse_release() replaces it by finding where the metadata STARTS and
# keeping the prefix, so nothing is ever removed from the middle. Measured against
# the real library before the switch — COMIC_TOOLS_ARCHITECTURE.md 10.3. This is
# migration step 5.


def extract_series_name(filename: str) -> str:
    """The single best guess at the series name.

    Prefer extract_series_candidates() at any call site that can consult the
    destination index. 'Revolution 9 006' and 'Cruel Kingdom 2 001' are
    structurally identical filenames, and only the library can say which trailing
    numeral belongs to the title — so a lone guess is guaranteed wrong for one of
    them, whichever way it guesses.
    """
    return release.parse_release(filename).series


def extract_series_candidates(filename: str) -> Tuple[str, ...]:
    """Every series this filename could name, most specific first. Never empty."""
    return release.parse_release(filename).series_candidates


def get_canonical_series_for_folder(folder_path: Path) -> Optional[str]:
    """Return most common series name among existing comic files in folder_path."""
    if not folder_path.exists() or not folder_path.is_dir():
        return None
    counts: Dict[str, int] = {}
    for f in folder_path.iterdir():
        if f.is_file() and f.suffix.lower() in {'.cbz', '.cbr'}:
            s = extract_series_name(f.name)
            if s:
                counts[s] = counts.get(s, 0) + 1
    return max(counts, key=counts.get) if counts else None


def propose_filename(src_filename: str, canonical_series: str) -> str:
    """Replace series prefix in src_filename with canonical_series.
    Returns src_filename unchanged if series already matches or issue can't be located."""
    if not canonical_series:
        return src_filename
    if any(kw in src_filename.lower() for kw in NO_RENAME_KEYWORDS):
        return src_filename
    src_series = extract_series_name(src_filename)
    if not src_series or src_series == canonical_series:
        return src_filename
    if ' - ' in src_series:
        return src_filename  # Arc/subtitle files keep their original name
    if normalize_name(canonical_series) != normalize_name(src_series):
        return src_filename  # Canonical is a different series — skip rename

    ext = Path(src_filename).suffix
    name_no_ext = src_filename[:-len(ext)] if ext else src_filename

    # Strip year and suffix — keep them to reattach later
    year_match = YEAR_PATTERN.search(name_no_ext)
    name_for_issue = name_no_ext[:year_match.start()].strip() if year_match else name_no_ext
    year_suffix = (' ' + name_no_ext[year_match.start():].strip()) if year_match else ''

    # Strip all parenthetical blocks — series/issue names are never inside parens
    name_for_issue = re.sub(r'\s*\([^)]*\)', '', name_for_issue).strip()

    # Remove volume patterns, then locate issue number in the pre-year portion
    name_clean = VOLUME_PATTERN.sub('', name_for_issue).strip()
    issue_match = ISSUE_PATTERN.search(name_clean)
    if not issue_match:
        return src_filename  # Can't safely determine where series ends

    tail = name_clean[issue_match.start():]  # e.g. " 004" or " 04 (of 05)"
    return canonical_series + tail + year_suffix + ext


# ═══════════════════════════════════════════════════════════════════════════
# FOLDER-BASED CONSOLIDATION (NEW)
# ═══════════════════════════════════════════════════════════════════════════

def normalize_name(name: str) -> str:
    """
    Normalize name for lenient matching:
    - Remove articles (The, A, An)
    - Remove volume indicators (v01, vol, 001-002, etc.)
    - Remove years and parenthetical info
    - Lowercase for comparison

    Examples:
      "The Owl 001-002 (1967-1968)" → "owl"
      "The Bank 01-02 (2025)" → "bank"
      "Sha 01-03" → "sha"
    """
    normalized = re.sub(r'\bthe\b\s*', '', name, flags=re.IGNORECASE)   # strip "the" anywhere
    normalized = re.sub(r'^\b(a|an)\s+', '', normalized, flags=re.IGNORECASE)  # a/an at start only

    # Remove volume patterns (v01, vol, book, 001-002, etc.)
    normalized = VOLUME_PATTERN.sub('', normalized)

    # Remove years and parenthetical info
    normalized = re.sub(r'\s*\([^)]*\)\s*', ' ', normalized)

    # Remove issue numbers
    normalized = ISSUE_PATTERN.sub('', normalized)

    # Clean up spaces, normalize dashes, lowercase
    normalized = re.sub(r'\s+', ' ', normalized).strip().lower()
    normalized = re.sub(r'\s*-\s*', ' ', normalized).strip()

    return normalized


def extract_folder_series_name(folder_name: str) -> str:
    """
    Extract series name from folder name.

    Examples:
      "Sha 01-03" → "Sha"
      "The Owl 001-002 (1967-1968)" → "The Owl"
      "The Bank 01-02 (2025)" → "The Bank"
    """
    # Remove volume patterns
    cleaned = VOLUME_PATTERN.sub('', folder_name).strip()

    # Remove years and parenthetical info
    cleaned = re.sub(r'\s*\([^)]*\)\s*', ' ', cleaned).strip()

    # Remove trailing issue numbers
    cleaned = re.sub(r'\s+\d+(?:-\d+)?$', '', cleaned).strip()

    # Strip website/domain tags (e.g. "GetComics.INFO", "www.example.com")
    cleaned = re.sub(r'\s+\w[\w.-]*\.\w{2,4}$', '', cleaned).strip()

    # Clean up spaces
    cleaned = re.sub(r'\s+', ' ', cleaned).strip()

    return cleaned


def find_matching_right_folders() -> Dict[str, str]:
    """
    Get all folders from right side, normalized for matching.
    Returns: {normalized_name: actual_folder_name}

    Example: {"owl": "Owl/", "bank": "Bank/", "the owl": "The Owl/"}
    """
    folder_map = {}

    if not DEST_DIR.exists():
        return folder_map

    for item in DEST_DIR.iterdir():
        if item.is_dir():
            folder_name = item.name
            normalized = normalize_name(folder_name)
            if normalized:
                folder_map[normalized] = folder_name

    return folder_map


def find_folder_match(folder_series: str, right_folders: Dict[str, str]) -> Tuple[Optional[str], str]:
    """
    Find matching folder on right side with STRICT matching (EXACT ONLY).

    Matching priority:
    1. Exact match (after normalization) ONLY
    2. NO first-word matching (causes false positives like "Broken Eye" → "Broken Pieces")
    3. NO fuzzy matching for folders (too risky for false positives)

    Returns: (matched_folder_name, match_type)
      match_type: "EXACT" or None if no match
    """
    if not folder_series or not right_folders:
        return None, None

    normalized_series = normalize_name(folder_series)

    if not normalized_series:
        return None, None

    # Only try exact match (safest approach for folders)
    if normalized_series in right_folders:
        return right_folders[normalized_series], "EXACT"

    # No match found
    return None, None


def scan_source_subfolders() -> Dict[str, Dict]:
    """
    Scan source directory for subfolders.

    Returns: {
        "Sha 01-03": {
            "series": "Sha",
            "files": ["Sha 01.cbr", "Sha 02.cbr"],
            "folder_path": Path(...),
            "matched_folder": "Sha/" or None,
            "match_type": "EXACT"/None
        },
        ...
    }
    """
    subfolders = {}

    if not SRC_DIR.exists():
        return subfolders

    print(f"📁 Scanning source subfolders: {SRC_DIR}")

    # Get all right-side folders for matching
    right_folders = find_matching_right_folders()

    # Find all direct subfolders (not recursive)
    for item in sorted(SRC_DIR.iterdir()):
        if not item.is_dir():
            continue

        folder_name = item.name

        # Find comic files in this folder
        comic_files = [f.name for f in item.rglob('*')
                       if f.is_file() and f.suffix.lower() in {'.cbz', '.cbr'}]

        if not comic_files:
            continue

        # Extract series from folder name
        series = extract_folder_series_name(folder_name)

        if not series:
            continue

        # Find matching folder on right side
        matched_folder, match_type = find_folder_match(series, right_folders)

        subfolders[folder_name] = {
            "series": series,
            "files": comic_files,
            "folder_path": item,
            "matched_folder": matched_folder,
            "match_type": match_type,
            "file_count": len(comic_files),
        }

        print(f"   📂 {folder_name}")
        print(f"      Series: {series}, Files: {len(comic_files)}", end="")
        if matched_folder:
            print(f", Match: {matched_folder} ({match_type})")
        else:
            print(f", Match: None")

    print()
    return subfolders


# ═══════════════════════════════════════════════════════════════════════════
# DIRECTORY SCANNING
# ═══════════════════════════════════════════════════════════════════════════

def scan_source_directory() -> Dict[str, List[str]]:
    """
    Scan source directory and group files by extracted series name.
    Returns: {series_name: [file1, file2, ...]}
    """
    series_map = defaultdict(list)
    series_canonical = {}  # lowercase → first-seen original casing

    if not SRC_DIR.exists():
        print(f"❌ Source directory not found: {SRC_DIR}")
        return {}

    print(f"📂 Scanning source: {SRC_DIR}")
    # Recursively find .cbz and .cbr files in all subdirectories
    files = [f for f in SRC_DIR.rglob('*') if f.is_file() and f.suffix.lower() in {'.cbz', '.cbr'}]
    all_files = [f for f in SRC_DIR.rglob('*') if f.is_file()]
    print(f"   Found {len(files)} comic files (out of {len(all_files)} total)\n")

    for i, file_path in enumerate(sorted(files)):
        filename = file_path.name

        # Skip directories
        if file_path.is_dir():
            continue

        # Extract series name
        series = extract_series_name(filename)
        if not series:
            print(f"   ⚠️  [{i + 1}] WARNING: Cannot extract series from {filename}")
            continue

        # Skip certain series (match by extracted series name, not filename substring)
        if any(skip.lower() == series.lower() for skip in SKIP_PATTERNS):
            print(f"   ⏭️  [{i + 1}] SKIP: {filename} (series: {series})")
            continue

        # Group by normalized key (strips "the", dashes, whitespace), preserve first-seen casing
        series_lower = normalize_name(series)
        if series_lower not in series_canonical:
            series_canonical[series_lower] = series
        canonical = series_canonical[series_lower]

        # Store relative path from source directory so files can be found later
        relative_path = str(file_path.relative_to(SRC_DIR))
        series_map[canonical].append(relative_path)

        if (i + 1) % 10 == 0:
            print(f"   [{i + 1}] Processed {filename} → {canonical}")

    print(f"\n✅ Source scan complete: {len(series_map)} unique series\n")
    return dict(series_map)


def scan_destination_directory() -> Dict[str, Dict]:
    """
    Scan destination directory for files and folders.

    Returns: {
        series_name: {
            "folders": [folder_names],
            "files_in_folders": [filenames in subdirs],
            "loose_files": [filenames in base dir]
        }
    }
    """
    series_map = defaultdict(lambda: {
        "folders": [],
        "files_in_folders": [],
        "loose_files": []
    })

    if not DEST_DIR.exists():
        print(f"❌ Destination directory not found: {DEST_DIR}")
        return {}

    print(f"📂 Scanning destination: {DEST_DIR}")
    print(f"   (This may take a moment...)\n")

    item_count = 0

    # First pass: Get folders and loose files in base directory
    for item in DEST_DIR.iterdir():
        item_count += 1

        if item.is_dir():
            # A FOLDER is indexed under ONE key — its own primary candidate, no
            # alternatives. The folder name is a deliberate choice by you, so
            # 'Ghost Machine - The Official Guidebook' must not also answer to
            # 'Ghost Machine': an unrelated incoming 'Ghost Machine 001' would be
            # swept into the guidebook. Where several folders do collide on one
            # key anyway, pick_destination_folder() decides between them.
            series = extract_series_name(item.name)
            if series:
                series_map[series]["folders"].append(item.name)

        elif item.is_file():
            # Loose file in base directory (only .cbz and .cbr)
            if item.suffix.lower() in {'.cbz', '.cbr'}:
                # A LOOSE FILE is indexed under EVERY candidate — the opposite of
                # a folder, and deliberately so. No folder exists yet, so grouping
                # is the entire point: the loose
                # 'Cindy and Biscuit - We Love Trouble.cbz' has to be reachable as
                # 'Cindy and Biscuit' for an incoming issue to join it and form a
                # folder. Indexing under several keys costs nothing here because
                # find_exact_match() still requires an EXACT key match.
                for series in extract_series_candidates(item.name):
                    if series:
                        series_map[series]["loose_files"].append(item.name)

    # Second pass: Scan inside folders for files
    for item in DEST_DIR.rglob("*"):
        item_count += 1

        if item_count % 500 == 0:
            print(f"   Scanned {item_count} items...")

        # Only count comic files inside subdirectories (not in base).
        # Primary candidate only: this list feeds counts and display, never a
        # match decision (find_exact_match ignores files_in_folders on its own),
        # so multi-key indexing here would inflate numbers for no benefit.
        if item.is_file() and item.parent != DEST_DIR and item.suffix.lower() in {'.cbz', '.cbr'}:
            series = extract_series_name(item.name)
            if series:
                series_map[series]["files_in_folders"].append(item.name)

    print(f"\n✅ Destination scan complete:")
    print(f"   Total items scanned: {item_count}")
    print(f"   Unique series found: {len(series_map)}\n")

    return dict(series_map)


# ═══════════════════════════════════════════════════════════════════════════
# MATCHING LOGIC
# ═══════════════════════════════════════════════════════════════════════════

def _words(text: str) -> str:
    """Reduce text to space-delimited lowercase words, padded with spaces.

    'Superman_Isnt_Jewish_(2018)_(Humanoids)' -> ' superman isnt jewish 2018 humanoids '

    Every separator — space, underscore, dash, dot, bracket, ampersand — collapses
    to a single space, so the padded result can be searched for ' word ' to get a
    whole-word test without any regex boundary logic at the call site.
    """
    return ' %s ' % ' '.join(re.findall(r'[a-z0-9]+', text.lower()))


def contains_words(text: str, phrase: str) -> bool:
    """True if every word of `phrase` appears in `text`, in order, as whole words.

    This replaces `phrase.lower() in text.lower()`, which matched inside words:
    'Soleil' matched 'Beausoleil' and 'SAF' matched 'Failsafe', sending those
    files into a publisher folder they have nothing to do with.

    Tokenising rather than adding regex boundaries is deliberate. The boundary
    conditions here are exactly the ones \\b gets wrong on release filenames
    (underscores) and the ones lookarounds make unreadable. Splitting into words
    once and comparing words states the intent directly.
    """
    if not text or not phrase:
        return False
    return _words(phrase).strip().join((' ', ' ')) in _words(text)


def find_specific_series_match(filename: str, dest_map: Dict) -> Optional[Tuple[str, Dict, str]]:
    """
    Rule 1: Check if filename contains a specific series folder name (exact match).
    Returns: (matched_folder_name, match_data, match_type) or None
    Example: "Billy & Buddy v10..." → finds "Billy & Buddy 001-008 (2009-2019)"
    """
    for specific_folder in SPECIFIC_SERIES_FOLDERS:
        if contains_words(filename, specific_folder):
            # Find the actual folder in destination
            for dest_folder, dest_data in dest_map.items():
                if contains_words(dest_folder, specific_folder):
                    return (dest_folder, dest_data, "SPECIFIC_SERIES")
    return None


def find_publisher_match(filename: str, dest_map: Dict) -> Optional[Tuple[str, Dict, str]]:
    """
    Rule 2: Check if filename contains a publisher name.
    Extracts just the publisher name (e.g., "Cinebook" from "(Cinebook 2025)").
    Returns: (matched_folder_name, match_data, match_type) or None
    Example: "Amazonia 04 (Cinebook 2025)..." → finds "Cinebook (Europe)"
    """
    # Extract publisher names from known folders (first word)
    # "Cinebook (Europe)" → "Cinebook"
    # "SAF Comics (Europe Collection) (2019)" → "SAF"
    publisher_keywords = {
        "Cinebook", "Fantagraphics", "Humanoids", "Soleil", "SAF"
    }

    # This used to duplicate a module-level PUBLISHER_FOLDERS constant that was
    # declared and never read, and which had already drifted from this set (it
    # also listed 'Europe Comics (Collection)'). The dead constant is gone; this
    # keyword set is the single source of truth for publisher matching.
    for keyword in publisher_keywords:
        if contains_words(filename, keyword):
            # Find the folder with this publisher name
            for dest_folder, dest_data in dest_map.items():
                if contains_words(dest_folder, keyword):
                    return (dest_folder, dest_data, "PUBLISHER")
    return None


def find_exact_match(src_series: str, dest_map: Dict) -> Optional[Tuple[str, Dict]]:
    """
    Rule 3a: Find exact series name match in destination (case-insensitive).
    Returns a match if dest entry has a folder OR loose files in base dir.
    Does NOT count files_in_folders alone — those belong to a different series'
    folder, so counting them would match the wrong parent.
    Also tries normalized comparison (strips 'The', etc.) as a second pass.
    Returns: (matched_series_name, match_data) or None
    """
    src_lower = src_series.lower()
    # First pass: raw case-insensitive
    for dest_series, dest_data in dest_map.items():
        if dest_series.lower() == src_lower:
            has_folder = bool(dest_data.get("folders"))
            has_loose = bool(dest_data.get("loose_files"))
            if has_folder or has_loose:
                return (dest_series, dest_data)
    # Second pass: normalized comparison (handles "The" insertion/removal, year parens, etc.)
    src_norm = normalize_name(src_series)
    for dest_series, dest_data in dest_map.items():
        if normalize_name(dest_series) == src_norm:
            has_folder = bool(dest_data.get("folders"))
            has_loose = bool(dest_data.get("loose_files"))
            if has_folder or has_loose:
                return (dest_series, dest_data)
    return None


# REMOVED: find_fuzzy_match(). It was defined but never called, and its FUZZY
# confidence value was therefore unreachable everywhere it was handled.
#
# It matched with `src_lower in dest_lower or dest_lower in src_lower` — a bare
# substring test, the same technique that made 'Sleep' collect 'Sleeper Book 01'
# and 'Odin' collect 'A. Rodin'. Requirement O4 settles that this tool never
# fuzzy-matches: a false positive silently files a comic into the wrong series,
# which is worse than not matching it at all.
#
# Do not reintroduce this. If matching needs to be more forgiving, make the
# PARSER better (prototype/parse_release.py) rather than making the COMPARISON
# looser.


def _match_candidates(src_filename: str, src_series: str) -> List[str]:
    """Series names to try against the destination index, most specific first.

    src_filename may be a path relative to SRC_DIR ('Sha 01-03/Sha 01.cbr'), so
    only the basename is parsed — a directory component is not part of the title.
    """
    ordered: List[str] = []
    seen = set()
    for cand in (src_series, *extract_series_candidates(Path(src_filename).name)):
        key = (cand or '').strip().lower()
        if key and key not in seen:
            seen.add(key)
            ordered.append(cand)
    return ordered


def find_matches(src_filename: str, src_series: str, dest_map: Dict) -> Tuple[Optional[str], Optional[Dict], str]:
    """
    Find matches using priority rules:
    1. Specific series folders (Billy & Buddy, Gomer Goof, etc.)
    2. Publisher folders (Cinebook, Fantagraphics, etc.)
    3. Series name exact match (case-insensitive) — folder or loose files
    4. No match (None)

    Returns: (matched_folder, match_data, confidence)
             where confidence is one of:
             - 'SPECIFIC_SERIES', 'PUBLISHER', 'EXACT', 'NONE'
    """
    # Rule 1: Check for specific series folders
    specific = find_specific_series_match(src_filename, dest_map)
    if specific:
        return (specific[0], specific[1], specific[2])

    # Rule 2: Try exact series match (before publisher — a series folder beats a
    # publisher folder). Every candidate the parser produced is tried, MOST
    # SPECIFIC FIRST, so the library decides an ambiguity the filename cannot:
    # 'Die - Loaded v01' lands on the 'Die - Loaded' folder when it exists and on
    # 'Die' when it does not.
    #
    # src_series leads because it is the key scan_source_directory() grouped this
    # file under; trying it first keeps grouping and matching from disagreeing.
    for candidate in _match_candidates(src_filename, src_series):
        exact = find_exact_match(candidate, dest_map)
        if exact:
            return (exact[0], exact[1], "EXACT")

    # Rule 2b: Before-dash fallback — try main series name without arc subtitle.
    #
    # Rule 2 now normally covers this: parse_release() already appends the
    # before-dash form to series_candidates. Measured over 92 real downloads and
    # all 5,152 base-level library items, this line fired ZERO times. It is kept
    # only for the case Rule 2 cannot reach — src_series is the group key taken
    # from the FIRST file in the group, so it can contain ' - ' when the file
    # being matched does not. Delete it if that case is ever shown impossible.
    if ' - ' in src_series:
        main_series = src_series.split(' - ')[0].strip()
        if main_series and main_series != src_series:
            exact_main = find_exact_match(main_series, dest_map)
            if exact_main:
                return (exact_main[0], exact_main[1], "EXACT")

    # REMOVED: Rule 2c, the trailing 3-4 digit fallback ("2000AD prog 2485" ->
    # "2000AD prog"). It is now unreachable, not merely unused.
    #
    # Its input is always a parse_release() series, and parse_release cuts the
    # title at the first STRONG number — three or more digits always qualifies
    # (release.py _is_strong). So a trailing 3-4 digit run is consumed as the
    # issue number and can never survive into the series name. The only survivor
    # would be a series that is nothing BUT digits, and the rule's own
    # r'\s+\d{3,4}$' requires preceding whitespace, so that misses too.
    #
    # Confirmed empirically alongside 2b: zero fires over the same 5,244 samples.

    # Rule 3: Check for publisher folders
    publisher = find_publisher_match(src_filename, dest_map)
    if publisher:
        return (publisher[0], publisher[1], publisher[2])

    # Rule 4: No match
    return (None, None, "NONE")


# ═══════════════════════════════════════════════════════════════════════════
# CONSOLIDATION STRATEGY GENERATION
# ═══════════════════════════════════════════════════════════════════════════

def pick_destination_folder(src_filename: str, folders: List[str]) -> str:
    """Which folder receives this file, when several share one series key?

    Decision O14 — the most specific folder the FILENAME ITSELF names wins.

    Ten destination keys hold more than one folder. 'Sleeper' holds three:
    'Sleeper 001-012', 'Sleeper - Season One 01-12' and 'Sleeper - Season Two
    001-012'. All derive the key 'Sleeper' because parse_release() absorbs
    'Season N' as a run marker, which is what you asked for at the FILE level
    ('Heartthrob Season 3 001' -> 'Heartthrob'). Without this function the winner
    was whichever folder os.scandir happened to yield first — so 'Sleeper - Season
    Two 003.cbz' had a two-in-three chance of landing in the wrong one.

    contains_words(), not `in`: a bare substring test would let 'Sleeper' match
    inside 'Sleepers'.

    Equally specific names are broken by FILE COUNT — the folder that already
    holds the series wins. 'Hello Darkness' and 'Hello Darkness (2024)' are both
    real folders here and both reduce to 'Hello Darkness'; the (2024) one holds
    six issues and the other holds one. Alphabetical order would have split the
    series across both. (Two folders for one series is a library problem worth
    tidying by hand — this only stops the tool making it worse.)

    When the filename names none of them — reachable via a SPECIFIC_SERIES or
    PUBLISHER match, where the folder is not expected to appear in the name —
    there is nothing to choose on, so it sorts for reproducibility rather than
    guessing. Run-to-run stability matters here: this string becomes a path.
    """
    if len(folders) == 1:
        return folders[0]
    named = [f for f in folders
             if contains_words(src_filename, extract_folder_series_name(f))]
    if not named:
        return sorted(folders)[0]
    return sorted(named, key=lambda f: (-len(extract_folder_series_name(f)),
                                        -_comic_file_count(f), f))[0]


def _comic_file_count(folder_name: str) -> int:
    """Comics directly inside a destination folder. 0 if it cannot be read."""
    try:
        return sum(1 for f in (DEST_DIR / folder_name).iterdir()
                   if f.is_file() and f.suffix.lower() in {'.cbz', '.cbr'})
    except OSError:
        return 0


def generate_consolidation_strategy(
    src_filename: str,
    src_series: str,
    matched_series: Optional[str],
    match_data: Optional[Dict],
    confidence: str,
    remaining_files_count: int = 0,
) -> Dict:
    """
    Generate consolidation strategy row data.

    Logic:
    1. If RIGHT has FOLDER:
       → Move LEFT into existing folder
    2. If RIGHT has LOOSE FILES but NO folder:
       → Create folder, move LEFT + loose RIGHT files into it
    3. If RIGHT has NOTHING:
       → Copy LEFT to base /mnt/extramedia/Comics/ folder
    """
    num_files_in_folders = 0
    num_loose_files = 0
    num_folders = 0

    if matched_series and match_data:
        num_files_in_folders = len(match_data.get("files_in_folders", []))
        num_loose_files = len(match_data.get("loose_files", []))
        num_folders = len(match_data.get("folders", []))

    # Case 1: RIGHT has FOLDER
    if num_folders > 0:
        action_type = "CONSOLIDATE"
        # Use actual destination folder name from match_data to preserve year/edition info
        if match_data and match_data.get("folders"):
            display_folder = pick_destination_folder(src_filename, match_data["folders"])
        else:
            display_folder = matched_series if matched_series else src_series
        dest_folder = f"/{display_folder}/"

        # Determine move source (include loose files if present)
        if num_loose_files > 0:
            move_source = f"LEFT + RIGHT_FILES({num_loose_files})"
            consolidation_strategy = f"Move left file + {num_loose_files} loose right file(s) into {dest_folder}folder"
        else:
            move_source = "LEFT"
            consolidation_strategy = f"Move left file into {dest_folder}folder"

        # Add match type explanation
        if confidence == "SPECIFIC_SERIES":
            consolidation_strategy += " (specific series folder match)"
        elif confidence == "PUBLISHER":
            consolidation_strategy += " (publisher folder match)"

        total_matches = num_files_in_folders + num_loose_files + num_folders
        has_files = "YES" if (num_files_in_folders + num_loose_files) > 0 else "NO"
        if has_files == "YES":
            has_files = f"YES ({num_files_in_folders + num_loose_files})"

        return {
            "Left Panel File": src_filename,
            "Series Name": src_series,
            "Action Type": action_type,
            "Suggested Folder Name": dest_folder,
            "Right Panel Matches (Count)": total_matches,
            "Has Existing Folder": "YES",
            "Has Existing Files": has_files,
            "Consolidation Strategy": consolidation_strategy,
            "Move Source": move_source,
            "Confidence": confidence,
        }

    # Case 2: RIGHT has LOOSE FILES but NO FOLDER
    if num_loose_files > 0:
        # Name the new folder after the key that MATCHED, not after the source
        # guess. The two can differ now that Rule 2 walks a candidate list, and
        # when they do the matched key is the right one: it is the name the loose
        # files themselves derive, and they are about to be moved in.
        #
        # 'Cruel Kingdom 2 001' guesses 'Cruel Kingdom 2' but matches the loose
        # 'Cruel Kingdom v01 (2025).cbz' on the second candidate. Using the guess
        # created '/Cruel Kingdom 2/' and moved a file called 'Cruel Kingdom v01'
        # into it. EXACT only — a PUBLISHER match would name the folder after the
        # publisher.
        new_folder_name = matched_series if (confidence == "EXACT" and matched_series) else src_series
        move_source = f"LEFT + RIGHT_FILES({num_loose_files})"
        consolidation_strategy = f"Create /{new_folder_name}/ folder and move left file + {num_loose_files} loose right file(s) into it"
        action_type = "CREATE_FOLDER_WITH_FILES"
        dest_folder = f"/{new_folder_name}/"

        return {
            "Left Panel File": src_filename,
            "Series Name": src_series,
            "Action Type": action_type,
            "Suggested Folder Name": dest_folder,
            "Right Panel Matches (Count)": num_loose_files,
            "Has Existing Folder": "NO",
            "Has Existing Files": f"YES ({num_loose_files})",
            "Consolidation Strategy": consolidation_strategy,
            "Move Source": move_source,
            "Confidence": confidence,
        }

    # Case 3: RIGHT has NOTHING
    # If there are multiple files from this series (2 or more total), create a folder to group them
    if remaining_files_count >= 1:
        consolidation_strategy = f"Create /{src_series}/ folder and move {remaining_files_count + 1} left files into it"
        move_source = "LEFT"
        action_type = "CREATE_FOLDER_WITH_FILES"
        dest_folder = f"/{src_series}/"
    else:
        consolidation_strategy = "Copy left file to base Comics folder (no matching series found)"
        move_source = "LEFT"
        action_type = "COPY_TO_BASE"
        dest_folder = "/"

    return {
        "Left Panel File": src_filename,
        "Series Name": src_series,
        "Action Type": action_type,
        "Suggested Folder Name": dest_folder,
        "Right Panel Matches (Count)": 0,
        "Has Existing Folder": "NO",
        "Has Existing Files": "NO",
        "Consolidation Strategy": consolidation_strategy,
        "Move Source": move_source,
        "Confidence": confidence,
    }


# ═══════════════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════════════

def main():
    global SRC_DIR, DEST_DIR, OUTPUT_FILE

    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Comic File Organizer — Matching Analysis Generator")
    parser.add_argument("--src", type=str, help="Source directory (default: /home/nesha/Downloads/comics_download/)")
    parser.add_argument("--dest", type=str, help="Destination directory (default: /mnt/extramedia/Comics)")
    args = parser.parse_args()

    # Update SRC_DIR and DEST_DIR if provided
    if args.src:
        SRC_DIR = Path(args.src)
    if args.dest:
        DEST_DIR = Path(args.dest)

    # Update OUTPUT_FILE to use current SRC_DIR
    OUTPUT_FILE = SRC_DIR / "matching_analysis_consolidated.csv"

    print("\n" + "=" * 80)
    print("🎬 Comic File Organizer — Matching Analysis Generator")
    print("=" * 80 + "\n")

    # Scan directories
    subfolders = scan_source_subfolders()
    src_map = scan_source_directory()
    dest_map = scan_destination_directory()

    if not src_map and not subfolders:
        print("✅ No files found in source directory — writing empty CSV.")
        csv_columns = [
            "Left Folder", "File Count", "Left Panel File", "Series Name",
            "Action Type", "Suggested Folder Name", "Right Panel Matches (Count)",
            "Has Existing Folder", "Has Existing Files", "Consolidation Strategy",
            "Move Source", "Files Details", "Right Loose Files", "Proposed Filename",
            "Proposed Files Details",
        ]
        output_dir = OUTPUT_FILE.parent
        output_dir.mkdir(parents=True, exist_ok=True)
        with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
            csv.DictWriter(f, fieldnames=csv_columns).writeheader()
        print(f"✅ CSV written to: {OUTPUT_FILE}")
        return

    # Generate analysis rows
    print("🔍 Analyzing and matching series...\n")

    rows = []
    consolidate_folder_count = 0
    create_folder_from_folder_count = 0
    consolidate_count = 0
    create_folder_with_files_count = 0
    copy_to_base_count = 0
    exact_matches = 0

    # STEP 1: Process all folders (with or without matches)
    print("📁 Processing subfolders...")
    processed_files = set()  # Track which files we've processed via folder

    for folder_name, folder_data in sorted(subfolders.items()):
        folder_series = folder_data["series"]
        matched_folder = folder_data["matched_folder"]
        match_type = folder_data["match_type"]
        files_in_folder = folder_data["files"]
        file_count = folder_data["file_count"]

        if matched_folder:
            # Folder has a match - consolidate all files together
            consolidate_folder_count += 1
            action_type = "CONSOLIDATE_FOLDER"
            consolidation_strategy = f"Move all {file_count} file(s) from {folder_name}/ to {matched_folder} ({match_type} folder match)"
            dest_folder = matched_folder.rstrip('/')
            print(f"   ✅ {folder_name} → {matched_folder} ({match_type})")

        else:
            # Folder has NO match - create new folder and move all files
            # Also check for loose right-side files matching this series
            create_folder_from_folder_count += 1
            action_type = "CREATE_FOLDER_FROM_FOLDER"
            dest_folder = folder_series

            # Find loose right-side files that should also move into the new folder
            right_loose = []
            if folder_series in dest_map:
                right_loose = dest_map[folder_series].get("loose_files", [])

            if right_loose:
                right_count = len(right_loose)
                consolidation_strategy = (
                    f"Create new /{folder_series}/ folder, move all {file_count} file(s) "
                    f"from {folder_name}/ + {right_count} loose right file(s) into it"
                )
                print(f"   📂 {folder_name} → CREATE new /{folder_series}/ folder + {right_count} right file(s)")
            else:
                consolidation_strategy = f"Create new /{folder_series}/ folder and move all {file_count} file(s) from {folder_name}/"
                print(f"   📂 {folder_name} → CREATE new /{folder_series}/ folder")

        # Create one row representing the folder consolidation
        move_source = "LEFT"

        # Create a representative row (folder level)
        # For CREATE_FOLDER_FROM_FOLDER, include right loose files in count
        right_loose_for_row = []
        if action_type == "CREATE_FOLDER_FROM_FOLDER" and folder_series in dest_map:
            right_loose_for_row = dest_map[folder_series].get("loose_files", [])

        right_match_count = len(right_loose_for_row) if right_loose_for_row else (file_count if matched_folder else 0)
        has_existing_files = f"YES ({len(right_loose_for_row)})" if right_loose_for_row else ("YES" if matched_folder else "NO")

        # Compute proposed filenames for each file in the folder
        dest_folder_path_for_canonical = DEST_DIR / dest_folder.strip('/')
        canonical = get_canonical_series_for_folder(dest_folder_path_for_canonical)
        if not canonical:
            # Use most common series name from source files themselves
            src_series_counts = Counter(extract_series_name(f) for f in files_in_folder if f)
            canonical = src_series_counts.most_common(1)[0][0] if src_series_counts else None

        proposed_files_details_parts = []
        for fname in files_in_folder:
            if canonical:
                proposed = propose_filename(fname, canonical)
                proposed_files_details_parts.append(proposed if proposed != fname else fname)
            else:
                proposed_files_details_parts.append(fname)

        row = {
            "Left Folder": folder_name,
            "File Count": file_count,
            "Left Panel File": f"[{file_count} files in {folder_name}/]",
            "Series Name": folder_series,
            "Action Type": action_type,
            "Suggested Folder Name": dest_folder,
            "Right Panel Matches (Count)": right_match_count,
            "Has Existing Folder": "YES" if matched_folder else "NO",
            "Has Existing Files": has_existing_files,
            "Consolidation Strategy": consolidation_strategy,
            "Move Source": move_source,
            "Confidence": match_type if matched_folder else "NEW",
            "Files Details": " | ".join(files_in_folder),
            "Right Loose Files": " | ".join(right_loose_for_row),
            "Proposed Files Details": " | ".join(proposed_files_details_parts),
        }
        rows.append(row)

        # Mark these files as processed
        for f in files_in_folder:
            processed_files.add(f)

    # STEP 2: Process remaining files (loose files + files in folders without matches)
    print("\n📄 Processing individual files (loose + unmatched folders)...")

    for i, (src_series, src_files) in enumerate(sorted(src_map.items()), 1):
        # For each file in this series
        for src_filename in src_files:
            # Skip if already processed via folder consolidation
            if src_filename in processed_files:
                continue

            # Count remaining files from this series (excluding current file and already processed)
            remaining_count = len([f for f in src_files if f != src_filename and f not in processed_files])

            # Find matches (pass filename for rule 1 & 2 checks)
            matched_series, match_data, confidence = find_matches(src_filename, src_series, dest_map)

            # Generate strategy
            row = generate_consolidation_strategy(
                src_filename, src_series, matched_series, match_data, confidence, remaining_count
            )

            # Compute proposed filename (rename to match canonical series in target folder)
            proposed_filename = ""
            if row.get("Action Type") == "CONSOLIDATE" and confidence != "PUBLISHER":
                dest_folder_name = row.get("Suggested Folder Name", "").strip("/").strip()
                if dest_folder_name:
                    canonical = get_canonical_series_for_folder(DEST_DIR / dest_folder_name)
                    if canonical:
                        src_basename = Path(src_filename).name
                        proposed = propose_filename(src_basename, canonical)
                        if proposed != src_basename:
                            proposed_filename = proposed
            row["Proposed Filename"] = proposed_filename

            # Populate Right Loose Files for all file-level action types
            loose = dest_map.get(matched_series, {}).get("loose_files", []) if matched_series else []
            row["Right Loose Files"] = " | ".join(loose)

            # Track statistics
            action_type = row["Action Type"]
            if action_type == "CONSOLIDATE":
                consolidate_count += 1
            elif action_type == "CREATE_FOLDER_WITH_FILES":
                create_folder_with_files_count += 1
            elif action_type == "COPY_TO_BASE":
                copy_to_base_count += 1

            if confidence in ["EXACT", "SPECIFIC_SERIES", "PUBLISHER"]:
                exact_matches += 1

            # Add folder info if file is in a subfolder
            file_parent = None
            for folder_name, folder_data in subfolders.items():
                if src_filename in folder_data["files"]:
                    file_parent = folder_name
                    break

            if file_parent:
                row["Left Folder"] = file_parent

            rows.append(row)

        if i % 10 == 0:
            print(f"   [{i}] Analyzed {i} series...")

    print(f"\n✅ Analysis complete!\n")

    # Write CSV
    print("📝 Writing CSV file...")
    output_dir = OUTPUT_FILE.parent
    output_dir.mkdir(parents=True, exist_ok=True)

    csv_columns = [
        "Left Folder",
        "File Count",
        "Left Panel File",
        "Series Name",
        "Action Type",
        "Suggested Folder Name",
        "Right Panel Matches (Count)",
        "Has Existing Folder",
        "Has Existing Files",
        "Consolidation Strategy",
        "Move Source",
        "Files Details",
        "Right Loose Files",
        "Proposed Filename",
        "Proposed Files Details",
    ]

    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=csv_columns, restval="")
        writer.writeheader()
        for row in rows:
            # Keep only CSV columns, ignore 'Confidence' (internal use only)
            output_row = {col: row.get(col, "") for col in csv_columns}
            writer.writerow(output_row)

    print(f"✅ CSV written to: {OUTPUT_FILE}\n")

    # Print summary
    print("=" * 80)
    print("📊 SUMMARY STATISTICS")
    print("=" * 80)
    print(f"Total Rows: {len(rows)}")
    print(f"  - Folder consolidations: {consolidate_folder_count + create_folder_from_folder_count}")
    print(f"  - Individual file operations: {len(rows) - (consolidate_folder_count + create_folder_from_folder_count)}")
    print(f"\nAction Types:")
    print(f"  → CONSOLIDATE_FOLDER (move folder to existing folder): {consolidate_folder_count}")
    print(f"  → CREATE_FOLDER_FROM_FOLDER (create folder for subfolder): {create_folder_from_folder_count}")
    print(f"  → CONSOLIDATE (move to existing folder): {consolidate_count}")
    print(f"  → CREATE_FOLDER_WITH_FILES (create folder + move files): {create_folder_with_files_count}")
    print(f"  → COPY_TO_BASE (copy to base Comics folder): {copy_to_base_count}")
    print(f"\nMatch Quality:")
    print(f"  → Matches: {exact_matches}")
    print(f"\nRight Panel (Destination):")
    print(f"  → Total unique series: {len(dest_map)}")
    print("=" * 80 + "\n")

    # List folder consolidations and creations for reference
    folder_ops = [row for row in rows if row["Action Type"] in ["CONSOLIDATE_FOLDER", "CREATE_FOLDER_FROM_FOLDER"]]
    if folder_ops:
        print(f"📁 {len(folder_ops)} Folder-Level Operations:")
        for row in folder_ops:
            folder = row.get("Left Folder", "Unknown")
            dest = row.get("Suggested Folder Name", "Unknown")
            count = row.get("File Count", "?")
            action = row.get("Action Type", "?")
            if action == "CONSOLIDATE_FOLDER":
                print(f"   → {folder} ({count} files) → {dest} (CONSOLIDATE)")
            else:
                print(f"   → {folder} ({count} files) → CREATE {dest}/ (NEW)")
        print()

    # List unmatched series for reference
    unmatched = [row["Series Name"] for row in rows if row["Action Type"] == "COPY_TO_BASE"]
    unique_unmatched = sorted(set(unmatched))
    if unique_unmatched:
        print(f"📋 {len(unique_unmatched)} Unique Unmatched Series (copy to base):")
        for series in unique_unmatched:
            print(f"   • {series}")
        print()


if __name__ == "__main__":
    main()
