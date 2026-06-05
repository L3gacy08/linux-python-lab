#!/bin/bash

echo "Starting audit..."

mkdir -p reports

echo "Running Python script..."

python scripts/check_usage.py > reports/disk_report.txt

echo "Audit complete."
echo "The report was saved in the reports folder."
echo "Here is the report:"
echo

cat reports/disk_report.txt
