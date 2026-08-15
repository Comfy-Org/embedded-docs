# HappyHorse 图像转视频

此节点使用 HappyHorse 模型从单个起始图像生成短视频。您提供首帧图像和描述预期运动与场景的文本提示，节点将创建从该图像继续生成的视频。

## 输入
### 通用输入

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `model` | 用于视频生成的 HappyHorse 模型。 | COMBO | 是 | `"happyhorse-1.1-i2v"`<br>`"happyhorse-1.0-i2v"` |
| `first_frame` | 首帧图像。输出的宽高比由此图像决定。 | IMAGE | 是 | 最小 300×300 像素；宽高比 1:2.5 至 2.5:1 |
| `seed` | 用于生成的种子。（默认值：0） | INT | 否 | 0 到 2147483647 |
| `watermark` | 是否在结果中添加 AI 生成的水印。（高级选项；默认值：False） | BOOLEAN | 否 | True / False |

### happyhorse-1.1-i2v 和 happyhorse-1.0-i2v 输入

两个模型版本共享相同的参数集。

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `提示词` | 描述元素和视觉特征的提示词。支持英文和中文。（默认值：""） | STRING | 否 | N/A |
| `分辨率` | 输出视频分辨率。（默认值："720P"） | COMBO | 是 | `"720P"`<br>`"1080P"` |
| `时长` | 生成视频的时长（秒）。（默认值：5） | INT | 是 | 3 到 15 |

注意：`first_frame` 图像必须至少为 300x300 像素，且其宽高比必须在 1:2.5 到 2.5:1 之间。

## 输出
| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `video` | 生成的视频文件。 | VIDEO |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HappyHorseImageToVideoApi/zh.md)

---
**Source fingerprint (SHA-256):** `4bf6eece0d1b4104ce2d84e29b2c918a0a6ba782da1dd801b66cbfa1666d150b`
