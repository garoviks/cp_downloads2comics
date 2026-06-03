#!/bin/bash
cd "$(dirname "$0")"
python3 serve_v2.py &
sleep 2
xdg-open http://localhost:8123/
