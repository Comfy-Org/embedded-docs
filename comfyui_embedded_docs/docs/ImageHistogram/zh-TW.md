# 影像直方圖

ImageHistogram 節點會分析輸入影像的色彩分佈。它計算並輸出多個直方圖，這些圖表顯示影像中具有每種可能強度值的像素數量。它會針對紅色、綠色和藍色色彩通道分別產生直方圖、一個複合 RGB 直方圖，以及一個基於標準亮度公式的亮度直方圖。

## 輸入

| 參數 | 描述 | 資料型態 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `image` | 要分析的輸入影像。此節點會處理批次中的第一張影像。 | IMAGE | Yes | N/A |

## 輸出

所有輸出的直方圖都包含 256 個數值，分別對應 0 到 255 的每個強度等級。

| 輸出名稱 | 描述 | 資料型態 |
| --- | --- | --- |
| `rgb` | 一個複合直方圖，代表紅色、綠色和藍色通道的平均像素強度。 | HISTOGRAM |
| `luminance` | 影像感知亮度的直方圖，使用 ITU-R BT.709 標準亮度公式計算。 | HISTOGRAM |
| `red` | 顯示紅色色彩通道中像素強度分佈的直方圖。 | HISTOGRAM |
| `green` | 顯示綠色色彩通道中像素強度分佈的直方圖。 | HISTOGRAM |
| `blue` | 顯示藍色色彩通道中像素強度分佈的直方圖。 | HISTOGRAM |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageHistogram/zh-TW.md)

---
**Source fingerprint (SHA-256):** `5020f5cedd325250a207a00950011f4b6dc19ddfe4d172665ffca4982731dd5e`
