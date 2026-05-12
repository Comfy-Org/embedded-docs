# 快速开始指南

## 第一次使用？跟着这 5 步走！

### ✅ 步骤 0：准备工作

```bash
# 1. 进入工作目录
cd /Users/linmoumou/Documents/local_env/embedded-docs/doc_automation

# 2. 安装依赖
pip3 install -r requirements.txt

# 3. 配置 API 密钥
# 编辑 ../.env 文件，添加你的 DeepSeek API Key
# DEEPSEEK_API_KEY=your_key_here
```

---

### 📊 步骤 1：扫描缺失节点

```bash
python3 scan_missing_nodes.py
```

**输出：** `missing_nodes_report.json`

**预期结果：**
```
✅ 扫描完成，共发现 494 个节点
✅ 发现 145 个已有文档
❌ 缺失文档的节点数: 401
```

---

### 🔍 步骤 2：准备测试节点

```bash
# 先准备 3 个节点测试
python3 prepare_ai_input.py test 3
```

**输出：** `ai_input/<节点名>/` 目录，包含：
- `source_code.py`
- `basic_info.json`  
- `ai_prompt.txt`

**预期结果：**
```
✅ 成功: 3
📁 输出目录: ai_input/
```

---

### 🤖 步骤 3：测试 AI 生成

```bash
# 生成刚才准备的 3 个节点文档
python3 batch_generate_docs.py test --count 3
```

**预期结果：**
```
✅ 成功: 3
❌ 失败: 0
📁 日志文件: logs/generation_20250109_143022.log
```

**检查生成的文档：**
```bash
ls -la ../comfyui_embedded_docs/docs/APG/en.md
cat ../comfyui_embedded_docs/docs/APG/en.md
```

---

### 📝 步骤 4：检查质量

打开生成的文档，检查：

- [ ] 有功能描述段落
- [ ] 有 "How It Works" 章节
- [ ] 有完整的输入参数表格
- [ ] 有输出结果表格
- [ ] 参数描述来自 tooltip
- [ ] 数据类型是英文大写
- [ ] 没有 Usage Tips 章节

---

### 🚀 步骤 5：批量生成

如果测试通过，可以批量生成：

```bash
# 方式 1：生成所有节点（需要确认）
python3 batch_generate_docs.py all

# 方式 2：先生成 50 个
python3 prepare_ai_input.py test 50
python3 batch_generate_docs.py all

# 方式 3：继续未完成的
python3 batch_generate_docs.py resume
```

---

## 🔧 常用命令

### 单独处理某个节点

```bash
# 1. 准备节点
python3 prepare_ai_input.py node OpenAIDalle2

# 2. 生成文档
python3 batch_generate_docs.py node --node OpenAIDalle2

# 3. 查看文档
cat ../comfyui_embedded_docs/docs/OpenAIDalle2/en.md
```

### 重新生成已有文档

```bash
python3 batch_generate_docs.py node --node OpenAIDalle2 --force
```

### 查看日志

```bash
# 查看最新日志
tail -f logs/generation_*.log

# 查看所有日志
ls -lt logs/
```

---

## ⚠️ 注意事项

### API 费用估算

- DeepSeek API: ~¥0.001/1K tokens
- 每个节点约 2K tokens（提示词）+ 1K tokens（响应）
- 401 个节点总计约：401 × 3K = 1.2M tokens ≈ ¥1.2

### 速率限制

如果遇到 429 错误（速率限制），调整 `.env`：

```bash
DELAY_BETWEEN_REQUESTS=5  # 增加延迟
BATCH_SIZE=3              # 减小批次
```

---

## 🐛 问题解决

### 问题 1：找不到 .env 文件

```bash
# 检查文件位置
ls -la ../.env

# 如果不存在，复制示例
cp env.example ../.env
# 然后编辑添加 API key
```

### 问题 2：生成的文档太短

查看日志文件，检查是否有错误：

```bash
grep "ERROR" logs/generation_*.log
```

### 问题 3：API 连接失败

检查网络和 API 密钥：

```bash
# 测试 API 连接
python3 -c "
from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv('../.env')
client = OpenAI(api_key=os.getenv('DEEPSEEK_API_KEY'), base_url='https://api.deepseek.com')
response = client.chat.completions.create(model='deepseek-chat', messages=[{'role': 'user', 'content': 'Hi'}])
print('✅ API 连接成功！')
"
```

---

## 📊 进度追踪

### 查看还剩多少节点

```bash
# 方法 1：使用 resume 模式查看
python3 batch_generate_docs.py resume
# 会显示"准备生成 X 个节点"

# 方法 2：手动统计
ls ../comfyui_embedded_docs/docs/*/en.md | wc -l
```

### 查看生成统计

```bash
# 查看最新日志的总结
tail -20 logs/generation_*.log | grep -A 10 "生成总结"
```

---

## 🎯 推荐工作流

### 第一天：测试验证（10-20 个节点）

```bash
python3 prepare_ai_input.py test 20
python3 batch_generate_docs.py test --count 20
# 人工检查质量
```

### 第二天：批量生成（100 个节点）

```bash
python3 prepare_ai_input.py test 100
python3 batch_generate_docs.py all
```

### 第三天：完成剩余（~280 个节点）

```bash
python3 prepare_ai_input.py all
python3 batch_generate_docs.py resume
```

---

## ✅ 成功标志

当你看到这些，说明一切正常：

```
================================================================================
📊 生成总结
================================================================================
✅ 成功: 401
❌ 失败: 0
⏭️  跳过: 0
📁 日志文件: logs/generation_20250109_143022.log
```

恭喜！🎉 你已经成功生成了所有节点文档！

