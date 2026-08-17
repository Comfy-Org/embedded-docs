# EulerAncestralCFG++采样器

SamplerEulerAncestralCFGPP 节点

此节点创建一个使用欧拉祖先方法和分类器自由引导（CFG++）进行图像生成的采样器。该采样器将祖先采样技术与引导条件相结合，以生成多样化的图像变体，同时保持连贯性，并允许通过控制噪声和步长调整的参数进行微调。

## 输入

| 参数 | 描述 | 数据类型 | 必填 | 范围 |
| --- | --- | --- | --- | --- |
| `eta` | 控制采样过程中的步长，值越大更新越激进（默认值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `s_noise` | 调整采样过程中添加的噪声量（默认值：1.0） | FLOAT | 是 | 0.0 - 10.0 |

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `sampler` | 返回一个配置好的采样器对象，可用于图像生成流水线 | SAMPLER |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerEulerAncestralCFGPP/zh.md)

---
**Source fingerprint (SHA-256):** `de83cb4c3e9aeee60f1554ad1af8181adb4fa62e3d23cec02a6f4396b96500c1`
