# 调节设置区域百分比视频

ConditioningSetAreaPercentageVideo 节点通过为视频生成定义特定区域和时间范围来修改 conditioning 数据。它允许您使用相对于整体尺寸的百分比值来设置 conditioning 应用区域的位置、大小和持续时间。这对于将生成集中在视频序列的特定部分很有用。

## 输入

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `conditioning` | 要修改的 conditioning 数据 | CONDITIONING | 是 | - |
| `width` | 区域的宽度，以占总宽度的百分比表示（默认值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `height` | 区域的高度，以占总高度的百分比表示（默认值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `temporal` | 区域的时间持续时间，以占总视频长度的百分比表示（默认值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `x` | 区域的水平起始位置，以百分比表示（默认值：0.0） | FLOAT | 是 | 0.0 - 1.0 |
| `y` | 区域的垂直起始位置，以百分比表示（默认值：0.0） | FLOAT | 是 | 0.0 - 1.0 |
| `z` | 区域的时间起始位置，以视频时间轴的百分比表示（默认值：0.0） | FLOAT | 是 | 0.0 - 1.0 |
| `strength` | 应用于定义区域内 conditioning 的强度乘数（默认值：1.0） | FLOAT | 是 | 0.0 - 10.0 |

注意：所有大小和位置值均为相对于整体视频尺寸和时间轴的归一化百分比（0.0 到 1.0）。

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `conditioning` | 应用了指定区域和强度设置的修改后 conditioning 数据 | CONDITIONING |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetAreaPercentageVideo/zh.md)

---
**Source fingerprint (SHA-256):** `9c5ddae6a2b1da5907fb52ef625eefb12b0b228fd3bd52c3033b5c4226d76150`
