# Topaz 图像增强

The Topaz Image Enhance 节点提供行业标准的放大和图像增强功能。它使用基于云的 AI 模型处理单张输入图像，以提升质量、细节和分辨率。该节点提供对增强过程的精细控制，包括创意引导、主体聚焦和面部保留等选项。

## 输入
| 参数 | 描述 | 数据类型 | 是否必填 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `model` | 用于图像增强的 AI 模型。 | COMBO | 是 | `"Reimagine"` |
| `image` | 待增强的输入图像。仅支持单张图像。 | IMAGE | 是 | - |
| `prompt` | 用于创意放大引导的可选文本提示（默认值：空）。 | STRING | 否 | - |
| `subject_detection` | 控制增强过程聚焦于图像的哪个部分（默认值："All"）。 | COMBO | 否 | `"All"`<br>`"Foreground"`<br>`"Background"` |
| `face_enhancement` | 在处理期间增强面部（如果存在）（默认值：True）。 | BOOLEAN | 否 | - |
| `face_enhancement_creativity` | 设置面部增强的创意水平（默认值：0.0）。 | FLOAT | 否 | 0.0 - 1.0 |
| `face_enhancement_strength` | 控制增强后面部相对于背景的锐利程度（默认值：1.0）。 | FLOAT | 否 | 0.0 - 1.0 |
| `crop_to_fill` | 默认情况下，当输出宽高比不同时，图像会以信箱格式显示。启用此选项可裁剪图像以填充输出尺寸（默认值：False）。 | BOOLEAN | 否 | - |
| `output_width` | 值为 0 时表示自动计算（通常为原始尺寸；若指定了 `output_height`，则为其对应宽度）（默认值：0）。 | INT | 否 | 0 - 32000 |
| `output_height` | 值为 0 时表示以原始高度或 `output_width` 对应的高度输出（默认值：0）。 | INT | 否 | 0 - 32000 |
| `creativity` | 控制增强过程的整体创意水平（默认值：3）。 | INT | 否 | 1 - 9 |
| `face_preservation` | 保留主体的面部身份特征（默认值：True）。 | BOOLEAN | 否 | - |
| `color_preservation` | 保留原始色彩（默认值：True）。 | BOOLEAN | 否 | - |

**注意：** 此节点只能处理单张输入图像。提供包含多张图像的批次将导致错误。

## 输出
| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `image` | 增强后的输出图像。 | IMAGE |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TopazImageEnhance/zh.md)

---
**Source fingerprint (SHA-256):** `a4b622ced661dd1dd1c57d4536359874d2203c8d4064c76fa684b9935e265085`
