> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageScaleToMaxDimension/zh-TW.md)

## 概述

ImageScaleToMaxDimension 節點會將圖片調整大小，以符合指定的最大尺寸，同時保持原始長寬比。它會計算圖片是直向還是橫向，然後將較大的尺寸縮放至目標大小，同時按比例調整較小的尺寸。此節點支援多種放大方法，以滿足不同的品質和效能需求。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `影像` | IMAGE | 是 | - | 要進行縮放的輸入圖片 |
| `放大方法` | STRING | 是 | "area"<br>"lanczos"<br>"bilinear"<br>"nearest-exact"<br>"bilinear"<br>"bicubic" | 用於縮放圖片的插值方法（預設值："area"） |
| `最大尺寸` | INT | 是 | 0 至 16384 | 縮放後圖片的最大尺寸（預設值：512） |

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `影像` | IMAGE | 縮放後的圖片，其最大尺寸符合指定的數值 |

---
**Source fingerprint (SHA-256):** `be113c1a98ab9d884b2c728b790c41fb236857d59af567e43e2be0ef0362cc5e`
