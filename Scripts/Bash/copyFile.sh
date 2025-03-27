#!/bin/bash

# Ensure an input file is provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <input_file>"
    exit 1
fi

# Input file containing the list
input_file="$1"

# Directory to copy images to
target_dir="Assets"

# Ensure the input file exists
if [ ! -f "$input_file" ]; then
    echo "Input file not found: $input_file"
    exit 1
fi

# Ensure the target directory exists
mkdir -p "$target_dir"

# Copy listed images to the target directory
while IFS= read -r image; do
    image=$(echo "$image" | tr -d '"')  # Remove double quotes
    if [ -f "$image" ]; then
        cp "$image" "$target_dir"
        echo "Copied: $image"
    else
        echo "File not found: $image"
    fi
done < "$input_file"

echo "Matches copied to: $target_dir"
