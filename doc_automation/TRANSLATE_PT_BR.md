# 如何只进行 pt-BR 翻译更新

## 🚀 方法 1：使用主脚本（最简单，推荐）

### 测试模式（先翻译少量节点测试）

```bash
cd /Users/linmoumou/Documents/local_env/embedded-docs/doc_automation
conda activate LLM_base  # 或你的环境名

# 翻译 10 个节点（测试）
python3 main.py --translate --lang pt-BR --count 10
```

### 完整模式（翻译所有缺失的 pt-BR 文档）

```bash
# 翻译所有缺失的 pt-BR 文档
python3 main.py --translate --lang pt-BR --mode all
```

### 强制重新翻译（覆盖已有翻译）

```bash
# 强制重新翻译所有 pt-BR 文档
python3 main.py --translate --lang pt-BR --mode all --force
```

---

## 🔧 方法 2：分步执行（更灵活）

### 第1步：扫描缺失的翻译（可选）

```bash
# 更新缺失翻译列表
python3 scan_missing_nodes.py
```

### 第2步：准备翻译批次

```bash
# 测试模式：准备 10 个节点
python3 prepare_translation.py --lang pt-BR --mode test --count 10

# 完整模式：准备所有缺失的节点
python3 prepare_translation.py --lang pt-BR --mode all
```

### 第3步：执行翻译

```bash
# 测试模式：翻译 10 个节点
python3 batch_translate_docs.py --lang pt-BR --mode test --count 10

# 完整模式：翻译所有准备的节点
python3 batch_translate_docs.py --lang pt-BR --mode all

# 强制重新翻译
python3 batch_translate_docs.py --lang pt-BR --mode all --force
```

---

## 📊 工作流程说明

使用 `main.py` 时，会自动执行以下步骤：

1. **同步前端翻译**（从 ComfyUI 前端获取参数翻译）
2. **扫描缺失翻译**（更新 `missing_nodes_report.json`）
3. **准备翻译批次**（创建 `translation_batches/batch_pt-BR.json`）
4. **执行翻译**（调用 AI API 翻译文档）
5. **更新参数翻译**（用前端翻译替换参数名）

---

## 🎯 常用命令示例

```bash
# 1. 测试翻译 5 个节点
python3 main.py --translate --lang pt-BR --count 5

# 2. 翻译所有缺失的 pt-BR 文档
python3 main.py --translate --lang pt-BR --mode all

# 3. 强制重新翻译特定节点
python3 main.py --translate --lang pt-BR --mode node --node SaveImage --force

# 4. 只扫描，不翻译（查看有多少缺失）
python3 main.py --scan-only
```

---

## 📝 注意事项

1. **环境要求**：确保已激活 conda 环境并配置了 API key
2. **自动跳过**：脚本会自动跳过已有翻译（除非使用 `--force`）
3. **增量更新**：翻译完成后会自动更新 `missing_nodes_report.json`
4. **日志文件**：翻译日志保存在 `logs/translation_*.log`

---

## 🔍 检查翻译状态

```bash
# 查看有多少节点缺少 pt-BR 翻译
python3 -c "
import json
with open('missing_nodes_report.json', 'r', encoding='utf-8') as f:
    report = json.load(f)
missing = [doc for doc in report.get('incomplete_docs', []) if 'pt-BR' in doc.get('missing_languages', [])]
print(f'缺少 pt-BR 翻译的节点数: {len(missing)}')
"
```

---

## 💡 推荐流程

对于首次使用 pt-BR 翻译：

```bash
# 1. 先测试翻译 5 个节点，确认效果
python3 main.py --translate --lang pt-BR --count 5

# 2. 检查翻译质量
cat ../comfyui_embedded_docs/docs/SaveImage/pt-BR.md

# 3. 如果满意，翻译所有缺失的文档
python3 main.py --translate --lang pt-BR --mode all
```
