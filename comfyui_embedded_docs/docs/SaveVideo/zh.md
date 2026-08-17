# 保存视频

SaveVideo 节点将输入视频保存到您的 ComfyUI 输出目录中。它允许您选择文件名前缀、视频格式和编解码器，并通过添加计数器自动创建唯一的文件名。默认情况下，该节点还会将工作流元数据存储到保存的视频中。

## 输入

### 通用输入

| 参数 | 描述 | 数据类型 | 必填 | 范围 |
| --- | --- | --- | --- | --- |
| `codec` | 用于视频的编解码器。选择 `h264` 将显示额外的编码选项（默认值："auto"）。 | DYNAMIC_COMBO | 是 | "auto"<br>"h264" |
| `video` | 要保存的视频。 | VIDEO | 是 | - |
| `filename_prefix` | 要保存文件的前缀。其中可包含格式化信息，例如 `%date:yyyy-MM-dd%` 或 `%Empty Latent Image.width%`，以包含来自节点的值（默认值："video/ComfyUI"）。 | STRING | 是 | - |
| `format` | 保存视频的格式。这决定了所保存视频的文件扩展名（默认值："auto"）。 | COMBO | 是 | "auto"<br>"mp4"<br>"webm"<br>"mkv"<br>"gif" |

### h264 输入

当 `codec` 设置为 `h264` 时，会显示这些输入。

| 参数 | 描述 | 数据类型 | 必填 | 范围 |
| --- | --- | --- | --- | --- |
| `encoding` | H.264 的编码模式。自动（Automatic）保留兼容的 H.264 流。重新编码（Re-encode）应用自定义 CRF（默认值："auto"）。 | DYNAMIC_COMBO | 否 | "auto"<br>"re-encode" |
| `crf` | 数值越低，质量越高，文件越大。仅当 `encoding` 设置为 `re-encode` 时可用（默认值：23.0）。 | FLOAT | 是（仅当 `encoding` 为 `re-encode` 时） | 0.0 to 51.0 (step: 1.0) |

注意：如果 `filename_prefix` 包含文件夹，例如 `video/ComfyUI`，视频将保存到输出目录中的该子文件夹内。文件名由前缀和追加的计数器构成，例如 `ComfyUI_00001_.mp4`，因此不会覆盖现有文件。

注意：当元数据功能启用时，节点会将工作流提示词和附加元数据嵌入保存的视频中。可通过在启动 ComfyUI 时添加 `--disable-metadata` 参数来禁用元数据。

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `video` | 已保存的视频，从输入中传递而来。 | VIDEO |
| `ui` | 所保存视频文件的预览，包含文件路径和子文件夹信息，用于在 UI 中显示。 | PREVIEW_VIDEO |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveVideo/zh.md)

---
**Source fingerprint (SHA-256):** `c1fd5ac1043f0811951136b2d09cd59840b0c542079da9ed04c17cca7c02562b`
