# Obsidian to GitHub Formatting Process
> Use Bash and Swift to mass format Assets and Markdown files for GitHub Syntax </br>

## Objective
This was not initially intended to be a project. I created this system during the development of my Wireshark analysis project. My primary objective is to minimize repetition and consistently and enhance efficiency. I have many unuploaded projects in this format, so I made effort to simplify and ensure the reliability of these bulk operations. The process was tedious but rewarding. I have significantly benefited from this project and hope that others can as well. 

## Strategy  
This task is quite surgical, as syntax, filenames, and paths are invalid if they are not exact. </br>
Then to manage hundreds (up to a theoretically much bigger number) simultaneously presents some challenge. 

To achive this reliabely I break it into 3 distict stages: </br>
Stage 1: Identify, Extract and Format Assets List. </br>
Stage 2: Isolate and Format the actual Assets for GitHub. </br>
Stage 3: Reformat asset text References for GitHub. </br>

Stage 1 can be achieved with simple terminal commands and polished with `format.sh` to space, trim and wrap the list, to ensure exact matchs in later use. In stage 2, I use `copyFiles.sh` to isolate the assets and `noSpaceName.sh` to format assets for GitHub. Finally in stage 3, I use `macSS->Git.swift` to reformat all asset references in my project for GitHub compatibility.

Voilà. A task that would have once taken days (or weeks depending on size) has been reduced to a matter of minutes.

## Prerequisites:

**Scripting Languages**
- Bash
- Swift

**Your Project**
- Text File
- Images

For best results, use:
- Apple Computer 
- Obsidian notes

It’s not a deal breaker, but the Regex patterns are fit to match on Mac Screenshot file names and Obsidian notes reference format. </br>
You may need to make some adjustments if you are working with other patterns.

## Step 1: Identify, List and Format Relevant Assets.

> I had a lot to sift through and didn't want to do all that manually.

![1048 Photos In One Folder](/Scripts/.assets/Screenshot_2025-03-24_at_15.36.15.png)

### 1a: Identify Assets

This wasn't difficult at all. 

You can easily append all your notes into one file:

```shell
@Massimo [PROJECT] % cat *.md | >> total.txt
```

### 1b: List Assets
And use grep to pull all references:
> Change your grep option if yours is different.
```shell
@Massimo [PROJECT] % cat total.txt | grep Screenshot | > assets.txt
@Massimo [PROJECT] % head -5 assets.txt
![[Screenshot 2025-03-10 at 01.16.56.png]]
![[Screenshot 2025-03-10 at 01.26.44.png]]
![[Screenshot 2025-03-10 at 01.32.48.png]]![[Screenshot 2025-03-10 at 01.38.34.png]]
![[Screenshot 2025-03-10 at 01.42.46.png]]
![[Screenshot 2025-03-10 at 01.53.57.png]]![[Screenshot 2025-03-10 at 02.01.48.png]]![[Screenshot 2025-03-10 at 02.08.13 1.png]]
```

### 1c: Formating Assets List

`format.sh` is based off of the obsidian reference structure ![[*]] </br>
3 main objectives of `format.sh` are spacing, extracting and wrapping.

To ensure proper spacing we replace all `![[` with a newline `\n[[`. </br>
Then, we try each line against a regex pattern to exreact between the `[[*]]`. </br>
We echo all matches between quotes resulting in every match being quoted. </br>
Finally we match on all empty lines and delete them.

To use this script or any other, you will have to allocate execute privileges. </br>
To do this use the command `chmod +x [SCRIPT].sh`

### `format.sh`
```bash
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
```

```shell
@Massimo [PROJECT] % chmod +x format.sh
@Massimo [PROJECT] % ./format.sh assets.txt
Formated. See wAssets.txt
@Massimo [PROJECT] % head -5 wAssets.txt
"Screenshot 2025-03-10 at 01.16.56.png"
"Screenshot 2025-03-10 at 01.26.44.png"
"Screenshot 2025-03-10 at 01.32.48.png"
"Screenshot 2025-03-10 at 01.38.34.png"
"Screenshot 2025-03-10 at 01.42.46.png"
```
## Step 2: Isolate and Format the Assets for GitHub.

### 2a: Isolate Assets

`copyFile.sh` will search it's current directory for matches in the provided input file. </br>
It will then copy all matches in a new nested directory called `assets`.

Drop both `./copyFile.sh` and  `assets.txt` into the photo folder, then pull the trigger.
### `copyFile.sh`
```bash
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
```

```shell
@Massimo [PROJECT] % cp copyFile.sh wAssets.txt ~/Photos
@Massimo [PROJECT] % cd ~/Photos
@Massimo Photos % chmod +x copyFile.sh
@Massimo Photos % ./copyFile.sh wAssets.txt
Copied: Screenshot 2025-03-10 at 01.16.56.png
Copied: Screenshot 2025-03-10 at 01.26.44.png
Copied: Screenshot 2025-03-10 at 01.32.48.png
Copied: Screenshot 2025-03-10 at 01.38.34.png
[.cut.]
Matches copied to: Assets
@Massimo Photos % ls Assets
Screenshot 2025-03-10 at 01.16.56.png
Screenshot 2025-03-10 at 01.26.44.png
Screenshot 2025-03-10 at 01.32.48.png
Screenshot 2025-03-10 at 01.38.34.png
[.cut.]
```

### 2b: Format the Assets for GitHub.

To ensure there are no formatting problems, I remove all spaces in the image names and replace them with underscores. </br>
This is important as GitHub won’t process the image references correctly if there are spaces in the file name.

From the new directory, you can now use `noSpaceName.sh`.  </br>

