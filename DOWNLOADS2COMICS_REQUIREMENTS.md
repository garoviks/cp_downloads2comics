# Downloads2Comics — Requirements

**Current version: v2.5**

## Overview

Downloads2Comics is a web-based tool for consolidating downloaded comic files from a source folder into an organized destination library. It scans both sides, matches series names using a priority-based algorithm, generates a CSV action plan, and executes file moves on confirmation.

| Item | Path |
|------|------|
| Source (left) | `/home/nesha/Downloads/comics_download/` |
| Destination (right) | `/mnt/extramedia/Comics/` (~47,000 items, ~11,900 series) |
| CSV plan | `{source_dir}/matching_analysis_consolidated.csv` |
| Server | `http://localhost:8123` |

---

## Functional Requirements

### FR1: Source Scanning (Two-Pass)

**Pass 1 — Subfolders:**
- Scan all direct subfolders of the source directory
- Treat each subfolder as a single unit: all files inside move together
- Extract series name from the folder name
- Attempt EXACT match only against destination folders (no fuzzy for subfolders — safety)
- Unmatched subfolders are assigned `CREATE_FOLDER_FROM_FOLDER`; also picks up matching loose right-side files

**Pass 2 — Loose files:**
- Scan all `.cbz`, `.cbr`, `.zip`, `.rar` files recursively in the source directory
- Skip files matching `SKIP_PATTERNS` (matched against extracted series name):
  ```
  comics_download.txt, sha 01, the bank, the owl
  ```
- Group files by extracted series name (case-insensitive)
- Files already processed as part of a subfolder in Pass 1 are excluded

### FR2: Destination Scanning

- Two-pass scan of destination directory:
  1. Base directory items (direct subfolders and loose files)
  2. Recursive scan inside all folders (to detect files already inside existing volumes)
- Build `dest_map`: `{ series_name: { folders, files_in_folders, loose_files } }`
- Case-insensitive keying

### FR3: Matching

Four rules applied in priority order per source file/series:

| Priority | Rule | Method | Description |
|----------|------|--------|-------------|
| 1 | Specific Series | Substring in filename | Hardcoded list: Billy & Buddy, Gomer Goof |
| 2 | Publisher | Keyword in filename | Cinebook, Fantagraphics, Humanoids, Soleil, SAF → publisher folder |
| 3 | Exact | Case-insensitive name match | Only matches if dest has a named folder OR loose files (NOT files_in_folders alone) |
| 4 | Fuzzy | Substring containment | Series > 5 chars; dest must have actual folder; prefers folder over file-only |

**Subfolder matching:** EXACT only (rules 1–4 do not apply to subfolder-level matching).

**Exact match guard:** `find_exact_match()` skips dest entries that have only `files_in_folders` with no named folder and no loose files — those files belong to a different series' folder.

### FR4: Action Type Assignment

| Action | Trigger | Description |
|--------|---------|-------------|
| `CONSOLIDATE_FOLDER` | Subfolder + dest folder found | Move all files from source subfolder into existing dest folder |
| `CREATE_FOLDER_FROM_FOLDER` | Subfolder + no dest match | Create new dest folder from subfolder name; also pull in any matching right loose files |
| `CONSOLIDATE` | Loose file + dest folder found | Move file into existing dest folder |
| `CREATE_FOLDER_WITH_FILES` | Loose file(s) + right loose files exist, OR 2+ files from same series | Create new folder; move source file(s) + right loose files into it |
| `COPY_TO_BASE` | Single unmatched loose file, no right-side match | Copy file to base destination directory (no folder created) |

Note: 2+ loose files sharing the same extracted series name always get `CREATE_FOLDER_WITH_FILES` even without a right-side match.

### FR5: Consolidation Strategy

- Each row includes a human-readable `Consolidation Strategy` description
- `Move Source` field: `LEFT` or `LEFT + RIGHT_FILES(N)` — indicates whether right-side loose files are also being moved
- Right loose files are identified by substring match of series name against base destination directory

### FR6: CSV Output

Written to `{source_dir}/matching_analysis_consolidated.csv` after each scan.

| Column | Description |
|--------|-------------|
| `Left Folder` | Source subfolder name (if applicable) |
| `File Count` | Number of files in subfolder |
| `Left Panel File` | Filename or `[N files in folder/]` |
| `Series Name` | Extracted series name |
| `Action Type` | One of 5 action types |
| `Suggested Folder Name` | Destination folder path |
| `Right Panel Matches (Count)` | Count of matching dest items |
| `Has Existing Folder` | YES / NO |
| `Has Existing Files` | YES / YES(N) / NO |
| `Consolidation Strategy` | Human-readable action description |
| `Move Source` | LEFT or LEFT + RIGHT_FILES(N) |
| `Files Details` | Pipe-separated filenames (for subfolders) |
| `Right Loose Files` | Pipe-separated right-side filenames to co-move |

### FR7: Dry Run

- Preview all planned moves without touching any files
- Full output streamed to UI console in real time
- Shows source path → destination path for each file
- Errors reported but no files modified

### FR8: Execution

- Requires explicit user confirmation before proceeding
- Creates destination folders with `mkdir(parents=True, exist_ok=True)` — non-existent folder paths are safe
- Moves files with `shutil.move()`
- Deletes empty source subfolders after all files moved
- Saves execution log to `.logs/last_execution.json` for rollback

### FR9: Overrides

**Series name override:**
- Single row: triggers live re-match via `/api/rescan-series` endpoint
- Multiple rows (bulk): applies label only; user must re-run Scan to refresh matching

**Destination folder override:**
- Single or bulk: applied immediately to the data array
- Non-existent folder paths are allowed — created automatically on execution
- Persisted in `data[].destOverride` until page reload or rescan

### FR10: Web UI

- Three scrollable table sections: Source Folders, Consolidations, New Folders/Unmatched
- Per-section filtering: text search + dropdown filters (folder, move source)
- Bulk select via checkboxes; Select All / Deselect All per section
- Resizable columns (width persisted to `localStorage` per table)
- Console panel at bottom: collapsible, streams all scan/dry-run/consolidate output in real time
- Folder picker modals for source and destination paths (Browse tab + Enter Path tab)
- Details modal: full row data for any entry
- Edit modals: series name and destination folder per row or in bulk

---

## Non-Functional Requirements

### Safety
- No file is moved until user explicitly clicks Consolidate and confirms
- Dry Run always available as a preview step
- Execution log allows rollback (delete-only; originals not restored from backup)
- Atomic at the file level: each `shutil.move()` is independent; failure logged per file

### Reliability
- CSV acts as a durable intermediate state — tool can be closed and reopened without re-scanning
- Streaming output means the user sees progress even for large collections
- Subprocess isolation: scan and move run in separate processes; server remains responsive

### Usability
- Scan → Dry Run → Consolidate is the linear happy path
- All overrides survive until the next scan
- Toast notifications for save actions
- Column resizing persists across sessions

---

## Out of Scope

- Comic metadata enrichment (no ComicVine/OMDB integration)
- Comic file reading or viewing
- Cloud storage or remote destinations
- Multi-user access
- Undo/restore of moved files (rollback deletes destination only)
- Recursive source folder structures beyond one level of subfolders

---

## Constraints

- **Python 3.8+** with standard library only (no pip requirements)
- **Local filesystem only** — source and destination must be mounted paths
- **Single source/destination pair** per session
- **Browser**: Modern ES6 support (Chrome, Firefox, Safari, Edge)

---

**Version**: v2.5
**Last Updated**: 2026-05-13 14:00
