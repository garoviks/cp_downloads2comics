# Downloads2Comics — Architecture

**Current version: v2.5**

## System Overview

Downloads2Comics is a client-server web application. The browser UI drives three backend components via a streaming HTTP API.

```
┌─────────────────────────┐
│   User Browser          │
│ (comic_organizer_v2     │
│  .html)                 │
│                         │
│  • 3-section UI         │
│  • State management     │
│  • Override editing     │
│  • Console streaming    │
└──────────┬──────────────┘
           │ HTTP
           │
┌──────────▼──────────────────────────┐
│ serve_v2.py (port 8123)             │
│                                     │
│  GET  /              → HTML         │
│  GET  /api/csv       → JSON         │
│  POST /api/scan      → stream       │
│  POST /api/dry-run   → stream       │
│  POST /api/consolidate → stream     │
│  POST /api/rescan-series → JSON     │
└──────┬────────────┬─────────────────┘
       │ subprocess │ subprocess
       ▼            ▼
matching_analysis   comic_mover.py
_generator.py       • plan_moves()
• scan source       • execute_moves()
• scan dest         • dry_run output
• match + strategy  • rollback
• write CSV         • override apply
       │            │
       └─────┬──────┘
             ▼
        Filesystem
  /home/nesha/Downloads/
  comics_download/        ← source
  /mnt/extramedia/Comics/ ← destination
```

---

## Technology Stack

### Backend
- **Language**: Python 3.8+
- **Web Framework**: `http.server.BaseHTTPRequestHandler` (stdlib)
- **File Operations**: `os`, `shutil`, `pathlib`
- **Subprocess**: `subprocess.Popen` with stdout streaming
- **Data**: CSV (`csv.DictReader/DictWriter`), JSON, temp files via `tempfile`

### Frontend
- **Markup**: HTML5
- **Styling**: CSS3 with hardcoded colour variables
- **Scripting**: Vanilla JavaScript ES6+ (no frameworks)
- **Storage**: `localStorage` for column widths
- **Protocol**: HTTP/1.1, text/event-stream for streaming

---

## Data Flow

### Scan Flow

```
User clicks [🔍 Scan Folders]
       ↓
POST /api/scan { src_dir, dest_dir }
       ↓
serve_v2.py: subprocess Popen
  python3 matching_analysis_generator.py --src X --dest Y
       ↓
  scan_source_subfolders()   ← Pass 1: folders
  scan_source_directory()    ← Pass 2: loose files
  scan_destination_directory()
       ↓
  find_matches() per file → generate_consolidation_strategy()
       ↓
  Write CSV
       ↓
Stream lines to browser console
       ↓
Frontend: GET /api/csv → data[] populated → renderAll()
```

### Dry Run Flow

```
User clicks [📋 Dry Run]
       ↓
buildOverrides() → collect destOverride / seriesOverride from data[]
       ↓
POST /api/dry-run { overrides: [...] }
       ↓
serve_v2.py: write overrides to /tmp/overrides_XXXX.json
  subprocess: python3 comic_mover.py --dry-run --overrides TMP
       ↓
comic_mover.py: read CSV + apply overrides → plan_moves()
  print "Would move: src → dst" per file
       ↓
Stream to console — no files touched
       ↓
finally: os.unlink(tmp_file)
```

### Consolidate Flow

```
User clicks [✨ Consolidate!] → confirm dialog
       ↓
buildOverrides()
       ↓
POST /api/consolidate { overrides: [...] }
       ↓
serve_v2.py: write overrides → subprocess comic_mover.py --execute --no-confirm --overrides TMP
       ↓
comic_mover.py:
  plan_moves() → for each operation:
    mkdir(dest, parents=True, exist_ok=True)
    shutil.move(src, dst) per file
    rmdir source subfolder if empty
       ↓
save_execution_log() → .logs/last_execution.json
       ↓
Stream output to console
```

---

## Component Architecture

### 1. `serve_v2.py` — HTTP Server

**Port:** 8123

#### Endpoints

**`GET /`**
- Serves `comic_organizer_v2.html`

