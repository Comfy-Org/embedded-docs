# 空Latent音频（AceStep）

EmptyAceStepLatentAudio 节点用于创建指定时长的空潜空间音频样本。它会生成一批完全由零填充的静音音频潜变量，其长度根据输入的秒数和音频处理参数计算。此节点适用于初始化需要潜空间表示的音频处理工作流。

## 输入
| 参数 | 描述 | 数据类型 | 必需 | 范围 |
| --- | --- | --- | --- | --- |
| `seconds` | 音频时长（秒，默认：120.0） | FLOAT | 是 | 1.0 - 1000.0 (step 0.1) |
| `batch_size` | 批次中的潜空间图像数量（默认：1） | INT | 是 | 1 - 4096 |

## 输出
| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `output` | 返回用零填充的空潜空间音频样本。输出包含一个 `samples` 张量，以及一个设置为 "audio" 的 `type` 字段。 | LATENT |

注意：潜空间长度由 `seconds` 值以内部 44100 Hz 采样率计算得出，公式为 `int(seconds × 44100 / 512 / 8)` 帧。生成的潜空间张量完全由零填充。

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyAceStepLatentAudio/zh.md)

---
**Source fingerprint (SHA-256):** `8268eb582a28c7acc495c52831cc6edd8f8fdd1b294857451ce94abc37ca0d14`
