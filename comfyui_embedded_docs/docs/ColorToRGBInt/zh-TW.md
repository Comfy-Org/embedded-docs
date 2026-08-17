# 顏色轉為 RGB 整數值

**ColorToRGBInt** 節點會將以十六進位格式（如 `#FF5733`）指定的顏色轉換為單一 RGB 整數值。它會從顏色字串中取出紅色、綠色和藍色分量，將其組合成一個整數，並傳回十六進位表示。也支援帶有 Alpha 色版的顏色（`#RRGGBBAA`），且 Alpha 值會單獨傳回。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `color` | 十六進位格式 `#RRGGBB` 或 `#RRGGBBAA` 的顏色值。長度必須正好為 7 或 9 個字元，且以 `#` 開頭。 | COLOR | 是 | `#RRGGBB`<br>`#RRGGBBAA` |

**注意：** 輸入的 `color` 字串必須完全符合 `#RRGGBB` 或 `#RRGGBBAA` 格式。如果字串長度不是 7 或 9 個字元、不是以 `#` 開頭，或包含非有效十六進位數字的字元，則節點會引發錯誤。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `rgb_int` | 計算出的 RGB 整數值，由公式 `(Red * 65536) + (Green * 256) + Blue` 推導而來。 | INT |
| `hex` | `#RRGGBB` 格式的十六進位顏色字串。如果輸入包含 alpha 色版，則此輸出會移除 alpha 色版。 | COLOR |
| `alpha` | Alpha（不透明度）值，數值範圍為 0.0 到 1.0。對於具有 alpha 色版（`#RRGGBBAA`）的輸入顏色，其值為兩位數 alpha 值除以 255。對於沒有 alpha 色版的顏色，其值為 1.0。 | FLOAT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ColorToRGBInt/zh-TW.md)

---
**Source fingerprint (SHA-256):** `4e64616d168beee73bca4364d47e2a089418b5046a76bfcfa061dfab9a5e49ed`
