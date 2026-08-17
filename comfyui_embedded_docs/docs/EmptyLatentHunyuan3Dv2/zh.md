# 空Latent图像（Hunyuan3Dv2）

EmptyLatentHunyuan3Dv2 节点创建专门为 Hunyuan3Dv2 3D 生成模型格式化的空白潜空间张量。它生成具有 Hunyuan3Dv2 架构所需正确尺寸和结构的空潜空间，使您能够从头开始 3D 生成工作流。该节点产生填充为零的潜空间张量，作为后续 3D 生成过程的基础。

## 输入

| 参数 | 描述 | 数据类型 | 必填 | 范围 |
| --- | --- | --- | --- | --- |
| `resolution` | 潜空间的分辨率尺寸（默认值：3072） | INT | 是 | 1 - 8192 |
| `batch_size` | 批次中潜空间图像的数量（默认值：1） | INT | 是 | 1 - 4096 |

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `LATENT` | 返回一个包含为 Hunyuan3Dv2 3D 生成格式化的空样本的潜空间张量 | LATENT |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyLatentHunyuan3Dv2/zh.md)

---
**Source fingerprint (SHA-256):** `e9061301341ab84290cd2b16d5307636310a0772562cf485e3444876e4786ddd`
