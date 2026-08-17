# 替换视频Latent

ReplaceVideoLatentFrames 节点将源潜在视频中的帧插入到目标潜在视频中，从指定的帧索引开始。如果未提供源潜在变量，则原样返回目标潜在变量。该节点支持负索引，并在源帧超出目标范围时发出警告。

## 输入

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
| --- | --- | --- | --- | --- |
| `destination` | 目标潜在变量，将在此处替换帧。 | LATENT | 是 | - |
| `source` | 源潜在变量，用于提供要插入到目标潜在变量中的帧。如果未提供，则原样返回目标潜在变量。 | LATENT | 否 | - |
| `index` | 目标潜在变量中源潜在变量帧的起始帧索引。负值表示从末尾计数（默认：0）。 | INT | 是 | -MAX_RESOLUTION 到 MAX_RESOLUTION（步长：1） |

**约束条件：**

* `index` 必须在目标潜在变量的帧数范围内。如果超出范围，将记录警告并原样返回目标。
* 从指定的 `index` 开始，源潜在变量帧必须能放入目标潜在变量帧中。如果无法放入，将记录警告并原样返回目标。

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `output` | 帧替换操作后得到的潜在视频。 | LATENT |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReplaceVideoLatentFrames/zh.md)

---
**Source fingerprint (SHA-256):** `5b98d875bdeaec63521bff19fecbc5510036c8b4f90322d8296b216688b557bf`
