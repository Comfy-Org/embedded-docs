# Latent操作锐化

LatentOperationSharpen 节点使用高斯核对潜在表示应用锐化效果。它通过归一化潜在数据、使用自定义锐化核进行卷积，然后恢复原始亮度来工作。这增强了潜在空间表示中的细节和边缘。

## 输入

| 参数 | 描述 | 数据类型 | 必填 | 范围 |
| --- | --- | --- | --- | --- |
| `sharpen_radius` | 锐化核的半径。完整核大小计算为此值的两倍加一（默认值：9）。 | INT | 是 | 1-31 |
| `sigma` | 高斯核的标准差（默认值：1.0）。 | FLOAT | 是 | 0.1-10.0 |
| `alpha` | 控制效果强度的锐化强度因子（默认值：0.1）。 | FLOAT | 是 | 0.0-5.0 |

所有输入均为高级参数。此节点被标记为实验性。

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `operation` | 可应用于潜在数据的锐化操作。将其应用于潜在数据会返回锐化版本，并保留原始亮度。 | LATENT_OPERATION |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentOperationSharpen/zh.md)

---
**Source fingerprint (SHA-256):** `8f49b7e47d35547a7169e9ec209328adbe084ee861ac26b9f26e4e644ac14d6d`
