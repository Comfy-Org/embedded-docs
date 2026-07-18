## 概述

ElevenLabs 語音轉文字節點可將音訊檔案轉錄為文字。它使用 ElevenLabs 的 API 將語音內容轉換為書面文字記錄，支援自動語言偵測、辨識不同說話者，以及標記音樂或笑聲等非語音聲音。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `音訊` | 要轉錄的音訊。 | AUDIO | 是 | - |
| `模型` | 用於轉錄的模型。選擇此模型會顯示其他參數。 | COMBO | 是 | `"scribe_v2"` |
| `tag_audio_events` | 在轉錄文字中標註如（笑聲）、（音樂）等聲音。此參數在選擇 `"scribe_v2"` 模型時顯示。（預設值：False） | BOOLEAN | 否 | - |
| `diarize` | 標註哪個說話者正在發言。此參數在選擇 `"scribe_v2"` 模型時顯示。（預設值：False） | BOOLEAN | 否 | - |
| `diarization_threshold` | 說話者分離敏感度。數值越低對說話者變化的敏感度越高。此參數在選擇 `"scribe_v2"` 模型且啟用 `diarize` 時顯示。（預設值：0.22） | FLOAT | 否 | 0.1 - 0.4 |
| `temperature` | 隨機性控制。0.0 使用模型預設值。數值越高隨機性越強。此參數在選擇 `"scribe_v2"` 模型時顯示。（預設值：0.0） | FLOAT | 否 | 0.0 - 2.0 |
| `timestamps_granularity` | 轉錄文字的時間戳記精確度。此參數在選擇 `"scribe_v2"` 模型時顯示。（預設值："word"） | COMBO | 否 | `"word"`<br>`"character"`<br>`"none"` |
| `語言代碼` | ISO-639-1 或 ISO-639-3 語言代碼（例如 'en'、'es'、'fra'）。留空以自動偵測。（預設值：""） | STRING | 否 | - |
| `說話者數量` | 要預測的最大說話者數量。設為 0 以自動偵測。（預設值：0） | INT | 否 | 0 - 32 |
| `隨機種子` | 用於可重現性的種子值（不保證確定性）。（預設值：1） | INT | 否 | 0 - 2147483647 |

**注意：** 當啟用 `diarize` 選項時，`num_speakers` 參數不能設定為大於 0 的值。您必須停用 `diarize`，或將 `num_speakers` 設定為 0。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `文字` | 從音訊轉錄的文字。 | STRING |
| `語言代碼` | 偵測到的音訊語言代碼。 | STRING |
| `單詞 JSON` | 包含詳細詞彙層級資訊的 JSON 格式字串，若啟用則包含時間戳記和說話者標籤。 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsSpeechToText/zh-TW.md)

---
**Source fingerprint (SHA-256):** `aca2ac04d7280ef2b604f7c8d29ad7fea1e7abcfc38beabb64ba6b268a8cade1`
