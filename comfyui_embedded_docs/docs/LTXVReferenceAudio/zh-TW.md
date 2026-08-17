# LTXV Reference Audio (ID-LoRA)

LTXV Reference Audio 節點會設定一段參考音訊片段，用於在音訊生成中進行 ID-LoRA 說話者身分轉移。它會將該片段編碼到條件中，使生成的音訊採用說話者的聲音特徵，並可選擇性地使用身分引導對模型進行修補；身分引導會在沒有參考片段的情況下每一步額外執行一次前向傳播，以增強說話者身分效果。

## 輸入
| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 要使用身分引導進行修補的模型。 | MODEL | 是 | - |
| `positive` | 正向條件輸入。 | CONDITIONING | 是 | - |
| `negative` | 負向條件輸入。 | CONDITIONING | 是 | - |
| `reference_audio` | 要轉移其說話者身分的參考音訊片段。建議約 5 秒（訓練時長）。較短或較長的片段可能會降低聲音身分轉移的效果。 | AUDIO | 是 | - |
| `audio_vae` | 用於編碼的 LTXV 音訊 VAE。 | VAE | 是 | - |
| `identity_guidance_scale` | 身分引導的強度。每一步都會在沒有參考片段的情況下額外執行一次前向傳播，以增強說話者身分。設定為 0 可停用（不額外執行）。（預設值：3.0） | FLOAT | 否 | 0.0 - 100.0 |
| `start_percent` | 身分引導啟動的 sigma 範圍起點。（預設值：0.0） | FLOAT | 否 | 0.0 - 1.0 |
| `end_percent` | 身分引導啟動的 sigma 範圍終點。（預設值：1.0） | FLOAT | 否 | 0.0 - 1.0 |

注意：身分引導僅對位於 `start_percent` 和 `end_percent` 所定義範圍內的 sigma 值有效；超出該範圍時，去噪輸出保持不變。參考音訊會被加入正向和負向條件中。如果參考音訊的取樣率與音訊 VAE 的取樣率不同，音訊會自動重新取樣以符合 VAE。

## 輸出
| 輸出名 | 說明 | 資料類型 |
| --- | --- | --- |
| `model` | 已套用身分引導功能修補的模型。 | MODEL |
| `positive` | 正向條件，現已包含編碼後的參考音訊資料。 | CONDITIONING |
| `negative` | 負向條件，現已包含編碼後的參考音訊資料。 | CONDITIONING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVReferenceAudio/zh-TW.md)

---
**Source fingerprint (SHA-256):** `ae15c5838656324667d099614b325b863341f05afda43054658999574522dd49`
