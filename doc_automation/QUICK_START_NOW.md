# 快速开始 - 文档生成和翻译

## 📊 当前状态

根据 `missing_nodes_report.json`：
- **总节点数**: 498
- **已有文档**: 509 (包含一些已废弃的)
- **缺失文档**: 7 个节点

## 🚀 快速开始（3步完成）

### 第1步：扫描缺失节点（可选，已扫描过）

```bash
cd /Users/linmoumou/Documents/local_env/embedded-docs/doc_automation
conda activate LLM_base  # 或你的环境名
python3 scan_missing_nodes.py
```

### 第2步：生成缺失的文档

```bash
# 使用主脚本（推荐）
python3 main.py --mode all

# 或者只生成缺失的7个节点
python3 main.py --count 7
```

### 第3步：翻译文档（如果需要）

```bash
# 翻译到中文（测试10个节点）
python3 main.py --translate --lang zh --count 10

# 翻译所有语言（测试模式）
python3 main.py --translate --all-languages --count 10

# 翻译所有文档到所有语言
python3 main.py --translate --all-languages --mode all
```

## 📋 缺失的7个节点

1. Epsilon Scaling
2. LtxvApiImageToVideo
3. LtxvApiTextToVideo
4. RecraftCreativeUpscaleNode
5. RecraftStyleV3DigitalIllustration
6. RecraftStyleV3VectorIllustrationNode
7. TemporalScoreRescaling

## 🎯 完整工作流程

### 生成文档

```bash
# 方法1：使用主脚本（最简单）
python3 main.py --mode all

# 方法2：分步执行
python3 prepare_ai_input.py all
python3 batch_generate_docs.py all
```

### 翻译文档

```bash
# 单语言翻译
python3 main.py --translate --lang zh --mode all

# 所有语言翻译
python3 main.py --translate --all-languages --mode all
```

## ⚙️ 环境要求

确保已激活正确的 conda 环境：
```bash
conda activate LLM_base
# 或者
conda activate base
```

## 📝 注意事项

- 确保 `.env` 文件中有 `DEEPSEEK_API_KEY` 或其他 API key
- 生成过程会自动跳过已有文档（除非使用 `--force`）
- 翻译会自动跳过已有翻译（除非使用 `--force`）
