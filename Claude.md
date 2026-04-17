# Comic File Organizer — Claude Context (v2.5)

## What This Project Does
Consolidates downloaded comic files from source folder into organized destination library.

**Source (left):**  `/home/nesha/Downloads/comics_download/`
**Destination (right):** `/mnt/extramedia/Comics/` (~47,000 items, ~11,900 unique series)
**CSV:** `/home/nesha/Downloads/comics_download/matching_analysis_consolidated.csv`

## Recent Updates (v2.5)
**Three critical matching bugs fixed:**
1. Year range handling — destination folders with year ranges like (2019-2024) now extract correctly
2. Consolidation path accuracy — now uses actual folder names instead of extracted keys (preserves year/edition)
3. Folder matching safety — removed risky FIRST_WORD matching that caused unrelated series to consolidate together

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
| `CREATE_FOLDER_WITH_FILES` | Loose file(s) + right loose files → new folder |
| `COPY_TO_BASE` | Single unmatched file → Comics/ base directory |

Note: 2+ loose files sharing the same series name always get `CREATE_FOLDER_WITH_FILES` even with no right-side match.

### Destination Override Behaviour
- User can override `dest_folder` on any row via "Edit dest.folder"
- `comic_mover.py` always calls `mkdir(parents=True, exist_ok=True)` before moving — so overriding to a non-existent folder name is safe; the folder is created automatically

## UI Sections
1. **Source Folders** — folder-level rows, expandable (▶) to show individual files
2. **Consolidations** — individual file → existing folder
3. **New Folders / Unmatched** — individual file → new folder or base

## Multi-Select Bulk Editing (v2.4)
- Check multiple rows, then click **Edit series name** or **Edit dest.folder** on any selected row
- If the clicked row is among the selection, the change applies to all selected rows
- Series name bulk edit: applies `seriesOverride` only — no rescan. Run Scan/Dry Run to refresh matching
- Dest folder bulk edit: applies `destOverride` to all selected rows immediately
- If the clicked row is NOT in the selection, edit applies to that row only (single-row behaviour)

## Folder Picker (v2.4)
- Top-level Browse buttons open a modal with two tabs: 📁 Browse (webkitdirectory) and ✏️ Enter Path
- Selected paths are sent to `/api/scan`, `/api/dry-run`, and `/api/consolidate` in POST JSON body
- `matching_analysis_generator.py` accepts `--src` and `--dest` CLI args to override hardcoded defaults

## Model Recommendation
- **Haiku 4.5** — UI tweaks, simple fixes, documentation
- **Sonnet 4.6** — matching logic, multi-file architecture changes, complex debugging
