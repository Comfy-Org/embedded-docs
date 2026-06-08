## 概述

ResizeAndPadImage 節點會將影像調整為符合指定尺寸，同時保持其原始長寬比。它會按比例縮小影像以符合目標寬度與高度，然後在邊緣添加填充以填滿剩餘空間。填充顏色與插值方法可自訂，以控制填充區域的外觀及調整大小的品質。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `圖像` | 要調整大小並填充的輸入影像 | IMAGE | 是 | - |
| `目標寬度` | 輸出影像的目標寬度（預設值：512） | INT | 是 | 1 至 MAX_RESOLUTION |
| `目標高度` | 輸出影像的目標高度（預設值：512） | INT | 是 | 1 至 MAX_RESOLUTION |
| `填充顏色` | 用於調整大小後影像周圍填充區域的顏色（預設值："white"） | COMBO | 是 | "white"<br>"black" |
| `插值方法` | 用於調整影像大小的插值方法（預設值："area"） | COMBO | 是 | "area"<br>"bicubic"<br>"nearest-exact"<br>"bilinear"<br>"lanczos" |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `圖像` | 調整大小並填充後的輸出影像 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResizeAndPadImage/zh-TW.md)

---
**Source fingerprint (SHA-256):** `01566327d46043d1ff9ce404b4df8f49e853d0b01d07cc189fb843157dac1cac`
