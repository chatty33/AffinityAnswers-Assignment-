#!/bin/bash

# Download the data file
wget https://www.amfiindia.com/spages/NAVAll.txt -O data.txt

# Extract Scheme Name and Asset Value fields and save them in a CSV file
awk -F';' 'BEGIN{OFS=","} NR>2 {print $4, $5}' data.txt > output.csv

# Remove the downloaded data file
rm data.txt

echo "Extraction complete. Output saved in output.csv."
