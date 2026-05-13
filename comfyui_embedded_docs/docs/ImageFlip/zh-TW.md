> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageFlip/zh-TW.md)

## 概述

ImageFlip 節點可沿不同軸翻轉影像。它能沿 x 軸垂直翻轉影像，或沿 y 軸水平翻轉影像。此節點根據所選方法使用 torch.flip 操作來執行翻轉。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | 是 | - | 要翻轉的輸入影像 |
| `flip_method` | STRING | 是 | "x-axis: vertically"<br>"y-axis: horizontally" | 要套用的翻轉方向（預設值："x-axis: vertically"） |

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `image` | IMAGE | 翻轉後的輸出影像 |

---
**Source fingerprint (SHA-256):** `5cb9949c53653192b1a696179351976c3a87e2e7afc4634624b4d827ad75b527`
