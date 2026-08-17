# 保存图像（高级）

**SaveImageAdvanced** 节点可将图像保存到你的 ComfyUI 输出目录，并支持对文件格式、位深度和色彩空间进行高级控制。它支持将图像保存为 PNG 或 EXR 文件，并可将工作流元数据嵌入到保存的文件中。

## 输入

### 通用输入

| 参数 | 描述 | 数据类型 | 必填 | 取值范围 |
|-----------|-------------|-----------|----------|-------|
| `images` | 要保存的图像。 | IMAGE | 是 | - |
| `filename_prefix` | 要保存文件的前缀。可包含格式化标记，例如 `%date:yyyy-MM-dd%` 或 `%Empty Latent Image.width%`。（默认值："ComfyUI"） | STRING | 是 | - |
| `format` | 保存图像时使用的文件格式。选择格式后，会显示该格式的附加选项。 | DYNAMIC_COMBO | 是 | `"png"`<br>`"exr"` |

### PNG 输入

当 `format` 设置为 `"png"` 时显示这些输入。

| 参数 | 描述 | 数据类型 | 必填 | 取值范围 |
|-----------|-------------|-----------|----------|-------|
| `bit_depth` | 保存图像时使用的位深度。（默认值："8-bit"） | COMBO | 是（条件性） | `"8-bit"`<br>`"16-bit"` |
| `input_color_space` | 输入张量的色彩空间。（默认值："sRGB"） | COMBO | 是（条件性） | `"sRGB"` |

### EXR 输入

当 `format` 设置为 `"exr"` 时显示这些输入。

| 参数 | 描述 | 数据类型 | 必填 | 取值范围 |
|-----------|-------------|-----------|----------|-------|
| `bit_depth` | 保存图像时使用的位深度。（默认值："32-bit float"） | COMBO | 是（条件性） | `"32-bit float"` |
| `input_color_space` | 输入张量的色彩空间。EXR 始终以匹配色域中的场景线性方式写入。（默认值："sRGB"） | COMBO | 是（条件性） | `"sRGB"`<br>`"HDR"`<br>`"linear"` |

**关于参数依赖和文件行为的说明：**

- 仅当选择了父级 `format` 时，`bit_depth` 和 `input_color_space` 才会出现。
- 对于 PNG 格式，仅可使用 `"8-bit"` 和 `"16-bit"` 位深度，且仅有 `"sRGB"` 色彩空间。色彩空间选择不会修改 PNG 像素——PNG 文件始终以 sRGB 编码图像的形式保存。
- 对于 EXR 格式，仅可使用 `"32-bit float"` 位深度，并可选 `"sRGB"`、`"HDR"` 或 `"linear"` 色彩空间。
- EXR 的 `input_color_space` 参数决定保存前如何解释输入张量：
  - `"sRGB"` — 输入为 sRGB 编码的 Rec.709；将应用 sRGB EOTF 的逆变换。
  - `"HDR"` — 输入为 HLG 编码的 Rec.2020 (BT.2100)；将应用 HLG OETF 的逆变换以获得场景线性光。
  - `"linear"` — 输入已经是场景线性（Rec.709 原色）；原样写出。渲染器/合成器输出请使用此选项。
- 工作流元数据（提示信息和额外 PNG 信息）会嵌入到保存的 PNG 和 EXR 文件中，除非通过 `--disable-metadata` 命令行参数禁用元数据写入。

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `images` | 已保存的图像（即传递给 `images` 输入的相同图像）。节点的界面结果包含已保存文件的列表，每个文件都报告了其文件名、子文件夹和类型（"output"）。 | IMAGE |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImageAdvanced/zh.md)

---
**Source fingerprint (SHA-256):** `b03a822a90cf50d30fbf4397ab280393951f08d2339dd48c0dbaf75d9c415bca`
