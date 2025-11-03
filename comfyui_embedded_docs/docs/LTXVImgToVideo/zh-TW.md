> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVImgToVideo/zh-TW.md)

LTXVImgToVideo 節點將輸入圖像轉換為影片潛在表示，供影片生成模型使用。它接收單張圖像並使用 VAE 編碼器將其擴展為影格序列，然後應用帶有強度控制的條件調節，以決定在影片生成過程中保留原始圖像內容與修改內容的比例。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 參數說明 |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | 是 | - | 用於引導影片生成的正向條件提示 |
| `negative` | CONDITIONING | 是 | - | 用於避免影片中出現特定元素的負向條件提示 |
| `vae` | VAE | 是 | - | 用於將輸入圖像編碼到潛在空間的 VAE 模型 |
| `image` | IMAGE | 是 | - | 要轉換為影片影格的輸入圖像 |
| `width` | INT | 否 | 64 至 MAX_RESOLUTION | 輸出影片的寬度（單位：像素，預設值：768，間距：32） |
| `height` | INT | 否 | 64 至 MAX_RESOLUTION | 輸出影片的高度（單位：像素，預設值：512，間距：32） |
| `length` | INT | 否 | 9 至 MAX_RESOLUTION | 生成影片的影格數量（預設值：97，間距：8） |
| `batch_size` | INT | 否 | 1 至 4096 | 同時生成的影片數量（預設值：1） |
| `strength` | FLOAT | 否 | 0.0 至 1.0 | 控制影片生成過程中對原始圖像的修改程度，1.0 保留最多原始內容，0.0 允許最大程度修改（預設值：1.0） |

## 輸出結果

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | 已處理並應用影片影格遮罩的正向條件調節 |
| `negative` | CONDITIONING | 已處理並應用影片影格遮罩的負向條件調節 |
| `latent` | LATENT | 包含編碼影格和雜訊遮罩的影片潛在表示，用於影片生成 |