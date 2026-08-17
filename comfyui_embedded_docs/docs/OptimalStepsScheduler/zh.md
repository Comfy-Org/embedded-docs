# OptimalSteps调度器

OptimalStepsScheduler 节点根据所选模型类型和步数配置，计算扩散模型的噪声调度 sigma 值。它会根据 `denoise` 参数调整总步数，并插值噪声水平以匹配请求的步数。该节点返回一组 sigma 值序列，用于确定扩散采样过程中使用的噪声水平。

## 输入

| 参数 | 描述 | 数据类型 | 是否必填 | 范围 |
| --- | --- | --- | --- | --- |
| `model_type` | 用于计算噪声水平的扩散模型类型 | COMBO | 是 | "FLUX"<br>"Wan"<br>"Chroma" |
| `steps` | 采样总步数（默认值：20） | INT | 是 | 3-1000 |
| `denoise` | 控制去噪强度，用于调整有效步数（默认值：1.0） | FLOAT | 是 | 0.0-1.0 |

**注意：** 当 `denoise` 设置为小于 1.0 时，节点会将有效步数计算为 `steps * denoise`。如果 `denoise` 设置为 0.0，节点将返回空张量。

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `sigmas` | 表示扩散采样噪声调度的 sigma 值序列 | SIGMAS |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OptimalStepsScheduler/zh.md)

---
**Source fingerprint (SHA-256):** `fd48c94ca16c8a3d8e6f0138018e7b13c15d100d6147807bcb23d838899045b7`
