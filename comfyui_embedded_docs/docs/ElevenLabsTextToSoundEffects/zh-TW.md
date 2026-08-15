# ElevenLabs 文字轉音效

ElevenLabs 文字轉音效節點使用 ElevenLabs API，從文字描述產生音效音訊。它會將您輸入的提示文字傳送至 ElevenLabs 音效生成服務，並傳回產生的音訊，同時提供控制項，可調整音訊長度、循環行為，以及音效跟隨文字描述的貼合程度。

## 輸入

### 通用輸入

| 參數 | 描述 | 資料型別 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `模型` | 用於音效生成的模型。所選模型決定下方列出的可用生成參數。 | DYNAMIC_COMBO | 是 | `"eleven_sfx_v2"` |
| `文字` | 要生成之音效的文字描述。至少需包含 1 個字元。（預設：空） | STRING | 是 | N/A |
| `輸出格式` | 音訊輸出格式。 | COMBO | 是 | `"mp3_44100_192"`<br>`"opus_48000_192"` |

### Eleven SFX v2 輸入

當 `model` 設為 `"eleven_sfx_v2"` 時顯示的子參數。

| 參數 | 描述 | 資料型別 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `duration` | 生成音效的持續時間（秒）。（預設：5.0） | FLOAT | 是 | 0.5 至 30.0 (步長: 0.1) |
| `loop` | 建立平滑循環的音效。（預設：False） | BOOLEAN | 否 | True or False |
| `prompt_influence` | 生成結果跟隨提示文字的程度。數值越高，音效越貼近文字描述。（預設：0.3） | FLOAT | 是 | 0.0 至 1.0 (步長: 0.01) |

## 輸出

| 輸出名稱 | 描述 | 資料型別 |
|-------------|-------------|-----------|
| `audio` | 生成的音效音訊檔案。 | AUDIO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsTextToSoundEffects/zh-TW.md)

---
**Source fingerprint (SHA-256):** `218ff617256cea33f310c1bcfc6407c46aaadc59201a0324b0ec64583166ce58`
