# Linux Python Lab

This lab is about using Linux commands, Python and a bash scripts.

The project checks disk usage for a few servers. The server names and disk usage numbers are stored in a text file. The Python script reads that file and checks if each server is OK, WARNING, or CRITICAL.

## project folders

- `data` holds the server usage text file
- `scripts` holds the Python script
- `reports` stores the report after the audit runs

## files used

`data/server_usage.txt`  
This file has the server names and disk usage percentages.

`scripts/check_usage.py`  
This python script reads the server usage file and prints a status for each server.

`run_audit.sh`  
This bash script runs the Python script and saves the output into a report file.

## How to run

First give the bash script permission to run:

```bash
chmod +x run_audit.sh
