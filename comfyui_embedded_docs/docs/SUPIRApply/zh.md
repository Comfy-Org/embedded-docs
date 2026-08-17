# SUPIRApply

SUPIRApply 节点将 SUPIR 模型补丁应用于扩散模型。它使用该补丁修改模型的行为，使其在采样过程中能够融入来自输入图像的引导。该节点还提供控件，可随时间调整此引导的强度，并包含一个可选功能，有助于保持对原始输入的保真度。

## 输入
| 参数 | 描述 | 数据类型 | 是否必需 | 范围 |
| --- | --- | --- | --- | --- |
| `model` | 将应用 SUPIR 补丁的基础扩散模型。 | MODEL | 是 | - |
| `model_patch` | 包含用于修改模型的权重和配置的 SUPIR 模型补丁。 | MODELPATCH | 是 | - |
| `vae` | 用于将输入图像编码为潜在表示的 VAE（变分自编码器）。 | VAE | 是 | - |
| `image` | 用于引导生成过程的输入图像。仅使用前三个颜色通道（RGB）。 | IMAGE | 是 | - |
| `strength_start` | 采样开始（高 sigma）时的控制强度。图像引导的影响从此值开始。（默认值：1.0） | FLOAT | 否 | 0.0 - 10.0 |
| `strength_end` | 采样结束（低 sigma）时的控制强度。从起始值线性插值。图像引导的影响到此值结束。（默认值：1.0） | FLOAT | 否 | 0.0 - 10.0 |
| `restore_cfg` | 将去噪输出拉向输入潜在表示。值越高，对输入的保真度越强。设为 0 可禁用。（默认值：4.0） | FLOAT | 否 | 0.0 - 20.0 |
| `restore_cfg_s_tmin` | 低于此 sigma 阈值时，`restore_cfg` 将被禁用。（默认值：0.05） | FLOAT | 否 | 0.0 - 1.0 |

*注意：* 处理 `image` 输入时会仅提取 RGB 通道。如果提供的图像带有 alpha 通道，则 alpha 通道将被忽略。

## 输出
| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `model` | 已应用 SUPIR 补丁并配置了任何附加 CFG 后置函数的扩散模型。 | MODEL |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SUPIRApply/zh.md)

---
**Source fingerprint (SHA-256):** `fa9f67f63777160863c44c620d8de11e92f79245c3f5b60e138975dfd0cc65c7`
