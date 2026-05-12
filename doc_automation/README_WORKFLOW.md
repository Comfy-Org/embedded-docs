# ComfyUI 节点文档自动化工作流程

## 🎯 目标

为 ComfyUI 的 494 个节点自动生成标准化的英文文档（en.md），当前缺失 401 个节点文档。

---

## 📋 文档结构（简化版）

每个节点文档包含 4 个部分：

1. **Function Description**（功能描述）- 1-2句话说明节点用途
2. **How It Works**（工作原理）- 清晰解释节点如何工作
3. **Inputs**（输入参数）- 完整的参数表格
4. **Outputs**（输出结果）- 输出表格

**不包含：**
- ❌ Usage Tips（避免 AI 幻觉）
- ❌ 示例代码
- ❌ 最佳实践建议

---

## 🔄 三步工作流程

### 步骤 1️⃣：扫描缺失节点

```bash
python3 scan_missing_nodes.py
```

**输出：** `missing_nodes_report.json`（包含 401 个缺失节点的详细信息）

---

### 步骤 2️⃣：准备 AI 输入

```bash
# 单个节点
python3 prepare_ai_input.py node OpenAIDalle2

# 批量准备（测试）
python3 prepare_ai_input.py test 10

# 准备所有缺失节点
python3 prepare_ai_input.py all
```

**为每个节点生成：**
```
ai_input/<节点名>/
├── source_code.py       # 完整源代码
├── basic_info.json      # 元信息（category, docstring等）
└── ai_prompt.txt        # 完整的 AI 提示词
```

**提取的信息包括：**
- ✅ 完整类源代码
- ✅ 类的 docstring
- ✅ 所有参数的 tooltip 说明
- ✅ 默认值、范围、选项
- ✅ 输入/输出类型

---

### 步骤 3️⃣：AI 生成文档

#### 方案 A：手动提交（推荐用于重要节点）

1. 打开 `ai_input/<节点名>/ai_prompt.txt`
2. 复制完整内容
3. 提交给 Claude/ChatGPT
4. 将生成的文档保存到 `comfyui_embedded_docs/docs/<节点名>/en.md`

#### 方案 B：API 批量处理（推荐用于大量节点）

```python
# 伪代码示例
import anthropic  # 或 openai

for node_dir in Path("ai_input").iterdir():
    prompt = (node_dir / "ai_prompt.txt").read_text()
    
    # 调用 AI API
    response = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        messages=[{"role": "user", "content": prompt}]
    )
    
    # 保存文档
    doc_path = f"comfyui_embedded_docs/docs/{node_dir.name}/en.md"
    save_doc(response.content, doc_path)
```

---

## 📊 当前进度

- **总节点数：** 494
- **已有文档：** 145（29.4%）
- **缺失文档：** 401（81.2%）
- **需补语言：** 121 个节点

---

## 📁 文件说明

| 文件 | 作用 |
|------|------|
| `scan_missing_nodes.py` | 扫描缺失节点，生成报告 |
| `prepare_ai_input.py` | 提取源代码和元信息，准备 AI 输入 |
| `doc_rules.txt` | 文档编写规则（AI 参考） |
| `missing_nodes_report.json` | 缺失节点详细报告 |
| `ai_input/` | 存储每个节点的 AI 输入文件 |

---

## ✅ 文档质量要求

### 必须做到：
- ✅ 使用源代码中的 tooltip 原文作为参数说明
- ✅ 数据类型保持英文大写（IMAGE, STRING, INT, FLOAT 等）
- ✅ 参数名用反引号：`parameter_name`
- ✅ 基于源代码的客观描述
- ✅ 提取 docstring 作为功能描述基础

### 禁止内容：
- ❌ 不要添加 Usage Tips 或最佳实践
- ❌ 不要使用表情符号
- ❌ 不要包含代码示例
- ❌ 不要翻译数据类型名称
- ❌ 不要推测用法或添加主观建议

---

## 🚀 快速开始

### 示例：为 5 个节点生成文档

```bash
# 1. 准备 AI 输入
python3 prepare_ai_input.py test 5

# 2. 查看生成的文件
ls -R ai_input/

# 3. 选择一个节点，复制提示词
cat ai_input/APG/ai_prompt.txt

# 4. 提交给 AI，获取文档

# 5. 保存到对应目录
# vim comfyui_embedded_docs/docs/APG/en.md
```

---

## 📝 文档示例

参考已生成的文档：
- `comfyui_embedded_docs/docs/OpenAIDalle2/en.md`
- `comfyui_embedded_docs/docs/TextEncodeAceStepAudio/en.md`
- `comfyui_embedded_docs/docs/EmptyAceStepLatentAudio/en.md`

---

## 💡 建议执行顺序

### 阶段 1：测试验证（5-10 个节点）
- 使用 `prepare_ai_input.py test 10`
- 手动提交 AI 生成
- 验证文档质量
- 优化提示词（如需要）

### 阶段 2：批量处理（100 个节点）
- 准备 API 批量处理脚本
- 分批生成文档
- 人工抽查质量

### 阶段 3：完整覆盖（剩余 300+ 节点）
- 批量生成所有缺失文档
- 重点审核核心节点

---

## 🔧 故障排查

**问题：提取的源代码不完整**
- 检查节点是否是新 API 格式
- 查看 `_node_info.json` 确认提取的信息

**问题：参数表格缺失某些参数**
- 检查 `source_code.py` 中的 INPUT_TYPES
- 确认 tooltip 是否存在

**问题：AI 生成了 Usage Tips**
- 重新提交时明确要求：不要包含 Usage Tips
- 检查 `doc_rules.txt` 是否更新

---

## 📞 下一步

1. ✅ 已完成：扫描工具、提取工具、文档规则
2. 🔄 进行中：测试 AI 生成质量
3. ⏳ 待办：建立批量处理流程
4. ⏳ 待办：多语言翻译（基于 en.md）

---

## 📌 重要提示

- 所有参数描述必须基于源代码的 tooltip
- 保持客观，避免主观建议
- 专注于"是什么"和"怎么做"，而非"应该怎么用"

