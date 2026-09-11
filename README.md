# Network-Config-Backup-Tool
network automation tool to save your network devices configuration daily keeping track to the changes made in the network 
A Python script using Netmiko to automatically connect to Cisco routers, gather the running and startup configurations, and save them locally in organized folders by date.

## Features
- Connects to multiple devices via SSH.
- Saves `show run` and `show startup-config`.
- Organizes backups into folders by Device IP and Day of the week.
- Handles connection errors gracefully without crashing the whole script.

## Requirements
- Python 3.x
- `netmiko` library (`pip install netmiko`)
