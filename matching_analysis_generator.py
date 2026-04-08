#!/usr/bin/env python3
"""
Comic File Organizer — Matching Analysis Generator

Reads source and destination directories, extracts series names,
performs exact/fuzzy matching, and generates consolidation strategies.

Output: matching_analysis_consolidated.csv
"""

import csv
import re
from pathlib import Path
from collections import defaultdict
from typing import Dict, List, Tuple, Optional

# ═══════════════════════════════════════════════════════════════════════════
# REGEX PATTERNS
# ═══════════════════════════════════════════════════════════════════════════

COMIC_EXTS = {'.cbz', '.cbr', '.zip', '.rar'}

VOLUME_PATTERN = re.compile(
    r'\b(?:v|vol|book|t)\.?\s*\d+|TPB|Omnibus|Collection|Graphic\s*Novel|GN|HC|Scanlation|Complete',
    re.IGNORECASE
)

ISSUE_PATTERN = re.compile(
    r'\s+#?\d+(?:\s*\(of\s*\d+\))?|\s+\(\d{1,3}\)'
)

YEAR_PATTERN = re.compile(r'\((\d{4})\)')

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

# Known publisher folders (rule 2 priority)
PUBLISHER_FOLDERS = {
    "Cinebook (Europe)",
    "Europe Comics (Collection)",
    "Fantagraphics (Europe)",
    "Humanoids (Europe)",
    "SAF Comics (Europe Collection) (2019)",
    "Soleil (Europe)",
}

# ═══════════════════════════════════════════════════════════════════════════
# FILENAME PARSING
# ═══════════════════════════════════════════════════════════════════════════

def parse_filename(filename: str) -> Dict[str, Optional[str]]:
    """
    Parse comic filename and extract structured data.

    Returns:
        {
            'series': str (base series name without volume info),
            'subtitle': str|None (text after ' - ' following issue),
            'year': str|None (YYYY)
        }

    Examples:
        "The Cold Witch 01 (of 05) - A Tale of the Shrouded College (2025) (Digital).cbr"
        → { series: "The Cold Witch", subtitle: "A Tale of the Shrouded College", year: "2025" }

        "Feral v04 - Pet City (2026) (Digital).cbr"
        → { series: "Feral", subtitle: "Pet City", year: "2026" }

        "Feral 021 (2024) (Series).cbz"
        → { series: "Feral", subtitle: None, year: "2024" }
    """
    if not filename:
        return {'series': '', 'subtitle': None, 'year': None}

    # Remove extension
    name = filename
    for ext in COMIC_EXTS:
        if name.lower().endswith(ext):
            name = name[:-len(ext)]
            break

    # Extract year
    year_match = YEAR_PATTERN.search(name)
    year = year_match.group(1) if year_match else None

    # Remove everything from year onwards
    if year_match:
        name = name[:year_match.start()].strip()

    # Remove volume patterns (v04, TPB, Omnibus, etc.)
    name = VOLUME_PATTERN.sub('', name).strip()

    # Find issue number block
    issue_match = ISSUE_PATTERN.search(name)

    if issue_match:
        # Series is everything before the issue block
        series = name[:issue_match.start()].strip()

        # Subtitle is text after ` - ` following the issue block
        remaining = name[issue_match.end():].strip()
        subtitle = None

        if remaining.startswith('-'):
            remaining = remaining[1:].strip()
            # Remove any (tags) at the end
            remaining = re.sub(r'\s*\([^)]*\)\s*$', '', remaining).strip()
            subtitle = remaining if remaining else None
    else:
        # No issue number found
        # Check if there's a " - " in the name (volume separator)
        if ' - ' in name:
            parts = name.split(' - ', 1)
            series = parts[0].strip()
            subtitle = parts[1].strip() if len(parts) > 1 else None
        else:
            series = name.strip()
            subtitle = None

    # Clean up series name
    series = re.sub(r'\s+', ' ', series).strip()

    return {
        'series': series if series else filename,
        'subtitle': subtitle,
        'year': year,
    }


