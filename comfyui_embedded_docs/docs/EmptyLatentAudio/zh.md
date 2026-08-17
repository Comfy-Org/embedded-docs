# 空Latent音频

EmptyLatentAudio 节点用于创建一个空的音频处理潜在张量。它会生成一个具有指定时长和批次大小的空白音频潜在表示，可用作音频生成或处理工作流的起始点。该节点会根据音频时长和采样率自动计算相应的潜在维度。

## 输入

| 参数 | 描述 | 数据类型 | 是否必填 | 范围 |
| --- | --- | --- | --- | --- |
| `seconds` | 音频时长（秒）（默认值：47.6） | FLOAT | 是 | 1.0 - 1000.0（步长 0.1） |
| `batch_size` | 批次中的潜在图像数量（默认值：1） | INT | 是 | 1 - 4096 |

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `LATENT` | 返回一个用于音频处理的空潜在张量，包含指定的时长和批次大小。该张量的形状为 [batch_size, 64, length]，其中 length 根据音频时长和采样率计算得出。输出还包含指示类型为“audio”的元数据，以及时间下采样比例 2048。 | LATENT |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyLatentAudio/zh.md)

---
**Source fingerprint (SHA-256):** `6ca63d26febe2d87ff751a57044eb81b553b19756f4b3f9478ecb5a733ec0041`
