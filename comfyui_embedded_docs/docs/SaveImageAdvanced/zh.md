# 保存图像（高级）

**Save Image (Advanced)** 节点将输入图像保存到您的 ComfyUI 输出目录，并可高级控制文件格式、位深度和色彩空间。它支持保存为 PNG 或 EXR 文件，并可将工作流元数据嵌入到保存的文件中。

## 输入

### 通用输入

| 参数 | 描述 | 数据类型 | 是否必填 | 范围 |
| --- | --- | --- | --- | --- |
| `图像` | 要保存的图像。 | IMAGE | 是 | - |
| `文件名前缀` | 保存文件的前缀。可包含格式化标记，如 `%date:yyyy-MM-dd%` 或 `%Empty Latent Image.width%`。（默认值："ComfyUI"） | STRING | 是 | - |
| `格式` | 保存图像的文件格式。选择一种格式后会显示该格式的附加选项。 | DYNAMIC_COMBO | 是 | `"png"`<br>`"exr"` |

### PNG 输入

当 `format` 设置为 `"png"` 时，将显示这些选项。

| 参数 | 描述 | 数据类型 | 是否必填 | 范围 |
| --- | --- | --- | --- | --- |
| `bit_depth` | 保存的 PNG 文件的位深度。（默认值："8-bit"） | COMBO | 是（条件性） | `"8-bit"`<br>`"16-bit"` |
| `input_color_space` | 输入张量的色彩空间。PNG 格式仅支持 sRGB。（默认值："sRGB"） | COMBO | 是（条件性） | `"sRGB"` |

### EXR 输入

当 `format` 设置为 `"exr"` 时，将显示这些选项。

| 参数 | 描述 | 数据类型 | 是否必填 | 范围 |
| --- | --- | --- | --- | --- |
| `bit_depth` | 保存的 EXR 文件的位深度。（默认值："32-bit float"） | COMBO | 是（条件性） | `"32-bit float"` |
| `input_color_space` | 输入张量的色彩空间。EXR 始终以匹配色域中的场景线性（scene-linear）写入。<br>`"sRGB"` — 输入为 sRGB 编码的 Rec.709；应用反向 sRGB EOTF。<br>`"HDR"` — 输入为 HLG 编码的 Rec.2020 (BT.2100)；应用反向 HLG OETF 以获取场景线性光。<br>`"linear"` — 输入已是场景线性（Rec.709 基色）；原样写出。用于渲染器/合成器输出。（默认值："sRGB"） | COMBO | 是（条件性） | `"sRGB"`<br>`"HDR"`<br>`"linear"` |

**关于参数依赖的说明：**
- `bit_depth` 和 `input_color_space` 参数仅在选择了特定的 `format` 时可用。
- 对于 PNG 格式，仅提供 "8-bit" 和 "16-bit" 位深度，且仅为 "sRGB" 色彩空间。
- 对于 EXR 格式，仅提供 "32-bit float" 位深度，色彩空间为 "sRGB"、"HDR" 或 "linear"。
- 图像必须具有 1（灰度）、3（RGB）或 4（RGBA）个通道；不支持其他通道数，否则会引发错误。

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `images` | 输入图像，原样传递。节点的 UI 输出提供已保存图像结果的列表，每个结果包含文件名、子文件夹和类型（"output"）。 | IMAGE |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImageAdvanced/zh.md)

---
**Source fingerprint (SHA-256):** `b03a822a90cf50d30fbf4397ab280393951f08d2339dd48c0dbaf75d9c415bca`
