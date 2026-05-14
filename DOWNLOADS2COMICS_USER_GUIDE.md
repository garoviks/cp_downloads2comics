# Downloads2Comics — User Guide

**Current version: v2.6**

---

## Quick Start

### 1. Start the Server

```bash
cd /home/nesha/scripts/cp_downloads2comics
python3 serve_v2.py
```

### 2. Open in Browser

```
http://localhost:8123
```

### 3. Run the Workflow

1. Click **🔍 Scan Folders** — analyses source and destination, generates action plan
2. Review the three tables
3. Edit any mismatched series names or destination folders
4. Click **📋 Dry Run** — preview every move without touching files
5. Click **✨ Consolidate!** — execute the moves

---

## How It Works

The tool compares two sides:

- **Left (source):** your downloads folder — new comic files to be organized
- **Right (destination):** your comics library — the organized collection

It scans both sides, matches series names, and proposes one of five actions for each file or folder. The plan is saved as a CSV. You review and adjust, then execute.

```
Source                     Action              Destination
─────────────────────────────────────────────────────────
Saga 025.cbr           →  CONSOLIDATE      →  Saga (2012)/
New Series 001.cbr     →  CREATE_FOLDER    →  New Series/ (new)
Briar 003.cbr          →  CONSOLIDATE      →  Briar (2022)/
Old File.cbr           →  COPY_TO_BASE     →  /Comics/
```

---

## Workflow — Step by Step

### Step 1: Scan

Click **🔍 Scan Folders**. The console streams progress as the tool:
1. Scans source subfolders (treated as units)
2. Scans source loose files (grouped by series)
3. Scans the destination library
4. Matches each source item to a destination
5. Writes the CSV action plan

When done, the three tables populate automatically.

### Step 2: Review

Check the three sections (see below). Look for:
- Wrong series name extraction → Edit series name
- Wrong destination folder → Edit dest. folder
- COPY_TO_BASE items that should be consolidated → Edit dest. folder

### Step 3: Dry Run

Click **📋 Dry Run**. The console shows every planned move:
```
📄 Would move: Saga 025.cbr → /mnt/extramedia/Comics/Saga (2012)/
📄 Would move: New Series 001.cbr → /mnt/extramedia/Comics/New Series/
```
No files are touched. Review the output and go back to editing if needed.

### Step 4: Consolidate

Click **✨ Consolidate!** and confirm. The console streams real-time progress:
```
✅ CONSOLIDATE: Saga
   → Destination: /mnt/extramedia/Comics/Saga (2012)
     📄 MOVE: Saga 025.cbr
     ✅ Moved: Saga 025.cbr → Saga (2012)/
```

---

## Understanding the Tables

### Source Folders

Subfolders in the source directory. Each subfolder is treated as a unit — all files inside move together.

Click **▶** to expand a row and see individual files.

| Action | Meaning |
|--------|---------|
| `CONSOLIDATE_FOLDER` | Subfolder matched an existing destination folder — all files move there |
| `CREATE_FOLDER_FROM_FOLDER` | No match found — a new destination folder will be created from the subfolder name |

### Consolidations

Individual loose files that match an existing destination folder.

| Action | Meaning |
|--------|---------|
| `CONSOLIDATE` | File moves into an existing destination folder |
| `CREATE_FOLDER_WITH_FILES` | File + existing loose right-side files → new folder created for all of them |

### New Folders / Unmatched

Individual files with no destination match, or files that need a new folder.

| Action | Meaning |
|--------|---------|
| `CREATE_FOLDER_WITH_FILES` | 2+ files from same series → new folder created |
| `COPY_TO_BASE` | Single unmatched file → copied to base Comics/ directory (no folder) |

---

## Action Types Reference

| Action | Files moved | Destination | Folder created? |
|--------|-------------|-------------|-----------------|
| `CONSOLIDATE_FOLDER` | All files in source subfolder | Existing dest folder | No |
| `CREATE_FOLDER_FROM_FOLDER` | All files in source subfolder + right loose files | New folder | Yes |
| `CONSOLIDATE` | Single source file | Existing dest folder | No |
| `CREATE_FOLDER_WITH_FILES` | Source file(s) + right loose files | New folder | Yes |
| `COPY_TO_BASE` | Single source file | Base Comics/ directory | No |

**Right loose files:** files already sitting loose in the destination that belong to the same series. They get moved into the new folder along with the source files.

---

## Editing & Overrides

### Edit Series Name

Click **Edit series name** on any row.

- The series name controls how matching is done. If the tool extracted the wrong name, correct it here.
- **Single row:** saves the override and immediately rescans matching for that file — the action type and destination update live.
- **Multiple rows selected:** applies the name to all selected rows as a label only. **You must re-run Scan** (or Dry Run) for matching to refresh.

### Edit Destination Folder

Click **Edit dest. folder** on any row.

