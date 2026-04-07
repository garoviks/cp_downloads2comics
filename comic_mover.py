#!/usr/bin/env python3
"""
Comic File Organizer — Move Script
Reads matching_analysis_consolidated.csv and orchestrates file consolidation.

Usage:
    python comic_mover.py --dry-run      # Preview without making changes
    python comic_mover.py --execute      # Execute moves after confirmation
    python comic_mover.py --rollback     # Undo last execution
"""

import csv
import os
import sys
import json
import shutil
import argparse
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Tuple, Optional

# ═══════════════════════════════════════════════════════════════════════════
# CONFIG
# ═══════════════════════════════════════════════════════════════════════════

SRC_DIR = Path("/home/nesha/Downloads/comics_download/")
DEST_DIR = Path("/mnt/extramedia/Comics")
CSV_FILE = Path("/home/nesha/scripts/cp_downloads2comics/matching_analysis_consolidated.csv")
LOG_DIR = Path("/home/nesha/scripts/cp_downloads2comics/.logs")
ROLLBACK_FILE = LOG_DIR / "last_execution.json"

# ═══════════════════════════════════════════════════════════════════════════
# CLASSES
# ═══════════════════════════════════════════════════════════════════════════

class Move:
    """Represents a single file move operation."""
    def __init__(self, src: Path, dst: Path, move_type: str = "FILE"):
        self.src = src
        self.dst = dst
        self.move_type = move_type  # FILE, FOLDER
        self.executed = False
        self.error = None

    def to_dict(self):
        return {
            "src": str(self.src),
            "dst": str(self.dst),
            "type": self.move_type,
            "executed": self.executed,
            "error": self.error,
        }

    @staticmethod
    def from_dict(d):
        m = Move(Path(d["src"]), Path(d["dst"]), d["type"])
        m.executed = d.get("executed", False)
        m.error = d.get("error")
        return m


class MoveOperation:
    """Groups moves related to a single row/series."""
    def __init__(self, row: Dict, series_name: str, dest_folder: str):
        self.row = row
        self.series_name = series_name
        self.dest_folder = dest_folder
        self.moves: List[Move] = []
        self.skipped_reason = None

    def add_move(self, src: Path, dst: Path, move_type: str = "FILE"):
        self.moves.append(Move(src, dst, move_type))

    def to_dict(self):
        return {
            "series": self.series_name,
            "dest_folder": self.dest_folder,
            "action_type": self.row.get("Action Type", "UNKNOWN"),
            "moves": [m.to_dict() for m in self.moves],
            "skipped": self.skipped_reason,
        }


# ═══════════════════════════════════════════════════════════════════════════
# HELPERS
# ═══════════════════════════════════════════════════════════════════════════

def ensure_dir():
    """Create log directory if needed."""
    LOG_DIR.mkdir(parents=True, exist_ok=True)

