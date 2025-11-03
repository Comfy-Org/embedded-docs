> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableZero123_Conditioning_Batched/zh-TW.md)

StableZero123_Conditioning_Batched 節點處理輸入圖像並生成用於 3D 模型生成的條件資料。它使用 CLIP 視覺和 VAE 模型對圖像進行編碼，然後根據仰角和方位角創建攝影機嵌入，以產生正負條件資料以及用於批次處理的潛在表示。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 參數說明 |
|-----------|-----------|----------|-------|-------------|
| `clip_vision` | CLIP_VISION | 是 | - | 用於編碼輸入圖像的 CLIP 視覺模型 |
| `init_image` | IMAGE | 是 | - | 要處理和編碼的初始輸入圖像 |
| `vae` | VAE | 是 | - | 用於將圖像像素編碼到潛在空間的 VAE 模型 |
| `width` | INT | 否 | 16 至 MAX_RESOLUTION | 處理後圖像的輸出寬度（預設值：256，必須可被 8 整除） |
| `height` | INT | 否 | 16 至 MAX_RESOLUTION | 處理後圖像的輸出高度（預設值：256，必須可被 8 整除） |
| `batch_size` | INT | 否 | 1 至 4096 | 批次中要生成的條件樣本數量（預設值：1） |
| `elevation` | FLOAT | 否 | -180.0 至 180.0 | 初始攝影機仰角（單位：度，預設值：0.0） |
| `azimuth` | FLOAT | 否 | -180.0 至 180.0 | 初始攝影機方位角（單位：度，預設值：0.0） |
| `elevation_batch_increment` | FLOAT | 否 | -180.0 至 180.0 | 每個批次項目的仰角增量（預設值：0.0） |
| `azimuth_batch_increment` | FLOAT | 否 | -180.0 至 180.0 | 每個批次項目的方位角增量（預設值：0.0） |

**注意：** `width` 和 `height` 參數必須可被 8 整除，因為節點在內部會將這些尺寸除以 8 以生成潛在空間。

## 輸出結果

| 輸出名稱 | 資料類型 | 輸出說明 |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | 包含圖像嵌入和攝影機參數的正向條件資料 |
| `negative` | CONDITIONING | 帶有零初始化嵌入的負向條件資料 |
| `latent` | LATENT | 帶有批次索引資訊的處理後圖像潛在表示 |