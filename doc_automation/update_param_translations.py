#!/usr/bin/env python3
"""
Update parameter names in documentation to match frontend translations
Uses node_translations.json exported from frontend nodeDefs
"""

import json
import re
import sys
from pathlib import Path

# Paths
DOC_AUTOMATION_PATH = Path(__file__).parent
DOCS_ROOT = DOC_AUTOMATION_PATH.parent / 'comfyui_embedded_docs' / 'docs'
TRANSLATIONS_FILE = DOC_AUTOMATION_PATH / 'node_translations.json'

# Supported languages
SUPPORTED_LANGS = ['zh', 'zh-TW', 'es', 'fr', 'ja', 'ko', 'ru', 'ar', 'tr', 'pt-BR', 'fa']

def load_frontend_translations():
    """Load frontend translations from exported JSON"""
    if not TRANSLATIONS_FILE.exists():
        print(f"❌ Error: {TRANSLATIONS_FILE} not found")
        print("   Please run: python sync_frontend_translations.py <frontend_path> --export")
        sys.exit(1)
    
    with open(TRANSLATIONS_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def extract_table_rows(content, table_type='inputs'):
    """Extract rows from Inputs or Outputs table"""
    # Find the table section
    if table_type == 'inputs':
        pattern = r'##\s+(?:输入|輸入|入力|입력|Входы|Entradas|Entrées|Inputs|المدخلات|Girdiler|ورودی‌ها)\s*\n\n(.*?)(?=\n##|\Z)'
    else:
        pattern = r'##\s+(?:输出|輸出|出力|출력|Выходы|Salidas|Sorties|Outputs|المخرجات|Çıktılar|خروجی‌ها)\s*\n\n(.*?)(?=\n##|\Z)'
    
    match = re.search(pattern, content, re.DOTALL)
    if not match:
        return None, None
    
    table_section = match.group(1)
    table_start = match.start(1)
    
    # Extract table lines
    lines = table_section.strip().split('\n')
    if len(lines) < 3:  # Must have header, separator, and at least one row
        return None, None
    
    return lines, table_start

def update_parameter_name_in_row(row, old_param_name, new_param_name):
    """Update parameter name in a table row while preserving backticks and structure"""
    # Parameter name is typically in the first column with backticks
    pattern = rf'\|\s*`{re.escape(old_param_name)}`\s*\|'
    replacement = f'| `{new_param_name}` |'
    return re.sub(pattern, replacement, row)

def update_doc_with_translations(doc_file, node_name, lang, frontend_translations):
    """Update a documentation file with frontend translations"""
    
    # Get translations for this node and language
    if lang not in frontend_translations:
        return False, "Language not in translations"
    
    if node_name not in frontend_translations[lang]:
        return False, "Node not in frontend translations"
    
    node_trans = frontend_translations[lang][node_name]
    
    # Read current documentation
    with open(doc_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    changes_made = []
    
    # Update input parameter names
    if 'inputs' in node_trans:
        for param_name, param_data in node_trans['inputs'].items():
            frontend_name = param_data.get('name', '')
            if frontend_name and frontend_name != param_name:
                # Try to find and replace the parameter name in the table
                old_pattern = f'`{param_name}`'
                if old_pattern in content:
                    # Only replace in table rows (lines starting with |)
                    lines = content.split('\n')
                    for i, line in enumerate(lines):
                        if line.strip().startswith('|') and old_pattern in line:
                            # This is a table row with the parameter
                            lines[i] = line.replace(f'`{param_name}`', f'`{frontend_name}`', 1)
                            changes_made.append(f"[Input] {param_name} → {frontend_name}")
                    content = '\n'.join(lines)
    
    # Update output parameter names
    if 'outputs' in node_trans:
        lines = content.split('\n')
        in_output_section = False
        output_row_index = 0  # Track which output row we're on (0-indexed)
        
        for i, line in enumerate(lines):
            # Detect if we're in the Outputs section
            if re.match(r'##\s+(?:输出|輸出|出力|출력|Выходы|Salidas|Sorties|Outputs|المخرجات|Çıktılar)', line):
                in_output_section = True
                output_row_index = 0
                continue
            elif line.startswith('##'):
                in_output_section = False
                continue
            
            # Update output names in the table (skip header and separator rows)
            if in_output_section and line.strip().startswith('|'):
                # Skip table header and separator
                if 'Output Name' in line or 'Data Type' in line or '---' in line:
                    continue
                
                # This is an actual data row
                output_idx_str = str(output_row_index)
                if output_idx_str in node_trans['outputs']:
                    output_data = node_trans['outputs'][output_idx_str]
                    frontend_name = output_data.get('name', '')
                    
                    if frontend_name:
                        # Replace the output name in the first column
                        # Format: | `OldName` | DataType | Description |
                        old_match = re.match(r'(\|\s*)`([^`]+)`(\s*\|)', line)
                        if old_match:
                            old_name = old_match.group(2)
                            lines[i] = re.sub(
                                r'(\|\s*)`[^`]+`(\s*\|)',
                                f'\\1`{frontend_name}`\\2',
                                line,
                                count=1
                            )
                            changes_made.append(f"[Output] {old_name} → {frontend_name}")
                
                output_row_index += 1
        
        content = '\n'.join(lines)
    
    # Save if changes were made
    if content != original_content:
        with open(doc_file, 'w', encoding='utf-8') as f:
            f.write(content)
        return True, changes_made
    
    return False, []

def main():
    """Main function"""
    
    # Parse arguments
    target_lang = None
    target_node = None
    dry_run = False
    
    for i, arg in enumerate(sys.argv[1:]):
        if arg == '--lang':
            target_lang = sys.argv[i + 2] if i + 2 < len(sys.argv) else None
        elif arg == '--node':
            target_node = sys.argv[i + 2] if i + 2 < len(sys.argv) else None
        elif arg == '--dry-run':
            dry_run = True
    
    print("=" * 80)
    print("Parameter Translation Updater")
    print("=" * 80)
    print(f"Target language: {target_lang or 'ALL'}")
    print(f"Target node: {target_node or 'ALL'}")
    print(f"Mode: {'Dry run (preview only)' if dry_run else 'Update files'}")
    print("=" * 80)
    print()
    
    # Load frontend translations
    print("📖 Loading frontend translations...")
    frontend_trans = load_frontend_translations()
    print(f"   Loaded translations for {len(SUPPORTED_LANGS)} languages\n")
    
    # Get list of nodes to process
    if target_node:
        node_dirs = [DOCS_ROOT / target_node]
        if not node_dirs[0].exists():
            print(f"❌ Error: Node directory not found: {node_dirs[0]}")
            sys.exit(1)
    else:
        node_dirs = [d for d in DOCS_ROOT.iterdir() if d.is_dir()]
    
    # Process each node
    total_updated = 0
    total_skipped = 0
    
    for node_dir in sorted(node_dirs):
        node_name = node_dir.name
        
        # Determine which languages to process
        langs_to_process = [target_lang] if target_lang else SUPPORTED_LANGS
        
        for lang in langs_to_process:
            if lang == 'en':  # Skip English (it's the source)
                continue
            
            doc_file = node_dir / f"{lang}.md"
            if not doc_file.exists():
                continue
            
            # Update document
            if not dry_run:
                updated, changes = update_doc_with_translations(doc_file, node_name, lang, frontend_trans)
                
                if updated:
                    print(f"✅ Updated {node_name} ({lang}): {', '.join(changes)}")
                    total_updated += 1
                else:
                    total_skipped += 1
            else:
                # Dry run - just check
                _, changes = update_doc_with_translations(doc_file, node_name, lang, frontend_trans)
                if changes:
                    print(f"🔍 Would update {node_name} ({lang}): {', '.join(changes)}")
                    total_updated += 1
                else:
                    total_skipped += 1
    
    print("\n" + "=" * 80)
    print("📊 Summary")
    print("=" * 80)
    print(f"✅ Updated: {total_updated}")
    print(f"⏭️  Skipped: {total_skipped}")
    if dry_run:
        print("\n💡 Run without --dry-run to apply changes")
    print("=" * 80)

if __name__ == '__main__':
    main()

