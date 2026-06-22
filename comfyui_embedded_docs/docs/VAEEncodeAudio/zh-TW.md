# VAE 編碼音訊

VAEEncodeAudio 節點使用變分自編碼器（VAE）將音頻數據轉換為潛在表示。它接收音頻輸入，並通過 VAE 進行處理，以生成可用於進一步音頻生成或處理任務的壓縮潛在樣本。如有需要，節點會在編碼前自動重新取樣音頻，以匹配 VAE 預期的取樣率。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `音訊` | 要編碼的音頻數據，包含波形和取樣率資訊 | AUDIO | 是 | - |
| `vae` | 用於將音頻編碼到潛在空間的變分自編碼器模型 | VAE | 是 | - |

**注意：** 如果原始取樣率與 VAE 預期的取樣率（預設值：44100 Hz）不同，音頻輸入將自動重新取樣以匹配該值。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `LATENT` | 編碼後的音頻在潛在空間中的表示，包含壓縮後的樣本 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEEncodeAudio/zh-TW.md)

---
**Source fingerprint (SHA-256):** `db509ab571154c4cedbfc6cae6591bd2b67b2c6e2261766565cdb0205b2c2ecc`
