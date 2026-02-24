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

# Find all markdown files (null-delimited for paths with spaces)
markdown_files=()
while IFS= read -r -d '' f; do markdown_files+=("$f"); done < <(find "$target_folder" -type f -name "*.md" -print0 2>/dev/null)

# Check if any markdown files were found
if [ ${#markdown_files[@]} -eq 0 ]; then
    echo "No markdown files found"
    exit 0
fi

total=${#markdown_files[@]}
# Batch size to stay under system ARG_MAX (command-line length limit)
BATCH_SIZE=500
echo "Fixing $total markdown files (batches of $BATCH_SIZE)..."

batch=()
for f in "${markdown_files[@]}"; do
    batch+=("$f")
    if [ ${#batch[@]} -ge "$BATCH_SIZE" ]; then
        markdownlint --fix "${batch[@]}" 2>/dev/null || true
        batch=()
    fi
done
[ ${#batch[@]} -gt 0 ] && markdownlint --fix "${batch[@]}" 2>/dev/null || true

echo "Done!"
