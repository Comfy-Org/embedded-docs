# ByteDanceSeedreamNodeV3

ByteDance Seedream 4.5 和 5.0 节点可根据文本提示生成图像（文生图），或借助可选的参考图像进行图像生成/编辑，使用 ByteDance Seedream 4.0、4.5 和 5.0 模型，最高支持 4K 分辨率。该节点会将提示词及任何参考图像发送到 ByteDance API，等待生成任务完成后，返回生成的图像张量（单个或多个）。

## 输入

### 通用输入

| 参数 | 描述 | 数据类型 | 必填 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 用于创建或编辑图像的文本提示词。去除首尾空格后不能为空。 | STRING | 是 | Multiline text |
| `model` | 选择要使用的 Seedream 模型。每个模型都有自己的一组子参数和下方列出的限制。 | DYNAMIC_COMBO | 是 | "seedream 5.0 pro"<br>"seedream 5.0 lite"<br>"seedream-4-5-251128"<br>"seedream-4-0-250828" |

### Seedream 5.0 Pro 输入 (seedream 5.0 pro)

| 参数 | 描述 | 数据类型 | 必填 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `size_preset` | 选择推荐的尺寸。选择 Custom 以使用下面的宽度和高度。默认值：此模型的第一个推荐预设。 | COMBO | 否 | Model-specific recommended size presets<br>"Custom" |
| `width` | 图像的自定义宽度。仅当 `size_preset` 设置为 `Custom` 时生效。默认值：2048。 | INT | 否 | 1024 to 3136 (step 2) |
| `height` | 图像的自定义高度。仅当 `size_preset` 设置为 `Custom` 时生效。默认值：2048。 | INT | 否 | 1024 to 2496 (step 2) |
| `prompt_optimization` | 提供参考图像时的提示词优化模式：'standard' 质量更高，'fast' 生成时间更短。默认值："standard"。 | COMBO | 否 | "standard"<br>"fast" |
| `seed` | 用于生成的随机种子。默认值：42。 | INT | 否 | 0 to 2147483647 |
| `watermark` | 是否在图像上添加“AI 生成”水印。默认值：false。 | BOOLEAN | 否 | true / false |
| `thinking` | 启用模型的提示词优化推理（'thinking'）以获得更好的提示遵循度。可能会显著增加生成时间——尤其是在 Seedream 5.0 Pro 上。仅在文生图模式下可以禁用（提供参考图像时不可禁用）。默认值：true。 | BOOLEAN | 否 | true / false |

### Seedream 5.0 Lite 输入 (seedream 5.0 lite)

| 参数 | 描述 | 数据类型 | 必填 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `size_preset` | 选择推荐的尺寸。选择 Custom 以使用下面的宽度和高度。默认值：此模型的第一个推荐预设。 | COMBO | 否 | Model-specific recommended size presets<br>"Custom" |
| `width` | 图像的自定义宽度。仅当 `size_preset` 设置为 `Custom` 时生效。默认值：2048。 | INT | 否 | 1024 to 6240 (step 2) |
| `height` | 图像的自定义高度。仅当 `size_preset` 设置为 `Custom` 时生效。默认值：2048。 | INT | 否 | 1024 to 4992 (step 2) |
| `max_images` | 生成图像的最大数量。设为 1 时，恰好生成一张图像。设为 >1 时，模型会生成 1 到 max_images 张相关图像（例如故事场景、角色变体）。图像总数（输入 + 生成）不能超过 15。默认值：1。 | INT | 否 | 1 to 14 |
| `fail_on_partial` | 如果启用，当任何请求的图像缺失或返回错误时中止执行。默认值：false。 | BOOLEAN | 否 | true / false |
| `seed` | 用于生成的随机种子。默认值：42。 | INT | 否 | 0 to 2147483647 |
| `watermark` | 是否在图像上添加“AI 生成”水印。默认值：false。 | BOOLEAN | 否 | true / false |
| `thinking` | 启用模型的提示词优化推理（'thinking'）以获得更好的提示遵循度。可能会显著增加生成时间——尤其是在 Seedream 5.0 Pro 上。仅在文生图模式下可以禁用（提供参考图像时不可禁用）。默认值：true。 | BOOLEAN | 否 | true / false |

### Seedream 4.5 输入 (seedream-4-5-251128)

