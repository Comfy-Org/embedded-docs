## 概述

ImageHistogram 節點用於分析輸入圖像的色彩分佈。它會計算並輸出多個直方圖，這些圖表顯示圖像中每個可能強度值所對應的像素數量。該節點會分別生成紅色、綠色和藍色色彩通道的直方圖、一個複合 RGB 直方圖，以及一個基於標準亮度公式計算的亮度直方圖。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `影像` | 要分析的輸入圖像。此節點會處理批次中的第一張圖像。 | IMAGE | 是 | 不適用 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `RGB` | 一個複合直方圖，代表紅色、綠色和藍色通道的平均像素強度。 | HISTOGRAM |
| `亮度` | 圖像感知亮度的直方圖，使用 ITU-R BT.709 標準亮度公式計算。 | HISTOGRAM |
| `紅色` | 顯示紅色色彩通道中像素強度分佈的直方圖。 | HISTOGRAM |
| `綠色` | 顯示綠色色彩通道中像素強度分佈的直方圖。 | HISTOGRAM |
| `藍色` | 顯示藍色色彩通道中像素強度分佈的直方圖。 | HISTOGRAM |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageHistogram/zh-TW.md)

---
**Source fingerprint (SHA-256):** `9bfcdb2907ab1e5cb2a9a736671fb9286b0e6ce6439fab95187f691b969ea53d`
