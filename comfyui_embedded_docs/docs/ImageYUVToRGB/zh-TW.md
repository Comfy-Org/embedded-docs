## 概述

ImageYUVToRGB 節點可將 YUV 色彩空間的影像轉換為 RGB 色彩空間。此節點接收三個分別代表 Y（亮度）、U（藍色投影）和 V（紅色投影）通道的獨立輸入影像，並透過色彩空間轉換將其組合成單一 RGB 影像。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `Y` | Y（亮度）通道輸入影像 | IMAGE | 是 | - |
| `U` | U（藍色投影）通道輸入影像 | IMAGE | 是 | - |
| `V` | V（紅色投影）通道輸入影像 | IMAGE | 是 | - |

**注意：** 三個輸入影像（Y、U 和 V）必須同時提供，且應具有相容的尺寸以確保正確轉換。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `output` | 轉換後的 RGB 影像 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageYUVToRGB/zh-TW.md)

---
**Source fingerprint (SHA-256):** `ee160be21fce75b3a3e41e25dc1cb0b20305383ff26f9698f07b93d42f98c64f`
