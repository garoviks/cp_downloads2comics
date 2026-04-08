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

    def handle_dry_run(self):
        """Handle dry-run request with streaming output."""
        self.send_response(200)
        self.send_header("Content-Type", "text/event-stream")
        self.send_header("Cache-Control", "no-cache")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()

        try:
            # Run comic_mover.py --dry-run and stream output
            process = subprocess.Popen(
                ["python3", "comic_mover.py", "--dry-run"],
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

    def handle_consolidate(self):
        """Handle consolidate request with streaming output."""
        self.send_response(200)
        self.send_header("Content-Type", "text/event-stream")
        self.send_header("Cache-Control", "no-cache")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()

        try:
            # Run comic_mover.py --execute and stream output
            process = subprocess.Popen(
                ["python3", "comic_mover.py", "--execute", "--no-confirm"],
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
