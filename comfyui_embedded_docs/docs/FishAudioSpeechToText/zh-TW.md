# FishAudioSpeechToText

此節點使用 Fish Audio 語音轉文字服務將音訊轉錄為文字。它會自動偵測音訊的語言，並可選擇以 JSON 格式傳回詞級別的時間戳記片段。

## 輸入

| 參數 | 描述 | 資料型別 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `audio` | 要轉錄的音訊。 | AUDIO | 是 | — |
| `language` | ISO 639-1 語言提示（例如 'en'、'zh'）。無論如何都會自動偵測語言。預設值：""（空字串）。 | STRING | 否 | 任何 ISO 639-1 語言代碼，例如 `en`、`zh`；空字串表示自動偵測 |
| `precise_timestamps` | 傳回詞級別的時間戳記片段。預設值：false。 | BOOLEAN | 否 | true or false |

注意：`language` 參數僅作為提示——語言始終會從音訊中自動偵測。當 `precise_timestamps` 為 false（預設值）時，不會傳回詞級別的時間戳記；當為 true 時，輸出片段會包含詞級別的時間戳記。

## 輸出

| 輸出名稱 | 描述 | 資料型別 |
|-------------|-------------|-----------|
| `text` | 轉錄後的文字。 | STRING |
| `language_code` | 偵測到的音訊之 ISO 639-1 語言代碼。 | STRING |
| `segments_json` | 包含轉錄片段的 JSON 字串。當啟用 `precise_timestamps` 時，會包含詞級別的時間戳記。 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FishAudioSpeechToText/zh-TW.md)

---
**Source fingerprint (SHA-256):** `eaf1c9a9d2b90ec962a408615cc417b552864354c3f272144b8e239b23961920`