def extract_series_name(filename: str) -> str:
    """Extract base series name from filename."""
    parsed = parse_filename(filename)
    return parsed['series']


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
    # Remove articles at start
    normalized = re.sub(r'^\b(the|a|an)\s+', '', name, flags=re.IGNORECASE)

    # Remove volume patterns (v01, vol, book, 001-002, etc.)
    normalized = VOLUME_PATTERN.sub('', normalized)

    # Remove years and parenthetical info
    normalized = re.sub(r'\s*\([^)]*\)\s*', ' ', normalized)

    # Remove issue numbers
    normalized = ISSUE_PATTERN.sub('', normalized)

    # Clean up spaces and lowercase
    normalized = re.sub(r'\s+', ' ', normalized).strip().lower()

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
    Find matching folder on right side with STRICT matching.

    Matching priority:
    1. Exact match (after normalization)
    2. First-word match (first word of series matches first word of folder)
    3. NO fuzzy matching for folders (too risky for false positives)

    Returns: (matched_folder_name, match_type)
      match_type: "EXACT", "FIRST_WORD", or None if no match
    """
    if not folder_series or not right_folders:
        return None, None

    normalized_series = normalize_name(folder_series)
    series_words = normalized_series.split()

    if not series_words:
        return None, None

    # 1. Try exact match
    if normalized_series in right_folders:
        return right_folders[normalized_series], "EXACT"

    # 2. Try first-word match (only if first word of series matches start of folder)
    series_first_word = series_words[0]

    for norm_folder, actual_folder in right_folders.items():
        folder_words = norm_folder.split()

        # Check if series first word matches any folder word AND
        # the series first word is at the START of the folder name (not buried in middle)
        if series_first_word in folder_words:
            # Get position of match
            match_index = folder_words.index(series_first_word)
            # Accept match only if it's in first 2 words (series name usually at start)
            if match_index <= 1:
                return actual_folder, "FIRST_WORD"

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
            "match_type": "EXACT"/"FUZZY"/None
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

        # Skip certain patterns
        if any(skip in filename.lower() for skip in SKIP_PATTERNS):
            print(f"   ⏭️  [{i + 1}] SKIP: {filename}")
            continue

        # Skip directories
        if file_path.is_dir():
            continue

        # Extract series name
        series = extract_series_name(filename)
        if not series:
            print(f"   ⚠️  [{i + 1}] WARNING: Cannot extract series from {filename}")
            continue

        # Store relative path from source directory so files can be found later
        relative_path = str(file_path.relative_to(SRC_DIR))
        series_map[series].append(relative_path)

        if (i + 1) % 10 == 0:
            print(f"   [{i + 1}] Processed {filename} → {series}")

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
            # Extract series name from folder
            series = extract_series_name(item.name)
            if series:
                series_map[series]["folders"].append(item.name)

        elif item.is_file():
            # Loose file in base directory (only .cbz and .cbr)
            if item.suffix.lower() in {'.cbz', '.cbr'}:
                series = extract_series_name(item.name)
                if series:
                    series_map[series]["loose_files"].append(item.name)

    # Second pass: Scan inside folders for files
    for item in DEST_DIR.rglob("*"):
        item_count += 1

        if item_count % 500 == 0:
            print(f"   Scanned {item_count} items...")

        # Only count comic files inside subdirectories (not in base)
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

def find_specific_series_match(filename: str, dest_map: Dict) -> Optional[Tuple[str, Dict, str]]:
    """
    Rule 1: Check if filename contains a specific series folder name (exact match).
    Returns: (matched_folder_name, match_data, match_type) or None
    Example: "Billy & Buddy v10..." → finds "Billy & Buddy 001-008 (2009-2019)"
    """
    for specific_folder in SPECIFIC_SERIES_FOLDERS:
        if specific_folder.lower() in filename.lower():
            # Find the actual folder in destination
            for dest_folder, dest_data in dest_map.items():
                if specific_folder.lower() in dest_folder.lower():
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

    for keyword in publisher_keywords:
        if keyword.lower() in filename.lower():
            # Find the folder with this publisher name
            for dest_folder, dest_data in dest_map.items():
                if keyword.lower() in dest_folder.lower():
                    return (dest_folder, dest_data, "PUBLISHER")
    return None


def find_exact_match(src_series: str, dest_map: Dict) -> Optional[Tuple[str, Dict]]:
    """
    Rule 3a: Find exact series name match in destination (case-insensitive).
    Only returns a match if the dest entry has an actual named folder.
    (Files that happen to share a series name but live in a different folder
    are not counted — fuzzy matching will find their parent folder instead.)
    Returns: (matched_series_name, match_data) or None
    """
    src_lower = src_series.lower()
    for dest_series, dest_data in dest_map.items():
        if dest_series.lower() == src_lower:
            # Only count as a real match if a dedicated folder exists
            if dest_data.get("folders"):
                return (dest_series, dest_data)
    return None


def find_fuzzy_match(src_series: str, dest_map: Dict) -> Optional[Tuple[str, Dict]]:
    """
    Rule 3b: Find fuzzy series match in destination.
    - Only if src_series > 5 characters
    - Check if src appears in dest or vice versa
    - Dest series must be > 3 characters
    - Dest entry must have an actual folder (not just stray files)
    - Prefer folder matches over file-only matches
    Returns: (matched_series_name, match_data) or None
    """
    if len(src_series) <= 5:
        return None

    src_lower = src_series.lower()

    folder_match = None   # Best match that has a folder
    file_match = None     # Fallback match with only loose files

    for dest_series, dest_data in dest_map.items():
        if len(dest_series) <= 3:
            continue

        # Skip exact self-match (same series name shouldn't fuzzy-match itself)
        if dest_series == src_series:
            continue

        dest_lower = dest_series.lower()

        # Check if one contains the other (substring match)
        if src_lower in dest_lower or dest_lower in src_lower:
            has_folder = bool(dest_data.get("folders"))
            has_files = bool(dest_data.get("files_in_folders") or dest_data.get("loose_files"))

            if has_folder and folder_match is None:
                folder_match = (dest_series, dest_data)
            elif has_files and file_match is None:
                file_match = (dest_series, dest_data)

    # Prefer folder matches
    return folder_match or file_match or None


def find_matches(src_filename: str, src_series: str, dest_map: Dict) -> Tuple[Optional[str], Optional[Dict], str]:
    """
    Find matches using priority rules:
    1. Specific series folders (Billy & Buddy, Gomer Goof, etc.)
    2. Publisher folders (Cinebook, Fantagraphics, etc.)
    3. Series name matching (exact, then fuzzy)
    4. No match (None)

    Returns: (matched_folder, match_data, confidence)
             where confidence is one of:
             - 'SPECIFIC_SERIES', 'PUBLISHER', 'EXACT', 'FUZZY', 'NONE'
    """
    # Rule 1: Check for specific series folders
    specific = find_specific_series_match(src_filename, dest_map)
    if specific:
        return (specific[0], specific[1], specific[2])

    # Rule 2: Check for publisher folders
    publisher = find_publisher_match(src_filename, dest_map)
    if publisher:
        return (publisher[0], publisher[1], publisher[2])

    # Rule 3a: Try exact series match
    exact = find_exact_match(src_series, dest_map)
    if exact:
        return (exact[0], exact[1], "EXACT")

    # Rule 3b: Try fuzzy series match
    fuzzy = find_fuzzy_match(src_series, dest_map)
    if fuzzy:
        return (fuzzy[0], fuzzy[1], "FUZZY")

    # Rule 4: No match
    return (None, None, "NONE")


# ═══════════════════════════════════════════════════════════════════════════
# CONSOLIDATION STRATEGY GENERATION
# ═══════════════════════════════════════════════════════════════════════════

def generate_consolidation_strategy(
    src_filename: str,
    src_series: str,
    matched_series: Optional[str],
    match_data: Optional[Dict],
    confidence: str,
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
        # Use matched_series (which may be publisher or specific folder) for display
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
        elif confidence == "FUZZY":
            consolidation_strategy += " (fuzzy match)"

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
        move_source = f"LEFT + RIGHT_FILES({num_loose_files})"
        consolidation_strategy = f"Create /{src_series}/ folder and move left file + {num_loose_files} loose right file(s) into it"
        action_type = "CREATE_FOLDER_WITH_FILES"
        dest_folder = f"/{src_series}/"

        if confidence == "FUZZY":
            consolidation_strategy += " (fuzzy match)"

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

    # Case 3: RIGHT has NOTHING — copy to base folder
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
    print("\n" + "=" * 80)
    print("🎬 Comic File Organizer — Matching Analysis Generator")
    print("=" * 80 + "\n")

    # Scan directories
    subfolders = scan_source_subfolders()
    src_map = scan_source_directory()
    dest_map = scan_destination_directory()

    if not src_map and not subfolders:
        print("❌ No files found in source directory.")
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
    fuzzy_matches = 0

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
            create_folder_from_folder_count += 1
            action_type = "CREATE_FOLDER_FROM_FOLDER"
            consolidation_strategy = f"Create new /{folder_series}/ folder and move all {file_count} file(s) from {folder_name}/"
            dest_folder = folder_series
            print(f"   📂 {folder_name} → CREATE new /{folder_series}/ folder")

        # Create one row representing the folder consolidation
        move_source = "LEFT"

        # Create a representative row (folder level)
        row = {
            "Left Folder": folder_name,
            "File Count": file_count,
            "Left Panel File": f"[{file_count} files in {folder_name}/]",
            "Series Name": folder_series,
            "Action Type": action_type,
            "Suggested Folder Name": dest_folder,
            "Right Panel Matches (Count)": file_count if matched_folder else 0,
            "Has Existing Folder": "YES" if matched_folder else "NO",
            "Has Existing Files": "YES" if matched_folder else "NO",
            "Consolidation Strategy": consolidation_strategy,
            "Move Source": move_source,
            "Confidence": match_type if matched_folder else "NEW",
            "Files Details": " | ".join(files_in_folder),
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

            # Find matches (pass filename for rule 1 & 2 checks)
            matched_series, match_data, confidence = find_matches(src_filename, src_series, dest_map)

            # Generate strategy
            row = generate_consolidation_strategy(
                src_filename, src_series, matched_series, match_data, confidence
            )

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
            elif confidence == "FUZZY":
                fuzzy_matches += 1

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
    print(f"  → Exact/Substring Matches: {exact_matches}")
    print(f"  → Fuzzy Matches: {fuzzy_matches}")
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