> Hindsight: </br>
> I believe you could skip this step and modify the Swift script to change spaces to '%20' instead of underscores </br>
I haven't tested this though. I'm keeping this `noSpaceName.sh` in the final cut because it is still a powerful tool.

### `noSpaceName.sh`
```bash
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
```
```shell
@Massimo [PROJECT] % cp noSpaceName.sh ~/Photos/Assets
@Massimo [PROJECT] % cd ~/Photos/Assets
@Massimo Assets % chmod +x noSpaceName.sh
@Massimo Assets % ./noSpaceName.sh
Renamed: Screenshot 2025-03-10 at 01.16.56.png -> Screenshot_2025-03-10_at_01.16.56.png
Renamed: Screenshot 2025-03-10 at 01.26.44.png -> Screenshot_2025-03-10_at_01.26.44.png
Renamed: Screenshot 2025-03-10 at 01.32.48.png -> Screenshot_2025-03-10_at_01.32.48.png
Renamed: Screenshot 2025-03-10 at 01.38.34.png -> Screenshot_2025-03-10_at_01.38.34.png
[.cut.]
Done.
@Massimo Assets % ls
Screenshot_2025-03-10_at_01.16.56.png
Screenshot_2025-03-10_at_01.26.44.png
Screenshot_2025-03-10_at_01.32.48.png
Screenshot_2025-03-10_at_01.38.34.png
[.cut.]
```
>You can now upload your images to your repository without any issues.

## Step 3: Reformat Note References for GitHub.

My notes app, Obsidian, uses a specific syntax for referencing images. GitHub is similar but uses a different syntax. </br> 
GitHub is also a completely different environment, so local references will require the complete path to the assets.

This Swift script is made to convert Markdown files using Obsidian syntax and converts them into the format that GitHub uses. </br>
This script affects all .md files in its directory. I recommend placing a copy of your notes with the script into a new directory.

Regex is used to identify the image reference pattern:
```
let pattern = #"!\[\[(Screenshot[^\]]+\.png)\]\]"#
```
And the "`/Local-GitHub/Assets-Path/`" is hardcoded, make sure to change this to match your environment.
```
let replacement = "![\(count)](/Wireshark/.assets/\(safeFilename))"
```
This will convert all references within the *.md files in the same directory as the script.
```
![[Screenshot 2025-03-24 at 15.36.15]] -> ![ANY](/Wireshark/.assets/Screenshot_2025-03-24_at_15.36.15)
```
### `macSS->Git.swift`
```swift
// Reformat obsidian.md image refrences to work on GitHub.

import Foundation

let currentDirectory = FileManager.default.currentDirectoryPath

// Locate all markdown files in the directory
func findMarkdownFiles(in directory: String) -> [String] {
    let enumerator = FileManager.default.enumerator(atPath: directory)
    var markdownFiles: [String] = []

    while let file = enumerator?.nextObject() as? String {
        if file.hasSuffix(".md") {
            markdownFiles.append("\(directory)/\(file)")
        }
    }

    return markdownFiles
}

// Process each markdown file
let markdownFiles = findMarkdownFiles(in: currentDirectory)

for markdownFile in markdownFiles {
    do {
        var content = try String(contentsOfFile: markdownFile, encoding: .utf8)
        var count = 1

        // Regular expression pattern to match MacBook's screenshot format.
        let pattern = #"!\[\[(Screenshot[^\]]+\.png)\]\]"#
        let regex = try NSRegularExpression(pattern: pattern, options: [])

        // Find all matches
        let matches = regex.matches(in: content, options: [], range: NSRange(content.startIndex..., in: content))

        for match in matches.reversed() {
            if let range = Range(match.range(at: 1), in: content) {
                let filename = content[range]

                // Convert spaces to underscores
                let safeFilename = filename.replacingOccurrences(of: " ", with: "_")

                // Create the replacement string
                let replacement = "![\(count)](/Wireshark/.assets/\(safeFilename))"
               
// Instead of /Wireshark/.assets/                           ^
// You Can Modify this to your "/Local-GitHub/Assets-Path/" |
                
                // Replace in content
                if let matchRange = Range(match.range, in: content) {
                    content.replaceSubrange(matchRange, with: replacement)
                }

                count += 1
            }
        }

        // Write the updated content back to the file
        try content.write(toFile: markdownFile, atomically: true, encoding: .utf8)

        print("Updated: \(markdownFile)")

    } catch {
        print("Error processing \(markdownFile): \(error)")
    }
}

print("Done.")
```
```shell
@Massimo [PROJECT] % mkdir Copy
@Massimo [PROJECT] % cp *.md Copy
@Massimo [PROJECT] % cd Copy
@Massimo Copy % chmod +x macSS->Git.swift
@Massimo Copy % swift macSS->Git.swift
Updated: /Users/massimopiccone/[PROJECT]/Copy/Traffic Analysis with Wireshark.md
Updated: /Users/massimopiccone/[PROJECT]/Copy/Other Malicious Traffic.md
Updated: /Users/massimopiccone/[PROJECT]/Copy/Examples of Non-Malicious Activity.md
Updated: /Users/massimopiccone/[PROJECT]/Copy/Intro to Windows MalwareInfections.md
Updated: /Users/massimopiccone/[PROJECT]/Copy/Incident report format.md
Updated: /Users/massimopiccone/[PROJECT]/Copy/Threat Hunting.md
Done.
```


## Summary
I employed a combination of Bash scripting and Swift scripting to optimize my workflow. This approach effectively eliminated numerous tedious and repetitive tasks, saving an immeasurable amount of time. The code is well-documented and includes comprehensive comments with troubleshooting snippets to identify potential issues. 

![Layout](/Scripts/.assets/Screenshot_2025-03-26_at_14.29.16.png)
