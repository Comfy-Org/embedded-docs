# TSR - 时序分数重缩放

此节点对扩散模型应用时间分数重缩放（TSR）。它通过去噪过程中对预测噪声或分数进行重缩放来修改模型的采样行为，从而可以控制生成输出的多样性。该功能作为后 CFG（无分类器引导）函数实现。

## 输入

| 参数 | 描述 | 数据类型 | 必填 | 范围 |
| --- | --- | --- | --- | --- |
| `model` | 要使用 TSR 函数进行修补的扩散模型。 | MODEL | 是 | - |
| `tsr_k` | 控制重缩放强度。k 值越低，图像生成结果越精细；k 值越高，图像生成结果越平滑。设置 k = 1 可禁用重缩放。（默认值：0.95） | FLOAT | 否 | 0.01 - 100.0 |
| `tsr_sigma` | 控制重缩放生效的早晚。数值越大，生效越早。（默认值：1.0） | FLOAT | 否 | 0.01 - 100.0 |

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `patched_model` | 输入模型，现已在采样过程中应用了时间分数重缩放函数。 | MODEL |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TemporalScoreRescaling/zh.md)

---
**Source fingerprint (SHA-256):** `4d4e3c64fb6e3a3fe4725ea944a361b46d871943a10e65d72d70e0e6d757dfca`
