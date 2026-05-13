> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanSoundImageToVideo/zh-TW.md)

# WanSoundImageToVideo 節點

WanSoundImageToVideo 節點可從影像生成影片內容，並可選擇加入音訊條件控制。它接收正向與負向條件提示以及 VAE 模型來建立影片潛在表示，並可整合參考影像、音訊編碼、控制影片及動作參考，以引導影片生成過程。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | 是 | - | 正向條件提示，引導生成影片中應出現的內容 |
| `negative` | CONDITIONING | 是 | - | 負向條件提示，指定生成影片中應避免的內容 |
| `vae` | VAE | 是 | - | 用於編碼和解碼影片潛在表示的 VAE 模型 |
| `width` | INT | 是 | 16 至 MAX_RESOLUTION | 輸出影片的寬度（像素），預設值：832，必須為 16 的倍數 |
| `height` | INT | 是 | 16 至 MAX_RESOLUTION | 輸出影片的高度（像素），預設值：480，必須為 16 的倍數 |
| `length` | INT | 是 | 1 至 MAX_RESOLUTION | 生成影片的影格數，預設值：77，必須為 4 的倍數 |
| `batch_size` | INT | 是 | 1 至 4096 | 同時生成的影片數量，預設值：1 |
| `audio_encoder_output` | AUDIOENCODEROUTPUT | 否 | - | 可選的音訊編碼，可根據聲音特徵影響影片生成 |
| `ref_image` | IMAGE | 否 | - | 可選的參考影像，為影片內容提供視覺引導 |
| `control_video` | IMAGE | 否 | - | 可選的控制影片，引導生成影片的動作和結構 |
| `ref_motion` | IMAGE | 否 | - | 可選的動作參考，為影片中的運動模式提供引導 |

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | 已處理的正向條件，已針對影片生成進行修改 |
| `negative` | CONDITIONING | 已處理的負向條件，已針對影片生成進行修改 |
| `latent` | LATENT | 在潛在空間中生成的影片表示，可解碼為最終影片影格 |

---
**Source fingerprint (SHA-256):** `f80f82b8671294a14ecfecf91bc13febae0c91c5efa438467a4413d52dc82d3f`
