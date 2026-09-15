# 影格插值

Frame Interpolate 節點會在一系列影像中的現有影格之間建立新影格，有效提高影格率。它使用 AI 模型預測中間影格應呈現的外觀，可用於建立流暢的慢動作效果，或提升影片的流暢度。

## 輸入

| 參數 | 說明 | 資料類型 | 必需 | 範圍 |
| --- | --- | --- | --- | --- |
| `插值模型` | 用於產生中間影格的影格插補模型 | INTERP_MODEL | 是 | - |
| `影像` | 要在其間進行插補的一批連續影像（影格）。至少需要 2 張影像。若提供的影格少於 2 張，節點會原樣傳回輸入影像。 | IMAGE | 是 | - |
| `倍數` | 影格數量要相乘的倍數。例如，`multiplier` 為 2 會讓影格數量加倍。（預設值：2） | INT | 是 | 2 至 16 |

**注意：** 節點至少需要 2 個輸入影格，且 `multiplier` 至少為 2。若任一條件不符，輸入影像會原樣傳回。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `IMAGE` | 一批新的影像，其中插補影格會插入原始影格之間，形成更流暢的序列。輸出影格總數為 `(number of input frames - 1) * multiplier + 1`。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FrameInterpolate/zh-TW.md)

---
**Source fingerprint (SHA-256):** `e0b9dd6ec3b09e665bcc0f95d2b7a0209d9045ba9b96828e46f126e6914f049c`