**`GET /api/csv`**
- Reads CSV with `csv.DictReader`
- Converts `Right Panel Matches (Count)` to int
- Returns JSON array of row objects

**`POST /api/scan`**
```json
Request:  { "src_dir": "/path", "dest_dir": "/path" }
Response: text/event-stream — progress lines from subprocess stdout
```
- Runs `matching_analysis_generator.py --src --dest` as subprocess
- Streams stdout line-by-line to client

**`POST /api/dry-run`**
```json
Request:  { "overrides": [{ "left_file": "...", "series_name": "...", "dest_folder": "..." }] }
Response: text/event-stream
```
- Writes overrides JSON to temp file
- Runs `comic_mover.py --dry-run --overrides TMP`
- Cleans up temp file in `finally`

**`POST /api/consolidate`**
```json
Request:  { "overrides": [...] }  (same shape as dry-run)
Response: text/event-stream
```
- Same as dry-run but runs `comic_mover.py --execute --no-confirm --overrides TMP`

**`POST /api/rescan-series`**
```json
Request:  { "left_file": "filename.cbr", "new_series": "New Series Name" }
Response: { "Series Name": "...", "Action Type": "...", "Suggested Folder Name": "...", ... }
```
- Subprocess calls `find_matches()` + `generate_consolidation_strategy()` directly
- Subprocess prints `RESCAN_JSON:<json>` which server parses and returns

**Streaming Implementation:**
```python
proc = subprocess.Popen(cmd, stdout=PIPE, stderr=STDOUT, text=True)
for line in proc.stdout:
    self.wfile.write(line.encode())
    self.wfile.flush()
```

---

### 2. `matching_analysis_generator.py` — Analysis Engine

#### Key Constants

```python
COMIC_EXTS      = {'.cbz', '.cbr', '.zip', '.rar'}
SKIP_PATTERNS   = {"comics_download.txt", "sha 01", "the bank", "the owl"}
VOLUME_PATTERN  = r'\b(?:v|vol|book|t)\.?\s*\d+|TPB|Omnibus|...'
ISSUE_PATTERN   = r'\s+#?\d+(?:\s*\(of\s*\d+\))?|\s+\(\d{1,3}\)'
YEAR_PATTERN    = r'\((\d{4}(?:-\d{4})?)\)'
SPECIFIC_SERIES_FOLDERS = {"Billy & Buddy", "Gomer Goof"}
PUBLISHER_FOLDERS       = {"Cinebook (Europe)", "Fantagraphics (Europe)", ...}
```

#### Key Functions

**Parsing:**
- `parse_filename(filename)` — extract series, subtitle, year from filename; strips volume/issue/year patterns
- `normalize_name(name)` — lowercase, remove articles/volumes/years for loose comparison
- `extract_folder_series_name(folder_name)` — strip year ranges, volume info from folder name

**Scanning:**
- `scan_source_subfolders()` — Pass 1: subfolders as units; EXACT folder match only
- `scan_source_directory()` — Pass 2: loose files grouped by series
- `scan_destination_directory()` — builds `dest_map` with `folders`, `files_in_folders`, `loose_files` per series

**Matching (in priority order):**
- `find_specific_series_match(filename, dest_map)` — rule 1: SPECIFIC_SERIES_FOLDERS substring
- `find_publisher_match(filename, dest_map)` — rule 2: publisher keyword
- `find_exact_match(src_series, dest_map)` — rule 3A: case-insensitive name; only if dest has folder OR loose_files
- `find_fuzzy_match(src_series, dest_map)` — rule 3B: substring containment; dest must have actual folder
- `find_matches(src_filename, src_series, dest_map)` — orchestrates rules 1–4; returns `(folder, data, confidence)`

**Strategy:**
- `generate_consolidation_strategy(src_filename, src_series, matched_series, match_data, confidence, remaining_files_count)` — maps match result → action type → CSV row dict

**CSV:**
- `write_csv(rows)` — writes 13-column CSV to `{SRC_DIR}/matching_analysis_consolidated.csv`

---

### 3. `comic_mover.py` — Execution Engine

#### CLI Modes

