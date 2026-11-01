#!/usr/bin/env python3
"""
Comic File Organizer v2.0 — HTTP Server with Streaming
Serves HTML, CSV data, and handles dry-run/consolidate operations with real-time logs.

Usage:
    python3 serve_v2.py
"""

import csv
import json
import shutil
import subprocess
import sys
import tempfile
import os
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
from urllib.parse import urlparse, parse_qs

CSV_FILE = Path("/home/nesha/Downloads/comics_download/matching_analysis_consolidated.csv")
HTML_FILE = Path("/home/nesha/scripts/cp_downloads2comics/comic_organizer_v2.html")
PORT = 8123

SRC_DIR = Path("/home/nesha/Downloads/comics_download/")
DEST_DIR = Path("/mnt/extramedia/Comics")


def mover_cmd(mode, src, dest, overrides_file=None, selected_ids=None,
              duplicate_decisions_file=None):
    """The comic_mover.py command line for a dry run or an execute.

    A module-level function purely so it can be tested. O17 was a missing pair of
    arguments here — the mover was launched with no folders and silently used its
    own hardcoded ones — and a command assembled inline inside a request handler
    is reachable only by booting a server and parsing its streamed output. The
    defect lived at this boundary, so this boundary is what the tests need.

    `mode` is trusted: it is supplied by the two call sites below, never by a
    request.
    """
    cmd = ["python3", "comic_mover.py"]
    cmd += ["--dry-run"] if mode == "dry-run" else ["--execute", "--no-confirm"]
    cmd += ["--src", str(src), "--dest", str(dest)]
    if overrides_file:
        cmd += ["--overrides", overrides_file]
    if selected_ids:
        cmd += ["--selected-ids", ",".join(str(i) for i in selected_ids)]
    if duplicate_decisions_file:
        cmd += ["--duplicate-decisions", duplicate_decisions_file]
    return cmd


MATCHING_RULES_FILE = ".comic_matching_rules.md"
RULE_DECISIONS = ("accept", "refuse")

RULES_TEMPLATE = """# Comic Organiser — Saved Matching Rules

Decisions you made in the Organiser about shortened-title matching, saved so the
same judgement is never asked for twice. A rule names a FOLDER, not a file, and
overrides `.comic_containers.md` in both directions.

## Accept (0)

Shortened titles may be filed into these folders.

## Refuse (0)

Shortened titles may not be filed into these folders. A folder's own series
still files here normally.

## Publisher home (0)

Series that live in their publisher folder rather than a folder of their own,
written '- Series => Publisher folder'.
"""


def clean_rule_folder(folder: str) -> str:
    """The folder name a rule may name, or ValueError explaining why not.

    This value arrives in a POST body and is written verbatim into a file whose
    every line is meaningful, so the checks are about the FILE FORMAT, not about
    taste. A name containing a newline could write its own `## ` heading or its
    own `- ` bullets and grant permissions nobody asked for; a name containing a
    slash is not a top-level folder name at all, which is the only thing the
    matcher ever compares against.
    """
    folder = (folder or "").strip()
    if not folder:
        raise ValueError("no folder given")
    # Newlines are the dangerous ones — \n and \r both end a line for
    # splitlines(), so either would let a name write its own '## ' heading or
    # its own '- ' bullets. Rejecting every control character rather than just
    # those two because none of them belong in a folder name anyway, and one
    # check cannot drift out of step with another.
    if any(ord(c) < 32 for c in folder):
        raise ValueError("a folder name cannot contain control characters")
    if "/" in folder or "\\" in folder:
        raise ValueError("a rule names a top-level folder, not a path")
    return folder


