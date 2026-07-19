# 解析度選擇器

## 概述

解析度選擇器節點會根據所選的長寬比和以百萬像素為單位的目標總解析度，計算圖片的像素寬度與高度。此節點有助於為其他節點（例如空白潛在影像節點）生成一致的尺寸。輸出的尺寸會四捨五入至最接近的 8 的倍數。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `長寬比` | 輸出尺寸的長寬比（預設值：`"SQUARE"`）。 | COMBO | 是 | `"SQUARE"`<br>`"PORTRAIT_2_3"`<br>`"PORTRAIT_3_4"`<br>`"PORTRAIT_9_16"`<br>`"LANDSCAPE_3_2"`<br>`"LANDSCAPE_4_3"`<br>`"LANDSCAPE_16_9"` |
| `百萬像素` | 目標總百萬像素。對於正方形長寬比，1.0 MP 約等於 1024×1024（預設值：1.0）。 | FLOAT | 是 | 0.1 - 16.0 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `寬度` | 計算出的像素寬度，為 8 的倍數。 | INT |
| `高度` | 計算出的像素高度，為 8 的倍數。 | INT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResolutionSelector/zh-TW.md)

---
**Source fingerprint (SHA-256):** `221d38fa72c9989e06b706d33fd3e0dc4caa0f741dd2931864c58a6bd7f52613`
