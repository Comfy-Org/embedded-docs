# GITS调度器

GITSScheduler 节点生成 GITS 采样方法所使用的 sigma（噪声级别）调度。它根据 `coeff` 参数和 `steps` 数量选择预定义的噪声级别表，并在使用低于 1.0 的 `denoise` 值时选择性地裁剪调度。

## 输入

| 参数 | 描述 | 数据类型 | 是否必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `coeff` | 用于选择预定义噪声级别表来构建调度的系数。该值四舍五入到小数点后两位（默认值：1.20） | FLOAT | 是 | 0.80 - 1.50 |
| `steps` | 要为 sigma 生成的总采样步数（默认值：10） | INT | 是 | 2 - 1000 |
| `denoise` | 用于减少所用步数的去噪因子（默认值：1.0） | FLOAT | 是 | 0.0 - 1.0 |

**注意：** 当 `denoise` 设置为 0.0 时，节点返回空张量。当 `denoise` 小于 1.0 时，实际使用的步数按 `round(steps * denoise)` 计算。对于不超过 20 的步数，节点直接使用预定义的噪声级别；对于大于 20 的步数，节点使用对数线性插值将预定义噪声级别扩展到所需步数。

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `sigmas` | 为噪声调度生成的 sigma 值 | SIGMAS |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GITSScheduler/zh.md)

---
**Source fingerprint (SHA-256):** `f46681970fece985f6a4b62d0817d1ea306f1ca9a20189f937512dd5717f458b`
