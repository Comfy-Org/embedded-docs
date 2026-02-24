> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsSpeechToText/zh-TW.md)

ElevenLabs 語音轉文字節點將音訊檔案轉錄為文字。它使用 ElevenLabs 的 API 將口語轉換為書面文字稿，支援自動語言偵測、識別不同說話者以及標記非語音聲音（如音樂或笑聲）等功能。

## 輸入參數

| 參數 | 資料類型 | 必填 | 範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `audio` | AUDIO | 是 | - | 要轉錄的音訊。 |
| `model` | COMBO | 是 | `"scribe_v2"` | 用於轉錄的模型。選擇此模型會顯示額外參數。 |
| `tag_audio_events` | BOOLEAN | 否 | - | 在文字稿中標註聲音，例如（笑聲）、（音樂）等。當選擇 `"scribe_v2"` 模型時，此參數會顯示。（預設值：False） |
| `diarize` | BOOLEAN | 否 | - | 標註正在說話的說話者。當選擇 `"scribe_v2"` 模型時，此參數會顯示。（預設值：False） |
| `diarization_threshold` | FLOAT | 否 | 0.1 - 0.4 | 說話者分離靈敏度。數值越低，對說話者變化的偵測越靈敏。當選擇 `"scribe_v2"` 模型且啟用 `diarize` 時，此參數會顯示。（預設值：0.22） |
| `temperature` | FLOAT | 否 | 0.0 - 2.0 | 隨機性控制。0.0 使用模型預設值。數值越高，隨機性越大。當選擇 `"scribe_v2"` 模型時，此參數會顯示。（預設值：0.0） |
| `timestamps_granularity` | COMBO | 否 | `"word"`<br>`"character"`<br>`"none"` | 文字稿單詞的時間戳記精確度。當選擇 `"scribe_v2"` 模型時，此參數會顯示。（預設值："word"） |
| `language_code` | STRING | 否 | - | ISO-639-1 或 ISO-639-3 語言代碼（例如 'en'、'es'、'fra'）。留空則自動偵測。（預設值：""） |
| `num_speakers` | INT | 否 | 0 - 32 | 要預測的最大說話者數量。設為 0 則自動偵測。（預設值：0） |
| `seed` | INT | 否 | 0 - 2147483647 | 用於重現性的種子（不保證確定性）。（預設值：1） |

**注意：** 當啟用 `diarize` 選項時，`num_speakers` 參數不能設定為大於 0 的值。您必須停用 `diarize` 或將 `num_speakers` 設為 0。

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `text` | STRING | 從音訊轉錄的文字。 |
| `language_code` | STRING | 偵測到的音訊語言代碼。 |
| `words_json` | STRING | 一個 JSON 格式的字串，包含詳細的單詞層級資訊，如果啟用則包括時間戳記和說話者標籤。 |
