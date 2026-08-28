# ElevenLabs 語音轉語音

ElevenLabs 語音轉語音節點可將輸入的音訊檔案從一種語音轉換為另一種語音。它使用 ElevenLabs API 來轉換語音，同時保留音訊的原始內容和情感語調。

## 輸入

### 通用輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `模型` | 用於語音轉語音轉換的模型。所選模型決定了下方列出的可用語音設定。 | DYNAMIC_COMBO | 是 | `eleven_multilingual_sts_v2`<br>`eleven_english_sts_v2` |
| `目標語音` | 轉換的目標語音。從 Voice Selector 或 Instant Voice Clone 連接。 | CUSTOM | 是 | - |
| `音訊` | 要轉換的來源音訊。 | AUDIO | 是 | - |
| `穩定性` | 語音穩定性。數值越低，情感範圍越廣；數值越高，語音越一致，但可能較為單調（預設值：0.5）。 | FLOAT | 是 | 0.0 - 1.0 |
| `輸出格式` | 音訊輸出格式（預設值："mp3_44100_192"）。 | COMBO | 是 | `"mp3_44100_192"`<br>`"opus_48000_192"` |
| `種子` | 用於可重現性的種子（預設值：0）。 | INT | 是 | 0 - 4294967295 |
| `移除背景噪音` | 使用音訊隔離移除輸入音訊中的背景雜訊（預設值：False）。 | BOOLEAN | 是 | - |

### eleven_multilingual_sts_v2 and eleven_english_sts_v2 輸入

兩個模型提供以下相同的語音設定。

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `speed` | 語音速度。1.0 為正常，<1.0 較慢，>1.0 較快（預設值：1.0）。 | FLOAT | 是 | 0.7 - 1.3 |
| `similarity_boost` | 相似度增強。數值越高，語音越接近原始語音（預設值：0.75）。 | FLOAT | 是 | 0.0 - 1.0 |
| `use_speaker_boost` | 增強與原始說話者語音的相似度（預設值：False）。 | BOOLEAN | 是 | - |
| `style` | 風格誇張程度。數值越高，風格表現越強，但可能降低穩定性（預設值：0.0）。 | FLOAT | 是 | 0.0 - 0.2 |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `audio` | 以指定輸出格式轉換後的音訊檔案。 | AUDIO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsSpeechToSpeech/zh-TW.md)

---
**Source fingerprint (SHA-256):** `a3cd602181d134b9ab517bfac092ea30b62ef5a9942a905c0c3e6959b34370ca`
