> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsTextToSpeech/zh-TW.md)

## 概述

ElevenLabs 文字轉語音節點使用 ElevenLabs API 將書面文字轉換為口語音訊。它允許您選擇特定的語音，並微調各種語音特徵，如穩定性、速度和風格，以產生自訂的音訊輸出。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `voice` | CUSTOM | 是 | N/A | 用於語音合成的語音。從語音選擇器或即時語音克隆連接。 |
| `text` | STRING | 是 | N/A | 要轉換為語音的文字。 |
| `stability` | FLOAT | 否 | 0.0 - 1.0 | 語音穩定性。較低的值提供更廣泛的情感範圍，較高的值產生更一致但可能單調的語音（預設值：0.5）。 |
| `apply_text_normalization` | COMBO | 否 | `"auto"`<br>`"on"`<br>`"off"` | 文字正規化模式。'auto' 讓系統決定，'on' 始終套用正規化，'off' 跳過正規化。 |
| `model` | DYNAMICCOMBO | 否 | `"eleven_multilingual_v2"`<br>`"eleven_v3"` | 用於文字轉語音的模型。選擇模型會顯示其特定參數。 |
| `language_code` | STRING | 否 | N/A | ISO-639-1 或 ISO-639-3 語言代碼（例如 'en'、'es'、'fra'）。留空以進行自動偵測（預設值：""）。 |
| `seed` | INT | 否 | 0 - 2147483647 | 用於可重現性的種子（不保證確定性）（預設值：1）。 |
| `output_format` | COMBO | 否 | `"mp3_44100_192"`<br>`"opus_48000_192"` | 音訊輸出格式。 |

**模型特定參數：**
當 `model` 參數設定為 `"eleven_multilingual_v2"` 時，以下額外參數將變為可用：

* `speed`：語音速度。1.0 為正常，<1.0 較慢，>1.0 較快（預設值：1.0，範圍：0.7 - 1.3）。
* `similarity_boost`：相似度增強。較高的值使語音更接近原始語音（預設值：0.75，範圍：0.0 - 1.0）。
* `use_speaker_boost`：增強與原始說話者語音的相似度（預設值：False）。
* `style`：風格誇張程度。較高的值會增加風格表現力，但可能降低穩定性（預設值：0.0，範圍：0.0 - 0.2）。

當 `model` 參數設定為 `"eleven_v3"` 時，以下額外參數將變為可用：

* `speed`：語音速度。1.0 為正常，<1.0 較慢，>1.0 較快（預設值：1.0，範圍：0.7 - 1.3）。
* `similarity_boost`：相似度增強。較高的值使語音更接近原始語音（預設值：0.75，範圍：0.0 - 1.0）。

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `audio` | AUDIO | 從文字轉語音轉換產生的音訊。 |

---
**Source fingerprint (SHA-256):** `d11d4ffa2d1f11dfd5ce378d9496cd9788d2197bf7f4135092ecefb287f3c2f7`
