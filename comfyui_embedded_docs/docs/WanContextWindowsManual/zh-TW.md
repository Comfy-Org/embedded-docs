> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanContextWindowsManual/zh-TW.md)

# WAN 上下文視窗（手動）節點

WAN 上下文視窗（手動）節點允許您為具有二維處理能力的 WAN 類模型手動配置上下文視窗。它透過指定視窗長度、重疊量、排程方法和融合技術，在取樣過程中應用自訂的上下文視窗設定。這讓您能夠精確控制模型在不同上下文區域間的資訊處理方式。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | 是 | - | 在取樣期間要套用上下文視窗的模型。 |
| `context_length` | INT | 是 | 1 至 1048576 | 上下文視窗的長度（預設值：81）。 |
| `context_overlap` | INT | 是 | 0 至 1048576 | 上下文視窗的重疊量（預設值：30）。 |
| `context_schedule` | COMBO | 是 | `"static_standard"`<br>`"uniform_standard"`<br>`"uniform_looped"`<br>`"batched"` | 上下文視窗的步長策略。 |
| `context_stride` | INT | 是 | 1 至 1048576 | 上下文視窗的步長；僅適用於均勻排程（預設值：1）。 |
| `closed_loop` | BOOLEAN | 是 | - | 是否閉合上下文視窗迴圈；僅適用於循環排程（預設值：False）。 |
| `fuse_method` | COMBO | 是 | `"pyramid"`<br>`"gaussian"`<br>`"average"`<br>`"overlap"` | 用於融合上下文視窗的方法（預設值："pyramid"）。 |
| `freenoise` | BOOLEAN | 是 | - | 是否應用 FreeNoise 噪聲洗牌，可改善視窗混合效果（預設值：False）。 |

**注意：** `context_stride` 參數僅影響均勻排程，而 `closed_loop` 僅適用於循環排程。上下文長度和重疊值會在處理過程中自動調整，以確保符合最小有效值。`fuse_method` 參數現在除了 "pyramid" 之外還包含其他選項。

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `model` | MODEL | 已套用上下文視窗配置的模型。 |

---
**Source fingerprint (SHA-256):** `33e539f1e6647a6a2bc98fadc357a25279b0900746f5b3d568e2782cdb770258`