def _write_rules(rules_path: Path, lines) -> None:
    """Write the rules file, first copying what is there to '<name>.bak'.

    One level of undo for a file the user hand-edits and two buttons rewrite: the
    previous .bak is overwritten, and a file that does not exist yet has nothing
    to keep.
    """
    if rules_path.exists():
        shutil.copy2(rules_path, rules_path.with_name(rules_path.name + ".bak"))
    rules_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def save_matching_rule(rules_path: Path, folder: str, decision: str) -> str:
    """Record one Accept/Refuse decision, and return what was done.

    Rewrites in place rather than appending, because the same folder may already
    be ruled on the other way — answering 'actually, refuse that' has to REPLACE
    the earlier yes, not sit beneath it where the first match would win.

    The prose under each heading is preserved: this file is meant to be read and
    hand-edited, and a writer that rebuilt it from the entries alone would strip
    the explanation the moment you clicked a button.
    """
    folder = clean_rule_folder(folder)
    decision = (decision or "").strip().lower()
    if decision not in RULE_DECISIONS:
        raise ValueError(f"decision must be one of {RULE_DECISIONS}")

    text = rules_path.read_text(encoding="utf-8") if rules_path.exists() else RULES_TEMPLATE
    lines = text.splitlines()

    # Drop any existing ruling on this folder, in either section.
    target = folder.lower()
    lines = [ln for ln in lines
             if not (ln.startswith("- ") and ln[2:].strip().lower() == target)]

    heading = decision.capitalize()
    section_starts = [i for i, ln in enumerate(lines) if ln.startswith("## ")]
    try:
        start = next(i for i in section_starts
                     if lines[i][3:].split("(")[0].strip().lower() == decision)
    except StopIteration:
        # A hand-edited file that lost the section. Re-add it rather than fail:
        # the alternative is a button that silently does nothing.
        lines += ["", f"## {heading} (0)", ""]
        start = len(lines) - 2

    end = next((i for i in section_starts if i > start), len(lines))
    bullets = [i for i in range(start + 1, end) if lines[i].startswith("- ")]
    if bullets:
        at = next((i for i in bullets if lines[i][2:].strip().lower() > target),
                  bullets[-1] + 1)
    else:
        # No entries yet: sit after the section's prose, before its blank tail.
        at = end
        while at > start + 1 and not lines[at - 1].strip():
            at -= 1
        lines.insert(at, "")
        at += 1
    lines.insert(at, f"- {folder}")

    _refresh_rule_counts(lines)

    _write_rules(rules_path, lines)
    return f"{heading}: {folder}"


def run_rescan(renames, dest_dir) -> list:
    """Match renamed rows against the library in a fresh process.

    A subprocess for the reason the single-row version used one: a fresh import
    reads the library as it is now. The renames travel as JSON on stdin so
    nothing from a request is ever spliced into code.
    """
    script = (
        "import sys, json\n"
        f"sys.path.insert(0, {str(Path(__file__).resolve().parent)!r})\n"
        "import matching_analysis_generator as mag\n"
        "req = json.load(sys.stdin)\n"
        "mag.DEST_DIR = mag.Path(req['dest'])\n"
        "dest_map = mag.scan_destination_directory()\n"
        "print('RESCAN_JSON:' + json.dumps(mag.rescan_renamed(req['renames'], dest_map)))\n"
    )
    proc = subprocess.run(["python3", "-c", script], capture_output=True, text=True, timeout=120,
                          input=json.dumps({"renames": renames, "dest": str(dest_dir)}))
    for line in proc.stdout.split("\n"):
        if line.startswith("RESCAN_JSON:"):
            return json.loads(line[len("RESCAN_JSON:"):])
    raise Exception(f"No result from rescan subprocess. stderr: {proc.stderr}")


def _refresh_rule_counts(lines):
    """Rewrite every '## Heading (n)' so the counts stay honest."""
    section_starts = [i for i, ln in enumerate(lines) if ln.startswith("## ")]
    for n, i in enumerate(section_starts):
        stop = section_starts[n + 1] if n + 1 < len(section_starts) else len(lines)
        count = sum(1 for j in range(i + 1, stop) if lines[j].startswith("- "))
        lines[i] = f"## {lines[i][3:].split('(')[0].strip()} ({count})"


