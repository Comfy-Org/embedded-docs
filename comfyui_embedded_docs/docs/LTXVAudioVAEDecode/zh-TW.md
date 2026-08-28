# LTXV 音訊 VAE 解碼

LTXV Audio VAE 解碼節點會將音訊的潛在表示轉換回音訊波形。它使用專門的 Audio VAE 模型來執行此解碼過程，產生具有相關聯取樣率的音訊輸出。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `samples` | 要解碼的潛在表示。 | LATENT | 是 | N/A |
| `audio_vae` | 用於解碼潛在表示的 Audio VAE 模型。 | VAE | 是 | N/A |

**注意事項：** 如果提供的潛在表示是巢狀的（包含多個潛在表示），節點會自動使用序列中的最後一個潛在表示進行解碼。

## 輸出

| 輸出名 | 說明 | 資料類型 |
| --- | --- | --- |
| `Audio` | 解碼後的音訊波形及其相關聯的取樣率。波形會放置在與輸入潛在表示相同的裝置上，取樣率則由 Audio VAE 模型決定。 | AUDIO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAudioVAEDecode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `fc94f3cb78ede86ada374444d613411cc9bb5849e5cdb8a24074babee50719b1`
