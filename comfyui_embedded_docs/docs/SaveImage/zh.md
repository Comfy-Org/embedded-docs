# 保存图像

SaveImage 节点会将接收到的图像保存到你的 `ComfyUI/output` 目录中。它会将每张图像保存为 PNG 文件，并可嵌入工作流元数据（如提示词）到已保存的文件中，以便日后参考。

## 输入

| 参数 | 描述 | 数据类型 | 是否必填 | 范围 |
| --- | --- | --- | --- | --- |
| `images` | 要保存的图像。 | IMAGE | 是 | - |
| `filename_prefix` | 保存文件的前缀。其中可包含格式化信息，例如 `%date:yyyy-MM-dd%` 或 `%Empty Latent Image.width%`，以引用来自其他节点的值（默认值："ComfyUI"）。 | STRING | 是 | - |
| `prompt` | 隐藏输入，由 ComfyUI 自动提供：作为元数据嵌入到已保存 PNG 文件中的提示词数据。 | PROMPT | 否 | - |
| `extra_pnginfo` | 隐藏输入，由 ComfyUI 自动提供：作为元数据嵌入到已保存 PNG 文件中的额外工作流信息。 | EXTRA_PNGINFO | 否 | - |

每张图像都会保存为 PNG 文件。在保存的文件名中，前缀里的 `%batch_num%` 会被替换为图像的批次号，并附加一个补零计数器。

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `images` | 已保存的相同图像，原样传递，以便其他节点使用。 | IMAGE |
| `ui` | UI 结果，包含已保存图像的列表，其中包含文件名、子文件夹和类型，并显示在 ComfyUI 界面中。 | UI_RESULT |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImage/zh.md)

---
**Source fingerprint (SHA-256):** `4a718495fd0801304d2bc3afee859e6b9839f9aba8e929bb9ba90ae6a229a750`
