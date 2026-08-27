# Trellis2UpsampleStage

此节点接收第一次形状阶段采样过程生成的 512 分辨率形状 latent，将其放大到更高的目标分辨率，并为第二次形状阶段采样过程准备所需的 conditioning 和 latent。它还会将每个阶段的元数据附加到 conditioning 上，以便模型在生成过程中使用。

## 输入
| 参数 | 描述 | 数据类型 | 是否必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `positive` | 附加了上采样阶段形状元数据的正向 conditioning。 | CONDITIONING | 是 | |
| `negative` | 附加了上采样阶段形状元数据的负向 conditioning。 | CONDITIONING | 是 | |
| `shape_latent` | 第一个形状阶段 KSampler 输出的 512 分辨率形状 latent。 | LATENT | 是 | |
| `vae` | 用于将形状 latent 解码为高分辨率稀疏坐标的 Trellis2 VAE。 | VAE | 是 | |
| `target_resolution` | 上采样形状的体素分辨率。值越高，细节越丰富，显存占用也越多。默认值：1024。 | INT | 是 | 1024 - 2048 (step 128) |

## 输出
| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `positive` | 附加了上采样阶段形状元数据的正向 conditioning。 | CONDITIONING |
| `negative` | 附加了上采样阶段形状元数据的负向 conditioning。 | CONDITIONING |
| `latent` | 为目标分辨率下的第二次形状阶段采样过程准备的零填充 latent，携带上采样后的坐标和分辨率元数据。 | LATENT |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Trellis2UpsampleStage/zh.md)

---
**Source fingerprint (SHA-256):** `0582579bfab487718d69789de508a5ec243d98a0e06ad7165c406154a64677d6`
