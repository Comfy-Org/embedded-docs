# LTXV条件

LTXVConditioning 节点用于为视频生成模型的正向和负向 conditioning 输入添加帧率信息。它接收现有的 conditioning 数据，并将指定的帧率值应用到两组 conditioning 上，使其适用于视频模型处理。

## 输入

| 参数 | 描述 | 数据类型 | 是否必填 | 范围 |
| --- | --- | --- | --- | --- |
| `positive` | 将接收帧率信息的正向 conditioning 输入 | CONDITIONING | 是 | - |
| `negative` | 将接收帧率信息的负向 conditioning 输入 | CONDITIONING | 是 | - |
| `frame_rate` | 应用于两组 conditioning 的帧率值（默认值：25.0） | FLOAT | 是 | 0.0 - 1000.0 |

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `positive` | 已应用帧率信息的正向 conditioning | CONDITIONING |
| `negative` | 已应用帧率信息的负向 conditioning | CONDITIONING |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVConditioning/zh.md)

---
**Source fingerprint (SHA-256):** `c8546b691329f2934995f97a6db2e1393d2928bf1a7438fd079d52f87bee1c35`
