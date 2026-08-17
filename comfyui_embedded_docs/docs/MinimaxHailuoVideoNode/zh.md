# MiniMax 海螺视频

使用 MiniMax Hailuo-02 模型根据文本提示生成视频。你可以选择提供一张起始图像作为第一帧，以生成从该图像继续的视频。

## 输入

| 参数 | 描述 | 数据类型 | 必填 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `prompt_text` | 用于指导视频生成的文本提示。 | STRING | 是 | - |
| `seed` | 用于创建噪声的随机种子（默认：0）。 | INT | 否 | 0 到 18446744073709551615 |
| `first_frame_image` | 可选图像，用作生成视频的第一帧。 | IMAGE | 否 | - |
| `prompt_optimizer` | 在需要时优化提示以提高生成质量（默认：True）。 | BOOLEAN | 否 | - |
| `duration` | 输出视频的时长（秒）（默认：6）。 | COMBO | 否 | `6`<br>`10` |
| `resolution` | 视频显示分辨率。1080p 为 1920x1080，768p 为 1366x768（默认："768P"）。 | COMBO | 否 | `"768P"`<br>`"1080P"` |

**注意：**
- 当未提供 `first_frame_image` 时，`prompt_text` 必须为非空字符串。
- 使用 MiniMax-Hailuo-02 模型且分辨率为 1080P 时，时长限制为 6 秒。

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `output` | 生成的视频文件。 | VIDEO |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuoVideoNode/zh.md)

---
**Source fingerprint (SHA-256):** `f371aae15cfbe7353236bc679c8a6d558703c5037e49ab7ddb9bdf5c50ef0995`
