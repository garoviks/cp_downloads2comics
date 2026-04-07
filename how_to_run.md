# Comic File Organizer — How to Run

Complete guide for running the Comic File Organizer on Linux/Ubuntu with Python3.

---

## Overview

The system consists of three components:

1. **CSV Generator** (`matching_analysis_generator.py`) — Analyzes directories and creates CSV
2. **Web Server** (`serve.py`) — Serves HTML page and provides CSV API
3. **Web Page** (`comic_organizer.html`) — Interactive UI to review and plan moves
4. **Move Script** (`comic_mover.py`) — Executes file moves

---

## Prerequisites

- Linux/Ubuntu 20+
- Python 3.6+
- Directories exist:
  - `/home/nesha/Downloads/comics_download/` (source)
  - `/mnt/extramedia/Comics/` (destination)

---

## Workflow

### Step 1: Generate Matching Analysis CSV

```bash
cd /home/nesha/scripts/cp_downloads2comics/
python3 matching_analysis_generator.py
```

**Output:**
- `matching_analysis_consolidated.csv` — 66 rows (54 consolidations + 12 new folders)
- Summary statistics in console
- List of unmatched series

**Time:** ~5 seconds for 72 source files + 5975 destination items

---

### Step 2: Start Web Server

Open a terminal and keep it running:

```bash
cd /home/nesha/scripts/cp_downloads2comics/
python3 serve.py
```

**Output:**
```
🌐 Comic Organizer Web Server
=====================================================================
📂 CSV File: /home/nesha/scripts/cp_downloads2comics/matching_analysis_consolidated.csv
📄 HTML File: /home/nesha/scripts/cp_downloads2comics/comic_organizer.html

🚀 Starting server on http://localhost:8888
   Open browser: http://localhost:8888
   To stop: Press Ctrl+C
=====================================================================
```

The server stays running. Open a new terminal for the next steps.

---

### Step 3: Open Web Page

In a new terminal (or direct browser):

```bash
xdg-open http://localhost:8888
```

Or manually open browser to: `http://localhost:8888`

**Features:**
- View 54 consolidation entries with match counts
- View 12 new folder entries needing creation
- Search/filter by series or filename
- Resizable columns (drag column borders, double-click to reset)
- View Details button — see all row data in modal
- Edit Dest button — change destination folder path
- Preview Moves button — see list of all planned operations
- Generate Script button — create executable Python script
- Export Report button — download CSV copy

---

### Step 4: Review and Plan

1. **Browse consolidations & new folders**
   - Read "Consolidation Strategy" to understand what will happen
   - Check "Move Source" (always `LEFT` — only source files, no destination touches)
   - Look for "Has Existing Folder" and "Has Existing Files" to understand destination state

2. **Search/filter** (optional)
   - Filter consolidations by: "Has Folder" status, "Move Source" type
   - Search by series name or filename

3. **Adjust destinations** (optional)
   - Click "Edit Dest" to change folder name for any row
   - Changes are temporary (stored in browser session)
   - Click "Save" to confirm

4. **Preview all moves**
   - Click "Preview Moves" button
   - Shows all planned file operations
   - Lists source path → destination path for each file
   - Conservative approach — preview before executing

---

### Step 5: Refresh CSV (if needed)

After updating CSV:

```bash
python3 matching_analysis_generator.py
```

Then refresh browser (F5 or Ctrl+R) to see updated data. No server restart needed.

---

### Step 6: Generate Move Script (Optional)

In the web page:

1. **Select rows** (optional)
   - Use checkboxes to select specific rows
   - Or "Select All" to include everything
   - Stat shows selected count

2. **Click "Generate Script"**
   - Creates Python script for file moves
   - Shows in modal with copy/download options
   - Safe to save and run manually

3. **Download or copy**
   - "Copy Script" — copies to clipboard
   - "Download .py" — saves `comic_move.py` file

---

### Step 7: Execute Moves

Use the command-line move script for actual execution:

```bash
cd /home/nesha/scripts/cp_downloads2comics/
python3 comic_mover.py --dry-run
```

**Shows preview without making any changes.**

If preview looks good:

```bash
python3 comic_mover.py --execute
```

**Will ask for confirmation before proceeding.**

---

## Command Reference

### CSV Generation

```bash
python3 matching_analysis_generator.py
```

Scans both directories, extracts series names, performs exact/fuzzy matching, writes CSV.

**Output file:** `matching_analysis_consolidated.csv`

---

### Web Server

```bash
python3 serve.py
```

