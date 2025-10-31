> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanSoundImageToVideo/zh-TW.md)

WanSoundImageToVideo 節點能從圖像生成影片內容，並可選擇性地加入音訊調節。它接收正向與負向調節提示詞以及 VAE 模型來創建影片潛在表徵，並能整合參考圖像、音訊編碼、控制影片和動作參考，以引導影片生成過程。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 參數說明 |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | 是 | - | 正向調節提示詞，用於引導生成影片中應出現的內容 |
| `negative` | CONDITIONING | 是 | - | 負向調節提示詞，用於指定生成影片中應避免的內容 |
| `vae` | VAE | 是 | - | 用於編碼和解碼影片潛在表徵的 VAE 模型 |
| `width` | INT | 是 | 16 至 MAX_RESOLUTION | 輸出影片的寬度（單位：像素，預設值：832，必須可被 16 整除） |
| `height` | INT | 是 | 16 至 MAX_RESOLUTION | 輸出影片的高度（單位：像素，預設值：480，必須可被 16 整除） |
| `length` | INT | 是 | 1 至 MAX_RESOLUTION | 生成影片的幀數（預設值：77，必須可被 4 整除） |
| `batch_size` | INT | 是 | 1 至 4096 | 同時生成的影片數量（預設值：1） |
| `audio_encoder_output` | AUDIOENCODEROUTPUT | 否 | - | 可選的音訊編碼，可根據聲音特性影響影片生成 |
| `ref_image` | IMAGE | 否 | - | 可選的參考圖像，為影片內容提供視覺引導 |
| `control_video` | IMAGE | 否 | - | 可選的控制影片，用於引導生成影片的動作和結構 |
| `ref_motion` | IMAGE | 否 | - | 可選的動作參考，為影片中的運動模式提供引導 |

## 輸出結果

| 輸出名稱 | 資料類型 | 輸出說明 |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | 經處理後適用於影片生成的正向調節 |
| `negative` | CONDITIONING | 經處理後適用於影片生成的負向調節 |
| `latent` | LATENT | 在潛在空間中生成的影片表徵，可解碼為最終的影片幀 |