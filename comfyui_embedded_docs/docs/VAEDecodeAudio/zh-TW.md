# VAE 解碼音訊

VAEDecodeAudio 節點使用變分自編碼器（Variational Autoencoder）將潛在表示轉換回音訊波形。它接收編碼後的音訊樣本，並透過 VAE 處理以重建原始音訊，同時套用正規化以確保一致的輸出電平。產生的音訊將以標準取樣率 44100 Hz 返回，或如果提供了輸入樣本的取樣率，則使用該取樣率。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `samples` | 潛在空間中編碼後的音訊樣本，將被解碼回音訊波形 | LATENT | 是 | - |
| `vae` | 用於將潛在樣本解碼為音訊的變分自編碼器模型 | VAE | 是 | - |

注意：如果 `samples` 包含巢狀的潛在資料，則僅使用最後一個元素進行解碼。

## 輸出

| 輸出名 | 描述 | 資料類型 |
| --- | --- | --- |
| `AUDIO` | 解碼後的音訊波形，具有正規化的音量和取樣率（預設為 44100 Hz，或若存在輸入 `samples` 的取樣率，則使用該取樣率） | AUDIO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEDecodeAudio/zh-TW.md)

---
**Source fingerprint (SHA-256):** `2a3f5c912d1d84eea7768979f6b8f0eaa9fe89041f3a3352434f38abd3c09fea`
