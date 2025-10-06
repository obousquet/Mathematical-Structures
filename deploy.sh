#!/bin/bash
# Run this script to generate all the websites for deployment to github pages

set -e
# List of directories to process
DIRS=("functors" "rings" "template")
# Location of the generate_website.py script
SCRIPT="../math_database/generate_website.py"

for DIR in "${DIRS[@]}"; do
    echo "Processing directory: $DIR"
    python3 "$SCRIPT" --data_dir="data/$DIR" --output_dir="docs/$DIR" --deploy=true
done