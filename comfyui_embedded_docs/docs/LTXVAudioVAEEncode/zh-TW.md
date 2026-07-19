# LTXV 音訊 VAE 編碼

LTXV 音頻 VAE 編碼節點接收音頻輸入，並使用指定的音頻 VAE 模型將其壓縮為較小的潛在表示。此過程對於在潛在空間工作流程中生成或操作音頻至關重要，因為它將原始音頻數據轉換為管線中其他節點可以理解和處理的格式。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `audio` | 要編碼的音頻。 | AUDIO | 是 | - |
| `audio_vae` | 用於編碼的音頻 VAE 模型。 | VAE | 是 | - |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| 音頻潛在 | 輸入音頻的壓縮潛在表示。輸出包含潛在樣本、VAE 模型的採樣率以及類型識別符。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAudioVAEEncode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `fc10d8bbdca5150b7c87adb52960b8690397c3d003c89f9ec6a8410c541a347f`
