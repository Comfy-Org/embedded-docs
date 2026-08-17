# 应用ControlNet（阿里妈妈局部重绘）

此节点通过将正向和负向条件与控制图像及掩码相结合，为修复（inpainting）任务应用 ControlNet 条件控制。它处理图像和掩码，生成修改后的条件数据，从而引导生成过程，实现对修复区域的精确控制。该节点还支持强度和时序控制，以便在生成过程中调整 ControlNet 的影响力。

## 输入

| 参数 | 描述 | 数据类型 | 是否必需 | 范围 |
| --- | --- | --- | --- | --- |
| `positive` | 引导生成过程朝向期望内容的正向条件。 | CONDITIONING | 是 | - |
| `negative` | 引导生成过程远离不希望内容的负向条件。 | CONDITIONING | 是 | - |
| `control_net` | 为生成过程提供额外控制的 ControlNet 模型。 | CONTROL_NET | 是 | - |
| `vae` | 用于编码和解码图像的 VAE。 | VAE | 是 | - |
| `image` | 用作 ControlNet 控制引导的输入图像。 | IMAGE | 是 | - |
| `mask` | 定义图像中需要修复区域的掩码。 | MASK | 是 | - |
| `strength` | ControlNet 效果的强度（默认值：1.0）。 | FLOAT | 是 | 0.0 到 10.0 |
| `start_percent` | 高级选项。ControlNet 影响开始时的生成过程比例（默认值：0.0）。 | FLOAT | 是 | 0.0 到 1.0 |
| `end_percent` | 高级选项。ControlNet 影响结束时的生成过程比例（默认值：1.0）。 | FLOAT | 是 | 0.0 到 1.0 |

**注意：** 当所选 ControlNet 启用了 `concat_mask` 时，掩码值会被反转（1 - mask），反转后的掩码会被调整尺寸后应用到图像上，并且反转后的掩码会包含在传递给 ControlNet 的额外拼接数据中。如果 `concat_mask` 未启用，则不使用 `mask` 输入。

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `positive` | 应用 ControlNet 进行修复后修改得到的正向条件。 | CONDITIONING |
| `negative` | 应用 ControlNet 进行修复后修改得到的负向条件。 | CONDITIONING |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ControlNetInpaintingAliMamaApply/zh.md)

---
**Source fingerprint (SHA-256):** `307b55c7b4936826b9e4424c172248fa4b41921c2362de724e5cfa2f1c25de68`
