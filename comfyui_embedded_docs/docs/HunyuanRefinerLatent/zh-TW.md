> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanRefinerLatent/zh-TW.md)

HunyuanRefinerLatent 節點處理用於精細化操作的條件調控和潛在輸入。它對正向和負向條件調控同時應用噪聲增強，並結合潛在圖像數據，生成具有特定維度的新潛在輸出以供後續處理。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 參數說明 |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | 是 | - | 待處理的正向條件調控輸入 |
| `negative` | CONDITIONING | 是 | - | 待處理的負向條件調控輸入 |
| `latent` | LATENT | 是 | - | 潛在表徵輸入 |
| `noise_augmentation` | FLOAT | 是 | 0.0 - 1.0 | 要應用的噪聲增強量（預設值：0.10） |

## 輸出結果

| 輸出名稱 | 資料類型 | 輸出說明 |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | 經過處理的正向條件調控，包含應用的噪聲增強和潛在圖像串接 |
| `negative` | CONDITIONING | 經過處理的負向條件調控，包含應用的噪聲增強和潛在圖像串接 |
| `latent` | LATENT | 具有 [batch_size, 32, height, width, channels] 維度的新潛在輸出 |