#!/bin/bash
# Double-click in Finder to start the CCAR exam portal.
cd "$(dirname "$0")"
python3 server.py --open
