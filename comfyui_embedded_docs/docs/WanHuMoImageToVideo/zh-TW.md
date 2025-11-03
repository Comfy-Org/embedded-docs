> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanHuMoImageToVideo/zh-TW.md)

WanHuMoImageToVideo 節點透過為影片影格生成潛在表徵來將圖像轉換為影片序列。它處理條件輸入，並可整合參考圖像和音訊嵌入來影響影片生成。該節點輸出經過修改的條件資料以及適用於影片合成的潛在表徵。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 參數說明 |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | 是 | - | 正向條件輸入，用於引導影片生成朝向期望的內容 |
| `negative` | CONDITIONING | 是 | - | 負向條件輸入，用於使影片生成遠離不需要的內容 |
| `vae` | VAE | 是 | - | 用於將參考圖像編碼到潛在空間的 VAE 模型 |
| `width` | INT | 是 | 16 至 MAX_RESOLUTION | 輸出影片影格的寬度（單位：像素，預設值：832，必須可被 16 整除） |
| `height` | INT | 是 | 16 至 MAX_RESOLUTION | 輸出影片影格的高度（單位：像素，預設值：480，必須可被 16 整除） |
| `length` | INT | 是 | 1 至 MAX_RESOLUTION | 生成影片序列的影格數量（預設值：97） |
| `batch_size` | INT | 是 | 1 至 4096 | 同時生成的影片序列數量（預設值：1） |
| `audio_encoder_output` | AUDIOENCODEROUTPUT | 否 | - | 可選的音訊編碼資料，可根據音訊內容影響影片生成 |
| `ref_image` | IMAGE | 否 | - | 可選的參考圖像，用於引導影片生成的風格和內容 |

**注意：** 當提供參考圖像時，它會被編碼並添加到正向和負向條件中。當提供音訊編碼器輸出時，它會被處理並整合到條件資料中。

## 輸出結果

| 輸出名稱 | 資料類型 | 輸出說明 |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | 經過修改的正向條件，已整合參考圖像和/或音訊嵌入 |
| `negative` | CONDITIONING | 經過修改的負向條件，已整合參考圖像和/或音訊嵌入 |
| `latent` | LATENT | 生成的潛在表徵，包含影片序列資料 |