# WAN上下文窗口（手動）

Wan Context Windows (Manual) 節點可讓您手動為具備二維處理能力的 Wan 類模型設定上下文視窗。它會在取樣時套用上下文視窗設定，透過指定視窗長度、重疊、排程方法與融合技術，讓您控制模型如何處理不同的上下文區域。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 在取樣期間要套用上下文視窗的模型。 | MODEL | 是 | - |
| `context_length` | 上下文視窗以實際幀數表示的長度。必須為 4*n + 1。（預設值：81） | INT | 是 | 1 至 16384（間距 4） |
| `context_overlap` | 上下文視窗以實際幀數表示的重疊量。（預設值：30） | INT | 是 | 0 或更大 |
| `context_schedule` | 上下文視窗的依步進排程演算法。（預設值："uniform_standard"） | COMBO | 是 | `"static_standard"`<br>`"uniform_standard"`<br>`"uniform_looped"`<br>`"batched"` |
| `context_stride` | 上下文視窗的步幅；僅適用於 uniform 排程。（預設值：1） | INT | 是 | 1 或更大 |
| `closed_loop` | 是否封閉上下文視窗迴圈；僅適用於 looped 排程。（預設值：False） | BOOLEAN | 是 | True 或 False |
| `fuse_method` | 用於融合上下文視窗的方法。（預設值："pyramid"） | COMBO | 是 | `"pyramid"`<br>`"gaussian"`<br>`"average"`<br>`"overlap"` |
| `freenoise` | 是否套用 FreeNoise 雜訊重排，以改善視窗混合效果。（預設值：True） | BOOLEAN | 是 | True 或 False |
| `retain_first_frame` | 在每個上下文視窗中保留第一個 I2V 幀（可能有助於保留初始參考）。（預設值：False） | BOOLEAN | 是 | True 或 False |
| `split_conds_to_windows` | 是否根據區域索引，將多個條件（由 ConditionCombine 建立）拆分到每個視窗。（預設值：False） | BOOLEAN | 是 | True 或 False |

**注意：** `context_stride` 僅影響 uniform 排程，`closed_loop` 僅適用於 looped 排程。`context_length` 應遵循 4n + 1 的模式。此節點會在套用前將 `context_length` 和 `context_overlap` 從實際幀數轉換為模型單位，並強制 `context_length` 最小值為 1，`context_overlap` 最小值為 0。`context_stride`、`closed_loop`、`freenoise` 和 `split_conds_to_windows` 輸入為進階選項。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `model` | 已套用上下文視窗設定的模型。 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanContextWindowsManual/zh-TW.md)

---
**Source fingerprint (SHA-256):** `cf4927371e9d4b509f2e6e5319cd6109e3ef36da6b3faee278bcf8c906672857`
