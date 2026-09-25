# ByteDance Seedance 2.0 首帧-末帧生成视频

此节点使用 ByteDance Seedance 模型，从必需的首帧图像和可选的尾帧图像生成视频。你通过文本提示描述视频；首帧引导视频的开始，尾帧引导视频的结束。它支持 Seedance 2.5 和 Seedance 2.0 系列（Seedance 2.0、Seedance 2.0 Fast 和 Seedance 2.0 Mini）。选择 `Seedance 2.5 Draft` 模型会改为渲染快速的 480p 预览；将生成的 `draft_task_id` 连接到 ByteDance Seedance 2.5 Draft to Final Video 节点，以渲染 1080p 最终视频。

## 输入

### 通用输入

| 参数 | 描述 | 数据类型 | 是否必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `模型` | Seedance 2.5 用于最新模型，视频最长 30 秒并输出 mp4/mov；Seedance 2.5 Draft 用于快速 480p 预览，其 `draft_task_id` 输出可在 ByteDance Seedance 2.5 Draft to Final Video 节点中渲染 1080p 最终视频；Seedance 2.0 用于最高质量和 4k；Seedance 2.0 Fast 用于速度优化；Seedance 2.0 Mini 用于最快、成本最低的生成。选择某个模型后，下方会显示该模型专属的输入。 | DYNAMIC_COMBO | 是 | `"Seedance 2.5"`<br>`"Seedance 2.5 Draft"`<br>`"Seedance 2.0"`<br>`"Seedance 2.0 Fast"`<br>`"Seedance 2.0 Mini"` |
| `首帧图像` | 视频的首帧图像。 | IMAGE | 否 | - |
| `末帧图像` | 视频的尾帧图像。 | IMAGE | 否 | - |
| `first_frame_asset_id` | 用作首帧的 Seedance asset_id。与 `first_frame` 图像输入互斥。默认值为空字符串。 | STRING | 否 | - |
| `last_frame_asset_id` | 用作尾帧的 Seedance asset_id。与 `last_frame` 图像输入互斥。默认值为空字符串。 | STRING | 否 | - |
| `种子` | `seed` 控制节点是否应重新运行；无论 `seed` 如何，结果都是非确定性的。默认值为 0。 | INT | 是 | 0 到 2147483647 |
| `水印` | 是否向视频添加水印。默认值为 False。 | BOOLEAN | 是 | False<br>True |

### Seedance 2.5 输入

当选择 `Seedance 2.5` 时，会显示这些输入。

| 参数 | 描述 | 数据类型 | 是否必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 用于视频生成的文本提示。将台词放在双引号中，以引导生成的对话。 | STRING | 是 | - |
| `resolution` | 输出视频的分辨率。默认值为 720p。 | COMBO | 是 | `"480p"`<br>`"720p"`<br>`"1080p"` |
| `duration` | 输出视频的时长，单位为秒（4-30）。默认值为 5。 | INT | 是 | 4 到 30 |
| `generate_audio` | 为输出视频启用音频生成。默认值为 True。 | BOOLEAN | 是 | False<br>True |
| `output_format` | 输出视频的容器格式。默认值为 mp4。 | COMBO | 是 | `"mp4"` |

### Seedance 2.5 Draft 输入

当选择 `Seedance 2.5 Draft` 时，会显示这些输入。参数集与上方的 Seedance 2.5 匹配，不同之处在于 `resolution` 仅提供 `"480p"`（默认 `"480p"`）。

### Seedance 2.0 输入

当选择 `Seedance 2.0` 时，会显示这些输入。

| 参数 | 描述 | 数据类型 | 是否必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 用于视频生成的文本提示。 | STRING | 是 | - |
| `resolution` | 输出视频的分辨率。 | COMBO | 是 | `"480p"`<br>`"720p"`<br>`"1080p"`<br>`"4k"` |
| `ratio` | 输出视频的宽高比。默认值为 `adaptive`，它会使用与输入帧宽高比最接近的受支持比例。 | COMBO | 是 | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | 输出视频的时长，单位为秒（4-15）。默认值为 7。 | INT | 是 | 4 到 15 |
| `generate_audio` | 为输出视频启用音频生成。默认值为 True。 | BOOLEAN | 是 | False<br>True |

### Seedance 2.0 Fast 和 Seedance 2.0 Mini 输入

由 `Seedance 2.0 Fast` 和 `Seedance 2.0 Mini` 共用。

| 参数 | 描述 | 数据类型 | 是否必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 用于视频生成的文本提示。 | STRING | 是 | - |
| `resolution` | 输出视频的分辨率。 | COMBO | 是 | `"480p"`<br>`"720p"` |
| `ratio` | 输出视频的宽高比。默认值为 `adaptive`，它会使用与输入帧宽高比最接近的受支持比例。 | COMBO | 是 | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | 输出视频的时长，单位为秒（4-15）。默认值为 7。 | INT | 是 | 4 到 15 |
| `generate_audio` | 为输出视频启用音频生成。默认值为 True。 | BOOLEAN | 是 | False<br>True |

**参数约束**

- 必须通过 `first_frame` 图像或 `first_frame_asset_id` 提供首帧。同时提供两者会引发错误；两者都不提供也会引发错误。
- `last_frame` 和 `last_frame_asset_id` 输入是可选的，但不能为同一帧同时提供两者。
- 资产 ID 必须引用现有且有效的 Seedance Image 资产。
- `prompt` 输入为必填项，不能为空。
- `draft_task_id` 输出仅由 `Seedance 2.5 Draft` 生成；使用任何其他模型时，必须将其保持未连接，否则运行会失败。
- 使用 `Seedance 2.5` 时，输出宽高比始终为 adaptive，并遵循首帧自身的宽高比，因此不会显示 `ratio` 输入。
- 使用 Seedance 2.0 系列模型和本地帧图像时，图像会在生成前被居中裁剪并调整为目标输出分辨率和宽高比。当 `ratio` 为 `adaptive` 时，会使用与输入图像最接近的受支持宽高比。
- 本地帧图像会针对受支持的宽高比和尺寸进行验证；过大的图像会被缩小。

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `output` | 生成的视频。 | VIDEO |
| `draft_task_id` | 草稿运行的任务 ID。仅 Seedance 2.5 Draft 模型会产生它；将其连接到 ByteDance Seedance 2.5 Draft to Final Video 节点，以渲染 1080p 最终视频。 | STRING |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2FirstLastFrameNode/zh.md)

---
**Source fingerprint (SHA-256):** `363f1baac1685c2dada0e64a0b339f6ab2671161dccb002eb81f6b4f0d0aa243`