- Two input methods: **Browse** (folder picker dialog) or **Enter Path** (type the folder name directly)
- The folder name can be just the final folder name (e.g. `Saga (2012)`) or a full path
- If the folder does not exist yet, it will be created automatically on execution
- Updates apply immediately to the table

---

## Bulk Operations

1. Check multiple rows using the checkboxes on the left
2. Click **Edit series name** or **Edit dest. folder** on any of the checked rows
3. The modal title shows "... will apply to N rows"
4. Confirm — the change applies to all selected rows

**Select All / Deselect All** buttons are available per section.

The selected count shows in the stats bar.

---

## Filtering & Search

Each section has its own filter bar:

| Control | Applies to | Effect |
|---------|-----------|--------|
| Search box | All sections | Filter rows by series name (case-insensitive substring) |
| Folder filter | Consolidations | Filter by Has Existing Folder (YES / NO) |
| Move Source filter | Consolidations | Filter by LEFT / LEFT + RIGHT_FILES |

Filters are cleared when you reload the CSV or re-scan.

---

## Console Output

The console panel at the bottom streams all output. It opens automatically when an operation starts.

| Symbol | Meaning |
|--------|---------|
| ✅ | Success |
| 📄 | File operation |
| 📁 | Folder created |
| 🗑️ | Empty folder deleted |
| ❌ | Error |
| ⚠️ | Warning |

To close: click **✕** in the console header.

---

## Dry Run vs Consolidate

| | Dry Run | Consolidate |
|-|---------|-------------|
| Files moved | Never | Yes |
| Folders created | Never | Yes |
| Overrides applied | Yes (preview) | Yes (execution) |
| Safe to run multiple times | Yes | Caution — files move |
| Use when | Reviewing the plan | Ready to execute |

Always run a Dry Run before Consolidate on a large batch.

---

## Rollback

Every Consolidate execution saves a log to:
```
/home/nesha/scripts/cp_downloads2comics/.logs/last_execution.json
```

To roll back the last execution (deletes destination files — does **not** restore source):
```bash
python3 comic_mover.py --rollback
```

> **Note:** Rollback removes destination files only. Source files are not restored from a backup. Use with care.

---

## Troubleshooting

**File not showing in any table after scan**
- Check if the filename matches a `SKIP_PATTERNS` entry (`sha 01`, `the bank`, `the owl`, `the owl`)
- Verify the file has a comic extension: `.cbz`, `.cbr`, `.zip`, `.rar`

**Wrong series name extracted**
- Use **Edit series name** → type the correct name → the tool rescans matching live

**File shows as COPY_TO_BASE but should consolidate**
- The series name didn't match any destination folder
- Use **Edit series name** or **Edit dest. folder** to point it at the right folder
- Or add the series to `SPECIFIC_SERIES_FOLDERS` in `matching_analysis_generator.py` if it recurs

**Subfolder not detected**
- Only direct subfolders of the source directory are treated as units
- Nested subfolders (source/sub/sub/) are not supported — files inside are treated as loose files

**Bulk series edit didn't update matching**
- Bulk series edits are label-only — run **🔍 Scan Folders** again to refresh matching with the new names

**Console shows no output after clicking Scan/Dry Run**
- Verify the server is running: `python3 serve_v2.py`
- Check the terminal running the server for error messages

---

## Version History

### v2.6 (2026-05-13)
- ComicVine metadata integration planned (Phase 2) — series name validation and matching assistance
- UI version string bumped to v2.6

### v2.5 (2026-05-13)
- Fixed year range extraction: `(2019-2024)` now correctly parsed as a range, not two years
- Fixed consolidation path accuracy: uses actual folder names instead of extracted series keys
- Removed risky FIRST_WORD matching that caused unrelated series to be merged together
- Fixed COPY_TO_BASE action ignoring destination folder overrides
- Fixed SKIP_PATTERNS using substring matching instead of full series name matching (false positives on e.g. "Owlhen")

### v2.4
- Multi-select bulk editing: apply series name or destination folder to multiple rows at once
- Folder picker modals for source and destination paths (Browse + Enter Path tabs)
- Resizable columns with localStorage persistence
- `/api/scan` accepts custom src/dest from UI

### v2.3
- Recursive source scanning: picks up files in subfolders
- `/api/rescan-series` endpoint for live single-row re-matching

### v2.2
- Two-pass source scanning: subfolders first, then loose files
- Subfolder-level consolidation (CONSOLIDATE_FOLDER, CREATE_FOLDER_FROM_FOLDER)

### v2.1
- Right loose files detection and co-moving (CREATE_FOLDER_WITH_FILES)
- Rollback log

### v2.0
- Complete rewrite: new matching engine, streaming API, web UI
- 5 action types

### v1.0
- Initial version: basic file scanning and CSV generation

---

**Version**: v2.6
**Last Updated**: 2026-05-13 14:00
**Server**: `serve_v2.py` (port 8123)
**UI**: `comic_organizer_v2.html`
