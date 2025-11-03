> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVConditioning/zh-TW.md)

LTXVConditioning 節點會為影片生成模型的正向與負向條件輸入添加幀率資訊。它接收現有的條件資料，並將指定的幀率值應用到兩組條件資料上，使其適用於影片模型處理。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 參數說明 |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | 是 | - | 將接收幀率資訊的正向條件輸入 |
| `negative` | CONDITIONING | 是 | - | 將接收幀率資訊的負向條件輸入 |
| `frame_rate` | FLOAT | 否 | 0.0 - 1000.0 | 要應用到兩組條件資料的幀率值（預設值：25.0） |

## 輸出結果

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | 已應用幀率資訊的正向條件資料 |
| `negative` | CONDITIONING | 已應用幀率資訊的負向條件資料 |