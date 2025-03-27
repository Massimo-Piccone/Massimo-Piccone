#!/bin/bash

# Ensure an input file is provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <input_file>"
    exit 1
fi

input_file="$1"
output_file="wAssets.txt"

# Ensure the input file exists
if [ ! -f "$input_file" ]; then
    echo "Input file not found: $input_file"
    exit 1
fi

# Replace all ! with newline
# Extract content + wrap in quotes,
# Remove empty lines. 
awk '{ gsub(/!\[\[/, "\n[["); print }' "$input_file" | \
    while IFS= read -r line; do
        if [[ "$line" =~ \[\[(.*)\]\] ]]; then
            echo "\"${BASH_REMATCH[1]}\""
        fi
    done | sed '/^$/d' > "$output_file"

echo "Formated. See $output_file"
