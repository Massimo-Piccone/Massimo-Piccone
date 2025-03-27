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
