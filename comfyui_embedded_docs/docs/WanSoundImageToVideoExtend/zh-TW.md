> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanSoundImageToVideoExtend/zh-TW.md)

WanSoundImageToVideoExtend 節點透過整合音訊調節和參考圖像來擴展圖像到影片的生成功能。它接收正向與負向調節提示、影片潛在資料以及可選的音訊嵌入，以生成擴展的影片序列。此節點會處理這些輸入內容，創建出能與音訊提示同步的連貫影片輸出。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 參數說明 |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | 是 | - | 正向調節提示，用於引導影片應包含的內容 |
| `negative` | CONDITIONING | 是 | - | 負向調節提示，用於指定影片應避免的內容 |
| `vae` | VAE | 是 | - | 用於編碼和解碼影片框架的變分自編碼器 |
| `length` | INT | 是 | 1 至 MAX_RESOLUTION | 為影片序列生成的幀數（預設值：77，步長：4） |
| `video_latent` | LATENT | 是 | - | 初始影片潛在表示，作為擴展的起始點 |
| `audio_encoder_output` | AUDIOENCODEROUTPUT | 否 | - | 可選的音訊嵌入，可根據聲音特徵影響影片生成 |
| `ref_image` | IMAGE | 否 | - | 可選的參考圖像，為影片生成提供視覺引導 |
| `control_video` | IMAGE | 否 | - | 可選的控制影片，可引導生成影片的動態和風格 |

## 輸出結果

| 輸出名稱 | 資料類型 | 輸出說明 |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | 已應用影片上下文處理後的正向調節 |
| `negative` | CONDITIONING | 已應用影片上下文處理後的負向調節 |
| `latent` | LATENT | 包含擴展影片序列的生成影片潛在表示 |