# Flux2调度器

Flux2Scheduler 节点会为去噪过程生成一系列噪声水平（sigma），专为 Flux2 模型定制。它根据去噪步数和目标图像的尺寸来计算调度，从而影响图像生成过程中噪声去除的进度。

## 输入

| 参数 | 描述 | 数据类型 | 是否必填 | 范围 |
| --- | --- | --- | --- | --- |
| `steps` | 要执行的去噪步数。数值越高，通常结果越精细，但处理时间更长（默认值：20）。 | INT | 是 | 1 到 4096 |
| `width` | 要生成的图像宽度（以像素为单位）。该值会影响噪声调度计算（默认值：1024）。 | INT | 是 | 16 到 16384 (MAX_RESOLUTION) |
| `height` | 要生成的图像高度（以像素为单位）。该值会影响噪声调度计算（默认值：1024）。 | INT | 是 | 16 到 16384 (MAX_RESOLUTION) |

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `sigmas` | 一系列噪声水平值（sigma），用于定义采样器的去噪调度。输出中包含的值个数比步数多一个（`steps + 1`）。 | SIGMAS |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux2Scheduler/zh.md)

---
**Source fingerprint (SHA-256):** `9606177f37f7bc03aef524623f03b7f24bcdc3d9327dcdf74863fe2befeb2b65`
