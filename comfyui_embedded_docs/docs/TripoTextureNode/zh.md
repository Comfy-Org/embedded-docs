# Tripo: 纹理化模型

TripoTextureNode 节点使用 Tripo API 生成带纹理的 3D 模型。它接收一个模型任务 ID，并应用多种纹理生成选项，包括 PBR 材质、纹理质量设置、对齐方法以及可选的文本引导。该节点与 Tripo API 通信以处理纹理生成请求，并返回生成的模型文件和任务 ID。

## 输入

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `model_task_id` | 要应用纹理的模型的任务 ID | MODEL_TASK_ID | 是 | - |
| `texture` | 是否生成纹理（默认：True） | BOOLEAN | 否 | - |
| `pbr` | 是否生成 PBR（基于物理的渲染）材质（默认：True） | BOOLEAN | 否 | - |
| `texture_seed` | 纹理生成的随机种子（默认：42） | INT | 否 | - |
| `texture_quality` | 纹理生成的质量级别（默认："standard"）。"detailed" 选项费用为 0.20 美元，而 "standard" 费用为 0.10 美元。 | COMBO | 否 | "standard"<br>"detailed" |
| `texture_alignment` | 纹理对齐方法（默认："original_image"）。"original_image" 将纹理对齐到原始输入图像，而 "geometry" 将其对齐到 3D 几何体。 | COMBO | 否 | "original_image"<br>"geometry" |
| `texture_prompt` | 用于纹理化的可选文本引导。对于导入的模型（Tripo: Import Model），实际使用中需要填写此项，因为这些模型没有可用于推断颜色的源图像。（多行文本框，默认：空字符串） | STRING | 否 | - |

*注意：此节点需要身份验证令牌和 API 密钥，这些将由系统自动处理。*

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `model_file` | 生成的已应用纹理的模型文件（仅用于向后兼容） | STRING |
| `model task_id` | 用于跟踪纹理生成过程的任务 ID | MODEL_TASK_ID |
| `GLB` | 生成的 GLB 格式的已应用纹理的 3D 模型 | FILE3DGLB |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoTextureNode/zh.md)

---
**Source fingerprint (SHA-256):** `a0157b7fa2bb94d174ea5893d7389885180876794032a510642586e310ba30d4`
