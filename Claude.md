# Comic File Organizer — Claude Context

## What This Project Does
Consolidates downloaded comic files from source folder into organized destination library.

**Source (left):**  `/home/nesha/Downloads/comics_download/`
**Destination (right):** `/mnt/extramedia/Comics/` (~47,000 items, ~11,900 unique series)
**CSV:** `/home/nesha/Downloads/comics_download/matching_analysis_consolidated.csv`

## How to Run
```bash
cd /home/nesha/scripts/cp_downloads2comics/
python3 serve_v2.py
# Open http://localhost:8123
```
Then: Scan Folders → Dry Run → Consolidate!

## Key Files
| File | Purpose |
|------|---------|
| `serve_v2.py` | HTTP server port 8123 |
| `comic_organizer_v2.html` | Web UI |
| `matching_analysis_generator.py` | Scan + match + generate CSV |
| `comic_mover.py` | Execute moves from CSV |

## Architecture — Important Notes

### Source Scanning (TWO passes)
1. **Subfolders first** — `scan_source_subfolders()` treats each subfolder as a unit
   - All files in a subfolder consolidate together (flattened, no nested structure)
   - Matching: EXACT or FIRST_WORD only (NO fuzzy for folders)
   - No match → CREATE_FOLDER_FROM_FOLDER (also picks up matching loose right files)
2. **Individual files** — `scan_source_directory()` handles loose files and files in unmatched subfolders

### SKIP_PATTERNS
Applied to **loose files only**, NOT folder names:
```python
SKIP_PATTERNS = {"comics_download.txt", "sha 01", "the bank", "the owl"}
```

### Matching Gotchas
- `find_exact_match`: only matches if dest has named folder OR loose_files
  (NOT files_in_folders alone — those live inside a different folder)
- `find_fuzzy_match`: prefers folder matches, skips self-matches
- Example: "Briar - Night's Terror" has files_in_folders in dest_map but NO folder
  → exact match skips it → fuzzy finds "Briar (2022)" folder ✓

### Action Types
| Action | Description |
|--------|-------------|
| `CONSOLIDATE_FOLDER` | Subfolder → existing right folder |
| `CREATE_FOLDER_FROM_FOLDER` | Subfolder → new folder (+ right loose files) |
| `CONSOLIDATE` | Loose file → existing right folder |
| `CREATE_FOLDER_WITH_FILES` | Loose file + right loose files → new folder |
| `COPY_TO_BASE` | No match → Comics/ base directory |

## UI Sections
1. **Source Folders** — folder-level rows, expandable (▶) to show individual files
2. **Consolidations** — individual file → existing folder
3. **New Folders / Unmatched** — individual file → new folder or base

## Model Recommendation
- **Haiku 4.5** — UI tweaks, simple fixes, documentation
- **Sonnet 4.6** — matching logic, multi-file architecture changes, complex debugging
