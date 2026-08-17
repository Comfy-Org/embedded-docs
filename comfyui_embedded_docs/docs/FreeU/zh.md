# FreeU

FreeU 节点对模型的输出模块应用频域修改，以提升图像生成质量。其工作原理是对不同的通道组进行缩放，并对特定特征图应用傅里叶滤波，从而在生成过程中对模型行为进行精细控制。

## 输入

| 参数 | 描述 | 数据类型 | 是否必需 | 范围 |
| --- | --- | --- | --- | --- |
| `model` | 要对其应用 FreeU 修改的模型 | MODEL | 是 | - |
| `b1` | 针对 model_channels × 4 特征的主干缩放因子（默认值：1.1） | FLOAT | 是 | 0.0 - 10.0 |
| `b2` | 针对 model_channels × 2 特征的主干缩放因子（默认值：1.2） | FLOAT | 是 | 0.0 - 10.0 |
| `s1` | 针对 model_channels × 4 特征的跳跃连接缩放因子（默认值：0.9） | FLOAT | 是 | 0.0 - 10.0 |
| `s2` | 针对 model_channels × 2 特征的跳跃连接缩放因子（默认值：0.2） | FLOAT | 是 | 0.0 - 10.0 |

注意：这些修改仅应用于具有 model_channels × 4 和 model_channels × 2 通道的特征图；`b1`/`s1` 影响前者，`b2`/`s2` 影响后者。其他特征图保持不变。

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `model` | 应用了 FreeU 补丁的修改后模型 | MODEL |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FreeU/zh.md)

---
**Source fingerprint (SHA-256):** `7f7bd34964218ed16c9e58caa446d0c1e69f116607334df4a114cdc4adaf047f`
