# ElevenLabs 語音轉文字

ElevenLabs 語音轉文字節點使用 ElevenLabs 的語音轉文字 API，將音訊轉錄為文字。它支援自動語言偵測、辨識目前說話的發言者，並在轉錄文字中標記非語音聲音，例如（笑聲）或（音樂）。

## 輸入

### 通用輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `模型` | 用於轉錄的模型。選取模型後會顯示其特定參數。 | DYNAMIC_COMBO | 是 | `"scribe_v2"` |
| `音訊` | 要轉錄的音訊。 | AUDIO | 是 | - |
| `語言代碼` | ISO-639-1 或 ISO-639-3 語言代碼（例如 'en'、'es'、'fra'）。留空以自動偵測。（預設值：""） | STRING | 否 | - |
| `說話者數量` | 要預測的最大發言者人數。設為 0 以自動偵測。（預設值：0） | INT | 否 | 0 - 32 |
| `隨機種子` | 用於可重現性的種子（不保證確定性）。（預設值：1） | INT | 否 | 0 - 2147483647 |

### Scribe v2 輸入

當選取 `"scribe_v2"` 模型時，會顯示這些參數。

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `tag_audio_events` | 在轉錄文字中標記（笑聲）、（音樂）等聲音。（預設值：False） | BOOLEAN | 否 | - |
| `diarize` | 標記目前說話的發言者。（預設值：False） | BOOLEAN | 否 | - |
| `diarization_threshold` | 發言者分離敏感度。數值越低，對發言者變化的偵測越敏感。僅在啟用 `diarize` 時使用。（預設值：0.22） | FLOAT | 否 | 0.1 - 0.4 |
| `temperature` | 隨機性控制。0.0 使用模型預設值。數值越高，隨機性越高。（預設值：0.0） | FLOAT | 否 | 0.0 - 2.0 |
| `timestamps_granularity` | 轉錄文字中單詞的時間精確度。（預設值："word"） | COMBO | 否 | `"word"`<br>`"character"`<br>`"none"` |

**注意：** 當啟用 `diarize` 時，`num_speakers` 不能設為大於 0 的值。請停用 `diarize` 或將 `num_speakers` 設為 0，否則會引發錯誤。

## 輸出

| 輸出名 | 描述 | 資料類型 |
| --- | --- | --- |
| `文字` | 從音訊轉錄而來的文字。 | STRING |
| `語言代碼` | 偵測到的音訊語言代碼。 | STRING |
| `單詞 JSON` | 包含詳細單詞層級資訊的 JSON 格式字串，包括時間戳記及（若啟用）發言者標籤。 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsSpeechToText/zh-TW.md)

---
**Source fingerprint (SHA-256):** `7eb5d72615aa8a9e4a8014e45b39cf83dc8d8432d7ce0dccba20489be80a5830`
