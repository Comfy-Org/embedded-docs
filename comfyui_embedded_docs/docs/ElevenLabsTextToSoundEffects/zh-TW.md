# ElevenLabs 文字轉音效

The ElevenLabs 文字轉音效節點可根據文字描述生成音效。它使用 ElevenLabs API 根據您的提示詞建立音效，讓您能控制音效長度、循環行為，以及聲音跟隨文字描述的緊密程度。

## 輸入

### 通用輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `模型` | 用於音效生成的模型。目前僅提供一個模型：`eleven_sfx_v2`。 | DYNAMIC_COMBO | 是 | `"eleven_sfx_v2"` |
| `文字` | 要生成之音效的文字描述。（預設值：空白） | STRING | 是 | N/A |
| `輸出格式` | 音訊輸出格式。 | COMBO | 是 | `"mp3_44100_192"`<br>`"opus_48000_192"` |

### eleven_sfx_v2 輸入

這些參數會在選取 `eleven_sfx_v2` 模型時顯示。

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `duration` | 生成音效的長度（秒）。（預設值：5.0） | FLOAT | 是 | 0.5 至 30.0 |
| `loop` | 建立可平滑循環的音效。（預設值：False） | BOOLEAN | 否 | True<br>False |
| `prompt_influence` | 生成結果跟隨提示詞的程度。數值越高，聲音越貼近文字描述。（預設值：0.3） | FLOAT | 是 | 0.0 至 1.0 |

**注意：** `text` 參數不可為空；在傳送音效生成請求之前會進行驗證。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `audio` | 生成的音效音訊檔案。 | AUDIO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsTextToSoundEffects/zh-TW.md)

---
**Source fingerprint (SHA-256):** `218ff617256cea33f310c1bcfc6407c46aaadc59201a0324b0ec64583166ce58`
