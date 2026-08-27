# EmptyTrellis2LatentStructure

此节点为 Trellis2 模型创建一个空的潜空间结构，其中所有值均设为零。它生成一个具有 32 个通道、分辨率为 16×16×16 的空白 3D 潜空间张量，其大小根据批次中指定的项目数量而定。

## 输入

| 参数 | 描述 | 数据类型 | 是否必填 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `batch_size` | 批次中潜空间图像的数量（默认：1）。 | INT | 是 | 1 to 4096 |

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `LATENT` | 一个空的 Trellis2 潜空间结构。samples 是一个零填充张量，形状为 (batch_size, 32, 16, 16, 16)，潜空间类型设置为 "trellis2"。 | LATENT |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyTrellis2LatentStructure/zh.md)

---
**Source fingerprint (SHA-256):** `a551f0e05e58b025df03a3babee36f57fd900b5e02926fbdbd67a512ebead078`
