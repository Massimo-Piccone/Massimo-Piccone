#!/bin/bash

# Use the current directory
currentDirectory="$(pwd)"

# Function to rename files and track name changes
rename_files() {
    local directory="$1"

    # Loop through all files in the directory
    for file in "$directory"/*; do
        if [[ -f "$file" ]]; then
            filename=$(basename "$file")
            newName=$(echo "$filename" | sed 's/ /_/g')

            # Rename if the name has changed
            if [[ "$filename" != "$newName" ]]; then
                mv "$directory/$filename" "$directory/$newName"
                echo "Renamed: $filename -> $newName"
            fi
        fi
    done
}

# Call the rename function
rename_files "$currentDirectory"

echo "Done."