Starts HTTP server on port 8888. Serves HTML and provides CSV API endpoint.

**Keep this running while using the web page.**

**Stop:** Press Ctrl+C

---

### Move Operations

```bash
# Preview only (safe)
python3 comic_mover.py --dry-run

# Execute with confirmation prompt
python3 comic_mover.py --execute

# Execute without confirmation (use with caution!)
python3 comic_mover.py --execute --no-confirm

# Undo last execution
python3 comic_mover.py --rollback
```

---

## Strategy Explanation

Each CSV row shows:

| Column | Meaning |
|--------|---------|
| **Left Panel File** | Source file from downloads |
| **Series Name** | Extracted series name |
| **Action Type** | `CONSOLIDATE` (has matches) or `CREATE_FOLDER` (new) |
| **Destination Folder** | Where file will go in `/mnt/extramedia/Comics/` |
| **Right Panel Matches** | Count of matching items found in destination |
| **Has Existing Folder** | YES = destination folder already exists |
| **Has Existing Files** | YES = individual matching files in destination |
| **Consolidation Strategy** | Human-readable description |
| **Move Source** | Always `LEFT` (only move source files, don't touch destination) |

---

## Example: 2000AD prog 2476

```
Left Panel File:  2000AD prog 2476 (2026) (4320p) (juvecube).cbz
Series Name:      2000AD prog 2476
Action:           CONSOLIDATE
Destination:      /2000AD/
Matches:          1
Has Folder:       YES
Strategy:         Move left file into /2000AD/ folder
Move Source:      LEFT
```

**What happens:**
1. Destination folder `/mnt/extramedia/Comics/2000AD/` exists
2. Source file is copied there
3. Existing files in `/2000AD/` are **NOT touched**
4. Result: Both files in same folder

---

## All-in-One Quick Start

```bash
# Terminal 1: Start server (keep running)
cd /home/nesha/scripts/cp_downloads2comics/
python3 serve.py &

# Terminal 2: Generate CSV
python3 matching_analysis_generator.py

# Terminal 2: Open web page
xdg-open http://localhost:8888

# Terminal 2: After reviewing, preview moves
python3 comic_mover.py --dry-run

# Terminal 2: If good, execute
python3 comic_mover.py --execute
```

---

## Troubleshooting

### "CSV file not found"
- Run `matching_analysis_generator.py` first
- Check file exists: `ls matching_analysis_consolidated.csv`

### "Source directory not found"
- Check `/home/nesha/Downloads/comics_download/` exists
- Check permissions: `ls /home/nesha/Downloads/comics_download/`

### "Destination directory not found"
- Check `/mnt/extramedia/Comics/` exists
- Check permissions: `ls /mnt/extramedia/Comics/`

### Web page shows old data
- Refresh browser (F5 or Ctrl+R)
- Make sure server (`serve.py`) is still running
- Check browser console (F12) for errors

### Port 8888 already in use
- Find process: `lsof -i :8888`
- Kill it: `kill -9 <PID>`
- Or edit `serve.py` to use different port

### Move script fails
- Check file permissions: `ls -la /home/nesha/Downloads/comics_download/`
- Check destination writable: `touch /mnt/extramedia/Comics/test.txt && rm /mnt/extramedia/Comics/test.txt`
- Review error message in `--dry-run` output

---

## Key Principles

✅ **Conservative approach**
- Preview first with `--dry-run`
- Confirm before executing
- Rollback available if needed

✅ **Only moves LEFT files**
- Source files from downloads copied to destination
- Existing destination folders/files **never touched**
- Safe for re-running if something fails

✅ **No auto-execution**
- CLI prompts for confirmation
- Web UI shows preview before generating script
- User runs script manually

✅ **Traceable operations**
- Execution logged to `.logs/last_execution.json`
- Can rollback with `--rollback`
- All operations visible in preview

---

## File Structure

```
/home/nesha/scripts/cp_downloads2comics/
├── how_to_run.md                              (this file)
├── matching_analysis_generator.py             (CSV generator)
├── serve.py                                   (web server)
├── comic_organizer.html                       (web UI)
├── comic_mover.py                             (move executor)
├── matching_analysis_consolidated.csv         (output)
└── .logs/
    └── last_execution.json                    (rollback data)
```

---

## Support

For issues or questions, check:
1. Console output of each script
2. Browser console (F12) for web page errors
3. File paths and permissions
4. Ensure Python 3.6+

All scripts are self-contained. No external dependencies required.