```bash
python3 comic_mover.py --dry-run
python3 comic_mover.py --execute [--no-confirm]
python3 comic_mover.py --rollback
python3 comic_mover.py --overrides /tmp/overrides_XXXX.json
```

#### Data Classes

```python
class Move:
    src: Path
    dst: Path
    move_type: str      # "FILE" or "FOLDER"
    executed: bool
    error: str | None

class MoveOperation:
    row: Dict           # CSV row
    series_name: str
    dest_folder: str
    moves: List[Move]
    skipped_reason: str | None
    source_subfolder: Path | None   # for empty-folder cleanup
```

#### Key Functions

- `read_csv()` — load and filter CSV rows
- `plan_moves(rows)` — build `List[MoveOperation]` from CSV rows + overrides
  - Folder actions: parse `Files Details` column for individual filenames
  - File actions: resolve source path, collect right loose files
  - Both: attach right loose files as additional Move objects
- `execute_moves(operations, dry_run)` — iterate operations:
  - `mkdir(dest, parents=True, exist_ok=True)`
  - `shutil.move(src, dst)` per Move
  - `rmdir` source subfolder if empty
- `save_execution_log(operations)` — write `.logs/last_execution.json`
- `rollback()` — read log, delete each executed destination file

#### Override Processing

Overrides JSON loaded before `plan_moves()`:
```json
[{ "left_file": "file.cbr", "series_name": "Override Name", "dest_folder": "Override Folder" }]
```
Applied by patching `Series Name` and `Suggested Folder Name` columns in the row dict before strategy resolution.

---

### 4. `comic_organizer_v2.html` — Web UI

#### State Management

```javascript
const data = [];            // Array of row objects (one per CSV row)
let _editId = null;         // Row ID currently being edited in modal
```

**Row object structure:**
```javascript
{
    id: 0,
    leftFile: "file.cbr",
    series: "Series Name",
    action: "CONSOLIDATE",
    folder: "/dest/folder",
    strategy: "Move left file...",
    matches: 5,
    hasFolder: "YES",
    hasFiles: "YES(3)",
    moveSource: "LEFT",
    destOverride: null,         // user-set destination folder
    seriesOverride: undefined,  // user-set series name
    // ...all CSV columns preserved
}
```

#### UI Sections

1. **Source Folders** — rows from Pass 1 (subfolders); expandable (▶) to show individual files
2. **Consolidations** — CONSOLIDATE and CREATE_FOLDER_WITH_FILES rows (file → existing dest)
3. **New Folders / Unmatched** — CREATE_FOLDER_FROM_FOLDER, CREATE_FOLDER_WITH_FILES (new), COPY_TO_BASE

#### Key Functions

**Rendering:**
- `renderAll()` — renders all three sections
- `renderFolders(rows)`, `renderConsolidate(rows)`, `renderNewfolder(rows)` — per-section render
- `getRows(section)` — returns filtered rows for section

**API calls:**
- `scanFolders()` — POST /api/scan → stream → GET /api/csv → renderAll()
- `dryRun()` — buildOverrides() → POST /api/dry-run → stream
- `consolidate()` — confirm → buildOverrides() → POST /api/consolidate → stream
- `reloadCSV()` — GET /api/csv → renderAll()

**Overrides:**
- `buildOverrides()` — collect all `destOverride` / `seriesOverride` from `data[]`
- `saveDestination()` — set `destOverride` on row(s); renderAll()
- `saveSeriesName()` — set `seriesOverride`; for single row call /api/rescan-series

**Selection:**
- `updateSelected()` — recount checked rows, update stats badge
- `toggleAllInSection(section, checked)` — bulk select/deselect
- `getSelectedIds()` — return array of checked row IDs

**Modals:**
- `openDetails(id)` — full row data grid
- `openEditDest(id)` — destination folder override (browse + text tabs)
- `openEditSeries(id)` — series name override (single: rescan; bulk: label only)

**Utilities:**
- `effectiveFolder(row)` — `row.destOverride || row.folder`
- `toast(msg)` — temporary notification bottom-right
- `initializeColumnResizing(tableId)` — drag-to-resize with localStorage persistence

#### Bulk Edit Logic

