# TripoSplat 条件编码

此节点使用 DINOv3 视觉编码器和 Flux2 VAE 对输入图像进行编码，为 TripoSplat 模型生成正向和负向条件数据。它还生成一个固定大小的噪声目标（潜在序列加相机令牌），作为 KSampler 的起点。

## 输入

| 参数 | 描述 | 数据类型 | 是否必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `clip_vision` | DINOv3 ViT-H/16+ 图像编码器 | CLIP_VISION | 是 | - |
| `vae` | Flux2 VAE | VAE | 是 | - |
| `image` | 要编码的输入图像 | IMAGE | 是 | - |

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `positive` | 包含 DINOv3 图像特征和输入图像的 Flux2 VAE 潜在表示的正向条件数据 | CONDITIONING |
| `negative` | 包含零填充 DINOv3 特征和零填充 Flux2 VAE 潜在表示的负向条件数据 | CONDITIONING |
| `latent` | 供 KSampler 使用的固定大小噪声目标（潜在表示 + 相机） | LATENT |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoSplatConditioning/zh.md)

---
**Source fingerprint (SHA-256):** `59ebeef272d125a2cc2045f4ff54f99268b1273d0a1fd46f7462e6d312f3a805`
