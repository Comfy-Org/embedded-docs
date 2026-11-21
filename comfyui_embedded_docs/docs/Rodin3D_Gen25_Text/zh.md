# Rodin 3D Gen-2.5 - 文本转3D

## 概述

使用 Rodin Gen-2.5 API 根据文本提示生成 3D 模型。您可以在不同的质量模式（Fast、Regular 或 Extreme-High）之间选择，以平衡生成速度和输出质量。

## 输入

| 参数 | 描述 | 数据类型 | 必填 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 用于 3D 模型的文本提示。 | STRING | 是 | 1 到 1024 个字符 |
| `mode` | 生成质量和速度模式。“Fast”最快，“Extreme-High”生成质量最高，但耗时更长。 | COMBO | 是 | `"Fast"`<br>`"Regular"`<br>`"Extreme-High"` |
| `material` | 生成的 3D 模型的材质风格。 | COMBO | 是 | `"PBR"`<br>`"Matte"`<br>`"Shiny"` |
| `geometry_file_format` | 输出 3D 模型的文件格式。 | COMBO | 是 | `"glb"`<br>`"obj"`<br>`"stl"`<br>`"usdz"` |
| `texture_mode` | 纹理生成模式。“None”不生成纹理，“Generated”创建标准纹理，“Generated+HD”创建高清纹理。 | COMBO | 是 | `"None"`<br>`"Generated"`<br>`"Generated+HD"` |
| `seed` | 用于可复现结果的随机种子。使用相同的种子和相同的输入将产生相同的输出。 | INT | 是 | 0 到 2147483647 |
| `TAPose` | 是否对生成的模型应用 T-pose（双臂展开）。 | BOOLEAN | 是 | True 或 False |
| `hd_texture` | 是否为模型生成高清纹理。 | BOOLEAN | 是 | True 或 False |
| `texture_delight` | 是否对模型应用纹理增强（提升纹理质量）。 | BOOLEAN | 是 | True 或 False |
| `addon_highpack` | 是否在标准版本之外额外生成模型的高多边形版本。 | BOOLEAN | 是 | True 或 False |
| `bbox_width` | 边界框的宽度，以世界单位计。 | INT | 是 | 1 到 1000 |
| `bbox_height` | 边界框的高度，以世界单位计。 | INT | 是 | 1 到 1000 |
| `bbox_length` | 边界框的长度，以世界单位计。 | INT | 是 | 1 到 1000 |
| `height_cm` | 生成的模型高度，以厘米计。 | INT | 是 | 1 到 300 |

**注意：** `prompt` 参数长度必须在 1 到 1024 个字符之间。如果未指定，`seed` 参数默认为 0（随机）。

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `model_file` | 按指定格式生成的 3D 模型文件。 | FILE3DANY |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Rodin3D_Gen25_Text/zh.md)

---
**Source fingerprint (SHA-256):** `95d5faa36298f09f0ae4dcda95dfd8913ebb393bb5934ae2c4622acfe79c85d6`