| 参数 | 描述 | 数据类型 | 必填 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `size_preset` | 选择推荐的尺寸。选择 Custom 以使用下面的宽度和高度。默认值：此模型的第一个推荐预设。 | COMBO | 否 | Model-specific recommended size presets<br>"Custom" |
| `width` | 图像的自定义宽度。仅当 `size_preset` 设置为 `Custom` 时生效。默认值：2048。 | INT | 否 | 1024 to 6240 (step 2) |
| `height` | 图像的自定义高度。仅当 `size_preset` 设置为 `Custom` 时生效。默认值：2048。 | INT | 否 | 1024 to 4992 (step 2) |
| `max_images` | 生成图像的最大数量。设为 1 时，恰好生成一张图像。设为 >1 时，模型会生成 1 到 max_images 张相关图像（例如故事场景、角色变体）。图像总数（输入 + 生成）不能超过 15。默认值：1。 | INT | 否 | 1 to 10 |
| `fail_on_partial` | 如果启用，当任何请求的图像缺失或返回错误时中止执行。默认值：false。 | BOOLEAN | 否 | true / false |
| `seed` | 用于生成的随机种子。默认值：42。 | INT | 否 | 0 to 2147483647 |
| `watermark` | 是否在图像上添加“AI 生成”水印。默认值：false。 | BOOLEAN | 否 | true / false |
| `thinking` | 启用模型的提示词优化推理（'thinking'）以获得更好的提示遵循度。可能会显著增加生成时间——尤其是在 Seedream 5.0 Pro 上。仅在文生图模式下可以禁用（提供参考图像时不可禁用）。默认值：true。 | BOOLEAN | 否 | true / false |

### Seedream 4.0 输入 (seedream-4-0-250828)

| 参数 | 描述 | 数据类型 | 必填 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `size_preset` | 选择推荐的尺寸。选择 Custom 以使用下面的宽度和高度。默认值：此模型的第一个推荐预设。 | COMBO | 否 | Model-specific recommended size presets<br>"Custom" |
| `width` | 图像的自定义宽度。仅当 `size_preset` 设置为 `Custom` 时生效。默认值：2048。 | INT | 否 | 1024 to 6240 (step 2) |
| `height` | 图像的自定义高度。仅当 `size_preset` 设置为 `Custom` 时生效。默认值：2048。 | INT | 否 | 1024 to 4992 (step 2) |
| `max_images` | 生成图像的最大数量。设为 1 时，恰好生成一张图像。设为 >1 时，模型会生成 1 到 max_images 张相关图像（例如故事场景、角色变体）。图像总数（输入 + 生成）不能超过 15。默认值：1。 | INT | 否 | 1 to 10 |
| `fail_on_partial` | 如果启用，当任何请求的图像缺失或返回错误时中止执行。默认值：false。 | BOOLEAN | 否 | true / false |
| `seed` | 用于生成的随机种子。默认值：42。 | INT | 否 | 0 to 2147483647 |
| `watermark` | 是否在图像上添加“AI 生成”水印。默认值：false。 | BOOLEAN | 否 | true / false |
| `thinking` | 启用模型的提示词优化推理（'thinking'）以获得更好的提示遵循度。可能会显著增加生成时间——尤其是在 Seedream 5.0 Pro 上。仅在文生图模式下可以禁用（提供参考图像时不可禁用）。默认值：true。 | BOOLEAN | 否 | true / false |

### 参考输入

| 参数 | 描述 | 数据类型 | 必填 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `images` | 可增长插槽：用于图生图或多参考生成的可选参考图像。可连接 1..N 张图像（例如 `image_1`、`image_2` ……）；数量上限取决于具体模型（见下方注意事项）。如果连接的图像包含一个批次的多张图像，则批次中的每一张图像都计入数量上限。 | IMAGE | 否 | 0 to 10 (Seedream 5.0 Pro, Seedream 4.5, Seedream 4.0)<br>0 to 14 (Seedream 5.0 Lite) |

**注意：**

- `prompt` 去除首尾空格后不能为空。
- 参考图像的最大数量：Seedream 5.0 Pro、Seedream 4.5 和 Seedream 4.0 为 10 张；Seedream 5.0 Lite 为 14 张。
- 每张参考图像的宽高比必须在 1:3 到 3:1 之间。
- 当 `max_images` 大于 1 时（Seedream 5.0 Pro 不可用），参考图像与生成图像的总数不能超过 15。
- `thinking` 仅在文生图生成时可以禁用。提供参考图像时，必须启用 `thinking`。
- 仅当 `size_preset` 设置为 "Custom" 时，`width` 和 `height` 才会生效。
- `prompt_optimization` 仅在 Seedream 5.0 Pro 上可用。
- `max_images` 和 `fail_on_partial` 仅在 Seedream 5.0 Lite、Seedream 4.5 和 Seedream 4.0 上可用；Seedream 5.0 Pro 始终只请求生成一张图像。
- 分辨率要求（宽度 x 高度）：
  - Seedream 5.0 Pro：介于 0.92MP（921,600 像素）和 4.19MP（4,194,304 像素）之间。
  - Seedream 5.0 Lite 和 Seedream 4.5：至少 3.68MP（3,686,400 像素）。
  - Seedream 4.0：至少 0.92MP（921,600 像素）。
  - 所有非 Pro 模型：最多 16.78MP（16,777,216 像素）。

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `image` | 生成的图像张量。当生成多张图像时，它们会被拼接为一个单独的批处理 IMAGE 张量。 | IMAGE |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedreamNodeV3/zh.md)

---
**Source fingerprint (SHA-256):** `68dd23afdb5720491cef784b22ad66ff0baf80984ea652ea4c13e6c264c029ac`
