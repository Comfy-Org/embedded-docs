# LTXV 音訊 VAE 編碼

LTXV Audio VAE Encode 節點接收音訊輸入，並使用指定的 Audio VAE 模型將其壓縮為較小的潛在表示。此過程對於在潛在空間工作流程中生成或操作音訊至關重要，因為它將原始音訊數據轉換為管線中其他節點可以理解和處理的格式。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `audio` | 要編碼的音訊。 | AUDIO | 是 | - |
| `audio_vae` | 用於編碼的 Audio VAE 模型。 | VAE | 是 | - |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `Audio Latent` | 輸入音訊的壓縮潛在表示。輸出包括潛在樣本、VAE 模型的取樣率以及類型識別碼。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAudioVAEEncode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `68f70e0f8048cd9ba723f52eefc93cc33564eb3e68c0cb9b677964dc99aecb97`
