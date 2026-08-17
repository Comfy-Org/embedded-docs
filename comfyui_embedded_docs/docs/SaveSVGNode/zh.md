# 保存SVG

将 SVG 文件保存到磁盘。此节点接收 SVG 数据作为输入，并将其保存到您的输出目录，可选择嵌入元数据。该节点自动处理带计数器后缀的文件命名，并可直接将工作流提示信息嵌入到 SVG 文件中。

## 输入

| 参数 | 描述 | 数据类型 | 是否必填 | 范围 |
| --- | --- | --- | --- | --- |
| `svg` | 要保存到磁盘的 SVG 数据 | SVG | 是 | - |
| `filename_prefix` | 要保存的文件前缀。可包含格式化信息，例如 `%date:yyyy-MM-dd%` 或 `%Empty Latent Image.width%`，以包含来自节点的值。（默认值：`"svg/ComfyUI"`） | STRING | 是 | - |

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `svg` | 已保存到磁盘的 SVG 数据 | SVG |
| `ui` | 返回文件信息，包括文件名、子文件夹和类型，用于在 ComfyUI 界面中显示 | DICT |

**注意：** 此节点会在可用时自动将工作流元数据（提示词和额外的 PNG 信息）嵌入到 SVG 文件中。元数据以 CDATA 部分的形式插入到 SVG 的 metadata 元素内。

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveSVGNode/zh.md)

---
**Source fingerprint (SHA-256):** `365137d5dacab3142c25945fd97bce4b827d9d7d4dd839986c68f491a28fb805`
