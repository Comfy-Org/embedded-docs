# LTXV Reference Audio (ID-LoRA)

LTXV Reference Audio 可將說話者的聲音身份從參考音訊片段轉移至生成的音訊。它會將參考音訊編碼至條件化資料中，並可選擇性地以身份引導（identity guidance）修補模型，此舉會在每個取樣步驟中額外執行一次不含參考的前向傳遞，以增強說話者身份的效果。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 要套用身份引導修補的模型。 | MODEL | 是 | - |
| `positive` | 正向條件化輸入。 | CONDITIONING | 是 | - |
| `negative` | 負向條件化輸入。 | CONDITIONING | 是 | - |
| `reference_audio` | 參考音訊片段，用於轉移其說話者身份。建議約 5 秒（訓練時長）。較短或較長的片段可能會降低聲音身份轉移的效果。 | AUDIO | 是 | - |
| `audio_vae` | 用於編碼的 LTXV Audio VAE。 | VAE | 是 | - |
| `identity_guidance_scale` | 身份引導的強度。每個步驟都會額外執行一次不含參考的前向傳遞，以增強說話者身份。設為 0 可停用（不會有額外傳遞）。（預設值：3.0） | FLOAT | 是 | 0.0 - 100.0 |
| `start_percent` | 身份引導作用範圍的 sigma 起點。（預設值：0.0） | FLOAT | 是 | 0.0 - 1.0 |
| `end_percent` | 身份引導作用範圍的 sigma 終點。（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |

注意：僅當 `identity_guidance_scale` 大於 0 且目前取樣步驟位於 `start_percent` 與 `end_percent` 定義的範圍內時，才會套用身份引導。若參考音訊的取樣率與音訊 VAE 的取樣率不同，則會重新取樣至後者的取樣率。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `model` | 已以身份引導功能修補的模型。 | MODEL |
| `positive` | 正向條件化，現已包含編碼後的參考音訊資料。 | CONDITIONING |
| `negative` | 負向條件化，現已包含編碼後的參考音訊資料。 | CONDITIONING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVReferenceAudio/zh-TW.md)

---
**Source fingerprint (SHA-256):** `ae15c5838656324667d099614b325b863341f05afda43054658999574522dd49`
