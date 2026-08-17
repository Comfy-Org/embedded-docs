# 采样算法（LTXV）

ModelSamplingLTXV 节点根据 token 数量对模型应用高级采样参数。它通过在线性插值中基于基础移位值和最大移位值之间计算移位值，具体计算取决于输入 latent 中的 token 数量。该节点随后创建专门的模型采样配置，并将其应用于输入模型。

## 输入

| 参数 | 描述 | 数据类型 | 是否必填 | 范围 |
| --- | --- | --- | --- | --- |
| `model` | 要应用采样参数的输入模型 | MODEL | 是 | - |
| `max_shift` | 线性插值计算中使用的最大移位值。当 token 数量为 4096 时，移位值等于该最大值（默认值：2.05） | FLOAT | 是 | 0.0 至 100.0 |
| `base_shift` | 线性插值计算中使用的基础移位值。当 token 数量为 1024 时，移位值等于该基础值（默认值：0.95） | FLOAT | 是 | 0.0 至 100.0 |
| `latent` | 可选的 latent 输入，用于确定移位计算中的 token 数量。token 数量为 latent 样本空间维度的乘积。如果未提供，则使用默认 token 数量 4096 | LATENT | 否 | - |

注意：移位值通过在 `base_shift`（1024 个 token）和 `max_shift`（4096 个 token）之间进行线性插值计算。当未提供 `latent` 时，默认 token 数量为 4096，移位值等于 `max_shift`。

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `model` | 已应用采样参数的修改后模型 | MODEL |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingLTXV/zh.md)

---
**Source fingerprint (SHA-256):** `aba596c5478e9d6ee821eec1eca15506935bcc765a368087ccc442fc2ed6671b`
