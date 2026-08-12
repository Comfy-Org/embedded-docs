import json
from pathlib import Path

import runtime  # noqa: F401
from lib.paths import NODE_TRANSLATIONS

data = json.load(open(NODE_TRANSLATIONS, encoding="utf-8"))
zh = data.get('zh', {})

nodes_with_outputs = []
for n, v in zh.items():
    if v.get('outputs'):
        nodes_with_outputs.append((n, v.get('outputs', {})))

print(f'有输出翻译的节点数: {len(nodes_with_outputs)}')
print('\n示例:')
for n, o in nodes_with_outputs[:5]:
    print(f'\n{n}:')
    print(json.dumps(o, ensure_ascii=False, indent=2))

