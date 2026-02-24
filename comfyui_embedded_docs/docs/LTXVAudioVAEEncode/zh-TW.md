> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAudioVAEEncode/zh-TW.md)

此節點接收音訊輸入，並使用指定的 Audio VAE 模型將其壓縮成較小的潛在表示。這個過程對於在潛在空間工作流程中生成或操作音訊至關重要，因為它將原始音訊數據轉換為流程中其他節點能夠理解和處理的格式。

## 輸入參數

| 參數 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `audio` | AUDIO | 是 | - | 要進行編碼的音訊。 |
| `audio_vae` | VAE | 是 | - | 用於編碼的 Audio VAE 模型。 |

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `Audio Latent` | LATENT | 輸入音訊的壓縮潛在表示。輸出包含潛在樣本、VAE 模型的採樣率以及一個類型識別碼。 |
