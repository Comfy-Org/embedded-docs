# LTXV 空音频潜空间

LTXV Empty Latent Audio 节点创建一批空（零填充）的潜空间音频张量。它使用所提供的 Audio VAE 模型的配置来确定潜空间的正确维度，例如通道数和频率 bin 数。音频潜变量的数量根据帧数和帧率，并利用 Audio VAE 模型计算得出。该空潜变量可作为 ComfyUI 中音频生成或处理工作流的起点。

## 输入
| 参数 | 描述 | 数据类型 | 必填 | 范围 |
| --- | --- | --- | --- | --- |
| `frames_number` | 帧数。默认值：97。 | INT | 是 | 1 to 1000 |
| `frame_rate` | 每秒帧数。接受浮点数或整数值。默认值：25.0。 | FLOAT (or INT) | 是 | 1.0 to 1000.0 |
| `batch_size` | 批次中潜空间音频样本的数量。默认值：1。 | INT | 是 | 1 to 4096 |
| `audio_vae` | 用于获取配置的 Audio VAE 模型。 | VAE | 是 | N/A |

**注意：** `audio_vae` 输入是必填项。如果未提供，节点将引发错误。

## 输出
| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `Latent` | 一个空的潜空间音频张量，结构为 (batch_size, z_channels, num_audio_latents, audio_freq)，配置为与输入的 Audio VAE 匹配。输出还包含一个设置为 "audio" 的 `type` 字段。 | LATENT |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVEmptyLatentAudio/zh.md)

---
**Source fingerprint (SHA-256):** `3ac1bf17ebdba7c3a73bdd795f561b7bee31798d8a1efc11b972db1944f873a4`
