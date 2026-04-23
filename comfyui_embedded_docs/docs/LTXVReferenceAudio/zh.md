> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVReferenceAudio/zh.md)

LTXV 参考音频节点用于音频生成中的说话人身份转换。它将参考音频片段编码为模型的调节条件，使生成的音频能够采用说话人的声音特征。该节点还可应用身份引导功能，通过额外的处理步骤来增强说话人身份效果。

## 输入参数

| 参数名 | 数据类型 | 必填 | 取值范围 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | 是 | - | 需要应用身份引导补丁的模型。 |
| `positive` | CONDITIONING | 是 | - | 正向调节条件输入。 |
| `negative` | CONDITIONING | 是 | - | 负向调节条件输入。 |
| `reference_audio` | AUDIO | 是 | - | 用于转换说话人身份的参考音频片段。建议时长约5秒（训练时长）。过短或过长的片段可能会降低声音身份转换质量。 |
| `audio_vae` | VAE | 是 | - | 用于编码参考音频的 LTXV 音频 VAE。 |
| `identity_guidance_scale` | FLOAT | 否 | 0.0 - 100.0 | 身份引导强度。在每一步执行额外的无参考前向传递以增强说话人身份。设置为0可禁用（无额外传递）。(默认值: 3.0) |
| `start_percent` | FLOAT | 否 | 0.0 - 1.0 | 身份引导生效的 sigma 范围起始点。(默认值: 0.0) |
| `end_percent` | FLOAT | 否 | 0.0 - 1.0 | 身份引导生效的 sigma 范围结束点。(默认值: 1.0) |

## 输出结果

| 输出名称 | 数据类型 | 描述 |
|-------------|-----------|-------------|
| `model` | MODEL | 已应用身份引导函数补丁的模型。 |
| `positive` | CONDITIONING | 正向调节条件，现已包含编码后的参考音频数据。 |
| `negative` | CONDITIONING | 负向调节条件，现已包含编码后的参考音频数据。 |