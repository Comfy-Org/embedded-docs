# Laplace调度器

LaplaceScheduler 节点生成一系列遵循拉普拉斯分布的 sigma 值，用于扩散采样。它使用拉普拉斯分布参数控制进度，创建一个从最大值逐渐减小到最小值的噪声水平调度。该调度器通常用于自定义采样工作流中，为扩散模型定义噪声调度。

## 输入
| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `steps` | 调度中的采样步数（默认值：20） | INT | Yes | 1 to 10000 |
| `sigma_max` | 调度开始时的最大 sigma 值（默认值：14.614642） | FLOAT | Yes | 0.0 to 5000.0 |
| `sigma_min` | 调度结束时的最小 sigma 值（默认值：0.0291675） | FLOAT | Yes | 0.0 to 5000.0 |
| `mu` | 拉普拉斯分布的均值参数（默认值：0.0） | FLOAT | Yes | -10.0 to 10.0 |
| `beta` | 拉普拉斯分布的尺度参数（默认值：0.5） | FLOAT | Yes | 0.0 to 10.0 |

## 输出
| Output Name | Description | Data Type |
| --- | --- | --- |
| `SIGMAS` | 遵循拉普拉斯分布调度的 sigma 值序列 | SIGMAS |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LaplaceScheduler/zh.md)

---
**Source fingerprint (SHA-256):** `8e5ca00f4797f863a2cf8b9b115ec27beb7f65981cbb04eb036150402fc19389`
