# EulerAncestral采样器

SamplerEulerAncestral 节点用于创建一个欧拉祖先采样器，以生成图像。该采样器采用一种特定的数学方法，将欧拉积分与祖先采样技术相结合，从而产生图像变体。通过调整控制生成过程中随机性和步长的参数，可以配置采样行为。

## 输入

| 参数 | 描述 | 数据类型 | 是否必填 | 范围 |
| --- | --- | --- | --- | --- |
| `eta` | 控制采样过程中的步长和随机性（默认值：1.0）。这是一个高级参数。 | FLOAT | 否 | 0.0 - 100.0 |
| `s_noise` | 控制采样过程中添加的噪声量（默认值：1.0）。这是一个高级参数。 | FLOAT | 否 | 0.0 - 100.0 |

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `sampler` | 返回一个已配置的欧拉祖先采样器，可用于采样流程中。 | SAMPLER |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerEulerAncestral/zh.md)

---
**Source fingerprint (SHA-256):** `0d3c1f0ffe01eb6cc17fd53e743713f659218ec19001c670440472ae7d0d3887`
