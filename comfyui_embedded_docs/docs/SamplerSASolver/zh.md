# SASolver采样器

SamplerSASolver 节点为扩散模型实现了一种自定义采样算法。它使用预测-校正方法，通过可配置的阶数设置和随机微分方程（SDE）参数，从输入模型生成样本。

## 输入

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `model` | 用于采样的扩散模型 | MODEL | 是 | - |
| `eta` | 控制步长缩放因子（默认：1.0） | FLOAT | 否 | 0.0 - 10.0 |
| `sde_start_percent` | 去噪过程中 SDE 采样开始的起始百分比，根据模型的采样调度转换为 sigma 值（默认：0.2） | FLOAT | 否 | 0.0 - 1.0 |
| `sde_end_percent` | 去噪过程中 SDE 采样结束的终止百分比，根据模型的采样调度转换为 sigma 值（默认：0.8） | FLOAT | 否 | 0.0 - 1.0 |
| `s_noise` | 控制采样过程中添加的噪声量（默认：1.0） | FLOAT | 否 | 0.0 - 100.0 |
| `predictor_order` | 求解器中预测器组件的阶数（默认：3） | INT | 否 | 1 - 6 |
| `corrector_order` | 求解器中校正器组件的阶数（默认：4） | INT | 否 | 0 - 6 |
| `use_pece` | 启用或禁用 PECE（预测-评估-校正-评估）方法 | BOOLEAN | 否 | - |
| `simple_order_2` | 启用或禁用简化的二阶计算 | BOOLEAN | 否 | - |

注意：除 `model` 外，所有输入均为高级参数，默认在节点界面中隐藏。

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `sampler` | 一个已配置的采样器对象，可与扩散模型一起使用 | SAMPLER |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerSASolver/zh.md)

---
**Source fingerprint (SHA-256):** `31da2d436665bf533c28b32248f632edab8f6d92372402904702ae954230f98d`
