# HeyGen Voice 1.0 Text to Speech

使用 HeyGen 的語音朗讀文字。此節點會將文字與語音 ID 傳送至 HeyGen，並將生成的語音以音訊形式傳回。提供兩種模型：`heygen-voice-1`，以及速度更快、費用更低的 `heygen-voice-1-turbo`。若要使用從錄音複製的語音，請使用 HeyGen Voice 1.0 Instant Clone Text to Speech 節點。

選取 `model` 後，會顯示該模型專屬的參數。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | 要使用的模型。`heygen-voice-1-turbo` 速度更快，費用更低。選取模型後會顯示其專屬參數：`voice_id`、`text`、`language` 與 `expressiveness_boost`。 | DYNAMIC_COMBO | 是 | `"heygen-voice-1"`<br>`"heygen-voice-1-turbo"` |
| `voice_id` | HeyGen 語音的 ID，例如來自 HeyGen 語音庫（預設：空）。 | STRING | 是 | N/A |
| `text` | 要朗讀的文字。最多 5000 個字元；超過約 12 分鐘的語音會失敗，因此請將非常長的中文或日文文字分段（預設：空）。 | STRING | 是 | 1 到 5000 個字元 |
| `language` | 文字語言。對於塞爾維亞語或馬來語等自動偵測可能混淆的相近語言，請設定此項（預設：`"auto"`）。 | COMBO | 是 | `"auto"`<br>多種語言預設 |
| `expressiveness_boost` | 數值越高，表現力越強；數值越低，越接近原始語音（預設：0.5）。 | FLOAT | 是 | 0.0 到 1.0（步進 0.05） |

**注意：** `voice_id` 不可為空；缺少時節點會停止並報錯。`text` 必須至少包含一個字元。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `AUDIO` | 根據文字生成並以所選語音朗讀的語音。 | AUDIO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenVoiceTextToSpeechNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `d5bc03344341f2562d4bdca3a8503928a0dbbf7bd2b85df073bd04ab20b4be98`
