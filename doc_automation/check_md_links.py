#!/usr/bin/env python3
"""
检查 Markdown 文档中的链接有效性和占位符
用法: python check_md_links.py [--fix-placeholders]
"""

import os
import re
import sys
from pathlib import Path

# 文档根目录（doc_automation 在项目根目录下）
DOCS_ROOT = Path(__file__).parent.parent / 'comfyui_embedded_docs' / 'docs'

# Supported file extensions
doc_exts = {'.md', '.mdx'}

# Match Markdown images/links and HTML img/video/audio/source tag src attributes
MD_LINK_RE = re.compile(r'!\[[^\]]*\]\(([^)]+)\)|\[[^\]]*\]\(([^)]+)\)')
HTML_SRC_RE = re.compile(r'<(?:img|video|audio|source)[^>]+src=["\']([^"\'>]+)["\']', re.IGNORECASE)
PLACEHOLDER_RE = re.compile(r'\{(heading_\w+)\}')

# 不同语言的标题映射
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
    """从文件名获取语言代码"""
    stem = Path(filename).stem
    return stem if stem in HEADING_TRANSLATIONS else None

def is_local_link(link):
    """只检查本地相对路径（非 http/https/data: 开头）"""
    link = link.strip()
    return not (link.startswith('http://') or link.startswith('https://') or link.startswith('data:'))

def find_links_in_line(line):
    """提取行中的所有本地链接"""
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
    """查找内容中的占位符"""
    return PLACEHOLDER_RE.findall(content)

def check_file(fpath, fix_placeholders=False):
    """检查单个文件的链接和占位符"""
    errors = []
    placeholder_issues = []
    rel_fpath = fpath.relative_to(DOCS_ROOT.parent.parent)
    lang = get_language_from_filename(fpath.name)
    
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
        lines = content.split('\n')
    
    # 检查占位符
    placeholders = find_placeholders_in_content(content)
    if placeholders:
        placeholder_issues.append(f"{rel_fpath}: 发现占位符 {placeholders}")
        
        # 如果需要修复且能识别语言
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
                placeholder_issues[-1] += " [已修复]"
    
    # 检查链接
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
                errors.append(f"[链接失效] {rel_fpath}:{idx}: {link}")
    
    return errors, placeholder_issues

def check_links():
    if not DOCS_ROOT.exists():
        print(f"错误: 文档目录不存在: {DOCS_ROOT}")
        sys.exit(1)
    
    fix_placeholders = '--fix-placeholders' in sys.argv
    link_errors = []
    placeholder_issues = []
    
    print(f"正在检查 {DOCS_ROOT} 下的所有文档...")
    
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
        print(f"发现 {len(placeholder_issues)} 个文件包含占位符：")
        print("=" * 80)
        for issue in placeholder_issues:
            print(f"  {issue}")
        if fix_placeholders:
            print("\n✓ 占位符已自动修复")
        else:
            print("\n提示: 运行 --fix-placeholders 参数来自动替换占位符")
    
    if link_errors:
        has_issues = True
        print("\n" + "=" * 80)
        print(f"发现 {len(link_errors)} 个无效链接：")
        print("=" * 80)
        for i, err in enumerate(link_errors):
            if i < 10:
                print(f"  {err}")
            elif i == 10:
                print(f"\n  ... 还有 {len(link_errors) - 10} 个错误（仅显示前10个）")
                break
        print("\n请修正上述链接问题。")
    
    if not has_issues:
        print("\n✓ 所有检查通过！")
    else:
        sys.exit(1)

if __name__ == '__main__':
    check_links()
