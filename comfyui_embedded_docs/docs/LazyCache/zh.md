# 惰性缓存

LazyCache 是 EasyCache 的自制版本，提供了更简单的实现。它适用于 ComfyUI 中的任何模型，并添加缓存功能以减少采样期间的计算。虽然它的性能通常比 EasyCache 差，但在一些罕见的情况下可能更有效，并且具有通用兼容性。

## 输入

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
| --- | --- | --- | --- | --- |
| `model` | 要添加 LazyCache 的模型。 | MODEL | 是 | - |
| `reuse_threshold` | 重用缓存步骤的阈值（默认值：0.2）。 | FLOAT | 否 | 0.0 - 3.0 |
| `start_percent` | 开始使用 LazyCache 的相对采样步骤（默认值：0.15）。 | FLOAT | 否 | 0.0 - 1.0 |
| `end_percent` | 结束使用 LazyCache 的相对采样步骤（默认值：0.95）。 | FLOAT | 否 | 0.0 - 1.0 |
| `verbose` | 是否记录详细信息（默认值：False）。 | BOOLEAN | 否 | - |

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `model` | 添加了 LazyCache 功能的模型。 | MODEL |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LazyCache/zh.md)

---
**Source fingerprint (SHA-256):** `78f9c13473567e068fc2be35b2f8f5aa459d43d3f13300a6ea858af98d3e2a44`
