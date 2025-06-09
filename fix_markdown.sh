#!/bin/bash
# Ensure markdownlint-cli is installed globally: npm install -g markdownlint-cli

# Get the folder path of the script
script_folder="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Set the base path
base_path="$script_folder/comfyui_embedded_docs/docs"

# Check if base path exists
if [ ! -d "$base_path" ]; then
    echo "Error: Base directory not found"
    exit 1
fi

# Set the target folder path
if [ -n "$1" ]; then
    target_folder="$base_path/$1"
    if [ ! -d "$target_folder" ]; then
        echo "Error: Subdirectory not found"
        exit 1
    fi
else
    target_folder="$base_path"
fi

# Find all markdown files in the target folder and subfolders
markdown_files=$(find "$target_folder" -type f -name "*.md")

# Check if any markdown files were found
if [ -z "$markdown_files" ]; then
    echo "No markdown files found"
    exit 0
fi

echo "Fixing markdown files..."

# Loop through each markdown file and fix linting issues
for file in $markdown_files; do
    # Run markdownlint and capture its output
    output=$(markdownlint --fix "$file" 2>&1)
    
    # Only show output if the file was modified
    if [ -n "$output" ]; then
        relative_path=${file#$base_path/}
        echo "Updated: $relative_path"
    fi
done

echo "Done!"
