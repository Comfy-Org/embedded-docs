## 概述

ImageRGBToYUV 節點可將 RGB 彩色影像轉換為 YUV 色彩空間。它接收 RGB 影像作為輸入，並將其分離為三個不同的通道：Y（亮度）、U（藍色投影）和 V（紅色投影）。每個輸出通道皆以獨立的灰階影像形式回傳，代表對應的 YUV 分量。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `影像` | 要轉換為 YUV 色彩空間的輸入 RGB 影像 | IMAGE | 是 | - |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `Y` | YUV 色彩空間中的亮度（明度）分量 | IMAGE |
| `U` | YUV 色彩空間中的藍色投影分量 | IMAGE |
| `V` | YUV 色彩空間中的紅色投影分量 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageRGBToYUV/zh-TW.md)

---
**Source fingerprint (SHA-256):** `119cba119b62c7b46ffdd2c0feca932a9af1ec41c338fead23c21fdf76a6abb2`
