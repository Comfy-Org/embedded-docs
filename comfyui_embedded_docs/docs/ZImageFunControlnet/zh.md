# ZImageFunControlnet

ZImageFunControlnet 节点应用专门的控制网络来影响图像生成或编辑过程。它使用基础模型、模型补丁和 VAE，允许您调整控制效果的强度。该节点还可以结合基础图像、修复图像和遮罩，实现更有针对性的编辑。

## 输入

| 参数 | 描述 | 数据类型 | 是否必填 | 范围 |
| --- | --- | --- | --- | --- |
| `model` | 用于生成过程的基础模型。 | MODEL | 是 | - |
| `model_patch` | 应用控制网络引导的专门补丁模型。 | MODEL_PATCH | 是 | - |
| `vae` | 用于图像编码和解码的变分自编码器。 | VAE | 是 | - |
| `strength` | 控制网络影响的强度。正值应用效果，负值可反转效果（默认值：1.0）。 | FLOAT | 是 | -10.0 to 10.0 |
| `image` | 可选的基础图像，用于引导生成过程。 | IMAGE | 否 | - |
| `inpaint_image` | 可选图像，专门用于根据遮罩定义的区域进行修复。 | IMAGE | 否 | - |
| `mask` | 可选遮罩，用于定义图像中应编辑或修复的区域。 | MASK | 否 | - |

**注意：** `inpaint_image` 参数通常与 `mask` 结合使用，以指定要修复的内容。根据提供的可选输入不同，节点的行为可能会有所变化（例如，使用 `image` 进行引导，或使用 `image`、`mask` 和 `inpaint_image` 进行修复）。

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `model` | 应用了控制网络补丁的模型，可直接用于采样流程。 | MODEL |
| `positive` | 正向条件，可能已被控制网络输入修改。 | CONDITIONING |
| `negative` | 负向条件，可能已被控制网络输入修改。 | CONDITIONING |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ZImageFunControlnet/zh.md)

---
**Source fingerprint (SHA-256):** `e1946190a06c52dd951078d9cb753962081957cb6c38accdea26eb4129a51793`