1. User checks N rows
2. Clicks Edit on any row
3. Modal title: "... will apply to N rows"
4. On save:
   - If clicked row is in selection AND N > 1 → apply to all selected
   - Otherwise → apply to clicked row only
5. Series bulk edit: no live rescan (label only); dest bulk edit: immediate renderAll()

---

## Cross-Component Dependencies

| Consumer | Depends on | Producer | What breaks if wrong |
|----------|-----------|----------|----------------------|
| `comic_mover.py` override apply | `buildOverrides()` returns `left_file` matching exactly the `Left Panel File` CSV column value | `comic_organizer_v2.html` — `data[].leftFile` must be the raw CSV value | Overrides silently ignored; wrong series/dest used |
| `find_exact_match()` | `dest_map` entry has `folders` or `loose_files` (not just `files_in_folders`) | `scan_destination_directory()` — must distinguish file locations correctly | Files in existing folders cause wrong EXACT matches |
| `CREATE_FOLDER_FROM_FOLDER` right-file moves | Right loose files read from CSV `Right Loose Files` column at move time | `matching_analysis_generator.py` — must write correct filenames to column at scan time | Right-side loose files not moved into new folder |
| Subfolder EXACT match safety | No fuzzy/first-word matching for subfolders | `find_folder_match()` — must use EXACT only | Unrelated series (e.g. "Broken Eye" ↔ "Broken Pieces") merged together |
| `comic_mover.py` folder cleanup | Source subfolder stored in `MoveOperation.source_subfolder` | `plan_moves()` — must set this field for folder-level actions | Empty source subfolders not deleted after move |
| Year range extraction in dest keys | `(2019-2024)` extracted as a year range, not two separate years | `scan_destination_directory()` `YEAR_PATTERN = r'\((\d{4}(?:-\d{4})?)\)'` | Year-range destination folders not matched; CREATE instead of CONSOLIDATE |

---

## API Specification

### GET /api/csv

**Response (200):**
```json
[
  {
    "Left Panel File": "Series 001.cbr",
    "Series Name": "Series",
    "Action Type": "CONSOLIDATE",
    "Suggested Folder Name": "Series (2022)",
    "Right Panel Matches (Count)": 3,
    "Has Existing Folder": "YES",
    "Has Existing Files": "YES(2)",
    "Consolidation Strategy": "Move left file into existing folder...",
    "Move Source": "LEFT",
    "Files Details": "",
    "Right Loose Files": ""
  }
]
```

### POST /api/scan

**Request:**
```json
{ "src_dir": "/home/nesha/Downloads/comics_download", "dest_dir": "/mnt/extramedia/Comics" }
```
**Response:** `text/event-stream` — progress lines

### POST /api/dry-run / POST /api/consolidate

**Request:**
```json
{
  "overrides": [
    { "left_file": "Series 001.cbr", "series_name": "Correct Series", "dest_folder": "Correct Series (2022)" }
  ]
}
```
**Response:** `text/event-stream` — move preview or execution output

### POST /api/rescan-series

**Request:**
```json
{ "left_file": "Series 001.cbr", "new_series": "Correct Series Name" }
```
**Response:**
```json
{
  "Series Name": "Correct Series Name",
  "Action Type": "CONSOLIDATE",
  "Suggested Folder Name": "Correct Series (2022)",
  "Right Panel Matches (Count)": 1,
  "Has Existing Folder": "YES",
  "Has Existing Files": "NO",
  "Consolidation Strategy": "Move left file into existing folder...",
  "Move Source": "LEFT"
}
```

---

## Known Limitations

1. **Single source/destination pair** — one scan covers one pair; no queue
2. **No parallel execution** — moves are sequential; large collections take time
3. **Rollback is delete-only** — removes destination files; does not restore source structure
4. **CSV is the only state** — overrides are lost on page reload (not written back to CSV until next scan)
5. **Subfolder depth** — only direct subfolders of source are treated as units; deeper nesting is flattened
6. **Bulk series edit requires re-scan** — matching not refreshed live for multi-row series overrides

---

**Version**: v2.5
**Last Updated**: 2026-05-13 14:00
