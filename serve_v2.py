#!/usr/bin/env python3
"""
Comic File Organizer v2.0 — HTTP Server with Streaming
Serves HTML, CSV data, and handles dry-run/consolidate operations with real-time logs.

Usage:
    python3 serve_v2.py
"""

import csv
import json
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

        # Serve static files
        try:
            super().do_GET()
        except Exception as e:
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
        self.send_response(200)
        self.send_header("Content-Type", "text/event-stream")
        self.send_header("Cache-Control", "no-cache")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()

        try:
            # Run matching_analysis_generator.py to regenerate CSV
            process = subprocess.Popen(
                ["python3", "matching_analysis_generator.py"],
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

    def read_post_json(self):
        """Read JSON body from POST request. Returns dict or {}."""
        try:
            length = int(self.headers.get("Content-Length", 0))
            if length > 0:
                return json.loads(self.rfile.read(length))
        except Exception:
            pass
        return {}

    def write_overrides_file(self, overrides: list) -> str:
        """Write overrides list to a temp JSON file. Returns file path."""
        tf = tempfile.NamedTemporaryFile(
            mode='w', suffix='.json', delete=False, dir='/tmp'
        )
        json.dump(overrides, tf)
        tf.close()
        return tf.name

    def handle_dry_run(self):
        """Handle dry-run request with streaming output. Accepts overrides in POST body."""
        body = self.read_post_json()
        overrides = body.get("overrides", [])

        self.send_response(200)
        self.send_header("Content-Type", "text/event-stream")
        self.send_header("Cache-Control", "no-cache")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()

        overrides_file = None
        try:
            cmd = ["python3", "comic_mover.py", "--dry-run"]
            if overrides:
                overrides_file = self.write_overrides_file(overrides)
                cmd += ["--overrides", overrides_file]

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
            if overrides_file and os.path.exists(overrides_file):
                os.unlink(overrides_file)

    def handle_consolidate(self):
        """Handle consolidate request with streaming output. Accepts overrides in POST body."""
        body = self.read_post_json()
        overrides = body.get("overrides", [])

        self.send_response(200)
        self.send_header("Content-Type", "text/event-stream")
        self.send_header("Cache-Control", "no-cache")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()

        overrides_file = None
        try:
            cmd = ["python3", "comic_mover.py", "--execute", "--no-confirm"]
            if overrides:
                overrides_file = self.write_overrides_file(overrides)
                cmd += ["--overrides", overrides_file]

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
            if overrides_file and os.path.exists(overrides_file):
                os.unlink(overrides_file)

    def handle_rescan_series(self):
        """Rescan matching logic for a single file with an overridden series name.
        Uses a subprocess to avoid blocking and to get a fresh import."""
        body = self.read_post_json()
        left_file = body.get("left_file", "").strip()
        new_series = body.get("new_series", "").strip()

        if not left_file or not new_series:
            self.send_error(400, "Missing left_file or new_series")
            return

        try:
            # Run a small Python script that does the rescan and outputs JSON
            script = f"""
import sys, json
sys.path.insert(0, '/home/nesha/scripts/cp_downloads2comics/')
import matching_analysis_generator as mag

dest_map = mag.scan_destination_directory()
matched, match_data, confidence = mag.find_matches(
    {json.dumps(left_file)}, {json.dumps(new_series)}, dest_map
)
row = mag.generate_consolidation_strategy(
    {json.dumps(left_file)}, {json.dumps(new_series)}, matched, match_data, confidence
)
result = {{
    "Series Name": {json.dumps(new_series)},
    "Action Type": row["Action Type"],
    "Suggested Folder Name": row["Suggested Folder Name"],
    "Right Panel Matches (Count)": row["Right Panel Matches (Count)"],
    "Has Existing Folder": row["Has Existing Folder"],
    "Has Existing Files": row["Has Existing Files"],
    "Consolidation Strategy": row["Consolidation Strategy"],
    "Move Source": row["Move Source"],
}}
print("RESCAN_JSON:" + json.dumps(result))
"""
            process = subprocess.Popen(
                ["python3", "-c", script],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )
            stdout, stderr = process.communicate(timeout=120)

            # Extract JSON from output (after RESCAN_JSON: marker)
            result_json = None
            for line in stdout.split("\n"):
                if line.startswith("RESCAN_JSON:"):
                    result_json = line[len("RESCAN_JSON:"):]
                    break

            if result_json is None:
                raise Exception(f"No result from rescan subprocess. stderr: {stderr}")

            json_data = result_json.encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(json_data)))
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(json_data)

        except Exception as e:
            self.send_error(500, f"Error rescanning: {str(e)}")

    def log_message(self, format, *args):
        """Override log format to be cleaner."""
        if "GET" in args[0] or "POST" in args[0]:
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

    server = HTTPServer(("localhost", PORT), ComicOrganizerV2Handler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n\n🛑 Server stopped.")
        print("=" * 80 + "\n")


if __name__ == "__main__":
    main()
