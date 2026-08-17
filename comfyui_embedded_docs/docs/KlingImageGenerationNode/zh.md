# Kling 图像生成

Kling Image Generation Node 根据文本提示生成图像，并可选择使用参考图像进行引导。它根据您的文本描述和参考设置生成一张或多张图像，然后将生成的图像作为输出返回。

## 输入

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 正向文本提示 | STRING | 是 | 最多500个字符 |
| `negative_prompt` | 反向文本提示 | STRING | 是 | 最多500个字符 |
| `image_type` | 图像参考类型选择（高级）。当提供参考图像时使用。 | COMBO | 是 | `"subject_reference"`<br>`"style_reference"` |
| `image_fidelity` | 用户上传图像的参考强度（默认值：0.5，高级） | FLOAT | 是 | 0.0 - 1.0 |
| `human_fidelity` | 主体参考相似度（默认值：0.45，高级） | FLOAT | 是 | 0.0 - 1.0 |
| `model_name` | 用于图像生成的模型选择（默认值："kling-v3"） | COMBO | 是 | `"kling-v3"`<br>`"kling-v2"` |
| `aspect_ratio` | 生成图像的宽高比（默认值："16:9"） | COMBO | 是 | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"`<br>`"21:9"`<br>`"9:21"` |
| `n` | 生成的图像数量（默认值：1） | INT | 是 | 1 - 9 |
| `image` | 可选的参考图像 | IMAGE | 否 | - |
| `seed` | 种子控制节点是否应重新运行；无论种子如何，结果都是非确定性的（默认值：0） | INT | 否 | 0 - 2147483647 |

**参数约束：**

- `image` 参数是可选的。当提供参考图像时，`image_type` 决定将其用作主体参考还是风格参考。当未提供参考图像时，`image_type` 不生效。
- `prompt` 必须包含至少 1 个字符，最多 500 个字符。`negative_prompt` 可以为空，但限制为 500 个字符。
- `seed` 参数是可选的，不保证确定性的结果。

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `output` | 根据输入参数生成的图像。当请求多张图像时，所有图像在单个批次中堆叠返回。 | IMAGE |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingImageGenerationNode/zh.md)

---
**Source fingerprint (SHA-256):** `165d18244870b5b4f34587633a5492e733ad0b0a923bb8c3e506319460321906`
