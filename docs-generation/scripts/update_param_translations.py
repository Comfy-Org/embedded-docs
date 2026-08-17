#!/usr/bin/env python3
"""
Update parameter names in documentation to match frontend translations
Uses node_translations.json exported from frontend nodeDefs

The translations file is refreshed from GitHub (Comfy-Org/ComfyUI_frontend)
when it is missing or older than TRANSLATIONS_MAX_AGE_HOURS, so param
localization does not depend on a local frontend checkout being up to date.
"""

import argparse
import json
import os
import re
import sys
import time
from pathlib import Path

import runtime  # noqa: F401
from lib.frontend_source import fetch_remote_translations, save_translations
from lib.paths import NODE_TRANSLATIONS, embedded_docs_dir, load_dotenv

load_dotenv()

DOCS_ROOT = embedded_docs_dir().resolve()
TRANSLATIONS_FILE = NODE_TRANSLATIONS

# Refresh the translations file from GitHub when older than this (hours)
TRANSLATIONS_MAX_AGE_HOURS = 12

# Supported languages
SUPPORTED_LANGS = ['zh', 'zh-TW', 'es', 'fr', 'ja', 'ko', 'ru', 'ar', 'tr', 'pt-BR', 'fa']

# The shared node_translations.json is also consumed by lib/doc_title.py,
# which relies on the English display_name as fallback. Always include 'en'
# when (re)writing the file, even though this script only updates non-en docs.
FETCH_LANGS = ['en'] + SUPPORTED_LANGS

def load_frontend_translations(force_refresh=False):
    """Load frontend translations from exported JSON, refreshing from GitHub
    if the file is missing or stale (older than TRANSLATIONS_MAX_AGE_HOURS)."""
    stale = False
    if not TRANSLATIONS_FILE.exists():
        print(f"ℹ️  {TRANSLATIONS_FILE} not found")
        stale = True
    else:
        age_h = (time.time() - TRANSLATIONS_FILE.stat().st_mtime) / 3600
        if age_h > TRANSLATIONS_MAX_AGE_HOURS:
            print(f"ℹ️  Translations file is {age_h:.1f}h old (max {TRANSLATIONS_MAX_AGE_HOURS}h); refreshing from GitHub")
            stale = True

    if stale or force_refresh:
        print("📡 Fetching frontend translations from GitHub (Comfy-Org/ComfyUI_frontend@master)...")
        data = fetch_remote_translations(FETCH_LANGS)
        if any(data.values()):
            # Merge over the existing file (atomic write) so languages whose
            # fetch failed and keys not managed here are preserved.
            merged = save_translations(TRANSLATIONS_FILE, data)
            print(f"✓ Refreshed {TRANSLATIONS_FILE} from GitHub")
            return merged
        # Fetch failed: fall back to existing file
        if TRANSLATIONS_FILE.exists():
            print("⚠️  GitHub fetch failed; using existing local translations file")
        else:
            print("❌ Error: no translations available (GitHub fetch failed and no local file)")
            print("   Please run: python sync_frontend_translations.py --export")
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
    # DynamicCombo sub-params: frontend key uses underscores (model_aspect_ratio),
    # docs may write dot form with prefix separator (model.aspect_ratio) or full
    # dot form (model.aspect.ratio). Try all variants.
    variants = [
        old_param_name,
        old_param_name.replace("_", ".", 1),
        old_param_name.replace("_", "."),
    ]
    for v in variants:
        pattern = rf'\|\s*`{re.escape(v)}`\s*\|'
        if re.search(pattern, row):
            return re.sub(pattern, f'| `{new_param_name}` |', row)
    return row

