> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ContextWindowsManual/zh-TW.md)

Context Windows (Manual) 節點允許您在取樣過程中手動配置模型的上下文窗口。它會建立具有指定長度、重疊和排程模式的上下文區段，以可管理的區塊處理資料，同時保持區段之間的連續性。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 參數說明 |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | 是 | - | 在取樣過程中要應用上下文窗口的模型。 |
| `context_length` | INT | 否 | 1+ | 上下文窗口的長度（預設值：16）。 |
| `context_overlap` | INT | 否 | 0+ | 上下文窗口的重疊量（預設值：4）。 |
| `context_schedule` | COMBO | 否 | `STATIC_STANDARD`<br>`UNIFORM_STANDARD`<br>`UNIFORM_LOOPED`<br>`BATCHED` | 上下文窗口的排程模式。 |
| `context_stride` | INT | 否 | 1+ | 上下文窗口的步幅；僅適用於均勻排程（預設值：1）。 |
| `closed_loop` | BOOLEAN | 否 | - | 是否關閉上下文窗口循環；僅適用於循環排程（預設值：False）。 |
| `fuse_method` | COMBO | 否 | `PYRAMID`<br>`LIST_STATIC` | 用於融合上下文窗口的方法（預設值：PYRAMID）。 |
| `dim` | INT | 否 | 0-5 | 要應用上下文窗口的維度（預設值：0）。 |

**參數限制條件：**

- `context_stride` 僅在選擇均勻排程時使用
- `closed_loop` 僅適用於循環排程
- `dim` 必須在 0 到 5 之間（含）

## 輸出參數

| 輸出名稱 | 資料類型 | 輸出說明 |
|-------------|-----------|-------------|
| `model` | MODEL | 在取樣過程中已應用上下文窗口的模型。 |