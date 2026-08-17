# CLIP文本编码

`CLIP Text Encode (CLIPTextEncode)` 充当翻译官，将你的文本描述转换为 AI 可以理解的格式。这有助于 AI 解释你的输入并生成所需的图像。

可以把它想象成与一位讲不同语言的艺术家交流。CLIP 模型基于大量图像-文本对进行训练，通过将你的描述转换为 AI 模型可以遵循的“指令”来弥合这一差距。

## 输入

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
| --- | --- | --- | --- | --- |
| `text` | 要编码的文本。支持多行输入和动态提示。 | STRING | 是 | 任意文本 |
| `clip` | 用于编码文本的 CLIP 模型。 | CLIP | 是 | 已加载的 CLIP 模型 |

**注意**：`clip` 输入必须是有效的 CLIP 模型。如果为 `None`，节点将报错。这通常发生在 checkpoint 加载节点加载的 checkpoint 不包含有效的 CLIP 或文本编码器模型时。

## 输出

| 输出名 | 描述 | 数据类型 |
| --- | --- | --- |
| `CONDITIONING` | 包含嵌入文本的条件，用于引导扩散模型。 | CONDITIONING |

## 提示词功能

### 嵌入模型

嵌入模型允许你应用特定的艺术效果或风格。支持的文件格式包括 `.safetensors`、`.pt` 和 `.bin`。要使用嵌入模型：

1. 将文件放入 `ComfyUI/models/embeddings` 文件夹。
2. 在文本中使用 `embedding:model_name` 引用它。

例如，如果你的 `ComfyUI/models/embeddings` 文件夹中有一个名为 `EasyNegative.pt` 的模型，你可以这样使用它：

```
worst quality, embedding:EasyNegative, bad quality
```

**重要**：使用嵌入模型时，请确保文件名与你的模型架构匹配且兼容。例如，为 SD1.5 设计的嵌入模型无法在 SDXL 模型上正常工作。

### 提示词权重调整

你可以使用括号调整描述中某些部分的重要性。例如：

- `(beautiful:1.2)` 增加“beautiful”的权重。
- `(beautiful:0.8)` 降低“beautiful”的权重。
- 普通括号 `(beautiful)` 将应用默认权重 1.1。

你可以使用键盘快捷键 `ctrl + up/down arrow` 快速调整权重。权重调整的步长可在设置中修改。

如果你想在提示词中包含字面括号而不改变权重，可以使用反斜杠进行转义，例如 `\(word\)`。

### 通配符/动态提示

使用 `{}` 创建动态提示。例如，每次处理提示时，`{day|night|morning}` 将随机选择一个选项。

如果你想在提示词中包含字面花括号而不触发动态行为，可以使用反斜杠进行转义，例如 `\{word\}`。

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncode/zh.md)

---
**Source fingerprint (SHA-256):** `ace7988df7aaa3ac26419b16a9bd8908a327da6e82c21c2b2704af091d2e76e7`
