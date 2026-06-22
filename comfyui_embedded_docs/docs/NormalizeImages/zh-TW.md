# 標準化圖片

此節點透過數學正規化過程調整輸入影像的像素值。它會從每個像素中減去指定的平均值，然後將結果除以指定的標準差。這是為其他機器學習模型準備影像資料時常見的預處理步驟。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `image` | 要進行正規化的輸入影像。 | IMAGE | 是 | - |
| `平均值` | 正規化的平均值（預設值：0.5）。 | FLOAT | 否 | 0.0 - 1.0 |
| `標準差` | 正規化的標準差（預設值：0.5）。 | FLOAT | 否 | 0.001 - 1.0 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `image` | 套用正規化過程後產生的結果影像。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/NormalizeImages/zh-TW.md)

---
**Source fingerprint (SHA-256):** `9d08c8dba7d13c6f255ed786d3d2d3005bce425dc04b14b7199d868c3fc81fd9`
