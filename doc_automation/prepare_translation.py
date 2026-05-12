#!/usr/bin/env python3
"""
Prepare translation batch list from missing_nodes_report.json
Verifies that files truly don't exist before adding to batch
"""

import argparse
import json
import os
import sys
from pathlib import Path

# Paths from environment variables
DOC_AUTOMATION_PATH = Path(__file__).parent
EMBEDDED_DOCS_PATH = Path(os.getenv('EMBEDDED_DOCS_PATH', DOC_AUTOMATION_PATH.parent))
DOCS_PATH = EMBEDDED_DOCS_PATH / "comfyui_embedded_docs" / "docs"
REPORT_FILE = DOC_AUTOMATION_PATH / "missing_nodes_report.json"
TRANSLATION_OUTPUT_DIR = DOC_AUTOMATION_PATH / "translation_batches"
TRANSLATION_CONFIG_FILE = DOC_AUTOMATION_PATH / "translation_config.json"

def main():
    """Main function"""
    parser = argparse.ArgumentParser(description="Prepare translation batch from missing_nodes_report.json")
    parser.add_argument("--lang", required=True, help="Target language code (e.g. zh, es)")
    parser.add_argument("--mode", choices=("test", "all"), default="all",
                        help="test = first N nodes, all = all missing (default: all)")
    parser.add_argument("--count", type=int, default=20,
                        help="Max nodes in test mode (default: 20)")
    args = parser.parse_args()
    target_lang = args.lang
    mode = args.mode
    count = args.count

    # Load translation config to validate language
    with open(TRANSLATION_CONFIG_FILE, 'r', encoding='utf-8') as f:
        translation_config = json.load(f)
    
    if not target_lang or target_lang not in translation_config:
        print("Error: Please specify a valid target language with --lang")
        print(f"Available languages: {', '.join(translation_config.keys())}")
        sys.exit(1)
    
    lang_info = translation_config[target_lang]
    
    print("=" * 80)
    print("ComfyUI Translation Batch Preparation")
    print("=" * 80)
    print(f"\nTarget language: {lang_info['name']} ({target_lang})")
    print(f"Mode: {mode}")
    if mode == "test":
        print(f"Count: {count}")
    print()
    
    # Load report
    if not REPORT_FILE.exists():
        print(f"❌ Error: Report file not found: {REPORT_FILE}")
        print("   Please run: python3 scan_missing_nodes.py first")
        sys.exit(1)
    
    with open(REPORT_FILE, 'r', encoding='utf-8') as f:
        report = json.load(f)
    
    # Get nodes missing target language from JSON
    print(f"📊 Reading missing translations from {REPORT_FILE.name}...")
    nodes_from_json = []
    for doc in report.get('incomplete_docs', []):
        if target_lang in doc.get('missing_languages', []):
            nodes_from_json.append(doc['node'])
    
    print(f"   Found {len(nodes_from_json)} nodes marked as missing {target_lang} in JSON")
    
    # Verify which ones truly don't have the translation file
    print(f"\n🔍 Verifying actual file status...")
    nodes_truly_missing = []
    nodes_already_exist = []
    
    for node_name in nodes_from_json:
        # Check if English source exists
        source_file = DOCS_PATH / node_name / "en.md"
        if not source_file.exists():
            print(f"   ⚠️  Skipping {node_name}: No English source")
            continue
        
        # Check if target translation exists
        target_file = DOCS_PATH / node_name / f"{target_lang}.md"
        if target_file.exists():
            nodes_already_exist.append(node_name)
        else:
            nodes_truly_missing.append(node_name)
    
    print(f"   ✅ Truly missing: {len(nodes_truly_missing)}")
    print(f"   ⏭️  Already exist: {len(nodes_already_exist)}")
    
    # Update JSON to remove nodes that already have translations
    if nodes_already_exist:
        print(f"\n🔄 Updating {REPORT_FILE.name} to remove {len(nodes_already_exist)} nodes that already exist...")
        updated_incomplete_docs = []
        for doc in report.get('incomplete_docs', []):
            if doc['node'] in nodes_already_exist and target_lang in doc.get('missing_languages', []):
                # Remove this language from missing_languages
                doc['missing_languages'] = [lang for lang in doc['missing_languages'] if lang != target_lang]
            # Only keep if still has missing languages
            if doc.get('missing_languages'):
                updated_incomplete_docs.append(doc)
        
        report['incomplete_docs'] = updated_incomplete_docs
        
        # Save updated report
        with open(REPORT_FILE, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        print(f"   ✅ Updated {REPORT_FILE.name}")
    
    if not nodes_truly_missing:
        print(f"\n✅ All nodes already have {target_lang} translation!")
        # Write empty batch so batch_translate_docs can run and do nothing (avoids reusing old batch)
        TRANSLATION_OUTPUT_DIR.mkdir(exist_ok=True)
        batch_data = {
            'target_language': target_lang,
            'language_name': lang_info['name'],
            'nodes': [],
            'total': 0,
            'truly_missing': 0,
            'already_exist': len(nodes_already_exist)
        }
        batch_file = TRANSLATION_OUTPUT_DIR / f"batch_{target_lang}.json"
        with open(batch_file, 'w', encoding='utf-8') as f:
            json.dump(batch_data, f, indent=2, ensure_ascii=False)
        print(f"📋 Empty batch written: {batch_file}")
        return

    # Determine which nodes to process
    if mode == "test":
        nodes_to_process = nodes_truly_missing[:count]
        print(f"\n🚀 Test mode: Preparing batch for {len(nodes_to_process)} nodes")
    else:
        nodes_to_process = nodes_truly_missing
        print(f"\n🚀 Full mode: Preparing batch for all {len(nodes_to_process)} nodes")
    
    # Create output directory
    TRANSLATION_OUTPUT_DIR.mkdir(exist_ok=True)
    
    # Create batch file
    batch_data = {
        'target_language': target_lang,
        'language_name': lang_info['name'],
        'nodes': nodes_to_process,
        'total': len(nodes_to_process),
        'truly_missing': len(nodes_truly_missing),
        'already_exist': len(nodes_already_exist)
    }
    
    batch_file = TRANSLATION_OUTPUT_DIR / f"batch_{target_lang}.json"
    with open(batch_file, 'w', encoding='utf-8') as f:
        json.dump(batch_data, f, indent=2, ensure_ascii=False)
    
    print("\n" + "=" * 80)
    print("📊 Batch Preparation Summary")
    print("=" * 80)
    print(f"✅ Nodes to translate: {len(nodes_to_process)}")
    print(f"📋 Batch file: {batch_file}")
    print(f"\n💡 Next: python3 batch_translate_docs.py --lang {target_lang} --mode {mode} --count {count}")
    print("=" * 80)

if __name__ == "__main__":
    main()
