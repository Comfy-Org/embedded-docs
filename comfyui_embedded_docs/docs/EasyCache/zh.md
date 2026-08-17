# EasyCache

EasyCache 节点实现了模型的原生缓存系统，通过在采样过程中复用先前已计算的步骤来提高性能。它为模型添加了 EasyCache 功能，并可在采样时间线上配置开始和停止使用缓存的阈值。

## 输入

| 参数 | 描述 | 数据类型 | 是否必填 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `model` | 要添加 EasyCache 的模型。 | MODEL | 是 | - |
| `reuse_threshold` | 复用缓存步骤的阈值（默认值：0.2）。 | FLOAT | 是 | 0.0 - 3.0 |
| `start_percent` | 开始使用 EasyCache 的相对采样步数（默认值：0.15）。 | FLOAT | 是 | 0.0 - 1.0 |
| `end_percent` | 结束使用 EasyCache 的相对采样步数（默认值：0.95）。 | FLOAT | 是 | 0.0 - 1.0 |
| `verbose` | 是否记录详细日志信息（默认值：False）。 | BOOLEAN | 是 | - |

## 输出

| 输出名 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `model` | 带有 EasyCache 的模型。 | MODEL |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EasyCache/zh.md)

---
**Source fingerprint (SHA-256):** `3e10ac65f8df58ce8649fdf599e62bfb86f2d4166840bed5622c0aa2c419cd38`
