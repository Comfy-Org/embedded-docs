# 收缩模型UNET（Kohya Deep Shrink）

PatchModelAddDownscale 节点通过将下采样和上采样操作应用于模型中的特定块来实现 Kohya Deep Shrink 功能。它在处理过程中降低中间特征的分辨率，然后将其恢复到原始大小，这可以在保持质量的同时提高性能。该节点允许在模型执行过程中精确控制这些缩放操作发生的时间和方式。

## 输入

| 参数 | 描述 | 数据类型 | 是否必填 | 范围 |
| --- | --- | --- | --- | --- |
| `model` | 要应用下采样补丁的模型 | MODEL | 是 | - |
| `block_number` | 将应用下采样的特定块编号（默认值：3） | INT | 否 | 1-32 |
| `downscale_factor` | 特征下采样的因子（默认值：2.0） | FLOAT | 否 | 0.1-9.0 |
| `start_percent` | 去噪过程中下采样开始的位置（默认值：0.0） | FLOAT | 否 | 0.0-1.0 |
| `end_percent` | 去噪过程中下采样结束的位置（默认值：0.35） | FLOAT | 否 | 0.0-1.0 |
| `downscale_after_skip` | 是否在跳跃连接之后应用下采样（默认值：True） | BOOLEAN | 否 | - |
| `downscale_method` | 用于下采样操作的插值方法 | COMBO | 否 | "bicubic"<br>"nearest-exact"<br>"bilinear"<br>"area"<br>"bislerp" |
| `upscale_method` | 用于上采样操作的插值方法 | COMBO | 否 | "bicubic"<br>"nearest-exact"<br>"bilinear"<br>"area"<br>"bislerp" |

## 输出

| 输出名 | 描述 | 数据类型 |
| --- | --- | --- |
| `model` | 应用了降采样补丁的修改后模型 | MODEL |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PatchModelAddDownscale/zh.md)

---
**Source fingerprint (SHA-256):** `aa9434a521ab585b290a3bd8db804469bd3bb02103a0d830b6be6eb8e8c26a5e`
