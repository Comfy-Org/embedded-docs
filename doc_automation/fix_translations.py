#!/usr/bin/env python3
"""
修复翻译文件中的占位符和参数名称问题
"""

import json
import re
from pathlib import Path

DOC_AUTOMATION_PATH = Path(__file__).parent
DOCS_PATH = DOC_AUTOMATION_PATH.parent / "comfyui_embedded_docs" / "docs"
TRANSLATION_CONFIG_FILE = DOC_AUTOMATION_PATH / "translation_config.json"
TRANSLATIONS_FILE = DOC_AUTOMATION_PATH / "node_translations.json"

def fix_heading_placeholders(content, lang_config):
    """替换标题占位符"""
    content = content.replace('{heading_overview}', f"## {lang_config.get('heading_overview', 'Overview')}")
    content = content.replace('{heading_inputs}', f"## {lang_config.get('heading_inputs', 'Inputs')}")
    content = content.replace('{heading_outputs}', f"## {lang_config.get('heading_outputs', 'Outputs')}")
    return content

def update_param_names(content, node_name, lang, frontend_translations):
    """更新参数名称"""
    if lang not in frontend_translations:
        return content, False
    
    if node_name not in frontend_translations[lang]:
        return content, False
    
    node_trans = frontend_translations[lang][node_name]
    original_content = content
    changes_made = []
    
    # 更新输入参数名
    if 'inputs' in node_trans:
        for param_name, param_data in node_trans['inputs'].items():
            frontend_name = param_data.get('name', '')
            if frontend_name and frontend_name != param_name:
                # 替换表格中的参数名
                pattern = rf'\|\s*`{re.escape(param_name)}`\s*\|'
                replacement = f'| `{frontend_name}` |'
                if re.search(pattern, content):
                    content = re.sub(pattern, replacement, content)
                    changes_made.append(f"{param_name} → {frontend_name}")
    
    # 更新输出参数名
    if 'outputs' in node_trans:
        lines = content.split('\n')
        in_output_section = False
        output_row_index = 0
        
        for i, line in enumerate(lines):
            # 检测输出部分
            if re.match(r'##\s+(?:输出|輸出|出力|출력|Выходы|Salidas|Sorties|Outputs|المخرجات|Çıktılar)', line):
                in_output_section = True
                output_row_index = 0
                continue
            elif line.startswith('##'):
                in_output_section = False
                continue
            
            # 更新输出名称
            if in_output_section and line.strip().startswith('|'):
                if 'Output Name' in line or 'Data Type' in line or '---' in line:
                    continue
                
                output_idx_str = str(output_row_index)
                if output_idx_str in node_trans['outputs']:
                    output_data = node_trans['outputs'][output_idx_str]
                    frontend_name = output_data.get('name', '')
                    
                    if frontend_name:
                        old_match = re.match(r'(\|\s*)`([^`]+)`(\s*\|)', line)
                        if old_match:
                            old_name = old_match.group aufgrund eines Errors unterbrochen wurde, ich muss fortfahren
