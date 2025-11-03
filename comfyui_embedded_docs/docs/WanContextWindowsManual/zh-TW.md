> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanContextWindowsManual/zh-TW.md)

WAN 上下文窗口（手動）節點允許您為具有二維處理功能的類 WAN 模型手動配置上下文窗口。該節點在採樣期間透過指定窗口長度、重疊區域、排程方法和融合技術來應用自定義上下文窗口設置，讓您能精確控制模型在不同上下文區域處理資訊的方式。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 參數說明 |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | 是 | - | 採樣期間要應用上下文窗口的模型。 |
| `context_length` | INT | 是 | 1 至 1048576 | 上下文窗口的長度（預設值：81）。 |
| `context_overlap` | INT | 是 | 0 至 1048576 | 上下文窗口的重疊區域（預設值：30）。 |
| `context_schedule` | COMBO | 是 | "static_standard"<br>"uniform_standard"<br>"uniform_looped"<br>"batched" | 上下文窗口的排程方法。 |
| `context_stride` | INT | 是 | 1 至 1048576 | 上下文窗口的步長；僅適用於均勻排程（預設值：1）。 |
| `closed_loop` | BOOLEAN | 是 | - | 是否關閉上下文窗口循環；僅適用於循環排程（預設值：False）。 |
| `fuse_method` | COMBO | 是 | "pyramid" | 用於融合上下文窗口的方法（預設值："pyramid"）。 |

**注意：** `context_stride` 參數僅影響均勻排程，而 `closed_loop` 僅適用於循環排程。上下文長度和重疊值在處理過程中會自動調整以確保符合最小有效值。

## 輸出結果

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `model` | MODEL | 已應用上下文窗口配置的模型。 |