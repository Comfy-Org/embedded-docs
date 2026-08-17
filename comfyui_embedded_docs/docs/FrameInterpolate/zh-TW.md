# 影格插值

Frame Interpolate 節點會在影像序列中的現有影格之間建立新影格，有效提高影格率。它使用 AI 模型來預測中間影格應有的樣貌，可用於建立流暢的慢動作效果，或提升影片的流暢度。對於每一對連續影格，此節點會產生 `multiplier - 1` 個新影格，並將它們插入原始影格之間。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `interp_model` | 用於產生中間影格的影格插值模型（例如 RIFE 或 FILM 模型） | INTERP_MODEL | 是 | - |
| `images` | 要進行插值的一批連續影像（影格）。至少需要 2 個影像；若少於 2 個，節點會直接回傳輸入影像而不做任何變更。 | IMAGE | 是 | - |
| `multiplier` | 影格數的倍率。例如，倍率為 2 時，影格數會變成兩倍。（預設值：2） | INT | 是 | 2 至 16 |

注意：輸入影像批次必須包含至少 2 個影格，因為插值會在連續影格對之間進行。輸出的總影格數為 `(輸入影格數 - 1) * multiplier + 1`。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `IMAGE` | 在原始影格之間插入插值影格後的新影像批次，產生更流暢的序列。輸出影格總數為 `(輸入影格數 - 1) * multiplier + 1`。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FrameInterpolate/zh-TW.md)

---
**Source fingerprint (SHA-256):** `e0b9dd6ec3b09e665bcc0f95d2b7a0209d9045ba9b96828e46f126e6914f049c`
