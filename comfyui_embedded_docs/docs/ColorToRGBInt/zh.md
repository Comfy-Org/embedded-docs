# 颜色转RGB整数

**ColorToRGBInt** 节点将十六进制格式（如 `#FF5733`）指定的颜色转换为单个 RGB 整数值。它从颜色字符串中提取红色、绿色和蓝色分量，将它们组合为一个整数，并返回十六进制表示。也支持带有 alpha 通道的颜色（`#RRGGBBAA`），alpha 值会单独返回。

## 输入

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `color` | 十六进制格式 `#RRGGBB` 或 `#RRGGBBAA` 的颜色值。长度必须恰好为 7 或 9 个字符，并以 `#` 开头。 | COLOR | 是 | `#RRGGBB`<br>`#RRGGBBAA` |

**注意：** 输入 `color` 字符串必须完全遵循 `#RRGGBB` 或 `#RRGGBBAA` 格式。如果字符串长度不是 7 或 9 个字符、不以 `#` 开头，或包含不是有效十六进制数字的字符，节点将引发错误。

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `rgb_int` | 计算得到的 RGB 整数值，由公式 `(Red * 65536) + (Green * 256) + Blue` 推导得出。 | INT |
| `hex` | `#RRGGBB` 格式的十六进制颜色字符串。如果输入包含 alpha 通道，则从该输出中移除。 | COLOR |
| `alpha` | alpha（不透明度）值，为 0.0 到 1.0 之间的数字。对于带有 alpha 通道的输入颜色（`#RRGGBBAA`），它是两位十六进制 alpha 值除以 255。对于没有 alpha 通道的颜色，则为 1.0。 | FLOAT |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ColorToRGBInt/zh.md)

---
**Source fingerprint (SHA-256):** `4e64616d168beee73bca4364d47e2a089418b5046a76bfcfa061dfab9a5e49ed`
