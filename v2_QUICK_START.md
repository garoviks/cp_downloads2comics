# Comic File Organizer v2.0 — Quick Start

## One-Minute Setup

```bash
cd /home/nesha/scripts/cp_downloads2comics/

# Terminal 1: Start the server
python3 serve_v2.py

# Terminal 2 (or new window): Open browser
xdg-open http://localhost:8123
```

That's it! The app is ready. 🎉

---

## The Workflow

### Step 1: Scan Folders
```
Click [🔍 Scan Folders]
         ↓
   Console opens at bottom
         ↓
   Shows: "Scanning folders..."
         ↓
   Table updates with plan
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
   Files are moved to destination
```

---

## Key Features

### Console Panel
- **Appears at bottom** when operations run
- **Shows real-time logs** as things happen
- **Color-coded** — green for success, red for errors
- **Scrollable** — read previous logs
- **Closes** when you click "Scan Folders" again

### Folder Picker
- **Source**: `/home/nesha/Downloads/comics_download/`
- **Destination**: `/mnt/extramedia/Comics/`
- Browse buttons ready for future enhancement

### Tables
- **Resizable columns** — drag borders
- **Search** — find files/series
- **Filter** — by folder status, move source
- **Select rows** — for batch operations
- **Edit destination** — change folder names

---

## Console Output Examples

### Scanning
```
🔍 Scanning folders...
Source: /home/nesha/Downloads/comics_download/
Destination: /mnt/extramedia/Comics/
⏳ Loading CSV from server...
✅ Loaded 65 rows from analysis
📊 Data ready: 65 files
✅ Scan complete
```

### Dry Run
```
📋 Starting dry-run analysis...
📁 Created folder: /mnt/extramedia/Comics/Feral/
   📄 Would move: Feral 021 (2024)...cbz
   📄 Would move: Feral 019 (2025)...cbr
   📄 Would move: Feral 020 (2026)...cbr
📊 Summary:
   Total operations: 1
   Files to move: 3
   Destination folders to ensure exist: 1
✅ Dry-run complete
```

### Consolidate
```
▶️ Starting file consolidation...
📁 Created folder: /mnt/extramedia/Comics/Feral/
   ✅ Moved: Feral 021 (2024)...cbz → Feral/
   ✅ Moved: Feral 019 (2025)...cbr → Feral/
   ✅ Moved: Feral 020 (2026)...cbr → Feral/
✅ Consolidation complete. 3 files moved.
```

---

## What's Different from v1.0

| | v1.0 | v2.0 |
|---|------|------|
| Start server | `python3 serve.py` | `python3 serve_v2.py` |
| Open page | `xdg-open http://...` | Same |
| View logs | Browser console (F12) | **Console panel** ✨ |
| Preview moves | Separate modal dialog | **In console** ✨ |
| Execute moves | Separate button | **"Consolidate!" button** ✨ |
| Feedback | Static after load | **Real-time streaming** ✨ |

---

## Troubleshooting

### Server won't start
```bash
# Check if port 8123 is already in use
lsof -i :8123

# Kill existing process
kill -9 <PID>

# Try again
python3 serve_v2.py
```

### Console panel doesn't show
1. Make sure server is running (`serve_v2.py`)
2. Click "Scan Folders" first (loads data)
3. Then click "Dry Run" or "Consolidate"

### Logs are empty
1. Check browser console (F12) for errors
2. Verify CSV file exists:
   ```bash
   ls -la matching_analysis_consolidated.csv
   ```
3. If missing, regenerate:
   ```bash
   python3 matching_analysis_generator.py
   ```

### Files not moving
- Make sure you click "Consolidate!", not "Dry Run"
- Check destination folder exists: `/mnt/extramedia/Comics/`
- Check permissions: `ls -la /mnt/extramedia/Comics/ | head`

---

## Button Reference

### Control Buttons
```
🔍 Scan Folders      → Load plan from both directories
📋 Dry Run...        → Preview moves (non-destructive)
✨ Consolidate!      → Execute actual file moves
♻️ Reload CSV         → Refresh data from CSV file
```

### Table Row Buttons
```
Details              → View all file information
Edit                 → Change destination folder
```

---

## Navigation

**Top of page:**
- Folder picker (Source / Destination)
- Control buttons
- Stats bar

**Main area:**
- Consolidations table (54 files with matches)
- New Folders table (12 files without matches)

**Bottom (when running):**
- Console panel with real-time logs
- Click ✕ or run "Scan Folders" to close

---

## Tips

### Optimize Views
1. **Resize columns** — Drag table headers to see full text
2. **Double-click borders** — Reset columns to default
3. **Use search** — Find specific files quickly
4. **Filter** — Show only certain file types

### Safe Workflow
1. **Always preview first** — Click "Dry Run..."
2. **Review console output** — Check what will happen
3. **Then execute** — Click "Consolidate!" with confidence

### Batch Operations
1. **Select multiple rows** — Check boxes
2. **Or Select All** — "Select All" button
3. When you generate script, only selected rows included

---

## Server Commands

```bash
# Start server
python3 serve_v2.py

# Stop server
# Press Ctrl+C in terminal

# Check if running
curl http://localhost:8123

# View logs (if saved)
cat .logs/last_execution.json
```

---

## File Locations

```
/home/nesha/scripts/cp_downloads2comics/
├── serve_v2.py                      (NEW server)
├── comic_organizer_v2.html          (NEW UI)
├── matching_analysis_generator.py   (existing)
├── comic_mover.py                   (existing)
├── matching_analysis_consolidated.csv
└── VERSION_2_RELEASE_NOTES.md       (detailed docs)
```

---

## Next Steps

### Try it now:
1. `python3 serve_v2.py`
2. Open http://localhost:8123
3. Click "Scan Folders"
4. Click "Dry Run..." (see what would happen)
5. Click "Consolidate!" (actually move files)

### Learn more:
- Read `VERSION_2_RELEASE_NOTES.md` for detailed info
- Check browser console (F12) for debug messages
- Review console logs while operations run

---

## Support

**If something doesn't work:**

1. **Check server is running** — You should see startup message in terminal
2. **Check browser console** — F12 → Console tab for JavaScript errors
3. **Check CSV exists** — Run `python3 matching_analysis_generator.py`
4. **Check folders exist** — Verify source and destination paths
5. **Restart everything** — Kill server, run new server, reload page

---

**Enjoy v2.0!** 🎉
