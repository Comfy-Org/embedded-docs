# HeyGenTextToSpeechNode

使用 HeyGen 的 Starfish TTS 引擎從文字生成語音音頻。此節點包含 HeyGen 最受歡迎的 17 種語言配音。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `text` | 要合成的文字（最多 5000 個字元）。生成的語音長度必須至少 1 秒。 | STRING | 是 | 1 到 5000 個字元 |
| `voice` | 要使用的配音（從 HeyGen 最受歡迎的 Starfish 相容配音中精選）。 | STRING | 是 | 提供多個選項 |
| `custom_voice_id` | 可選的 HeyGen 配音 ID。設定後將覆蓋上方選擇的配音。該配音必須支援 Starfish 引擎。 | STRING | 否 | 任何有效的 HeyGen 配音 ID |
| `speed` | 語音速度倍率（預設值：1.0）。 | FLOAT | 否 | 0.5 到 2.0（步長：0.05） |
| `ssml` | 將文字視為 SSML 標記（用於控制停頓、強調和發音）（預設值：False）。 | BOOLEAN | 否 | True / False |
| `seed` | 不會發送到 HeyGen；更改它以強制重新執行（預設值：42）。 | INT | 否 | 0 到 2147483647 |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `AUDIO` | 從輸入文字生成的合成語音音頻。 | AUDIO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenTextToSpeechNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `82300626657db8ab16e96ae96b7dfe3291b77bf75efec35971dc772e5123cce7`
