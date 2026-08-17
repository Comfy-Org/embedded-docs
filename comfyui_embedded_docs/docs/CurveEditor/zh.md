# 曲线编辑器

曲线编辑节点提供了一个可视化界面，用于调整和微调曲线。您可以修改输入曲线的形状，并可选地通过直方图可视化其分布。该节点输出修改后的曲线，供工作流中的其他部分使用。

## 输入

| 参数 | 描述 | 数据类型 | 是否必填 | 范围 |
| --- | --- | --- | --- | --- |
| `curve` | 待编辑的输入曲线。 | CURVE | 是 | 不适用 |
| `histogram` | 可选的直方图，与曲线一同显示以作视觉参考。 | HISTOGRAM | 否 | 不适用 |

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `curve` | 在节点界面中进行调整后得到的已编辑曲线。 | CURVE |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CurveEditor/zh.md)

---
**Source fingerprint (SHA-256):** `6c4459998b1a3dd3a53f84cb1c231c448c64aa55b96444bc4ac7470556a3b915`
