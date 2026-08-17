# Latent应用操作CFG

LatentApplyOperationCFG 节点通过应用潜在操作来修改模型中的条件引导过程。其工作原理是在无分类器引导（CFG）采样过程中拦截条件输出，并在潜在表示用于生成之前对它们应用指定操作。

当模型产生两个条件输出（例如正向和负向条件）时，该操作应用于它们之间的差值，然后再加回第二个条件。当只有一个条件输出时，该操作直接应用于该输出。此节点标记为实验性。

## 输入
| 参数 | 描述 | 数据类型 | 必需 | 范围 |
| --- | --- | --- | --- | --- |
| `model` | 将应用 CFG 操作的模型 | MODEL | 是 | - |
| `operation` | 在 CFG 采样过程中应用的潜在操作 | LATENT_OPERATION | 是 | - |

## 输出
| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `model` | 应用了 CFG 操作以修改其采样过程的模型 | MODEL |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentApplyOperationCFG/zh.md)

---
**Source fingerprint (SHA-256):** `e383684a785878bfa4004c2fac78ae562d8e035fdfe081f8e4ebbb2c50161987`
