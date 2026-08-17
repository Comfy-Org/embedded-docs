# FreeU_V2

FreeU_V2 节点通过将基于频率的修改应用于扩散模型的 U-Net 架构来提升图像生成质量。它使用可配置的缩放因子来调整不同块中的特征通道，无需额外训练即可改善输出。

## 输入

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
| --- | --- | --- | --- | --- |
| `model` | 要应用 FreeU 增强的扩散模型 | MODEL | 是 | - |
| `b1` | 第一个块的主干特征缩放因子（默认值：1.3） | FLOAT | 是 | 0.0 - 10.0 |
| `b2` | 第二个块的主干特征缩放因子（默认值：1.4） | FLOAT | 是 | 0.0 - 10.0 |
| `s1` | 第一个块的跳跃特征缩放因子（默认值：0.9） | FLOAT | 是 | 0.0 - 10.0 |
| `s2` | 第二个块的跳跃特征缩放因子（默认值：0.2） | FLOAT | 是 | 0.0 - 10.0 |

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `model` | 应用了 FreeU 修改的增强扩散模型 | MODEL |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FreeU_V2/zh.md)

---
**Source fingerprint (SHA-256):** `4cef2af9b04164a8ead25bea9c9bb3311be9224f2539a5cc6edbe97ad8465d65`
