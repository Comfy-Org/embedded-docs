# 采样算法（连续V）

ModelSamplingContinuousV 节点通过应用连续 V-prediction 采样参数来修改模型的采样行为。它会创建输入模型的克隆，并为其配置自定义 sigma 范围设置，以实现高级采样控制。这允许用户通过指定最小和最大 sigma 值来微调采样过程。

## 输入

| 参数 | 描述 | 数据类型 | 是否必需 | 范围 |
| --- | --- | --- | --- | --- |
| `model` | 要应用连续 V-prediction 采样修改的输入模型 | MODEL | 是 | - |
| `sampling` | 要应用的采样方法。目前仅支持 V-prediction。 | COMBO | 是 | `"v_prediction"` |
| `sigma_max` | 采样的最大 sigma 值（默认：500.0） | FLOAT | 是 | 0.0 – 1000.0（步长 0.001） |
| `sigma_min` | 采样的最小 sigma 值（默认：0.03） | FLOAT | 是 | 0.0 – 1000.0（步长 0.001） |

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `model` | 已应用连续 V-prediction 采样的修改后模型 | MODEL |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingContinuousV/zh.md)

---
**Source fingerprint (SHA-256):** `8549be9dd2375374c20da7c74a756a90285716db0e52fed8a1a2b753cd6d75fe`
