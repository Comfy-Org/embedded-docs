#!/usr/bin/env python3
"""
Sync parameter translations from the frontend repo's nodeDefs.json into the docs
Usage: python sync_frontend_translations.py <frontend_repo_path>
Example: python sync_frontend_translations.py /path/to/ComfyUI_frontend
"""

import json
import os
import sys
from pathlib import Path

import runtime  # noqa: F401
from lib.paths import NODE_TRANSLATIONS, embedded_docs_dir, load_dotenv

load_dotenv()

DOCS_ROOT = embedded_docs_dir()

# Supported languages
SUPPORTED_LANGS = ['en', 'zh', 'zh-TW', 'es', 'fr', 'ja', 'ko', 'ru', 'ar', 'tr', 'pt-BR', 'fa']

def load_frontend_translations(frontend_path, lang):
    """Load translations for a language from the frontend repo"""
    locale_file = Path(frontend_path) / 'src' / 'locales' / lang / 'nodeDefs.json'
    
    if not locale_file.exists():
        print(f"⚠️  Warning: language file not found for {lang}: {locale_file}")
        return {}
    
    try:
        with open(locale_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"❌ Failed to read language file for {lang}: {e}")
        return {}

def get_node_translations(frontend_translations, node_name):
    """Get translation info for a node"""
    if node_name not in frontend_translations:
        return None
    
    node_data = frontend_translations[node_name]
    translations = {
        'display_name': node_data.get('display_name', ''),
        'description': node_data.get('description', ''),
        'inputs': {},
        'outputs': {}
    }
    
    # Extract input parameter translations
    if 'inputs' in node_data:
        for param_name, param_data in node_data['inputs'].items():
            if isinstance(param_data, dict):
                translations['inputs'][param_name] = {
                    'name': param_data.get('name', param_name),
                    'tooltip': param_data.get('tooltip', '')
                }
    
    # Extract output translations
    if 'outputs' in node_data:
        for output_idx, output_data in node_data['outputs'].items():
            if isinstance(output_data, dict):
                translations['outputs'][output_idx] = {
                    'name': output_data.get('name', ''),
                    'tooltip': output_data.get('tooltip', '')
                }
    
    return translations

def create_translation_report(frontend_path):
    """Generate a translation comparison report"""
    print(f"\nLoading translations from frontend repo: {frontend_path}\n")
    
    # Load translations for all languages
    all_translations = {}
    for lang in SUPPORTED_LANGS:
        all_translations[lang] = load_frontend_translations(frontend_path, lang)
    
    # Get all node names (from the docs directory)
    node_dirs = [d for d in DOCS_ROOT.iterdir() if d.is_dir()]
    
    print(f"Found {len(node_dirs)} node doc directories\n")
    print("=" * 80)
    
    # Generate a translation report per node
    for node_dir in sorted(node_dirs):
        node_name = node_dir.name
        
        # Check whether a frontend translation exists
        has_translation = any(node_name in all_translations[lang] for lang in SUPPORTED_LANGS)
        
        if not has_translation:
            print(f"\n⚠️  {node_name}: no frontend translation found")
            continue
        
        print(f"\n✓ {node_name}")
        print("-" * 80)
        
        # Show per-language parameter translations
        for lang in SUPPORTED_LANGS:
            if node_name in all_translations[lang]:
                trans = get_node_translations(all_translations[lang], node_name)
                if trans and trans['inputs']:
                    print(f"\n  [{lang.upper()}] Parameter translations:")
                    for param_name, param_trans in trans['inputs'].items():
                        print(f"    - {param_name}: {param_trans['name']}")
                        if param_trans['tooltip']:
                            print(f"      Tooltip: {param_trans['tooltip'][:60]}...")

def export_translation_json(frontend_path, output_file=None):
    """Export all node translations to a JSON file for later use"""
    all_translations = {}
    for lang in SUPPORTED_LANGS:
        all_translations[lang] = load_frontend_translations(frontend_path, lang)
    
    output_path = NODE_TRANSLATIONS if output_file is None else Path(output_file)
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(all_translations, f, ensure_ascii=False, indent=2)
    
    print(f"\n✓ Translation data exported to: {output_path}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python sync_frontend_translations.py <frontend_repo_path> [--export]")
        print("Example: python sync_frontend_translations.py /path/to/ComfyUI_frontend")
        print("\nOptions:")
        print("  --export  export translations to JSON file")
        sys.exit(1)
    
    frontend_path = Path(sys.argv[1])
    
    if not frontend_path.exists():
        print(f"❌ Error: frontend repo path does not exist: {frontend_path}")
        sys.exit(1)
    
    if '--export' in sys.argv:
        export_translation_json(frontend_path)
    else:
        create_translation_report(frontend_path)

if __name__ == '__main__':
    main()

