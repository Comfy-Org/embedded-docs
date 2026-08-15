#!/usr/bin/env python3
"""
Sync parameter translations from the frontend repo's nodeDefs.json into the docs

Sources (in priority order):
1. Remote: Comfy-Org/ComfyUI_frontend nodeDefs.json via raw.githubusercontent.com
   (default when no local path is given, or when --remote is passed)
2. Local: a checked-out ComfyUI_frontend repo (fallback, offline-capable)

Usage:
  python sync_frontend_translations.py --export                 # fetch from GitHub
  python sync_frontend_translations.py /path/to/ComfyUI_frontend --export  # local repo
"""

import json
import os
import sys
import urllib.request
from pathlib import Path

import runtime  # noqa: F401
from lib.paths import NODE_TRANSLATIONS, embedded_docs_dir, load_dotenv

load_dotenv()

DOCS_ROOT = embedded_docs_dir()

# Supported languages
SUPPORTED_LANGS = ['en', 'zh', 'zh-TW', 'es', 'fr', 'ja', 'ko', 'ru', 'ar', 'tr', 'pt-BR', 'fa']

# Default remote source: ComfyUI frontend repo on GitHub (master branch)
REMOTE_REPO = "Comfy-Org/ComfyUI_frontend"
REMOTE_BRANCH = "master"
REMOTE_BASE = f"https://raw.githubusercontent.com/{REMOTE_REPO}/{REMOTE_BRANCH}/src/locales"

def load_frontend_translations(frontend_path, lang, use_remote=False):
    """Load translations for a language from the frontend repo (remote or local)"""
    if use_remote or frontend_path is None:
        return load_frontend_translations_remote(lang)
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

def load_frontend_translations_remote(lang):
    """Fetch nodeDefs.json for a language from GitHub raw (master branch)"""
    url = f"{REMOTE_BASE}/{lang}/nodeDefs.json"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "docs-generation"})
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except Exception as e:
        print(f"⚠️  Warning: failed to fetch {lang} from GitHub ({url}): {e}")
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

def export_translation_json(frontend_path, output_file=None, use_remote=False):
    """Export all node translations to a JSON file for later use"""
    source_desc = "GitHub (remote)" if (use_remote or frontend_path is None) else str(frontend_path)
    print(f"Loading translations from: {source_desc}")
    all_translations = {}
    for lang in SUPPORTED_LANGS:
        all_translations[lang] = load_frontend_translations(frontend_path, lang, use_remote=use_remote)
    
    output_path = NODE_TRANSLATIONS if output_file is None else Path(output_file)
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(all_translations, f, ensure_ascii=False, indent=2)
    
    print(f"\n✓ Translation data exported to: {output_path}")
    print(f"  Source: {source_desc}")

def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    flags = [a for a in sys.argv[1:] if a.startswith('--')]
    use_remote = '--remote' in flags
    do_export = '--export' in flags
    
    # No positional path + no --remote: default to remote GitHub source
    if not args:
        if use_remote or do_export:
            frontend_path = None
        else:
            print("Usage:")
            print("  python sync_frontend_translations.py --export                # fetch from GitHub (default)")
            print("  python sync_frontend_translations.py --remote --export       # force remote")
            print("  python sync_frontend_translations.py /path/to/ComfyUI_frontend [--export]  # local repo")
            print("  python sync_frontend_translations.py --report                # report only")
            sys.exit(1)
    else:
        frontend_path = Path(args[0])
        if frontend_path.exists():
            # Local path given: use it unless --remote forces GitHub
            if use_remote:
                print("⚠️  --remote given; using GitHub source (ignoring local path)")
                frontend_path = None
        else:
            print(f"⚠️  Path does not exist ({frontend_path}); falling back to GitHub source")
            frontend_path = None
    
    if do_export or frontend_path is None:
        export_translation_json(frontend_path, use_remote=use_remote)
    else:
        create_translation_report(frontend_path)

if __name__ == '__main__':
    main()

