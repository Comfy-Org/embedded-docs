#!/usr/bin/env python3
"""
Check link validity and placeholders in Markdown docs
Usage: python check_md_links.py [--fix-placeholders]
"""

import os
import re
import sys
from pathlib import Path

import runtime  # noqa: F401
from lib.paths import embedded_docs_dir

DOCS_ROOT = embedded_docs_dir()

# Supported file extensions
doc_exts = {'.md', '.mdx'}

# Match Markdown images/links and HTML img/video/audio/source tag src attributes
MD_LINK_RE = re.compile(r'!\[[^\]]*\]\(([^)]+)\)|\[[^\]]*\]\(([^)]+)\)')
HTML_SRC_RE = re.compile(r'<(?:img|video|audio|source)[^>]+src=["\']([^"\'>]+)["\']', re.IGNORECASE)
PLACEHOLDER_RE = re.compile(r'\{(heading_\w+)\}')

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

def is_local_link(link):
    """Only check local relative paths (not http/https/data: prefixed)"""
    link = link.strip()
    return not (link.startswith('http://') or link.startswith('https://') or link.startswith('data:'))

def find_links_in_line(line):
    """Extract all local links in a line"""
    links = []
    for m in MD_LINK_RE.finditer(line):
        for g in m.groups():
            if g and is_local_link(g):
                links.append(g)
    for m in HTML_SRC_RE.finditer(line):
        g = m.group(1)
        if g and is_local_link(g):
            links.append(g)
    return links

def find_placeholders_in_content(content):
    """Find placeholders in content"""
    return PLACEHOLDER_RE.findall(content)

def check_file(fpath, fix_placeholders=False):
    """Check links and placeholders in a single file"""
    errors = []
    placeholder_issues = []
    rel_fpath = fpath.relative_to(DOCS_ROOT.parent.parent)
    lang = get_language_from_filename(fpath.name)
    
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
        lines = content.split('\n')
    
    # Check placeholders
    placeholders = find_placeholders_in_content(content)
    if placeholders:
        placeholder_issues.append(f"{rel_fpath}: found placeholders {placeholders}")
        
        # Fix if requested and language is detectable
        if fix_placeholders and lang:
            translations = HEADING_TRANSLATIONS[lang]
            modified = False
            for placeholder in placeholders:
                pattern = '{' + placeholder + '}'
                if placeholder in translations:
                    content = content.replace(pattern, translations[placeholder])
                    modified = True
            
            if modified:
                with open(fpath, 'w', encoding='utf-8') as f:
                    f.write(content)
                placeholder_issues[-1] += " [fixed]"
    
    # Check links
    for idx, line in enumerate(lines, 1):
        for link in find_links_in_line(line):
            link_path = link.split('#')[0].split('?')[0]
            if not link_path:
                continue
            
            if link_path.startswith('/'):
                abs_path = DOCS_ROOT / link_path.lstrip('/')
            else:
                try:
                    abs_path = (fpath.parent / link_path).resolve()
                    if not abs_path.exists():
                        abs_path_alt = (fpath.parent / link_path).absolute()
                        if abs_path_alt.exists():
                            abs_path = abs_path_alt
                except (OSError, ValueError):
                    abs_path = (fpath.parent / link_path).absolute()
            
            if not abs_path.exists():
                errors.append(f"[broken link] {rel_fpath}:{idx}: {link}")
    
    return errors, placeholder_issues

def check_links():
    if not DOCS_ROOT.exists():
        print(f"Error: docs directory does not exist: {DOCS_ROOT}")
        sys.exit(1)
    
    fix_placeholders = '--fix-placeholders' in sys.argv
    link_errors = []
    placeholder_issues = []
    
    print(f"Checking all docs under {DOCS_ROOT}...")
    
    for root, _, files in os.walk(DOCS_ROOT):
        for fname in files:
            if Path(fname).suffix.lower() in doc_exts:
                fpath = Path(root) / fname
                errors, placeholders = check_file(fpath, fix_placeholders)
                link_errors.extend(errors)
                placeholder_issues.extend(placeholders)
    
    has_issues = False
    
    if placeholder_issues:
        has_issues = True
        print("\n" + "=" * 80)
        print(f"Found {len(placeholder_issues)} files with placeholders:")
        print("=" * 80)
        for issue in placeholder_issues:
            print(f"  {issue}")
        if fix_placeholders:
            print("\n✓ Placeholders auto-fixed")
        else:
            print("\nTip: run with --fix-placeholders to auto-replace placeholders")
    
    if link_errors:
        has_issues = True
        print("\n" + "=" * 80)
        print(f"Found {len(link_errors)} broken links:")
        print("=" * 80)
        for i, err in enumerate(link_errors):
            if i < 10:
                print(f"  {err}")
            elif i == 10:
                print(f"\n  ... {len(link_errors) - 10} more errors (showing first 10 only)")
                break
        print("\nPlease fix the link issues above.")
    
    if not has_issues:
        print("\n✓ All checks passed!")
    else:
        sys.exit(1)

if __name__ == '__main__':
    check_links()
