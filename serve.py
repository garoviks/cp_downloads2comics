#!/usr/bin/env python3
"""
Simple HTTP server for Comic Organizer web page.
Serves HTML and dynamically loads CSV data.

Usage:
    python3 serve.py

Then open browser to: http://localhost:8888
"""

import csv
import json
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
from urllib.parse import urlparse

CSV_FILE = Path("/home/nesha/scripts/cp_downloads2comics/matching_analysis_consolidated.csv")
HTML_FILE = Path("/home/nesha/scripts/cp_downloads2comics/comic_organizer.html")
PORT = 8888

class ComicOrganizerHandler(SimpleHTTPRequestHandler):
    """Custom HTTP handler for Comic Organizer."""

    def do_GET(self):
        """Handle GET requests."""
        parsed_path = urlparse(self.path)
        path = parsed_path.path

        # API: Load CSV as JSON
        if path == "/api/csv":
            self.send_csv_json()
            return

        # Serve HTML
        if path == "/" or path == "":
            self.serve_file(HTML_FILE, "text/html")
            return

        # Serve other static files from current directory
        try:
            super().do_GET()
        except Exception as e:
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
                    # Convert count to int
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

    def log_message(self, format, *args):
        """Override log format to be cleaner."""
        # Only log actual requests, not every little thing
        if "GET" in args[0]:
            print(f"  {self.address_string()} - {args[0]}")


def main():
    """Start HTTP server."""
    print("\n" + "=" * 80)
    print("🌐 Comic Organizer Web Server")
    print("=" * 80)
    print(f"\n📂 CSV File: {CSV_FILE}")
    print(f"📄 HTML File: {HTML_FILE}")
    print(f"\n🚀 Starting server on http://localhost:{PORT}")
    print(f"\n   Open browser: http://localhost:{PORT}")
    print(f"   To stop: Press Ctrl+C\n")
    print("=" * 80 + "\n")

    server = HTTPServer(("localhost", PORT), ComicOrganizerHandler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n\n🛑 Server stopped.")
        print("=" * 80 + "\n")


if __name__ == "__main__":
    main()
