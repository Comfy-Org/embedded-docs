#!/usr/bin/env python3
"""
Replace placeholders in docs with language-specific headings
Usage: python replace_placeholders.py [--check-only]
"""

import os
import re
import sys
from pathlib import Path

import runtime  # noqa: F401
from lib.paths import embedded_docs_dir

DOCS_ROOT = embedded_docs_dir()

# Heading mapping per language
HEADING_TRANSLATIONS = {
    'en': {
        'heading_overview': '## Overview',
        'heading_inputs': '## Inputs',
        'heading_outputs': '## Outputs',
        'heading_usage': '## Usage',
        'heading_examples': '## Examples',
    },
    'zh': {
        'heading_overview': '## 概述',
        'heading_inputs': '## 输入',
        'heading_outputs': '## 输出',
        'heading_usage': '## 用法',
        'heading_examples': '## 示例',
    },
    'es': {
        'heading_overview': '## Descripción general',
        'heading_inputs': '## Entradas',
        'heading_outputs': '## Salidas',
        'heading_usage': '## Uso',
        'heading_examples': '## Ejemplos',
    },
    'fr': {
        'heading_overview': '## Aperçu',
        'heading_inputs': '## Entrées',
        'heading_outputs': '## Sorties',
        'heading_usage': '## Utilisation',
        'heading_examples': '## Exemples',
    },
    'ja': {
        'heading_overview': '## 概要',
        'heading_inputs': '## 入力',
        'heading_outputs': '## 出力',
        'heading_usage': '## 使用方法',
        'heading_examples': '## 例',
    },
    'ko': {
        'heading_overview': '## 개요',
        'heading_inputs': '## 입력',
        'heading_outputs': '## 출력',
        'heading_usage': '## 사용법',
        'heading_examples': '## 예시',
    },
    'ru': {
        'heading_overview': '## Обзор',
        'heading_inputs': '## Входы',
        'heading_outputs': '## Выходы',
        'heading_usage': '## Использование',
        'heading_examples': '## Примеры',
    },
}

def get_language_from_filename(filename):
    """Get the language code from a filename"""
    stem = Path(filename).stem
    return stem if stem in HEADING_TRANSLATIONS else None

def replace_placeholders_in_file(filepath, check_only=False):
    """Replace placeholders in a file"""
    lang = get_language_from_filename(filepath.name)
    if not lang:
        return False, []
    
    translations = HEADING_TRANSLATIONS[lang]
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    modified = False
    replacements = []
    
    for placeholder, heading in translations.items():
        pattern = '{' + placeholder + '}'
        if pattern in content:
            replacements.append(f"  {filepath.relative_to(DOCS_ROOT.parent.parent)}: {placeholder} -> {heading}")
            content = content.replace(pattern, heading)
            modified = True
    
    if modified and not check_only:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
    
    return modified, replacements

def main():
    check_only = '--check-only' in sys.argv
    
    files_with_placeholders = []
    all_replacements = []
    
    for root, _, files in os.walk(DOCS_ROOT):
        for fname in files:
            if fname.endswith('.md') or fname.endswith('.mdx'):
                fpath = Path(root) / fname
                modified, replacements = replace_placeholders_in_file(fpath, check_only)
                
                if modified:
                    files_with_placeholders.append(fpath)
                    all_replacements.extend(replacements)
    
    if files_with_placeholders:
        if check_only:
            print(f"\nFound {len(files_with_placeholders)} files with placeholders:")
            for repl in all_replacements:
                print(repl)
            print(f"\nRun without --check-only to replace these placeholders.")
            sys.exit(1)
        else:
            print(f"\nReplaced placeholders in {len(files_with_placeholders)} files:")
            for repl in all_replacements:
                print(repl)
            print(f"\n✓ Done!")
    else:
        print("✓ No placeholders found to replace.")

if __name__ == '__main__':
    main()

