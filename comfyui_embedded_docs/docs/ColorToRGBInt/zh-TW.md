## 概述

ColorToRGBInt 節點將以十六進位格式指定的顏色轉換為單一整數值。它接收像 `#FF5733` 這樣的顏色字串，並透過結合紅色、綠色和藍色分量來計算對應的 RGB 整數。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `顏色` | 以十六進位格式 `#RRGGBB` 表示的顏色值。 | STRING | 是 | N/A |

**注意：** 輸入的 `color` 字串長度必須恰好為 7 個字元，並以 `#` 符號開頭，後面接著六個十六進位數字（例如，紅色為 `#FF0000`）。如果格式不正確，節點將會引發錯誤。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `rgb 整數值` | 計算出的 RGB 整數值。此值由以下公式推導得出：`(Red * 65536) + (Green * 256) + Blue`。 | INT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ColorToRGBInt/zh-TW.md)

---
**Source fingerprint (SHA-256):** `5b8617d6b28caaa5f01dad1c6a302fa321f1bd53a0454451d468e36747e70e8f`
