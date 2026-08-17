# 图像到视频Latent（CosmosPredict2）

CosmosPredict2ImageToVideoLatent 节点从图像创建视频潜在表示，用于视频生成。它可以生成空白的视频潜在表示，或结合起始图像和结束图像，创建具有指定尺寸和时长的视频序列。该节点负责将图像编码为适合视频处理的潜在空间格式。

## 输入

| 参数 | 描述 | 数据类型 | 是否必需 | 范围 |
| --- | --- | --- | --- | --- |
| `vae` | 用于将图像编码到潜在空间的 VAE 模型 | VAE | 是 | - |
| `width` | 输出视频的宽度（像素）（默认值：848，必须能被 16 整除） | INT | 是 | 16 到 MAX_RESOLUTION（步长 16） |
| `height` | 输出视频的高度（像素）（默认值：480，必须能被 16 整除） | INT | 是 | 16 到 MAX_RESOLUTION（步长 16） |
| `length` | 视频序列中的帧数（默认值：93） | INT | 是 | 1 到 MAX_RESOLUTION（步长 4） |
| `batch_size` | 要生成的视频序列数量（默认值：1） | INT | 是 | 1 到 4096 |
| `start_image` | 视频序列的可选起始图像 | IMAGE | 否 | - |
| `end_image` | 视频序列的可选结束图像 | IMAGE | 否 | - |

**注意：** 当既未提供 `start_image` 也未提供 `end_image` 时，节点会生成空白的视频潜在表示。当提供图像时，图像会被编码并放置在视频序列的开头和/或结尾，并带有适当的遮罩。

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `samples` | 生成的视频潜在表示，包含编码后的视频序列 | LATENT |
| `noise_mask` | 一个遮罩，指示生成过程中应保留潜在表示的哪些部分 | LATENT |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CosmosPredict2ImageToVideoLatent/zh.md)

---
**Source fingerprint (SHA-256):** `842bd2b8cda438e7b938439d4eba280478939e3302dc1846d52595d40082ff05`
