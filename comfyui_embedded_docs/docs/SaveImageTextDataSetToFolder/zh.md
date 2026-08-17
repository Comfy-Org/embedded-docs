# 保存图像文本数据集

保存图像-文本（到文件夹）是一个输出节点，用于将成对的图像和文本描述数据集保存到 ComfyUI 输出目录内的文件夹中。每张图像保存为 PNG 文件，当提供描述时，会为每张图像创建一个同名的 TXT 文件。这对于构建由生成图像及其描述组成的有序数据集非常有用。

## 输入

| 参数 | 描述 | 数据类型 | 是否必填 | 范围 |
| --- | --- | --- | --- | --- |
| `images` | 要保存的图像列表。 | IMAGE | 是 | - |
| `texts` | 要保存的文本描述列表。此输入为可选项。 | STRING | 否 | - |
| `folder_name` | 保存图像的文件夹名称（位于输出目录内）。（默认值："dataset"） | STRING | 是 | - |
| `filename_prefix` | 保存的图像文件名的前缀。（默认值："image"） | STRING | 是 | - |
| `mode` | 是覆盖现有文件，还是递增文件名以避免覆盖。（默认值："overwrite"） | COMBO | 是 | "overwrite"<br>"increment" |

**注意：** `images` 输入是一个列表。`texts` 输入是可选的；如果提供，则应为一个文本描述列表。描述按顺序与图像配对，每个描述保存为一个 UTF-8 编码的 `.txt` 文件，文件名与其配对的图像相同（例如，`image_00000.png` 对应 `image_00000.txt`）。如果描述数量少于图像数量，则剩余图像将不带描述保存；多余描述将被忽略。

具有默认值的输入（`folder_name`、`filename_prefix`、`mode`）无需连接；将自动使用其默认值。

当 `mode` 设置为 `overwrite`（默认值）时，图像将以类似 `image_00000.png` 的名称保存，并替换任何同名的现有文件。当 `mode` 设置为 `increment` 时，文件名中会添加一个自动递增的计数器，从而不会覆盖现有文件。

`folder_name` 值必须解析为 ComfyUI 输出目录内的位置。试图逃逸输出目录的文件夹名称（例如，使用 `..`）将被拒绝。

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| - | 此节点没有输出。它直接将文件保存到文件系统。 | - |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImageTextDataSetToFolder/zh.md)

---
**Source fingerprint (SHA-256):** `46c5a04ba1befedf62b75abbff2442dde934048f365fa7e2604ea37e70d8fdcb`
