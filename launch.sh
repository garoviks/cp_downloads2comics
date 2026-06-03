#!/bin/bash
cd "$(dirname "$0")"
pkill -f "serve_v2.py" 2>/dev/null
sleep 1
python3 serve_v2.py &
sleep 2
xdg-open http://localhost:8123/
