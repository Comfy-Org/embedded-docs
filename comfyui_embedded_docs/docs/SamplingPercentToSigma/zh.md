# 采样比到Sigma

SamplingPercentToSigma 节点使用模型的采样参数将采样百分比值转换为对应的 sigma 值。它接受一个介于 0.0 和 1.0 之间的百分比值，并将其映射到模型噪声调度中的相应 sigma 值，并提供相应选项，可返回计算得到的 sigma 值或边界处的实际最大/最小 sigma 值。

## 输入

| 参数 | 描述 | 数据类型 | 是否必需 | 范围 |
| --- | --- | --- | --- | --- |
| `model` | 包含用于转换的采样参数的模型 | MODEL | 是 | - |
| `sampling_percent` | 要转换为 sigma 的采样百分比（默认值：0.0） | FLOAT | 是 | 0.0 to 1.0 (step: 0.0001) |
| `return_actual_sigma` | 返回实际的 sigma 值，而不是用于区间检查的值。这仅影响 0.0 和 1.0 处的结果。（默认值：False） | BOOLEAN | 是 | - |

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `sigma_value` | 与输入采样百分比对应的转换后的 sigma 值 | FLOAT |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplingPercentToSigma/zh.md)

---
**Source fingerprint (SHA-256):** `30decf1d4804accbdf2a70eba1a773b41ef0e09cfb74f2a9388044dadf0a1ac1`
