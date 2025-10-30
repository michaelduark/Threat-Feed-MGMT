# Threat Feed Management

Requirements
- Python3
- BASH or SH for edl-updater.sh
- Internet connectivity (HTTP/HTTPS)
- Threat intel feed URLs

    
Order of execution or utilize edl-updater.sh
1. edl-downloader.py
1. edl-ip-handler.py
1. edl-domain-handler.py

All files should be placed in the same folder, i.e. /scripts/python/threat-feed-management/.

All scripts except edl-update.sh are path agnostic; edl-update.sh should be updated with the paths of where the individual files are located.
