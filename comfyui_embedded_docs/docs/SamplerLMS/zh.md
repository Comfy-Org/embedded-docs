# LMS采样器

SamplerLMS 节点创建一个用于扩散模型的最小均方（LMS）采样器。它会生成一个可用于采样过程的采样器对象，使您能够控制 LMS 算法的阶数，以实现数值稳定性和准确性。

## 输入

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
| --- | --- | --- | --- | --- |
| `order` | LMS 采样器算法的阶数参数，控制数值方法的准确性和稳定性（默认值：4；高级参数） | INT | 是 | 1 to 100 |

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `sampler` | 一个已配置的 LMS 采样器对象，可用于采样流程 | SAMPLER |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerLMS/zh.md)

---
**Source fingerprint (SHA-256):** `3d59fbbd5b9b0bfa2ee3b384aca08855988d0b7a2a94d805f978b9dd7caa0f39`
