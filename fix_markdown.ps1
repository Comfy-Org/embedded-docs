# Ensure markdownlint-cli is installed globally: npm install -g markdownlint-cli

# Get the folder path of the script
$scriptFolder = Split-Path -Parent $MyInvocation.MyCommand.Definition

# Define the sibling folder containing markdown files
$folderPath = Join-Path $scriptFolder ".\comfyui_embedded_docs\docs"

# Resolve the full path of the sibling folder
$resolvedFolderPath = Resolve-Path $folderPath

# Find all markdown files in the folder and subfolders
$markdownFiles = Get-ChildItem -Path $resolvedFolderPath -Recurse -Filter *.md

# Loop through each markdown file and fix linting issues
foreach ($file in $markdownFiles) {
    Write-Host "Fixing linting issues for: $($file.FullName)"
    markdownlint --fix $file.FullName
}

Write-Host "Markdown linting fixes completed!"