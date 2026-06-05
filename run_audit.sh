#!/bin/bash

# prints a message so the user knows the audit is starting
echo "Starting audit..."

# makes the `reports` folder if it does not already exist
mkdir -p reports

# prints a message before running the Python script
echo "Running Python script..."

# runs the python script and saves the output into a report file
python scripts/check_usage.py > reports/disk_report.txt

# print a message when the audit is finished
echo "Audit complete."

# tell the user where the report was saved
echo "The report was saved in the reports folder."

# shows the report in the terminal
echo "Here is the report:"
echo

# display the contents of the disk report file after it is created
cat reports/disk_report.txt
