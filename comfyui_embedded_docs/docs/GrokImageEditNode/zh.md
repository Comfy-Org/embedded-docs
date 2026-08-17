# Grok 图像编辑

根据您提供的翻译规则，以下是英文文档的中文翻译：

---

Grok 图像编辑节点根据文本提示修改现有图像。它使用 Grok API 生成一个或多个输入图像的变体，由您的描述引导生成。

## 输入

| 参数 | 描述 | 数据类型 | 是否必填 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `model` | 用于图像编辑的特定 AI 模型。 | COMBO | 是 | `"grok-imagine-image-quality"`<br>`"grok-imagine-image-pro"`<br>`"grok-imagine-image"` |
| `image` | 要编辑的输入图像。最多支持 3 个输入图像，但“pro”模型仅支持 1 个。 | IMAGE | 是 |  |
| `prompt` | 用于生成图像的文本提示。去除空白后必须至少包含 1 个字符。 | STRING | 是 |  |
| `resolution` | 输出图像的分辨率。 | COMBO | 是 | `"1K"`<br>`"2K"` |
| `number_of_images` | 要生成的编辑图像数量（默认：1）。 | INT | 是 | 1 to 10 |
| `seed` | 用于确定节点是否应重新运行的种子；无论种子如何，实际结果都是不确定的（默认：0）。 | INT | 是 | 0 to 2147483647 |
| `aspect_ratio` | 输出图像的宽高比。仅当多个图像连接到 `image` 输入时允许设置。如果设置为 "auto"，则自动确定宽高比（默认："auto"）。 | COMBO | 否 | `"auto"`<br>`"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"9:16"`<br>`"16:9"`<br>`"9:19.5"`<br>`"19.5:9"`<br>`"9:20"`<br>`"20:9"`<br>`"1:2"`<br>`"2:1"` |

**重要限制：**
- `image` 输入最多支持 3 个图像，但使用 `grok-imagine-image-pro` 模型时仅支持 1 个输入图像。
- 仅当多个图像连接到 `image` 输入时，`aspect_ratio` 参数才能设置为自定义值（非 "auto"）。如果使用单个输入图像设置自定义宽高比，将导致错误。

**注意：** 此节点已弃用。

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `output` | 节点生成的编辑图像。如果 `number_of_images` 大于 1，则输出会拼接成一个批次。 | IMAGE |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokImageEditNode/zh.md)

---
**Source fingerprint (SHA-256):** `e2ace07d10901c4e57086da8e3294a5d04e379103e9740131f5355cd4b07625d`
