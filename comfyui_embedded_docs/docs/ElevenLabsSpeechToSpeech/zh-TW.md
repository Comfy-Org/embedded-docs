# ElevenLabs 語音轉語音

ElevenLabs Speech to Speech 節點將輸入的音訊檔案從一種聲音轉換為另一種聲音。它使用 ElevenLabs API 轉換語音，同時保留音訊的原始內容和情緒語調。

## 輸入

### 通用輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `模型` | 用於語音轉換的模型。每個模型選項都提供一組相符的語音設定（`similarity_boost`、`style`、`use_speaker_boost`、`speed`）。 | DYNAMIC_COMBO | 否 | `eleven_multilingual_sts_v2`<br>`eleven_english_sts_v2` |
| `目標語音` | 轉換的目標聲音。從 Voice Selector 或 Instant Voice Clone 連接。 | CUSTOM | 是 | - |
| `音訊` | 要轉換的來源音訊。 | AUDIO | 是 | - |
| `穩定性` | 語音穩定性。較低的值提供更廣泛的情緒範圍，較高的值產生更一致但可能單調的語音（預設值：0.5）。 | FLOAT | 否 | 0.0 - 1.0 |
| `輸出格式` | 音訊輸出格式（預設值：\"mp3_44100_192\"）。 | COMBO | 否 | `"mp3_44100_192"`<br>`"opus_48000_192"` |
| `種子` | 用於再現性的種子（預設值：0）。 | INT | 否 | 0 - 4294967295 |
| `移除背景噪音` | 使用音訊隔離從輸入音訊中移除背景雜訊（預設值：False）。 | BOOLEAN | 否 | - |

### 語音設定（由 `eleven_multilingual_sts_v2` 和 `eleven_english_sts_v2` 共用）

選擇模型後，這些語音設定即可用於轉換。

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `speed` | 語音速度。1.0 為正常，<1.0 較慢，>1.0 較快（預設值：1.0）。 | FLOAT | 否 | 0.7 - 1.3 |
| `similarity_boost` | 相似度增強。較高的值使聲音更接近原始聲音（預設值：0.75）。 | FLOAT | 否 | 0.0 - 1.0 |
| `use_speaker_boost` | 增強與原始說話者聲音的相似度（預設值：False）。 | BOOLEAN | 否 | - |
| `style` | 風格誇張程度。較高的值會增加風格表現力，但可能降低穩定性（預設值：0.0）。 | FLOAT | 否 | 0.0 - 0.2 |

## 輸出

| 輸出名 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `audio` | 以指定輸出格式轉換後的音訊檔案。 | AUDIO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsSpeechToSpeech/zh-TW.md)

---
**Source fingerprint (SHA-256):** `a3cd602181d134b9ab517bfac092ea30b62ef5a9942a905c0c3e6959b34370ca`
