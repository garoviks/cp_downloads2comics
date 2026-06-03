#!/bin/bash
cd "$(dirname "$0")"
pkill -f "serve_v2.py" 2>/dev/null
sleep 1
python3 serve_v2.py &
until nc -z localhost 8123 2>/dev/null; do sleep 0.2; done
xdg-open http://localhost:8123/
