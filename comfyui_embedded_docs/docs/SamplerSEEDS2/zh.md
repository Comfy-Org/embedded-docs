# SEEDS2采样器

此节点提供了一个可配置的采样器，用于生成图像。它实现了 SEEDS-2 算法，这是一种随机微分方程（SDE）求解器。通过调整其参数，您可以将其配置为类似多种特定采样器的行为，包括 `seeds_2`、`exp_heun_2_x0` 和 `exp_heun_2_x0_sde`。

## 输入

| 参数 | 描述 | 数据类型 | 是否必需 | 范围 |
| --- | --- | --- | --- | --- |
| `solver_type` | 选择采样器所使用的底层求解器算法。 | COMBO | 是 | `"phi_1"`<br>`"phi_2"` |
| `eta` | 随机强度（默认值：1.0）。 | FLOAT | 否 | 0.0 - 100.0 |
| `s_noise` | SDE 噪声乘数（默认值：1.0）。 | FLOAT | 否 | 0.0 - 100.0 |
| `r` | 中间阶段（c2 节点）的相对步长（默认值：0.5）。 | FLOAT | 否 | 0.01 - 1.0 |

根据参数设置，此采样器可以表示：

- `seeds_2` — 默认设置
- `exp_heun_2_x0` — `solver_type`=`phi_2`, `r`=1.0, `eta`=0.0
- `exp_heun_2_x0_sde` — `solver_type`=`phi_2`, `r`=1.0, `eta`=1.0, `s_noise`=1.0

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `sampler` | 一个已配置的采样器对象，可传递给其他采样节点。 | SAMPLER |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerSEEDS2/zh.md)

---
**Source fingerprint (SHA-256):** `f48744a706a49ef93d41845bf8c308af971853f6150afd00ded45f0317ffc4f9`
