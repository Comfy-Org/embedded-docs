# WAN上下文窗口（手動）

WAN 上下文視窗（手動）節點可讓您手動設定 Wan 風格影片模型的上下文視窗。它會在取樣期間套用這些設定，讓您控制模型處理影片時的視窗長度、重疊、排程及融合方法。上下文長度和重疊以實際幀為單位指定，並在內部轉換以供模型的 2D 處理使用。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `模型` | 要在取樣期間套用上下文視窗的模型。 | MODEL | 是 | - |
| `上下文長度` | 上下文視窗的長度，以實際幀為單位。必須為 4*n + 1（預設值：81）。 | INT | 是 | 1 至 16384 (MAX_RESOLUTION), step 4 |
| `上下文重疊` | 上下文視窗的重疊，以實際幀為單位（預設值：30）。 | INT | 是 | 0 或更高 |
| `上下文排程` | 上下文視窗的依步驟排程演算法（預設值："uniform_standard"）。 | COMBO | 是 | `"static_standard"`<br>`"uniform_standard"`<br>`"uniform_looped"`<br>`"batched"` |
| `上下文步幅` | 上下文視窗的步幅；僅適用於 uniform 排程（預設值：1）。 | INT | 是 | 1 或更高 |
| `閉環` | 是否關閉上下文視窗迴圈；僅適用於 looped 排程（預設值：False）。 | BOOLEAN | 是 | - |
| `融合方法` | 用於融合上下文視窗的方法（預設值："pyramid"）。 | COMBO | 是 | `"pyramid"`<br>`"gaussian"`<br>`"average"`<br>`"overlap"` |
| `freenoise` | 是否套用 FreeNoise 雜訊洗牌，可改善視窗混合（預設值：True）。 | BOOLEAN | 是 | - |
| `retain_first_frame` | 在每個上下文視窗中保留第一幀 I2V 畫面（可能有助於保留初始參考）（預設值：False）。 | BOOLEAN | 是 | - |
| `split_conds_to_windows` | 是否根據區域索引將多個 conditioning（由 ConditionCombine 節點建立）拆分到每個視窗（預設值：False）。 | BOOLEAN | 是 | - |

**注意：** `context_stride` 僅影響 uniform 排程，而 `closed_loop` 僅適用於 looped 排程。上下文長度和重疊以實際幀為單位指定，並在處理期間自動轉換並限制為最小有效值（`context_length` 變為 ((length - 1) / 4) + 1，`context_overlap` 變為 overlap / 4）。`context_length` 必須符合 4*n + 1 的形式。`retain_first_frame` 用於圖生影片（image-to-video）用途。`split_conds_to_windows` 預期使用 ConditionCombine 節點建立的多個 conditioning。`fuse_method` 參數除了 "pyramid" 之外還包含多個選項。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `model` | 已套用上下文視窗設定的模型。 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanContextWindowsManual/zh-TW.md)

---
**Source fingerprint (SHA-256):** `cf4927371e9d4b509f2e6e5319cd6109e3ef36da6b3faee278bcf8c906672857`
