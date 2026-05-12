#!/usr/bin/env python3
"""
从前端仓库的 nodeDefs.json 同步参数翻译到文档
用法: python sync_frontend_translations.py <frontend_repo_path>
示例: python sync_frontend_translations.py /path/to/ComfyUI_frontend
"""

import json
import sys
from pathlib import Path

# 文档根目录（doc_automation 在项目根目录下）
DOCS_ROOT = Path(__file__).parent.parent / 'comfyui_embedded_docs' / 'docs'

# 支持的语言
SUPPORTED_LANGS = ['en', 'zh', 'zh-TW', 'es', 'fr', 'ja', 'ko', 'ru', 'ar', 'tr', 'pt-BR', 'fa']

def load_frontend_translations(frontend_path, lang):
    """从前端仓库加载指定语言的翻译"""
    locale_file = Path(frontend_path) / 'src' / 'locales' / lang / 'nodeDefs.json'
    
    if not locale_file.exists():
        print(f"⚠️  警告: 未找到 {lang} 语言文件: {locale_file}")
        return {}
    
    try:
        with open(locale_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"❌ 读取 {lang} 语言文件失败: {e}")
        return {}

def get_node_translations(frontend_translations, node_name):
    """获取节点的翻译信息"""
    if node_name not in frontend_translations:
        return None
    
    node_data = frontend_translations[node_name]
    translations = {
        'display_name': node_data.get('display_name', ''),
        'description': node_data.get('description', ''),
        'inputs': {},
        'outputs': {}
    }
    
    # 提取输入参数翻译
    if 'inputs' in node_data:
        for param_name, param_data in node_data['inputs'].items():
            if isinstance(param_data, dict):
                translations['inputs'][param_name] = {
                    'name': param_data.get('name', param_name),
                    'tooltip': param_data.get('tooltip', '')
                }
    
    # 提取输出翻译
    if 'outputs' in node_data:
        for output_idx, output_data in node_data['outputs'].items():
            if isinstance(output_data, dict):
                translations['outputs'][output_idx] = {
                    'name': output_data.get('name', ''),
                    'tooltip': output_data.get('tooltip', '')
                }
    
    return translations

def create_translation_report(frontend_path):
    """生成翻译对照报告"""
    print(f"\n正在从前端仓库加载翻译: {frontend_path}\n")
    
    # 加载所有语言的翻译
    all_translations = {}
    for lang in SUPPORTED_LANGS:
        all_translations[lang] = load_frontend_translations(frontend_path, lang)
    
    # 获取所有节点名称（从文档目录）
    node_dirs = [d for d in DOCS_ROOT.iterdir() if d.is_dir()]
    
    print(f"找到 {len(node_dirs)} 个节点文档目录\n")
    print("=" * 80)
    
    # 为每个节点生成翻译报告
    for node_dir in sorted(node_dirs):
        node_name = node_dir.name
        
        # 检查是否有对应的前端翻译
        has_translation = any(node_name in all_translations[lang] for lang in SUPPORTED_LANGS)
        
        if not has_translation:
            print(f"\n⚠️  {node_name}: 未找到前端翻译")
            continue
        
        print(f"\n✓ {node_name}")
        print("-" * 80)
        
        # 显示各语言的参数翻译
        for lang in SUPPORTED_LANGS:
            if node_name in all_translations[lang]:
                trans = get_node_translations(all_translations[lang], node_name)
                if trans and trans['inputs']:
                    print(f"\n  [{lang.upper()}] 参数翻译:")
                    for param_name, param_trans in trans['inputs'].items():
                        print(f"    - {param_name}: {param_trans['name']}")
                        if param_trans['tooltip']:
                            print(f"      提示: {param_trans['tooltip'][:60]}...")

def export_translation_json(frontend_path, output_file='node_translations.json'):
    """导出所有节点的翻译为JSON文件，便于后续使用"""
    all_translations = {}
    for lang in SUPPORTED_LANGS:
        all_translations[lang] = load_frontend_translations(frontend_path, lang)
    
    # 保存到 doc_automation 目录
    output_path = Path(__file__).parent / output_file
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(all_translations, f, ensure_ascii=False, indent=2)
    
    print(f"\n✓ 翻译数据已导出到: {output_path}")

def main():
    if len(sys.argv) < 2:
        print("用法: python sync_frontend_translations.py <frontend_repo_path> [--export]")
        print("示例: python sync_frontend_translations.py /path/to/ComfyUI_frontend")
        print("\n选项:")
        print("  --export  导出翻译为JSON文件")
        sys.exit(1)
    
    frontend_path = Path(sys.argv[1])
    
    if not frontend_path.exists():
        print(f"❌ 错误: 前端仓库路径不存在: {frontend_path}")
        sys.exit(1)
    
    if '--export' in sys.argv:
        export_translation_json(frontend_path)
    else:
        create_translation_report(frontend_path)

if __name__ == '__main__':
    main()

