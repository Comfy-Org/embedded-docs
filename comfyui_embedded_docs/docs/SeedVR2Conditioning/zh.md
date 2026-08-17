# 应用 SeedVR2 条件

此节点从 VAE 潜在变量构建正面和负面条件，用于 SeedVR2 模型。它向潜在变量添加一个掩码通道，然后将其与模型内置的正面和负面条件嵌入配对，以生成采样所需的条件值。

## 输入

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `model` | SeedVR2 模型。 | MODEL | 是 | - |
| `vae_conditioning` | 用于构建条件的 VAE 潜在变量。显示名称：latent。 | LATENT | 是 | - |

`vae_conditioning` 潜在变量必须是 Comfy 通道优先布局（B、C、T、H、W）下的 5 维张量，且通道数需与 SeedVR2 VAE 预期的一致。通道在后的潜在变量将被拒绝并报错。`model` 输入必须是有效的 SeedVR2 模型，且具有预期的内部结构。

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `positive` | 用于采样的正面条件。 | CONDITIONING |
| `negative` | 用于采样的负面条件。 | CONDITIONING |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedVR2Conditioning/zh.md)

---
**Source fingerprint (SHA-256):** `28e508bdd776e2e3f5f2f93bfc29a1a1d1c34a11dbdc7f421d197ddbfa85f0f5`
