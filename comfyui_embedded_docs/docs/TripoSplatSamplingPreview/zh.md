# TripoSplat 采样预览

此节点会修补 TripoSplat 模型，使其在与标准 KSampler 节点配合使用时，能在每个采样步骤显示解码后高斯溅射的实时预览。实现方式是将采样器的回调函数包装起来，在每一步之后把模型输出解码为预览图像。

## 输入

| 参数 | 描述 | 数据类型 | 必填 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `model` | 要修补以启用实时预览的 TripoSplat 模型 | MODEL | 是 | |
| `vae` | TripoSplat VAE 解码器 | VAE | 是 | |
| `octree_level` | 预览解码的八叉树深度（较低 = 更便宜/更粗糙）。默认值：5 | INT | 否 | 2 至 8 |
| `num_gaussians` | 用于预览的高斯分布数量（按 32 的倍数取整）。默认值：16384 | INT | 否 | 1024 至 262144（步长：32） |
| `yaw` | 预览摄像机的偏航角（度）。默认值：90.0 | FLOAT | 否 | -360.0 至 360.0（步长：1.0） |
| `pitch` | 预览摄像机的俯仰角（度）。默认值：15.0 | FLOAT | 否 | -89.0 至 89.0（步长：1.0） |
| `point_size` | 最大溅射半径（像素）。每个高斯分布的大小根据其缩放值缩放并以此值封顶；较低 = 更精细/更像点，较高 = 更粗。默认值：3 | INT | 否 | 1 至 16 |

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `MODEL` | 已添加实时预览功能的修补后 TripoSplat 模型 | MODEL |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoSplatSamplingPreview/zh.md)

---
**Source fingerprint (SHA-256):** `78678b65df325da964cfd3e8cd0dc07fa25b92d26bb2057117db413a205e9535`