def update_doc_with_translations(doc_file, node_name, lang, frontend_translations, dry_run=False):
    """Update a documentation file with frontend translations.

    When ``dry_run`` is True, compute changes but never write to disk.
    """
    
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
    
    # Update input parameter names, restricted to the Inputs table so
    # same-named rows in Outputs or other tables are not touched.
    if 'inputs' in node_trans:
        renames = {}
        for param_name, param_data in node_trans['inputs'].items():
            if not isinstance(param_data, dict):
                continue
            frontend_name = param_data.get('name', '')
            if frontend_name and frontend_name != param_name:
                renames[param_name] = frontend_name
        if renames:
            lines = content.split('\n')
            in_input_section = False
            for i, line in enumerate(lines):
                # Detect if we're in the Inputs section.
                # Only H2 (## X) opens/closes a section; H3 (### X) subheadings
                # like "### Common Inputs" must NOT close it.
                if re.match(r'^##\s+(?:输入|輸入|入力|입력|Входы|Entradas|Entrées|Inputs|المدخلات|Girdiler|ورودی‌ها)', line):
                    in_input_section = True
                    continue
                elif re.match(r'^##(?!\s*#)', line):
                    in_input_section = False
                    continue
                if not (in_input_section and line.strip().startswith('|')):
                    continue
                for param_name, frontend_name in renames.items():
                    updated = update_parameter_name_in_row(line, param_name, frontend_name)
                    if updated != line:
                        lines[i] = updated
                        line = updated
                        changes_made.append(f"[Input] {param_name} → {frontend_name}")
                        break
            content = '\n'.join(lines)
    
    # Update output parameter names
    if 'outputs' in node_trans:
        lines = content.split('\n')
        in_output_section = False
        output_row_index = 0  # Track which output row we're on (0-indexed)
        
        for i, line in enumerate(lines):
            # Detect if we're in the Outputs section
            if re.match(r'##\s+(?:输出|輸出|出力|출력|Выходы|Salidas|Sorties|Outputs|المخرجات|Çıktılar|خروجی‌ها)', line):
                in_output_section = True
                output_row_index = 0
                continue
            elif re.match(r'^##(?!\s*#)', line):
                in_output_section = False
                continue
            
            # Update output names in the table (skip header and separator rows)
            if in_output_section and line.strip().startswith('|'):
                # Skip table header and separator
                if '---' in line:
                    continue
            
                # Skip any row where the first column doesn't have a backtick (header in any language)
                if not re.match(r'\|\s*`', line):
                    continue
                
                # This is an actual data row
                output_idx_str = str(output_row_index)
                if output_idx_str in node_trans['outputs']:
                    output_data = node_trans['outputs'][output_idx_str]
                    if not isinstance(output_data, dict):
                        output_row_index += 1
                        continue
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
    
    # Save if changes were made (never write in dry-run mode)
    if content != original_content:
        if not dry_run:
            with open(doc_file, 'w', encoding='utf-8') as f:
                f.write(content)
        return True, changes_made
    
    return False, []

def main():
    """Main function"""

    parser = argparse.ArgumentParser(
        description="Update parameter names in docs to match frontend translations"
    )
    parser.add_argument("--lang", default=None,
                        help=f"Target language (default: all of {' '.join(SUPPORTED_LANGS)})")
    parser.add_argument("--node", default=None, help="Process a single node directory")
    parser.add_argument("--dry-run", action="store_true",
                        help="Preview changes without writing files")
    parser.add_argument("--refresh", action="store_true",
                        help="Force re-fetch of frontend translations from GitHub")
    args = parser.parse_args()

    if args.lang and args.lang not in SUPPORTED_LANGS:
        print(f"❌ Error: unknown language '{args.lang}'")
        print(f"   Supported: {', '.join(SUPPORTED_LANGS)}")
        sys.exit(1)

    target_lang = args.lang
    target_node = args.node
    dry_run = args.dry_run
    force_refresh = args.refresh
    
    print("=" * 80)
    print("Parameter Translation Updater")
    print("=" * 80)
    print(f"Docs root: {DOCS_ROOT}")
    print(f"Translations file: {TRANSLATIONS_FILE}")
    print(f"Target language: {target_lang or 'ALL'}")
    print(f"Target node: {target_node or 'ALL'}")
    print(f"Mode: {'Dry run (preview only)' if dry_run else 'Update files'}")
    print("=" * 80)
    print()
    
    # Load frontend translations
    print("📖 Loading frontend translations...")
    frontend_trans = load_frontend_translations(force_refresh=force_refresh)
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
            
            # Update document (update_doc_with_translations honors dry_run internally)
            updated, changes = update_doc_with_translations(
                doc_file, node_name, lang, frontend_trans, dry_run=dry_run
            )

            if updated:
                prefix = "🔍 Would update" if dry_run else "✅ Updated"
                print(f"{prefix} {node_name} ({lang}): {', '.join(changes)}")
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

