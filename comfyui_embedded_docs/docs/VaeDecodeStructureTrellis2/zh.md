# VaeDecodeStructureTrellis2

此节点使用 VAE 的结构解码器，将 Trellis 结构潜在样本转换为 3D 体素网格。它仅读取潜在变量的前 8 个通道，重建体素占用状态，并将输出分辨率调整为所请求的 32 或 64。

## 输入

| 参数 | 描述 | 数据类型 | 必填 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `samples` | 待解码结构的潜在表示。解码时仅使用潜在变量的前 8 个通道。 | LATENT | 是 | - |
| `vae` | 其结构解码器将潜在变量转换为体素网格的 VAE。解码过程按批次执行。 | VAE | 是 | - |
| `resolution` | 输出体素网格的目标空间分辨率（默认值："32"）。如果解码后的网格分辨率不同，则会进行下采样以匹配。 | COMBO | 是 | "32"<br>"64" |

注意：当解码后的体素网格分辨率与所选 `resolution` 不同时，网格将使用 3D 最大池化下采样到所请求的大小。

## 输出

| 输出名 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `voxel` | 一个二值体素占用网格，表示为形状为 [batch, depth, height, width] 的浮点张量。占用体素的值为 1.0，空体素的值为 0.0。 | VOXEL |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VaeDecodeStructureTrellis2/zh.md)

---
**Source fingerprint (SHA-256):** `37764ef7351b3619d4cddb57b11d9a0da24dadeedc0fc0f70d089038d37e03b0`
