# TextGenerate

The TextGenerate 节点使用 CLIP 模型根据用户的提示词生成文本。它还可以选择使用图像、视频或音频作为额外上下文来引导文本生成。您可以控制输出的长度，为支持的模型启用思考模式，并选择是使用带有各种设置的随机采样，还是在不进行采样的情况下生成文本。

## 输入

### 通用输入

| 参数 | 描述 | 数据类型 | 是否必需 | 范围 |
| --- | --- | --- | --- | --- |
| `clip` | 用于对提示词进行分词并生成文本的 CLIP 模型。 | CLIP | 是 | N/A |
| `prompt` | 用于引导生成的文本提示词。此字段支持多行内容和动态提示词。默认值为空字符串。 | STRING | 是 | N/A |
| `image` | 可选的图像输入，可结合文本提示词一起影响生成的文本。 | IMAGE | 否 | N/A |
| `video` | 视频帧作为图像批次输入。假定为 24 FPS；内部按 1 FPS 进行子采样。 | IMAGE | 否 | N/A |
| `audio` | 可选的音频输入，可结合文本提示词一起影响生成的文本。 | AUDIO | 否 | N/A |
| `max_length` | 模型将生成的最大 token 数量。默认值为 512。 | INT | 是 | 1 to 32768 |
| `sampling_mode` | 控制文本生成时是否使用随机采样。设置为“on”时，用于控制采样的附加参数会变得可用。默认为“on”。 | DYNAMIC_COMBO | 是 | "on"<br>"off" |
| `thinking` | 如果模型支持，则以思考模式运行。默认值为 False。 | BOOLEAN | 否 | True or False |
| `use_default_template` | 如果模型有内置的系统提示词/模板，则使用它。默认值为 True。这是一个高级参数。 | BOOLEAN | 否 | True or False |

### “on” 输入

当 `sampling_mode` 设置为“on”时，以下采样参数可用：

| 参数 | 描述 | 数据类型 | 是否必需 | 范围 |
| --- | --- | --- | --- | --- |
| `temperature` | 控制输出的随机性。较低的值使输出更可预测，较高的值使其更具创造性。默认值为 0.7。 | FLOAT | 否 | 0.01 to 2.0 |
| `top_k` | 将采样池限制为概率最高的前 K 个下一个 token。值为 0 时禁用此过滤器。默认值为 64。 | INT | 否 | 0 to 1000 |
| `top_p` | 使用核采样，将候选 token 限制为累积概率小于此值的 token。默认值为 0.95。 | FLOAT | 否 | 0.0 to 1.0 |
| `min_p` | 为可被考虑的 token 设置最小概率阈值。默认值为 0.05。 | FLOAT | 否 | 0.0 to 1.0 |
| `repetition_penalty` | 对已经生成的 token 施加惩罚以减少重复。值为 1.0 时不施加惩罚。默认值为 1.05。 | FLOAT | 否 | 0.0 to 5.0 |
| `presence_penalty` | 根据新 token 是否已在当前文本中出现过而对其进行惩罚，鼓励模型谈论新话题。默认值为 0.0。 | FLOAT | 否 | 0.0 to 5.0 |
| `seed` | 用于初始化随机数生成器的数字，以便在采样为“on”时获得可重现的结果。默认值为 0。 | INT | 否 | 0 to 18446744073709551615 |

### “off” 输入

当 `sampling_mode` 设置为“off”时，没有可用的附加采样参数，节点将在不进行随机采样的情况下生成文本。

**注意：** 参数 `temperature`、`top_k`、`top_p`、`min_p`、`repetition_penalty`、`presence_penalty` 和 `seed` 仅在 `sampling_mode` 设置为“on”时，才会在节点界面中激活并可见。

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `generated_text` | 模型根据输入提示词以及可选的图像、视频或音频生成的文本。 | STRING |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextGenerate/zh.md)

---
**Source fingerprint (SHA-256):** `6274a2db7c9a963304daf6df494b2b20879155e918d73429fd2ce7f3b5b9da02`