def save_publisher_home(rules_path: Path, series: str, folder: str) -> str:
    """Record 'this series lives in its publisher folder' as '- series => folder'.

    Same file, same in-place rewrite as save_matching_rule(), in its own
    '## Publisher home' section, which is added if a hand-edited file lost it.
    An earlier line for the same series is replaced, not stacked. Both values
    are written into a file whose every line is meaningful, so control
    characters, a '=>' inside the series and a path for the folder are refused.
    """
    series = (series or "").strip()
    if not series:
        raise ValueError("no series given")
    if any(ord(c) < 32 for c in series) or "=>" in series:
        raise ValueError("a series name cannot contain control characters or '=>'")
    folder = clean_rule_folder(folder)

    text = rules_path.read_text(encoding="utf-8") if rules_path.exists() else RULES_TEMPLATE
    lines = text.splitlines()
    key = series.lower()
    lines = [ln for ln in lines
             if not (ln.startswith("- ") and "=>" in ln
                     and ln[2:].split("=>")[0].strip().lower() == key)]

    starts = [i for i, ln in enumerate(lines) if ln.startswith("## ")]
    try:
        start = next(i for i in starts
                     if lines[i][3:].split("(")[0].strip().lower() == "publisher home")
    except StopIteration:
        lines += ["", "## Publisher home (0)", ""]
        start = len(lines) - 2
        starts.append(start)
    end = next((i for i in starts if i > start), len(lines))
    at = end
    while at > start + 1 and not lines[at - 1].strip():
        at -= 1
    if at == start + 1:
        lines.insert(at, "")
        at += 1
    lines.insert(at, f"- {series} => {folder}")
    _refresh_rule_counts(lines)
    _write_rules(rules_path, lines)
    return f"Publisher home: {series} => {folder}"


