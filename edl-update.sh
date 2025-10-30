#!/bin/bash

# Execute the first python script
python3 /scripts/python3/threat-feed-management/edl-downloader.py

# Execute the second python script
python3 /scripts/python3/threat-feed-management/edl-sanitizer.py

python3 /scripts/python3/threat-feed-management/edl-ip-handler.py

# Execute the third python script
python3 /scripts/python3/threat-feed-management/edl-domain-handler.py
