# 浮点数

The PrimitiveFloat 节点创建一个可以在工作流程中使用的浮点数数值。它接受单个数值输入并输出相同的值，使您能够在 ComfyUI 流程中的不同节点之间定义和传递浮点数值。

## 输入

| 参数 | 描述 | 数据类型 | 是否必填 | 范围 |
| --- | --- | --- | --- | --- |
| `value` | 要输出的浮点数数值（默认值：0.0） | FLOAT | 是 | -sys.maxsize 到 sys.maxsize（步长：0.1） |

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `output` | 输入的浮点数数值 | FLOAT |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PrimitiveFloat/zh.md)

---
**Source fingerprint (SHA-256):** `df57e5900e972e17da365fbbdb7b7db777dda6f9f938e1074f1a89451d4b7c73`
