> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KSamplerAdvanced/zh.md)

KSamplerAdvanced 节点旨在通过提供高级配置和技术来增强采样过程。它旨在为从模型生成样本提供更复杂的选项，从而改进基础 KSampler 的功能。

## 输入

| 参数 | 数据类型 | 描述 |
|------|----------|------|
| `model` | MODEL | 指定用于生成样本的模型，在采样过程中起着关键作用。 |
| `add_noise` | COMBO[STRING] | 决定是否在采样过程中添加噪声，影响生成样本的多样性和质量。 |
| `noise_seed` | INT | 设置噪声生成的种子，确保采样过程的可重复性。 |
| `steps` | INT | 定义采样过程中执行的步数，影响输出的细节和质量。 |
| `cfg` | FLOAT | 控制条件因子，影响采样的方向和空间。 |
| `sampler_name` | COMBO[STRING] | 选择要使用的特定采样器，允许自定义采样技术。 |
| `scheduler` | COMBO[STRING] | 选择用于控制采样过程的调度器，影响样本的进展和质量。 |
| `positive` | CONDITIONING | 指定正向条件，引导采样朝向期望的属性。 |
| `negative` | CONDITIONING | 指定负向条件，引导采样远离某些属性。 |
| `latent_image` | LATENT | 提供采样过程中使用的初始潜在图像，作为起始点。 |
| `start_at_step` | INT | 确定采样过程的起始步骤，允许控制采样的进展。 |
| `end_at_step` | INT | 设置采样过程的结束步骤，定义采样的范围。 |
| `return_with_leftover_noise` | COMBO[STRING] | 指示是否返回带有残留噪声的样本，影响最终输出的外观。 |

## 输出

| 参数 | 数据类型 | 描述 |
|------|----------|------|
| `latent` | LATENT | 输出表示从模型生成的潜在图像，反映了所应用的配置和技术。 |