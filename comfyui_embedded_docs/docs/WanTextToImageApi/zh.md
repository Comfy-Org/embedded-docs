> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanTextToImageApi/zh.md)

Wan 文生图节点根据文本描述生成图像。它利用 AI 模型从文字提示中创建视觉内容，支持中英文文本输入。该节点提供多种控制选项，用于调整输出图像的尺寸、质量和风格偏好。

## 输入

| 参数 | 数据类型 | 是否必填 | 取值范围 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | 是 | "wan2.5-t2i-preview" | 使用的模型（默认值："wan2.5-t2i-preview"） |
| `prompt` | STRING | 是 | - | 描述画面元素和视觉特征的提示词。支持中英文（默认值：空） |
| `negative_prompt` | STRING | 否 | - | 描述需要避免内容的负面提示词（默认值：空） |
| `width` | INT | 否 | 768-1440 | 图像宽度（像素）（默认值：1024，步长：32） |
| `height` | INT | 否 | 768-1440 | 图像高度（像素）（默认值：1024，步长：32） |
| `seed` | INT | 否 | 0-2147483647 | 用于生成的随机种子（默认值：0） |
| `prompt_extend` | BOOLEAN | 否 | - | 是否使用 AI 辅助增强提示词（默认值：True） |
| `watermark` | BOOLEAN | 否 | - | 是否在结果中添加 AI 生成水印（默认值：False） |

## 输出

| 输出名称 | 数据类型 | 描述 |
|-------------|-----------|-------------|
| `output` | IMAGE | 根据文本提示生成的图像 |

---
**Source fingerprint (SHA-256):** `2a59551d7ff0fc0553f41561afd94092d2d950ac3e1aa3f6402436540da7d6fb`
