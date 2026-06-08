## 概述

VideoTriangleCFGGuidance 節點對影片模型應用三角形式的無分類器引導縮放模式。它使用三角波函數在最小 CFG 值與原始條件縮放之間隨時間振盪，從而修改條件縮放比例。這會產生動態引導模式，有助於提升影片生成的一致性與品質。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 要套用三角 CFG 引導的影片模型 | MODEL | 是 | - |
| `min_cfg` | 三角模式的最小 CFG 縮放值（預設：1.0） | FLOAT | 是 | 0.0 - 100.0 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `model` | 已套用三角 CFG 引導的修改後模型 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VideoTriangleCFGGuidance/zh-TW.md)

---
**Source fingerprint (SHA-256):** `0b854d78f32e265b1a4322cb11b231df33e6072611142537e0c8cff4e93db49a`