def read_csv() -> List[Dict]:
    """Read and parse CSV file."""
    if not CSV_FILE.exists():
        print(f"❌ CSV file not found: {CSV_FILE}")
        sys.exit(1)

    rows = []
    with open(CSV_FILE, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row.get('Left Panel File', '').strip():
                rows.append(row)
    return rows

def find_loose_right_files(series_name: str) -> List[Path]:
    """
    Find loose comic files in base Comics directory matching this series.
    Only looks for .cbz and .cbr files.
    Example: /mnt/extramedia/Comics/Feral 019.cbr
    """
    result = []

    # Search base directory for files matching this series
    for item in DEST_DIR.iterdir():
        if item.is_file() and item.suffix.lower() in {'.cbz', '.cbr'}:
            # Check if filename contains the series name
            if series_name.lower() in item.name.lower():
                result.append(item)

    return result

def find_right_panel_folder(dest_folder_name: str) -> Optional[Path]:
    """Find existing folder for this series destination."""
    dest_path = DEST_DIR / dest_folder_name.strip('/')
    if dest_path.exists() and dest_path.is_dir():
        return dest_path
    return None

def plan_moves(rows: List[Dict]) -> List[MoveOperation]:
    """
    Create move plan for all rows.
    Returns list of MoveOperation objects.

    Action types:
    - CONSOLIDATE: Move LEFT into existing folder (folder exists)
    - CREATE_FOLDER_WITH_FILES: Create folder, move LEFT + loose RIGHT files
    - COPY_TO_BASE: Copy LEFT to base Comics folder (no matches)
    """
    operations = []

    for row in rows:
        left_file = row.get('Left Panel File', '').strip()
        series = row.get('Series Name', '').strip()
        dest_folder = row.get('Suggested Folder Name', '').strip()
        action = row.get('Action Type', '').strip()
        move_source = row.get('Move Source', '').strip()

        if not left_file or not series:
            continue

        op = MoveOperation(row, series, dest_folder)

        # Check if source file exists
        src_file = SRC_DIR / left_file
        if not src_file.exists():
            op.skipped_reason = f"Source file not found: {src_file}"
            operations.append(op)
            continue

        # Determine destination folder path
        if action == "COPY_TO_BASE":
            # Copy to base folder
            dest_folder_path = DEST_DIR
        else:
            # Move to series folder
            dest_folder_path = DEST_DIR / dest_folder.strip('/')

        # Add move for left panel file
        op.add_move(src_file, dest_folder_path / left_file, "FILE")

        # Handle right files if present (both CONSOLIDATE and CREATE_FOLDER_WITH_FILES)
        if action in ["CONSOLIDATE", "CREATE_FOLDER_WITH_FILES"]:
            # Find and move loose right files matching this series
            loose_files = find_loose_right_files(series)
            for rf in loose_files:
                op.add_move(rf, dest_folder_path / rf.name, "FILE")

        operations.append(op)

    return operations

def print_dry_run(operations: List[MoveOperation]):
    """Print preview of all operations."""
    print("\n" + "=" * 80)
    print("📋 DRY RUN — Preview of all moves")
    print("=" * 80 + "\n")

    total_files = 0
    skipped = 0
    total_folders_created = set()

    for op in operations:
        if op.skipped_reason:
            print(f"⚠️  [{op.series_name}] SKIPPED: {op.skipped_reason}")
            skipped += 1
            continue

        action = op.row.get('Action Type', 'UNKNOWN')
        print(f"✅ [{action}] {op.series_name}")
        print(f"   → Destination: {op.dest_folder}")

        for move in op.moves:
            if move.move_type == "FILE":
                print(f"     📄 MOVE: {move.src.name}")
                print(f"             → {move.dst}")
                total_files += 1
                total_folders_created.add(str(move.dst.parent))

        print()

    print("=" * 80)
    print(f"📊 Summary:")
    print(f"   Total operations: {len(operations)}")
    print(f"   Files to move: {total_files}")
    print(f"   Destination folders to ensure exist: {len(total_folders_created)}")
    print(f"   Skipped: {skipped}")
    print(f"   NOTE: Only LEFT files are moved. Existing RIGHT folders/files untouched.")
    print("=" * 80 + "\n")

def execute_moves(operations: List[MoveOperation], dry_run: bool = False) -> bool:
    """
    Execute all moves. Returns True if successful, False otherwise.
    If dry_run=True, only simulates without touching files.
    """
    ensure_dir()

    executed_ops = []
    errors = []

    print("\n" + "=" * 80)
    if dry_run:
        print("🔍 Simulating moves (DRY RUN — no files will be changed)")
    else:
        print("▶️  Executing moves...")
    print("=" * 80 + "\n")

    for op in operations:
        if op.skipped_reason:
            print(f"⏭️  [{op.series_name}] Skipped")
            continue

        # Ensure destination folder exists
        dest_folder = DEST_DIR / op.dest_folder.strip('/')
        if not dry_run:
            dest_folder.mkdir(parents=True, exist_ok=True)
            print(f"📁 Created folder: {dest_folder}")
        else:
            print(f"📁 Would create folder: {dest_folder}")

        # Execute file moves (LEFT only)
        for move in op.moves:
            try:
                if move.move_type == "FILE":
                    if dry_run:
                        print(f"   📄 Would move: {move.src.name} → {move.dst.parent.name}/")
                    else:
                        if not move.src.exists():
                            raise FileNotFoundError(f"Source not found: {move.src}")
                        shutil.move(str(move.src), str(move.dst))
                        print(f"   ✅ Moved: {move.src.name} → {move.dst.parent.name}/")
                        move.executed = True

            except Exception as e:
                error_msg = f"Error moving {move.src}: {str(e)}"
                print(f"   ❌ {error_msg}")
                move.error = error_msg
                errors.append((op.series_name, error_msg))

        executed_ops.append(op)

    # Save execution log for potential rollback
    if not dry_run and executed_ops:
        save_execution_log(executed_ops)

    print("\n" + "=" * 80)
    if errors:
        print(f"⚠️  Execution completed with {len(errors)} error(s):")
        for series, error in errors:
            print(f"   [{series}] {error}")
        print("=" * 80 + "\n")
        return False
    else:
        if dry_run:
            print("✅ Dry run complete. No changes made.")
        else:
            print("✅ All moves executed successfully!")
        print("=" * 80 + "\n")
        return True

def save_execution_log(operations: List[MoveOperation]):
    """Save execution log for rollback capability."""
    ensure_dir()
    log_data = {
        "timestamp": datetime.now().isoformat(),
        "operations": [op.to_dict() for op in operations],
    }
    with open(ROLLBACK_FILE, 'w') as f:
        json.dump(log_data, f, indent=2)
    print(f"📝 Execution log saved to: {ROLLBACK_FILE}")

def rollback():
    """Undo last execution."""
    if not ROLLBACK_FILE.exists():
        print("❌ No execution log found. Cannot rollback.")
        return

    with open(ROLLBACK_FILE, 'r') as f:
        log_data = json.load(f)

    timestamp = log_data.get("timestamp", "unknown")
    operations_data = log_data.get("operations", [])

    print(f"\n🔙 Rolling back execution from {timestamp}")
    print(f"   Total operations: {len(operations_data)}\n")

    rolled_back = 0
    for op_data in operations_data:
        for move_data in op_data.get("moves", []):
            if move_data.get("executed"):
                src = Path(move_data["dst"])
                if src.exists():
                    try:
                        if src.is_file():
                            src.unlink()
                            print(f"   ✅ Deleted: {src.name}")
                        rolled_back += 1
                    except Exception as e:
                        print(f"   ❌ Error deleting {src}: {e}")

    print(f"\n✅ Rollback complete. {rolled_back} files deleted.")

# ═══════════════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════════════

def main():
    parser = argparse.ArgumentParser(
        description="Comic File Organizer — Move orchestration script",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python comic_mover.py --dry-run       # Preview all moves
  python comic_mover.py --execute       # Execute after preview
  python comic_mover.py --rollback      # Undo last execution
        """,
    )
    parser.add_argument("--dry-run", action="store_true",
                        help="Preview all moves without making changes")
    parser.add_argument("--execute", action="store_true",
                        help="Execute moves (will ask for confirmation)")
    parser.add_argument("--rollback", action="store_true",
                        help="Rollback last execution")
    parser.add_argument("--no-confirm", action="store_true",
                        help="Skip confirmation prompt (use with caution)")

    args = parser.parse_args()

    # Validate directories
    if not SRC_DIR.exists():
        print(f"❌ Source directory not found: {SRC_DIR}")
        sys.exit(1)
    if not DEST_DIR.exists():
        print(f"❌ Destination directory not found: {DEST_DIR}")
        sys.exit(1)

    # Handle rollback
    if args.rollback:
        rollback()
        return

    # Read CSV and plan moves
    print(f"📖 Reading CSV: {CSV_FILE}")
    rows = read_csv()
    print(f"✅ Loaded {len(rows)} rows\n")

    print("📐 Planning moves...")
    operations = plan_moves(rows)
    print(f"✅ Planned {len(operations)} operations\n")

    # Handle dry-run
    if args.dry_run:
        print_dry_run(operations)
        return

    # Handle execute
    if args.execute:
        print_dry_run(operations)

        # Confirmation
        if not args.no_confirm:
            response = input("⚠️  Proceed with moves? (yes/no): ").strip().lower()
            if response not in ['yes', 'y']:
                print("❌ Cancelled.")
                return

        success = execute_moves(operations, dry_run=False)
        sys.exit(0 if success else 1)

    # No action specified
    print("ℹ️  No action specified. Use --dry-run, --execute, or --rollback")
    print("   Run with --help for full usage information.")

if __name__ == "__main__":
    main()
