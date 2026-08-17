# ByteDance Seedream 4.5 & 5.0

此节点使用字节跳动 Seedream 模型（4.0、4.5、5.0 Lite 和 5.0 Pro）创建或编辑图像。它可以根据文本提示生成新图像，也可以基于参考图像和单句指令编辑现有图像，最高支持 4K 分辨率。

## 输入

`model` 选择器决定可用的模型特定输入。下表列出了通用输入、各模型输入以及可增长的参考图像插槽。

### 通用输入

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `model` | 用于生成的 Seedream 模型版本。每个模型具有不同的能力、限制和定价。 | DYNAMIC_COMBO | 是 | `"seedream 5.0 pro"`<br>`"seedream 5.0 lite"`<br>`"seedream-4-5-251128"`<br>`"seedream-4-0-250828"` |
| `prompt` | 用于创建或编辑图像的文本提示。 | STRING | 是 | 任意文本（非空） |
| `seed` | 用于生成的种子（默认值：0）。 | INT | 是 | 0 到 2147483647 |
| `watermark` | 是否在图像上添加“AI 生成”水印（默认值：False）。 | BOOLEAN | 是 | True / False |
| `thinking` | 启用模型的提示优化推理（“thinking”），以获得更好的指令遵循效果。会大幅增加生成时间——在 Seedream 5.0 Pro 上尤为明显。仅可在文生图时禁用（提供参考图像时不可禁用）。（默认值：True） | BOOLEAN | 否 | True / False |

### seedream 5.0 pro 输入

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `size_preset` | 选择推荐尺寸。选择 Custom 以使用下方的宽度和高度。 | COMBO | 是 | 模型特定预设（包含 Custom） |
| `width` | 图像的自定义宽度。仅当 `size_preset` 设置为 Custom 时此值才生效（默认值：2048）。 | INT | 是 | 1024 到 3136（步长 2） |
| `height` | 图像的自定义高度。仅当 `size_preset` 设置为 Custom 时此值才生效（默认值：2048）。 | INT | 是 | 1024 到 2496（步长 2） |

### seedream 5.0 lite 输入

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `size_preset` | 选择推荐尺寸。选择 Custom 以使用下方的宽度和高度。 | COMBO | 是 | 模型特定预设（包含 Custom） |
| `width` | 图像的自定义宽度。仅当 `size_preset` 设置为 Custom 时此值才生效（默认值：2048）。 | INT | 是 | 1024 到 6240（步长 2） |
| `height` | 图像的自定义高度。仅当 `size_preset` 设置为 Custom 时此值才生效（默认值：2048）。 | INT | 是 | 1024 到 4992（步长 2） |
| `max_images` | 要生成的最大图像数量。设置为 1 时，正好生成一张图像。设置为 >1 时，模型会生成 1 到 `max_images` 张相关图像（例如故事场景、角色变体）。图像总数（输入 + 生成）不能超过 15。（默认值：1） | INT | 是 | 1 到 14 |
| `fail_on_partial` | 启用后，如果任何请求的图像缺失或返回错误，则中止执行。（默认值：False） | BOOLEAN | 是 | True / False |

### seedream-4-5-251128 输入

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `size_preset` | 选择推荐尺寸。选择 Custom 以使用下方的宽度和高度。 | COMBO | 是 | 模型特定预设（包含 Custom） |
| `width` | 图像的自定义宽度。仅当 `size_preset` 设置为 Custom 时此值才生效（默认值：2048）。 | INT | 是 | 1024 到 6240（步长 2） |
| `height` | 图像的自定义高度。仅当 `size_preset` 设置为 Custom 时此值才生效（默认值：2048）。 | INT | 是 | 1024 到 4992（步长 2） |
| `max_images` | 要生成的最大图像数量。设置为 1 时，正好生成一张图像。设置为 >1 时，模型会生成 1 到 `max_images` 张相关图像（例如故事场景、角色变体）。图像总数（输入 + 生成）不能超过 15。（默认值：1） | INT | 是 | 1 到 10 |
| `fail_on_partial` | 启用后，如果任何请求的图像缺失或返回错误，则中止执行。（默认值：False） | BOOLEAN | 是 | True / False |

### seedream-4-0-250828 输入

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `size_preset` | 选择推荐尺寸。选择 Custom 以使用下方的宽度和高度。 | COMBO | 是 | 模型特定预设（包含 Custom） |
| `width` | 图像的自定义宽度。仅当 `size_preset` 设置为 Custom 时此值才生效（默认值：2048）。 | INT | 是 | 1024 到 6240（步长 2） |
| `height` | 图像的自定义高度。仅当 `size_preset` 设置为 Custom 时此值才生效（默认值：2048）。 | INT | 是 | 1024 到 4992（步长 2） |
| `max_images` | 要生成的最大图像数量。设置为 1 时，正好生成一张图像。设置为 >1 时，模型会生成 1 到 `max_images` 张相关图像（例如故事场景、角色变体）。图像总数（输入 + 生成）不能超过 15。（默认值：1） | INT | 是 | 1 到 10 |
| `fail_on_partial` | 启用后，如果任何请求的图像缺失或返回错误，则中止执行。（默认值：False） | BOOLEAN | 是 | True / False |

### 参考输入

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `images` | 用于图生图或多参考图像生成的可选参考图像。可增长插槽：连接 1..N 个项目（`image_1`、`image_2`、……、`image_N`）；最大数量取决于所选模型（seedream 5.0 pro、seedream-4-5-251128 和 seedream-4-0-250828 为 10；seedream 5.0 lite 为 14）。 | IMAGE | 否 | 0 到 10<br>0 到 14（seedream 5.0 lite） |

### 备注

- 自定义 `width` 和 `height` 值仅在 `size_preset` 设置为 Custom 时生效。
- 分辨率限制（基于宽 × 高）：
  - seedream 5.0 pro：最小 0.92 MP，最大 4.19 MP。
  - seedream 5.0 lite 和 seedream-4-5-251128：最小 3.68 MP。
  - seedream-4-0-250828：最小 0.92 MP。
  - seedream 5.0 lite、seedream-4-5-251128 和 seedream-4-0-250828：最大 16.78 MP。
- 参考图像的宽高比必须在 1:3 到 3:1 之间。
- 当 `max_images` 大于 1 时（在 seedream 5.0 lite、seedream-4-5-251128 和 seedream-4-0-250828 上可用），图像总数（参考图像加生成图像）不能超过 15。
- `thinking` 只能在文生图时禁用；提供参考图像时必须启用。
- seedream 5.0 pro 始终生成单张图像，不显示 `max_images` 或 `fail_on_partial` 输入。

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `image` | 生成或编辑后的图像。如果使用 `max_images` 请求了多张图像，它们会拼接为一个批次返回。 | IMAGE |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedreamNodeV2/zh.md)

---
**Source fingerprint (SHA-256):** `b57e0d85a586aaeb7cf02ceaaddcd2d36cdac20f5251cba48de602a979420f1c`
