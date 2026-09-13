# LTXV Reference Audio (ID-LoRA)

LTXV Reference Audio 會將說話者的聲音身分從參考音訊片段轉移到生成的音訊。它會將參考音訊編碼至條件資料中，並可選擇替模型套用身分引導；此引導會在每個步驟執行一次不使用參考音訊的額外前向傳遞，以強化說話者身分效果。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 要套用身分引導的模型。 | MODEL | 是 | - |
| `positive` | 正向條件輸入。 | CONDITIONING | 是 | - |
| `negative` | 負向條件輸入。 | CONDITIONING | 是 | - |
| `reference_audio` | 參考音訊片段，用於轉移其說話者的聲音身分。建議約 5 秒（訓練時長）。較短或較長的片段可能會降低聲音身分的轉移效果。 | AUDIO | 是 | - |
| `audio_vae` | 用於編碼的 LTXV Audio VAE。 | VAE | 是 | - |
| `identity_guidance_scale` | 身分引導的強度。每個步驟會在不使用參考音訊的情況下執行一次額外的前向傳遞，以強化說話者身分。設為 0 可停用（不執行額外傳遞）。（預設值：3.0） | FLOAT | 是 | 0.0 - 100.0 |
| `start_percent` | 身分引導作用中的 sigma 範圍起點。（預設值：0.0） | FLOAT | 是 | 0.0 - 1.0 |
| `end_percent` | 身分引導作用中的 sigma 範圍終點。（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |

注意：只有在 `identity_guidance_scale` 大於 0，且目前取樣步驟位於 `start_percent` 與 `end_percent` 定義的範圍內時，才會套用身分引導。若參考音訊與音訊 VAE 的取樣率不同，會將參考音訊重新取樣為音訊 VAE 的取樣率。

注意：`start_percent` 與 `end_percent` 是進階參數，僅在介面中啟用進階選項時顯示。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `model` | 已套用身分引導功能的模型。 | MODEL |
| `positive` | 正向條件，現在包含已編碼的參考音訊資料。 | CONDITIONING |
| `negative` | 負向條件，現在包含已編碼的參考音訊資料。 | CONDITIONING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVReferenceAudio/zh-TW.md)

---
**Source fingerprint (SHA-256):** `ae15c5838656324667d099614b325b863341f05afda43054658999574522dd49`
