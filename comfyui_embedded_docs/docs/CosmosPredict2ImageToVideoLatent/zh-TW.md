> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CosmosPredict2ImageToVideoLatent/zh-TW.md)

CosmosPredict2ImageToVideoLatent 節點可從圖像建立影片潛在表示，用於影片生成。它可以生成空白影片潛在表示，或結合起始和結束圖像來建立具有指定尺寸和時長的影片序列。該節點負責將圖像編碼為適合影片處理的潛在空間格式。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `vae` | VAE | 是 | - | 用於將圖像編碼至潛在空間的 VAE 模型 |
| `width` | INT | 否 | 16 至 MAX_RESOLUTION | 輸出影片的寬度（單位：像素，預設值：848，必須可被 16 整除） |
| `height` | INT | 否 | 16 至 MAX_RESOLUTION | 輸出影片的高度（單位：像素，預設值：480，必須可被 16 整除） |
| `length` | INT | 否 | 1 至 MAX_RESOLUTION | 影片序列的影格數量（預設值：93，步長：4） |
| `batch_size` | INT | 否 | 1 至 4096 | 要生成的影片序列數量（預設值：1） |
| `start_image` | IMAGE | 否 | - | 影片序列的起始圖像（可選） |
| `end_image` | IMAGE | 否 | - | 影片序列的結束圖像（可選） |

**注意：** 當未提供 `start_image` 和 `end_image` 時，節點會生成空白影片潛在表示。當提供圖像時，它們會被編碼並放置在影片序列的開頭和/或結尾，並套用適當的遮罩。

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `samples` | LATENT | 生成的影片潛在表示，包含編碼後的影片序列 |
| `noise_mask` | LATENT | 指示在生成過程中應保留潛在表示哪些部分的遮罩 |