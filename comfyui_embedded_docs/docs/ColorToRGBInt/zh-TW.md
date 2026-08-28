# 顏色轉為 RGB 整數值

**ColorToRGBInt** 節點可將十六進位格式的顏色（例如 `#FF5733`）轉換為單一的 RGB 整數值。它會從顏色字串中提取紅色、綠色和藍色分量，將其組合成一個整數，同時傳回原始的十六進位表示法和 alpha（不透明度）值。

## Inputs

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `顏色` | 十六進位格式 `#RRGGBB` 或 `#RRGGBBAA` 的顏色值。必須為 7 或 9 個字元，且以 `#` 開頭。 | COLOR | 是 | `#RRGGBB`<br>`#RRGGBBAA` |

**注意：** 輸入 `color` 字串必須符合 `#RRGGBB` 或 `#RRGGBBAA` 格式。如果長度不是 7 或 9 個字元、不是以 `#` 開頭，或包含無效的十六進位字元，節點將拋出錯誤。

## Outputs

| Output Name | Description | Data Type |
|-------------|-------------|-----------|
| `rgb 整數值` | 計算出的 RGB 整數值，公式為：`(Red * 65536) + (Green * 256) + Blue`。 | INT |
| `hex` | 格式為 `#RRGGBB` 的十六進位顏色字串。如果輸入包含 alpha 通道，則此輸出會將其移除。 | COLOR |
| `alpha` | 介於 0.0 和 1.0 之間的 alpha（不透明度）值。當輸入為 `#RRGGBB` 時等於 1.0；當輸入為 `#RRGGBBAA` 時為 alpha 通道值除以 255。 | FLOAT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ColorToRGBInt/zh-TW.md)

---
**Source fingerprint (SHA-256):** `4e64616d168beee73bca4364d47e2a089418b5046a76bfcfa061dfab9a5e49ed`
