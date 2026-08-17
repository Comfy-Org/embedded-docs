# CLIP保存

`CLIPSave` 节点将 CLIP 文本编码器模型以 SafeTensors 格式保存到磁盘。它专为高级模型合并工作流设计，会根据模型的内部结构自动将 CLIP 模型拆分为其组成部分（如 CLIP-L、CLIP-G 或 T5XXL），并将每个组件保存为单独的文件。

## 输入
| 参数 | 描述 | 数据类型 | 必填 | 范围 |
| --- | --- | --- | --- | --- |
| `clip` | 要保存的 CLIP 模型。 | CLIP | 是 | - |
| `filename_prefix` | 保存文件的前缀路径和文件名。节点会追加组件后缀（例如 `_clip_l`、`_clip_g`）和计数器来生成唯一文件名（默认：`clip/ComfyUI`）。 | STRING | 是 | - |
| `prompt` | 工作流提示信息，作为元数据保存在输出文件中。此参数在 UI 中隐藏。 | PROMPT | 否 | - |
| `extra_pnginfo` | 附加元数据，以键值对形式保存在输出文件中。此参数在 UI 中隐藏。 | EXTRA_PNGINFO | 否 | - |

## 输出
此节点没有输出连接。它直接将处理后的文件保存到 `ComfyUI/output/` 目录。

### 已保存文件详情

节点分析 CLIP 模型的状态字典，并为检测到的每个组件保存单独的 SafeTensors 文件。组件通过其参数键的前缀来识别。节点按以下顺序检查这些前缀：

- `clip_l.`（CLIP-L 文本编码器）
- `clip_g.`（CLIP-G 文本编码器）
- `clip_h.`（CLIP-H 文本编码器）
- `t5xxl.`（T5-XXL 文本编码器）
- `pile_t5xl.`（Pile-T5-XL 文本编码器）
- `mt5xl.`（mT5-XL 文本编码器）
- `umt5xxl.`（UMT5-XXL 文本编码器）
- `t5base.`（T5-Base 文本编码器）
- `gemma2_2b.`（Gemma 2 2B 文本编码器）
- `llama.`（LLaMA 文本编码器）
- `hydit_clip.`（Hydit CLIP 文本编码器）
- 空前缀（其他 CLIP 组件）

对于检测到的每个组件，节点会创建一个名为 `{filename}_{counter:05}_.safetensors` 的文件（例如 `ComfyUI_clip_l_00001_.safetensors`），其中组件名称会附加到文件名前缀之后，计数器则确保文件名唯一。保存组件时，会从其参数键中移除 `transformer.` 前缀。

写入每个文件的元数据包括工作流提示和任何额外的 PNG 信息，除非使用 `--disable-metadata` 命令行参数禁用元数据保存。

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPSave/zh.md)

---
**Source fingerprint (SHA-256):** `4ab9171e4245b10f738f78bac8a5b564c0957dde352e207ec3f9865e4fac0cab`
