> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsSpeechToSpeech/zh-TW.md)

此節點將輸入的音訊檔案從一個聲音轉換為另一個聲音。它使用 ElevenLabs API 來轉換語音，同時保留原始音訊的內容和情感基調。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `voice` | CUSTOM | 是 | - | 轉換的目標聲音。請從 Voice Selector 或 Instant Voice Clone 節點連接。 |
| `audio` | AUDIO | 是 | - | 要轉換的來源音訊。 |
| `stability` | FLOAT | 否 | 0.0 - 1.0 | 聲音穩定性。較低的值提供更廣泛的情感範圍，較高的值產生更一致但可能單調的語音（預設值：0.5）。 |
| `model` | DYNAMICCOMBO | 否 | `eleven_multilingual_sts_v2`<br>`eleven_english_sts_v2` | 用於語音轉語音轉換的模型。每個選項提供一組特定的聲音設定（相似度增強、風格、使用說話者增強、速度）。 |
| `output_format` | COMBO | 否 | `"mp3_44100_192"`<br>`"opus_48000_192"` | 音訊輸出格式（預設值："mp3_44100_192"）。 |
| `seed` | INT | 否 | 0 - 4294967295 | 用於重現性的種子值（預設值：0）。 |
| `remove_background_noise` | BOOLEAN | 否 | - | 使用音訊隔離功能移除輸入音訊中的背景噪音（預設值：False）。 |

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `audio` | AUDIO | 以指定輸出格式轉換後的音訊檔案。 |
