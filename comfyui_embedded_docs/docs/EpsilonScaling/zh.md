> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EpsilonScaling/zh.md)

实现研究论文《Elucidating the Exposure Bias in Diffusion Models》中提出的 Epsilon Scaling 方法。该方法通过在采样过程中缩放预测噪声来提升样本质量，并采用均匀调度策略来减轻扩散模型中的暴露偏差。

## 输入

| 参数 | 数据类型 | 是否必填 | 取值范围 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | 是 | - | 应用 epsilon 缩放的模型 |
| `scaling_factor` | FLOAT | 否 | 0.5 - 1.5 | 用于缩放预测噪声的因子（默认值：1.005） |

## 输出

| 输出名称 | 数据类型 | 描述 |
|-------------|-----------|-------------|
| `model` | MODEL | 已应用 epsilon 缩放的模型 |