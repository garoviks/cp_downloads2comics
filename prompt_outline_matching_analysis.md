# Prompt Outline: Generate matching_analysis_consolidated.csv

## High-Level Goal
Create a Python script that scans two directories (source and destination), matches comic files by series name, identifies consolidation opportunities, and generates a CSV report with move/consolidation strategies.

---

## Input Parameters
```python
SRC_DIR = Path("/home/nesha/Downloads/comics_download/")
DEST_DIR = Path("/mnt/extramedia/Comics")
```

---

## Series Name Extraction Logic

### Algorithm
1. **Remove file extensions**: `.cbr`, `.cbz`, `.zip`, `.encrypted.part`, `.txt`
2. **Remove metadata patterns** (in order):
   - Year and everything after: `(\d{4}).*$`
   - Format info: `(digital|Digital|webrip|Webrip).*$`
3. **Extract FIRST PART** (before hyphens or issue numbers):
   - Pattern: `^([^-\d]+?)(?:\s*-|\s+\d|\s*\()`
   - If pattern matches, take group 1 and strip whitespace
   - If no pattern match, use entire cleaned name
4. **Result**: Series name (e.g., "Astro Quantum", "Babs", "Feral")

### Examples
- `Astro Quantum 003 (of 005) (2026) (Limited Series)...` → `Astro Quantum`
- `Babs - The Black Road South 003 (2026) (Digital)...` → `Babs`
- `Feral 021 (2024) (Series)...` → `Feral`
- `2000AD prog 2476 (2026)...` → `2000AD prog 2476`

---

## Matching Strategy

### Phase 1: Scan Source Directory
**Input**: `/home/nesha/Downloads/comics_download/`
- List all files (not directories)
- Extract series name from each file
- Store: `{series_name: [file_list]}`
- Skip metadata files: `comics_download.txt`, `sha`, `the bank`, `the owl`

### Phase 2: Scan Destination Directory
**Input**: `/mnt/extramedia/Comics`
- Recursively scan ALL items (files + folders)
- Extract series name from each item
- Track: `{series_name: {folders: [...], files: [...]}}`
- Identify if series has existing folder, existing files, or both

### Phase 3: Exact Matching
For each SOURCE series:
1. Look for EXACT match in DEST by series name (case-insensitive)
2. If found, collect ALL matching items from destination
3. Store match confidence: `EXACT`

### Phase 4: Fuzzy Matching (Fallback)
For unmatched source series (only if > 5 characters):
1. Check if source series appears in any DEST series name (substring)
2. Check if DEST series appears in source series name
3. Require DEST series to be > 3 characters (avoid single-letter false positives)
4. Store match confidence: `FUZZY`

### Phase 5: Consolidation Strategy Assignment
For each SOURCE file with matches:
- **Action Type**: `CONSOLIDATE`
- **Suggested Folder Name**: Use source series name (or refined version)
- **Right Panel Matches**: Count of matching files + folders in destination
- **Has Existing Folder**: Boolean (check if folder exists in dest)
- **Has Existing Files**: Boolean (check if individual files exist in dest)
- **Consolidation Strategy**: Text description of what to do
- **Move Source**: List what to move (LEFT + RIGHT_FILES + RIGHT_FOLDER combinations)

For unmatched SOURCE files:
- **Action Type**: `CREATE_FOLDER`
- **Suggested Folder Name**: Series name
- **Right Panel Matches**: 0
- **Has Existing Folder**: False
- **Has Existing Files**: False
- **Consolidation Strategy**: `Create new folder /SeriesName/`
- **Move Source**: `LEFT`

---

## Output CSV Structure

### Columns
1. `Left Panel File` - Full filename from source directory
2. `Series Name` - Extracted series name
3. `Action Type` - `CONSOLIDATE` or `CREATE_FOLDER`
4. `Suggested Folder Name` - Proposed destination folder path
5. `Right Panel Matches (Count)` - Number of matching items in destination
6. `Has Existing Folder` - `YES` or `NO`
7. `Has Existing Files` - `YES` or `NO` (count in parentheses if yes)
8. `Consolidation Strategy` - Human-readable description
9. `Move Source` - What to move (e.g., `LEFT + RIGHT_FILES(3)`, `LEFT + RIGHT_FOLDER`)

