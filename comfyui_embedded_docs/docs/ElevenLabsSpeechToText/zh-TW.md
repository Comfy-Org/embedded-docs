# ElevenLabs 語音轉文字

ElevenLabs 語音轉文字節點使用 ElevenLabs API 將音訊轉錄為文字。它支援自動語言偵測、說話者分割（辨識不同說話者）以及音訊事件標記（在轉錄稿中標註笑聲或音樂等聲音）。

## 輸入

### 通用輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `模型` | 用於轉錄的模型。選取此模型會顯示其他參數。 | DYNAMIC_COMBO | 是 | `"scribe_v2"` |
| `音訊` | 要轉錄的音訊。 | AUDIO | 是 | - |
| `語言代碼` | ISO-639-1 或 ISO-639-3 語言代碼（例如 'en'、'es'、'fra'）。留空以自動偵測。(預設值："") | STRING | 否 | - |
| `說話者數量` | 要預測的最大說話者數量。設為 0 以自動偵測。(預設值：0) | INT | 否 | 0 - 32 |
| `隨機種子` | 用於可重現性的隨機種子（不保證確定性）。(預設值：1) | INT | 否 | 0 - 2147483647 |

### Scribe v2 輸入

選取 `"scribe_v2"` 模型時會顯示這些參數。

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `tag_audio_events` | 在轉錄稿中標註 (laughter)、(music) 等聲音。(預設值：False) | BOOLEAN | 否 | - |
| `diarize` | 標註哪個說話者正在說話。(預設值：False) | BOOLEAN | 否 | - |
| `diarization_threshold` | 說話者分離敏感度。數值越低，對說話者變更越敏感。僅在啟用 `diarize` 時使用。(預設值：0.22) | FLOAT | 否 | 0.1 - 0.4 |
| `temperature` | 隨機性控制。0.0 使用模型預設值。數值越高隨機性越大。(預設值：0.0) | FLOAT | 否 | 0.0 - 2.0 |
| `timestamps_granularity` | 轉錄字詞的時間戳記精確度。(預設值："word") | COMBO | 否 | `"word"`<br>`"character"`<br>`"none"` |

**注意：** 當 `diarize` 啟用時，`num_speakers` 不能設定為大於 0 的值。您必須停用 `diarize`，或將 `num_speakers` 設定為 0。

## 輸出

| 輸出名 | 描述 | 資料類型 |
| --- | --- | --- |
| `文字` | 來自音訊的轉錄文字。 | STRING |
| `語言代碼` | 音訊的偵測語言代碼。 | STRING |
| `單詞 JSON` | 包含詳細詞級資訊的 JSON 格式字串，包含時間戳記和（如果啟用）說話者標籤。 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsSpeechToText/zh-TW.md)

---
**Source fingerprint (SHA-256):** `7eb5d72615aa8a9e4a8014e45b39cf83dc8d8432d7ce0dccba20489be80a5830`
