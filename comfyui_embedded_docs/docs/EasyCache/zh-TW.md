> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EasyCache/zh-TW.md)

EasyCache 節點實現了一個原生模型快取系統，透過在採樣過程中重複使用先前計算的步驟來提升效能。它為模型添加了 EasyCache 功能，並可配置在採樣時間軸中開始和停止使用快取的閾值。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 參數說明 |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | 是 | - | 要添加 EasyCache 功能的模型。 |
| `reuse_threshold` | FLOAT | 否 | 0.0 - 3.0 | 重複使用快取步驟的閾值（預設值：0.2）。 |
| `start_percent` | FLOAT | 否 | 0.0 - 1.0 | 開始使用 EasyCache 的相對採樣步驟（預設值：0.15）。 |
| `end_percent` | FLOAT | 否 | 0.0 - 1.0 | 停止使用 EasyCache 的相對採樣步驟（預設值：0.95）。 |
| `verbose` | BOOLEAN | 否 | - | 是否記錄詳細資訊（預設值：False）。 |

## 輸出結果

| 輸出名稱 | 資料類型 | 輸出說明 |
|-------------|-----------|-------------|
| `model` | MODEL | 已添加 EasyCache 功能的模型。 |