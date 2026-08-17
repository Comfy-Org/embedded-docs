# 萬聲圖像轉影片

WanSoundImageToVideo 節點用於從帶有可選音訊條件的圖像準備影片生成。它接收正向與負向條件化提示詞，以及一個 VAE 模型，以建立條件化輸入和一個空的潛在張量，並可整合參考圖像、音訊編碼、控制影片與動作參考，以引導影片生成過程。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `positive` | 正向條件化提示詞，用來引導生成影片中應出現的內容。 | CONDITIONING | 是 | - |
| `negative` | 負向條件化提示詞，指定生成影片中應避免的內容。 | CONDITIONING | 是 | - |
| `vae` | 用於編碼和解碼影片潛在表示的 VAE 模型。 | VAE | 是 | - |
| `width` | 輸出影片的寬度（像素）。預設值為 832，必須能被 16 整除。 | INT | 是 | 16 至 MAX_RESOLUTION（步長：16） |
| `height` | 輸出影片的高度（像素）。預設值為 480，必須能被 16 整除。 | INT | 是 | 16 至 MAX_RESOLUTION（步長：16） |
| `length` | 生成影片的幀數。預設值為 77，必須能被 4 整除。 | INT | 是 | 1 至 MAX_RESOLUTION（步長：4） |
| `batch_size` | 同時生成的影片數量。預設值為 1。 | INT | 是 | 1 至 4096 |
| `audio_encoder_output` | 可選的音訊編碼，可根據聲音特徵影響影片生成。提供時，音訊特徵會被插值並用於條件化影片生成。 | AUDIOENCODEROUTPUT | 否 | - |
| `ref_image` | 可選的參考圖像，為影片內容提供視覺引導。圖像會被放大以符合指定的寬度和高度，然後編碼為潛在表示。只會使用輸入批次中的第一張圖像。 | IMAGE | 否 | - |
| `control_video` | 可選的控制影片，引導生成影片的動作與結構。影片會被放大並編碼，然後用於條件化輸出。只會使用前 `length` 幀。 | IMAGE | 否 | - |
| `ref_motion` | 可選的動作參考，為影片中的運動模式提供引導。如果輸入超過 73 幀，只會使用最後 73 幀。如果少於 73 幀，則序列會以中性幀填充。 | IMAGE | 否 | - |

**注意：** 可選輸入（`audio_encoder_output`、`ref_image`、`control_video`、`ref_motion`）可以獨立使用或組合使用。控制影片條件化始終會被套用；當未提供 `control_video` 時，會使用一個空的（零）控制影片。

## 輸出

| 輸出名 | 說明 | 資料類型 |
| --- | --- | --- |
| `positive` | 經處理並針對影片生成調整的正向條件化。當提供對應的可選輸入時，會包含音訊嵌入、參考潛在表示、動作參考與控制影片條件化。 | CONDITIONING |
| `negative` | 經處理並針對影片生成調整的負向條件化。當提供對應的可選輸入時，會包含音訊嵌入（設為零）、參考潛在表示、動作參考與控制影片條件化。 | CONDITIONING |
| `latent` | 作為影片生成起點的空潛在張量。該潛在張量的形狀為 [batch_size, 16, latent_t, height/8, width/8]，其中 latent_t = ((length - 1) // 4) + 1。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanSoundImageToVideo/zh-TW.md)

---
**Source fingerprint (SHA-256):** `b1148cd00d8999dd6842e3c2fb13655fda8f20d5befed975a6d1652688b2807c`