class ComicOrganizerV2Handler(SimpleHTTPRequestHandler):
    """HTTP handler for v2.0 with streaming support."""

    def do_GET(self):
        """Handle GET requests."""
        parsed_path = urlparse(self.path)
        path = parsed_path.path

        # API: Load CSV as JSON
        if path == "/api/csv":
            self.send_csv_json()
            return

        # Serve main HTML
        if path == "/" or path == "":
            self.serve_file(HTML_FILE, "text/html")
            return

        # Nothing else is served. Falling through to SimpleHTTPRequestHandler.do_GET()
        # would serve the whole working directory over HTTP — including the SSH keys
        # and any other file in the project folder. The UI needs no other assets.
        self.send_error(404)

    def do_POST(self):
        """Handle POST requests (scan, dry-run, consolidate)."""
        parsed_path = urlparse(self.path)
        path = parsed_path.path

        if path == "/api/scan":
            self.handle_scan()
            return

        if path == "/api/dry-run":
            self.handle_dry_run()
            return

        if path == "/api/consolidate":
            self.handle_consolidate()
            return

        if path == "/api/rescan-series":
            self.handle_rescan_series()
            return

        if path == "/api/save-rule":
            self.handle_save_rule()
            return

        if path == "/api/save-publisher-home":
            self.handle_save_publisher_home()
            return

        self.send_error(404)

    def serve_file(self, file_path: Path, content_type: str):
        """Serve a file with specified content type."""
        if not file_path.exists():
            self.send_error(404, f"File not found: {file_path}")
            return

        try:
            with open(file_path, "rb") as f:
                content = f.read()

            self.send_response(200)
            self.send_header("Content-Type", content_type)
            self.send_header("Content-Length", str(len(content)))
            self.end_headers()
            self.wfile.write(content)
        except Exception as e:
            self.send_error(500, f"Error serving file: {str(e)}")

    def send_csv_json(self):
        """Load CSV and send as JSON."""
        if not CSV_FILE.exists():
            self.send_error(404, f"CSV file not found: {CSV_FILE}")
            return

        try:
            rows = []
            with open(CSV_FILE, "r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    if "Right Panel Matches (Count)" in row:
                        try:
                            row["Right Panel Matches (Count)"] = int(row["Right Panel Matches (Count)"])
                        except:
                            pass
                    rows.append(row)

            json_data = json.dumps(rows, indent=2).encode("utf-8")

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(json_data)))
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(json_data)
        except Exception as e:
            self.send_error(500, f"Error reading CSV: {str(e)}")

    def handle_scan(self):
        """Handle scan request - regenerate CSV from folders."""
        body = self.read_post_json()
        src_dir, dest_dir = self.folder_pair(body)

        self.send_response(200)
        self.send_header("Content-Type", "text/event-stream")
        self.send_header("Cache-Control", "no-cache")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()

        try:
            # Run matching_analysis_generator.py with custom folders
            process = subprocess.Popen(
                ["python3", "matching_analysis_generator.py", "--src", src_dir, "--dest", dest_dir],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                cwd="/home/nesha/scripts/cp_downloads2comics/",
            )

            for line in process.stdout:
                if line.strip():
                    self.wfile.write(f"{line}".encode())
                    self.wfile.flush()

            process.wait()

            # Send final message with CSV location
            self.wfile.write(f"\n✅ CSV saved to: {CSV_FILE}\n".encode())
            self.wfile.write("\n📝 Loading CSV data into page...\n".encode())
        except Exception as e:
            self.wfile.write(f"ERROR: {str(e)}".encode())

    def folder_pair(self, body):
        """The source/destination pair this request works on (O17).

        Both are pickable in the UI (REQUIREMENTS FR:132) and must reach EVERY
        subprocess, not just the generator. comic_mover.py used to be launched with
        no folders at all, so it fell back to its own hardcoded pair: picking a
        different library scanned one place and moved into another, and picking a
        different source left it reading a CSV the generator had written elsewhere.

        Falling back to the module constants rather than repeating the literals, so
        the default lives in exactly one place.
        """
        src = (body.get("src_dir") or "").strip() or str(SRC_DIR)
        dest = (body.get("dest_dir") or "").strip() or str(DEST_DIR)
        return src, dest

    def read_post_json(self):
        """Read JSON body from POST request. Returns dict or {}."""
        try:
            length = int(self.headers.get("Content-Length", 0))
            if length > 0:
                return json.loads(self.rfile.read(length))
        except Exception:
            pass
        return {}

    def write_temp_json(self, payload) -> str:
        """Write a POST-body value to a temp JSON file. Returns file path.

        The mover takes both overrides and duplicate decisions as files rather
        than arguments: either can be long enough to exceed a command line, and
        both are arbitrary filenames, which have no business on one.
        """
        tf = tempfile.NamedTemporaryFile(
            mode='w', suffix='.json', delete=False, dir='/tmp'
        )
        json.dump(payload, tf)
        tf.close()
        return tf.name

    def handle_dry_run(self):
        """Handle dry-run request with streaming output. Accepts overrides in POST body."""
        body = self.read_post_json()
        overrides = body.get("overrides", [])
        selected_ids = body.get("selected_ids", [])
        duplicate_decisions = body.get("duplicate_decisions", {})
        src_dir, dest_dir = self.folder_pair(body)

        self.send_response(200)
        self.send_header("Content-Type", "text/event-stream")
        self.send_header("Cache-Control", "no-cache")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()

        overrides_file = decisions_file = None
        try:
            if overrides:
                overrides_file = self.write_temp_json(overrides)
            if duplicate_decisions:
                decisions_file = self.write_temp_json(duplicate_decisions)
            cmd = mover_cmd("dry-run", src_dir, dest_dir, overrides_file, selected_ids,
                            decisions_file)

            process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                cwd="/home/nesha/scripts/cp_downloads2comics/",
            )

            for line in process.stdout:
                if line.strip():
                    self.wfile.write(f"{line}".encode())
                    self.wfile.flush()

            process.wait()
        except Exception as e:
            self.wfile.write(f"ERROR: {str(e)}".encode())
        finally:
            for tmp in (overrides_file, decisions_file):
                if tmp and os.path.exists(tmp):
                    os.unlink(tmp)

    def handle_consolidate(self):
        """Handle consolidate request with streaming output. Accepts overrides in POST body."""
        body = self.read_post_json()
        overrides = body.get("overrides", [])
        selected_ids = body.get("selected_ids", [])
        duplicate_decisions = body.get("duplicate_decisions", {})
        src_dir, dest_dir = self.folder_pair(body)

        self.send_response(200)
        self.send_header("Content-Type", "text/event-stream")
        self.send_header("Cache-Control", "no-cache")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()

        overrides_file = decisions_file = None
        try:
            if overrides:
                overrides_file = self.write_temp_json(overrides)
            if duplicate_decisions:
                decisions_file = self.write_temp_json(duplicate_decisions)
            cmd = mover_cmd("execute", src_dir, dest_dir, overrides_file, selected_ids,
                            decisions_file)

            process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                cwd="/home/nesha/scripts/cp_downloads2comics/",
            )

            for line in process.stdout:
                if line.strip():
                    self.wfile.write(f"{line}".encode())
                    self.wfile.flush()

            process.wait()
        except Exception as e:
            self.wfile.write(f"ERROR: {str(e)}".encode())
        finally:
            for tmp in (overrides_file, decisions_file):
                if tmp and os.path.exists(tmp):
                    os.unlink(tmp)

    def handle_rescan_series(self):
        """Rescan every row the user has renamed, together (see rescan_renamed).

        The body carries the row just edited (`left_file`, `new_series`) and,
        in `renamed`, every other row renamed this session. They are matched in
        one go because whether a new series needs its own folder depends on how
        many rows now carry it. The reply keeps the single-row fields the page
        always read, and adds `results` with one entry per row.
        """
        body = self.read_post_json()
        left_file = body.get("left_file", "").strip()
        new_series = body.get("new_series", "").strip()

        if not left_file or not new_series:
            self.send_error(400, "Missing left_file or new_series")
            return

        renames = [{"left_file": left_file, "new_series": new_series}]
        for other in body.get("renamed") or []:
            f, n = str(other.get("left_file", "")).strip(), str(other.get("new_series", "")).strip()
            if f and n and f != left_file and all(f != r["left_file"] for r in renames):
                renames.append({"left_file": f, "new_series": n})

        try:
            _src, dest_dir = self.folder_pair(body)
            results = run_rescan(renames, dest_dir)
            json_data = json.dumps({**results[0], "results": results}).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(json_data)))
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(json_data)
        except Exception as e:
            self.send_error(500, f"Error rescanning: {str(e)}")

    def handle_save_publisher_home(self):
        """Record 'this series lives in its publisher folder' for the CURRENT library.

        The server picks the folder, not the page: it is the first top-level
        folder whose name carries the publisher keyword found in the filename,
        which is the folder find_publisher_match() would pick.
        """
        body = self.read_post_json()
        _src, dest_dir = self.folder_pair(body)
        try:
            import matching_analysis_generator as mag
            names = sorted(e.name for e in Path(dest_dir).iterdir() if e.is_dir())
            folder = mag.publisher_folder_for(body.get("file", ""), names)
            if not folder:
                raise ValueError("no publisher folder found for that file")
            message = save_publisher_home(
                Path(dest_dir) / MATCHING_RULES_FILE, body.get("series", ""), folder)
        except ValueError as e:
            self.send_error(400, str(e))
            return
        except Exception as e:
            self.send_error(500, f"Could not save: {e}")
            return
        payload = json.dumps({"saved": message, "folder": folder}).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    def handle_save_rule(self):
        """Record an Accept/Refuse decision against the CURRENT library root.

        The root comes from the same folder_pair() every other endpoint uses, so
        a rule saved while pointed at one library cannot land in another (O17).
        """
        body = self.read_post_json()
        _src, dest_dir = self.folder_pair(body)

        try:
            message = save_matching_rule(
                Path(dest_dir) / MATCHING_RULES_FILE,
                body.get("folder", ""),
                body.get("decision", ""),
            )
        except ValueError as e:
            self.send_error(400, str(e))
            return
        except Exception as e:
            self.send_error(500, f"Could not save rule: {e}")
            return

        payload = json.dumps({"saved": message}).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    def log_message(self, format, *args):
        """Override log format to be cleaner."""
        if isinstance(args[0], str) and ("GET" in args[0] or "POST" in args[0]):
            print(f"  {self.address_string()} - {args[0]}")


def main():
    """Start HTTP server."""
    print("\n" + "=" * 80)
    print("🌐 Comic Organizer v2.0 — HTTP Server")
    print("=" * 80)
    print(f"\n📂 CSV File: {CSV_FILE}")
    print(f"📄 HTML File: {HTML_FILE}")
    print(f"\n🚀 Starting server on http://localhost:{PORT}")
    print(f"\n   Open browser: http://localhost:{PORT}")
    print(f"   To stop: Press Ctrl+C\n")
    print("=" * 80 + "\n")

    # Bind the literal loopback address, not the hostname. "localhost" goes
    # through name resolution and can be remapped in /etc/hosts or resolve to
    # ::1, so what it ends up bound to is not guaranteed. comic_volume_creator
    # already binds '127.0.0.1'; this aligns the two.
    server = HTTPServer(("127.0.0.1", PORT), ComicOrganizerV2Handler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n\n🛑 Server stopped.")
        print("=" * 80 + "\n")


if __name__ == "__main__":
    main()
