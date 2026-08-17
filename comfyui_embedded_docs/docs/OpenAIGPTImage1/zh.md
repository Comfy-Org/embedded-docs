# OpenAI GPT Image 2

通过 OpenAI 的 GPT Image 端点同步生成图像。此节点可以根据文本提示创建新图像，或在提供输入图像和可选掩码时编辑现有图像。它支持多个 GPT Image 模型，包括 gpt-image-1、gpt-image-1.5 和 gpt-image-2。此节点已弃用。

## 输入

| 参数 | 描述 | 数据类型 | 必填 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | GPT Image 的文本提示（默认：""） | STRING | 是 | - |
| `seed` | 生成时的随机种子（默认：0）- 后端尚未实现 | INT | 否 | 0 到 2147483647 |
| `quality` | 图像质量，影响成本和生成时间（默认："low"） | COMBO | 否 | "low"<br>"medium"<br>"high" |
| `background` | 返回带背景或不带背景的图像（默认："auto"） | COMBO | 否 | "auto"<br>"opaque"<br>"transparent" |
| `size` | 图像大小。选择 "Custom" 以使用自定义宽度和高度（仅 GPT Image 2）（默认："auto"） | COMBO | 否 | "auto"<br>"1024x1024"<br>"1024x1536"<br>"1536x1024"<br>"2048x2048"<br>"2048x1152"<br>"1152x2048"<br>"3840x2160"<br>"2160x3840"<br>"Custom" |
| `n` | 生成图像的数量（默认：1） | INT | 否 | 1 到 8 |
| `image` | 用于图像编辑的可选参考图像 | IMAGE | 否 | - |
| `mask` | 用于修复的可选掩码（白色区域将被替换） | MASK | 否 | - |
| `model` | 要使用的 GPT Image 模型（默认："gpt-image-2"） | COMBO | 否 | "gpt-image-1"<br>"gpt-image-1.5"<br>"gpt-image-2" |
| `custom_width` | 仅当 `size` 为 "Custom" 时使用。必须是 16 的倍数（仅 GPT Image 2）（默认：1024） | INT | 否 | 1024 到 3840 |
| `custom_height` | 仅当 `size` 为 "Custom" 时使用。必须是 16 的倍数（仅 GPT Image 2）（默认：1024） | INT | 否 | 1024 到 3840 |

**参数约束：**

- 当提供 `image` 时，节点切换到图像编辑模式
- 仅当提供 `image` 时才能使用 `mask`
- 使用 `mask` 时，仅支持单张图像（批次大小必须为 1）
- `mask` 和 `image` 必须具有相同大小
- 自定义分辨率（`size` = "Custom"）仅受 gpt-image-2 模型支持
- 自定义宽度和高度必须是 16 的倍数
- 自定义分辨率的宽高比不得超过 3:1
- 自定义分辨率的总像素必须介于 655,360 和 8,294,400 之间
- gpt-image-2 模型不支持透明背景
- 大于 1536x1024 的尺寸（例如 2048x2048、3840x2160）仅受 gpt-image-2 模型支持

## 输出

| 输出名 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `IMAGE` | 生成或编辑后的图像 | IMAGE |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIGPTImage1/zh.md)

---
**Source fingerprint (SHA-256):** `bf588bffced6e66536b4cb54655ef6ebb9cf988d9739e3c379a8ebda1486e20a`