### Row Types
- **Consolidation rows** (54 files): Source file has matches in destination
- **New Folder rows** (12 files): Source file has no matches

### Example Rows

#### Consolidation Example
```
Astro Quantum 003 (of 005) (2026) (Limited Series) (Mad Cave Studios) (Digital) (LeDuch).cbz,
Astro Quantum,
CONSOLIDATE,
/Astro Quantum/,
2,
NO,
YES (2),
Create /Astro Quantum/ and move all 3 files into it,
LEFT + RIGHT_FILES(2)
```

#### New Folder Example
```
Amazonia 04 (Cinebook 2025) (webrip) (MagicMan-DCP).cbr,
Amazonia,
CREATE_FOLDER,
/Amazonia/,
0,
NO,
NO,
Create new folder /Amazonia/,
LEFT
```

---

## Expected Results

### Summary Statistics
- **Total Left Panel Files**: ~72
- **Files with Consolidation Matches**: ~54
- **Files Needing New Folders**: ~12
- **Right Panel Items Scanned**: ~5975

### Consolidation Categories
- **Files only**: X count (move individual files to series folder)
- **Folders only**: Y count (consolidate existing folder)
- **Files + Folders**: Z count (both)
- **Exact matches**: X count
- **Fuzzy matches**: Y count

---

## Edge Cases & Handling

### Skip Scenarios
- Files without extensions or unusual formats
- Metadata files: `comics_download.txt`, `*.zip` (archives), directories in src
- Archive files: `Sha 01-03.zip`, `The Bank 01-02 (2025).zip`

### Duplicate Series from Multiple Sources
- If left has multiple versions of same series (different sources/providers)
- Keep all; each gets consolidated to same destination folder
- Example: Uri Tupka and the Gods (2 different versions) → both go to `/Uri Tupka and the Gods/`

### Folder Consolidation
- If destination already has a folder for the series
- Strategy: Consolidate that folder + move loose files into it
- Example: `Feral` folder exists + individual Feral files → all into `/Feral/`

### Mixed Formats
- Some files .cbr, some .cbz, some encrypted
- Include all in consolidation; note format in move source

---

## Output File Path
```
/mnt/user-data/outputs/matching_analysis_consolidated.csv
```

---

## Implementation Requirements

### Python Libraries
- `pathlib` (Path handling)
- `csv` (CSV writing)
- `re` (Regex for name extraction)
- `collections` (defaultdict for grouping)

### Functions
1. `extract_series_name(filename: str) -> str`
   - Takes filename, returns extracted series name
   
2. `scan_directory(path: Path) -> dict`
   - Returns `{series_name: {files: [...], is_dir: bool}}`
   
3. `find_matches(src_series: str, dest_dict: dict) -> list`
   - Returns list of matching items with confidence scores
   
4. `generate_consolidation_strategy(src_file, matches) -> dict`
   - Returns row data for CSV
   
5. `main()`
   - Orchestrates entire flow
   - Writes CSV file

### Error Handling
- Handle missing directories gracefully
- Skip inaccessible files
- Log warnings for unusual filenames
- Validate extracted series names aren't empty

### Performance
- Should complete in < 5 seconds for 72 + 5975 items
- Print progress every 10 files processed
- Show final summary statistics

---

## Testing Checklist

- [ ] Series extraction works correctly (test with examples)
- [ ] Exact matching finds all relevant matches
- [ ] Fuzzy matching avoids single-letter false positives
- [ ] CSV has correct number of rows (66 total: 54 + 12)
- [ ] Consolidation rows have > 0 matches count
- [ ] New folder rows have 0 matches count
- [ ] Suggested folder names are clean (no special characters)
- [ ] Move source notation is clear and accurate
- [ ] Unmatched files list matches expected 12 series

---

## Success Criteria

✅ CSV file generated at `/mnt/user-data/outputs/matching_analysis_consolidated.csv`
✅ All 72 left panel files appear in CSV
✅ 54 consolidation strategies identified
✅ 12 new folder creation strategies identified
✅ Series name extraction is accurate (first part before hyphens/numbers)
✅ CSV is human-readable and importable into web page
✅ No errors or warnings in console output
