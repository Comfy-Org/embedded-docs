# Stable Cascade_超分辨率ControlNet

StableCascade_SuperResolutionControlnet 节点为 Stable Cascade 超分辨率处理准备输入。它接收输入图像，并使用 VAE 对其进行编码以创建 controlnet 输入，同时为 Stable Cascade 流程中的 stage C 和 stage B 生成占位潜空间表示。

## 输入

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
| --- | --- | --- | --- | --- |
| `image` | 用于超分辨率处理的输入图像 | IMAGE | 是 | - |
| `vae` | 用于编码输入图像的 VAE 模型 | VAE | 是 | - |

注意：使用 VAE 编码时，仅使用输入图像的前三个颜色通道。

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `controlnet_input` | 适合作为 controlnet 输入的编码图像表示 | IMAGE |
| `stage_c` | Stable Cascade 处理中 stage C 的占位潜空间表示，其维度基于输入图像尺寸除以 16 | LATENT |
| `stage_b` | Stable Cascade 处理中 stage B 的占位潜空间表示，其维度基于输入图像尺寸除以 2 | LATENT |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_SuperResolutionControlnet/zh.md)

---
**Source fingerprint (SHA-256):** `d9eff373ac7736f2e2f9788d1b43c04bb3212422aa1703d1d58ac512ce476925`
