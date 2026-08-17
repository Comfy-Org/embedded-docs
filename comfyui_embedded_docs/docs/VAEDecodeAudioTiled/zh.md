# VAE解码音频（分块）

此节点使用变分自编码器（VAE）将压缩的音频表示（潜在样本）转换回音频波形。它通过较小的重叠区块（tiles）处理数据，以节省内存，从而适合处理较长的音频序列。

## 输入

| 参数 | 描述 | 数据类型 | 必填 | 范围 |
| --- | --- | --- | --- | --- |
| `samples` | 待解码音频的压缩潜在表示。 | LATENT | 是 | N/A |
| `vae` | 用于执行解码的变分自编码器模型。 | VAE | 是 | N/A |
| `tile_size` | 每个处理区块的大小。音频按此长度分段解码以节省内存（默认：512）。 | INT | 是 | 32 to 8192 |
| `overlap` | 相邻区块重叠的样本数。这有助于减少区块边界处的伪影（默认：64）。 | INT | 是 | 0 to 1024 |

## 输出

| 输出名 | 描述 | 数据类型 |
| --- | --- | --- |
| `output` | 解码后的音频波形。 | AUDIO |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEDecodeAudioTiled/zh.md)

---
**Source fingerprint (SHA-256):** `5ddedf218ba27ab9f463646c1e5288091172f2d7fae8f2980bb2b5e4d3dca89c`
