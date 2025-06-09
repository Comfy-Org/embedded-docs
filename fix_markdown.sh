#!/bin/bash
# Ensure markdownlint-cli is installed globally: npm install -g markdownlint-cli

# Get the folder path of the script
script_folder="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Define the sibling folder containing markdown files
folder_path="$script_folder/comfyui_embedded_docs/docs"

# Resolve the full path of the sibling folder
resolved_folder_path="$(realpath "$folder_path")"

# Find all markdown files in the folder and subfolders
markdown_files=$(find "$resolved_folder_path" -type f -name "*.md")

# Loop through each markdown file and fix linting issues
for file in $markdown_files; do
    echo "Fixing linting issues for: $file"
    markdownlint --fix "$file"
done

echo "Markdown linting fixes completed!"
