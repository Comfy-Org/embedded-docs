> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDWarpedNoiseSource/zh.md)

## ## 概述

此节点将 LATENT（例如 VOIDWarpedNoise 节点的输出）转换为 NOISE 源。这样，您就可以将扭曲噪声与 SamplerCustomAdvanced 节点结合使用，实现更可控的图像生成。

## ## 输入

| 参数 | 数据类型 | 是否必需 | 范围 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `warped_noise` | LATENT | 是 | 不适用 | 来自 VOIDWarpedNoise 的扭曲噪声潜空间数据 |

## ## 输出

| 输出名称 | 数据类型 | 描述 |
|-------------|-----------|-------------|
| `NOISE` | NOISE | 可与 SamplerCustomAdvanced 配合使用的噪声源 |