# Comic File Organizer v2.2 — Quick Start

## One-Minute Setup

```bash
cd /home/nesha/scripts/cp_downloads2comics/
python3 serve_v2.py
# Then open http://localhost:8123 in browser
```

---

## The Workflow

### Step 1: Scan Folders
```
Click [🔍 Scan Folders]
         ↓
   Regenerates CSV from current filesystem
         ↓
   Console shows progress
         ↓
   Tables update with fresh data
```

### Step 2: Preview
```
Click [📋 Dry Run...]
         ↓
   Console shows what would happen
         ↓
   No files are moved (safe preview)
```

### Step 3: Execute
```
Click [✨ Consolidate!]
         ↓
   Confirmation popup
         ↓
   Console shows moves happening
         ↓
   Files moved, empty source folders deleted
```

---

## Three Table Sections

### 1. Source Folders
Files organized in subfolders on the left side.
- Click **▶** to expand and see individual files
- Left files shown in teal, right loose files in green
- Action: CONSOLIDATE (into existing right folder) or CREATE FOLDER (new folder)

### 2. Consolidations
Individual loose files that match an existing right-side folder.

### 3. New Folders / Unmatched
Individual loose files with no existing match — creates new folder or moves to base.

---

## What Gets Moved

### Folder operations (Source Folders section):
- All files from source subfolder → destination folder (flattened)
- If creating new folder: also picks up matching loose right-side files
- Empty source subfolder deleted after move

### File operations (Consolidations / New Folders):
- Single file moves
- May include matching loose right-side files

---

## Console Output Colors
- 🔵 Info (blue) — general progress
- ✅ Success (green) — successful moves
- ❌ Error (red) — failures
- ⚠️ Warning (yellow) — skipped items

---

## Troubleshooting

### Files not showing after Scan
- Always click **Scan Folders** first (not just Reload CSV)
- Scan regenerates the CSV from actual filesystem state

### Source folder shows as CREATE instead of CONSOLIDATE
- No matching folder found on right side
- System will create a new folder at destination

### File appears in Source Folders section but not Consolidations
- It's being handled at folder level (whole subfolder moves together)

---

## File Locations
```
/home/nesha/scripts/cp_downloads2comics/
├── serve_v2.py                      (HTTP server)
├── comic_organizer_v2.html          (Web UI)
├── matching_analysis_generator.py   (Analysis engine)
├── comic_mover.py                   (Execution engine)
└── Claude.md                        (Architecture notes for Claude)

/home/nesha/Downloads/comics_download/
└── matching_analysis_consolidated.csv  (Generated CSV — lives here)
```
