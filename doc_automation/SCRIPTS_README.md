# 文档质量检查脚本

本目录包含用于检查和维护 ComfyUI 节点文档质量的工具脚本。

## 脚本列表

### 1. check_md_links.py - 链接和占位符检查

**功能：**
- 检查所有 `.md` 和 `.mdx` 文件中的本地资源链接（图片、视频等）是否有效
- 检查文档中是否包含未替换的占位符（如 `{heading_inputs}`）
- 支持自动修复占位符

**用法：**

```bash
# 基础检查（检查链接和占位符）
python3 .github/scripts/check_md_links.py

# 自动修复占位符
python3 .github/scripts/check_md_links.py --fix-placeholders
```

**支持的占位符：**
- `{heading_overview}` → 各语言的"概述"/"Overview"等
- `{heading_inputs}` → 各语言的"输入"/"Inputs"等
- `{heading_outputs}` → 各语言的"输出"/"Outputs"等
- `{heading_usage}` → 各语言的"用法"/"Usage"等
- `{heading_examples}` → 各语言的"示例"/"Examples"等

### 2. sync_frontend_translations.py - 前端翻译同步

**功能：**
- 从 ComfyUI_frontend 仓库读取各语言的节点翻译
- 生成翻译对照报告，显示每个节点在不同语言中的参数名称
- 导出翻译数据为 JSON 文件，便于文档翻译时参考

**用法：**

```bash
# 生成翻译对照报告
python3 .github/scripts/sync_frontend_translations.py /path/to/ComfyUI_frontend

# 导出翻译数据为 JSON
python3 .github/scripts/sync_frontend_translations.py /path/to/ComfyUI_frontend --export
```

**示例（使用你的前端仓库路径）：**

```bash
python3 .github/scripts/sync_frontend_translations.py /Users/linmoumou/Documents/comfy/ComfyUI_frontend --export
```

导出后会在项目根目录生成 `node_translations.json` 文件，包含所有语言的节点翻译。

### 3. replace_placeholders.py - 占位符批量替换

**功能：**
- 批量查找并替换文档中的占位符
- 支持检查模式（不实际修改文件）

**用法：**

```bash
# 仅检查，不修改
python3 .github/scripts/replace_placeholders.py --check-only

# 执行替换
python3 .github/scripts/replace_placeholders.py
```

## 工作流程建议

### 创建或更新文档时

1. **写文档时使用占位符**（可选）：
   ```markdown
   {heading_inputs}
   
   | 参数 | 类型 | 说明 |
   |------|------|------|
   ```

2. **完成后自动替换占位符**：
   ```bash
   python3 .github/scripts/check_md_links.py --fix-placeholders
   ```

3. **翻译文档前，导出前端翻译**：
   ```bash
   python3 .github/scripts/sync_frontend_translations.py /Users/linmoumou/Documents/comfy/ComfyUI_frontend --export
   ```
   
   然后参考生成的 `node_translations.json` 确保参数名称翻译与界面一致。

4. **提交前检查链接**：
   ```bash
   python3 .github/scripts/check_md_links.py
   ```

### PR 前的最终检查

```bash
# 一键检查并修复所有问题
python3 .github/scripts/check_md_links.py --fix-placeholders
```

## 常见问题

### Q: 为什么翻译后的文档包含占位符？

A: 这通常是因为：
1. AI 生成的文档使用了占位符模板
2. 翻译过程中没有替换占位符

**解决方案**：运行 `python3 .github/scripts/check_md_links.py --fix-placeholders` 自动修复。

### Q: 如何确保参数翻译与界面一致？

A: 
1. 运行 `sync_frontend_translations.py --export` 导出前端翻译
2. 翻译文档时参考导出的 `node_translations.json` 文件
3. 使用前端中对应语言的参数名称，而不是AI自动翻译

### Q: 检查失败了怎么办？

A: 脚本会详细列出所有问题：
- **链接失效**：检查图片/视频文件路径是否正确，文件是否存在
- **占位符未替换**：运行 `--fix-placeholders` 自动修复

## 支持的语言

脚本支持以下语言的占位符替换和翻译同步：
- `en` - English
- `zh` - 简体中文
- `zh-TW` - 繁體中文
- `es` - Español
- `fr` - Français
- `ja` - 日本語
- `ko` - 한국어
- `ru` - Русский
- `ar` - العربية
- `tr` - Türkçe
- `pt-BR` - Português (BR)
- `fa` - فارسی

