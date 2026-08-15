# Grok 图像编辑

根据文本提示修改现有图像。此节点将您的图像和文本描述发送到 Grok API，该 API 会根据您的指令编辑图像并返回结果。

## 输入

### 通用输入

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `模型` | 要使用的 Grok 图像模型。下方显示的子参数会因所选模型而异。 | MODEL | 是 | "grok-imagine-image-2.0"<br>"grok-imagine-image-quality"<br>"grok-imagine-image-pro"<br>"grok-imagine-image" |
| `提示词` | 用于生成图像的文本提示。（默认值：""） | STRING | 是 | N/A |
| `种子` | 用于确定节点是否应重新运行的种子；实际结果与种子无关，始终是不确定的。（默认值：0） | INT | 是 | 0 到 2147483647 |

### grok-imagine-image-2.0 输入

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `images` | 要编辑的参考图像。最多 3 张。 | IMAGE | 是 | 1 到 3 张图像 |
| `resolution` | 编辑后图像的输出分辨率。 | STRING | 是 | "1K"<br>"2K" |
| `number_of_images` | 要生成的编辑后图像数量。（默认值：1） | INT | 是 | 1 到 10 |
| `quality` | 生成图像的质量级别。 | STRING | 是 | "medium"<br>"low" |
| `aspect_ratio` | 编辑后图像的宽高比。（默认值："auto"） | STRING | 是 | "auto"<br>"1:1"<br>"2:3"<br>"3:2"<br>"3:4"<br>"4:3"<br>"9:16"<br>"16:9"<br>"9:19.5"<br>"19.5:9"<br>"9:20"<br>"20:9"<br>"1:2"<br>"2:1" |

### grok-imagine-image-quality 和 grok-imagine-image 输入

由 grok-imagine-image-quality 和 grok-imagine-image 共享。

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `images` | 要编辑的参考图像。最多 3 张。 | IMAGE | 是 | 1 到 3 张图像 |
| `resolution` | 编辑后图像的输出分辨率。 | STRING | 是 | "1K"<br>"2K" |
| `number_of_images` | 要生成的编辑后图像数量。（默认值：1） | INT | 是 | 1 到 10 |
| `aspect_ratio` | 仅当连接了多张图像时允许使用。（默认值："auto"） | STRING | 是 | "auto"<br>"1:1"<br>"2:3"<br>"3:2"<br>"3:4"<br>"4:3"<br>"9:16"<br>"16:9"<br>"9:19.5"<br>"19.5:9"<br>"9:20"<br>"20:9"<br>"1:2"<br>"2:1" |

### grok-imagine-image-pro 输入

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `images` | 要编辑的参考图像。 | IMAGE | 是 | 1 张图像 |
| `resolution` | 编辑后图像的输出分辨率。 | STRING | 是 | "1K"<br>"2K" |
| `number_of_images` | 要生成的编辑后图像数量。（默认值：1） | INT | 是 | 1 到 10 |

### 参考输入

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `images` | 可增长槽位：连接 1 张或多张要编辑的参考图像。可以添加编号槽位，例如 `image_1`、`image_2`、`image_3`。最大图像数量取决于所选模型（请参阅上面的模型部分）。 | IMAGE | 是 | 1 到 3 张图像，具体取决于模型 |

**关于约束的说明：**
- `prompt` 必须包含至少 1 个非空白字符。
- 编辑至少需要一张参考图像；如果未连接任何图像，节点将引发错误。
- 对于 `grok-imagine-image-pro`，输入图像的最大数量为 1；对于 `grok-imagine-image-2.0`、`grok-imagine-image-quality` 和 `grok-imagine-image`，最大数量为 3。连接超过模型支持数量的图像会引发错误。
- 对于 `grok-imagine-image-quality` 和 `grok-imagine-image`，仅当连接了多张图像时才允许使用自定义 `aspect_ratio`（"auto" 以外的任何值）。使用单张图像时，`aspect_ratio` 必须为 "auto"。
- 对于 `grok-imagine-image-2.0`，即使在单张图像时也可以自由设置 `aspect_ratio`。
- `quality` 子参数仅可用于 `grok-imagine-image-2.0`。

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `IMAGE` | Grok API 返回的编辑后图像。如果生成单个图像，则直接返回该图像。如果生成多个图像，则将它们连接成一个批量张量。 | IMAGE |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokImageEditNodeV2/zh.md)

---
**Source fingerprint (SHA-256):** `7d75b1cb8405c5024567b1119bcbd5e4b318152605f74b62bdd5173dda75949f`
