# LTXV图像转视频（原地）

LTXVImgToVideoInplace 节点通过将输入图像编码到其初始帧中，对视频潜在表示进行条件化。其工作原理是使用 VAE 将图像编码到潜在空间，然后用此编码图像替换视频潜在样本的前几帧。应用噪声掩码，使条件化强度控制图像在生成过程中对这些初始帧的影响程度。

## 输入

| 参数 | 描述 | 数据类型 | 是否必需 | 范围 |
| --- | --- | --- | --- | --- |
| `vae` | 用于将输入图像编码到潜在空间的 VAE 模型。 | VAE | 是 | - |
| `image` | 要编码并用于对视频潜在表示进行条件化的输入图像。 | IMAGE | 是 | - |
| `latent` | 要修改的目标视频潜在表示。 | LATENT | 是 | - |
| `strength` | 控制编码图像对初始潜在帧的条件化强度。值为 1.0 时完全条件化初始帧，较低值则应用较弱条件化。（默认值：1.0） | FLOAT | 否 | 0.0 - 1.0 |
| `bypass` | 绕过条件化。启用后，节点将原样返回输入的 `latent`，保持不变。（默认值：False） | BOOLEAN | 否 | - |

**注意：** `image` 将根据 `latent` 输入的宽度和高度，自动调整大小（使用双线性插值），以匹配 `vae` 编码所需的空间维度。仅使用图像的前 3 个颜色通道（RGB），任何 Alpha 通道都将被忽略。

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `latent` | 修改后的视频潜在表示。包含更新后的样本，以及一个将条件化强度应用于初始帧的 `noise_mask`。 | LATENT |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVImgToVideoInplace/zh.md)

---
**Source fingerprint (SHA-256):** `69faa4b2e7b0fedeee531dc5a8809e23a79c9ce03e9760afb865160594fef30d`
