#!/bin/bash
# Ensure markdownlint-cli is installed globally: npm install -g markdownlint-cli

# Get the folder path of the script
script_folder="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Set the base path
base_path="$script_folder/comfyui_embedded_docs/docs"

# Check if base path exists
if [ ! -d "$base_path" ]; then
    echo "Error: Base directory '$base_path' does not exist!"
    exit 1
fi

# Set the target folder path
if [ -n "$1" ]; then
    # If subdirectory is provided, check if it exists in base path
    target_folder="$base_path/$1"
    if [ ! -d "$target_folder" ]; then
        echo "Error: Subdirectory '$1' not found in $base_path"
        exit 1
    fi
    echo "Checking markdown files in subdirectory: $1"
else
    # Use base path to check all files
    target_folder="$base_path"
    echo "Checking all markdown files in: $base_path"
fi

# Find all markdown files in the target folder and subfolders
markdown_files=$(find "$target_folder" -type f -name "*.md")

# Check if any markdown files were found
if [ -z "$markdown_files" ]; then
    echo "No markdown files found in specified path"
    exit 0
fi

# Loop through each markdown file and fix linting issues
for file in $markdown_files; do
    # Get relative path for cleaner output
    relative_path=${file#$base_path/}
    echo "Fixing linting issues for: $relative_path"
    markdownlint --fix "$file"
done

echo "Markdown linting fixes completed!"
