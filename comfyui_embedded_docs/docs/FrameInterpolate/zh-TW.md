# 影格插值

Frame Interpolate 節點會在影像序列中的現有幀之間建立新幀，從而有效提高幀率。它使用 AI 模型來預測中間幀的外觀，可用於建立流暢的慢動作效果或提高影片的流暢度。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `插值模型` | 用於產生中間幀的幀插值模型 | INTERP_MODEL | 是 | - |
| `影像` | 一批連續的影像（幀），用於在它們之間進行插值。至少需要 2 張影像。如果提供的幀少於 2 張，節點將原樣返回輸入影像。 | IMAGE | 是 | - |
| `倍數` | 幀數的倍增效應。例如，倍數為 2 時，幀數會加倍。（預設值：2） | INT | 是 | 2 至 16 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `IMAGE` | 一批新的影像，包含插入在原始幀之間的插值幀，形成更流暢的序列。輸出幀總數為 `(number of input frames - 1) * multiplier + 1`。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FrameInterpolate/zh-TW.md)

---
**Source fingerprint (SHA-256):** `e0b9dd6ec3b09e665bcc0f95d2b7a0209d9045ba9b96828e46f126e6914f049c`
