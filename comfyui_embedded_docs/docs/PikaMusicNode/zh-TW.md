# Pika Music

此節點可使用 Pika 從文字描述與選填歌詞生成音樂，或翻唱你提供的歌曲。選擇 `"text to music"` 可依你設定的長度創作新歌，或選擇 `"cover"` 重新錄製歌曲並保留其長度。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `mode` | 此節點的作用：`"text to music"` 會創作一首新歌，`"cover"` 會重新錄製提供的歌曲。每種模式會在下方顯示各自的輸入。預設：`"text to music"`。 | DYNAMIC_COMBO | 是 | `"text to music"`<br>`"cover"` |

### Text to Music 輸入

當 `mode` 設為 `"text to music"` 時，會顯示這些輸入。

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 音樂應呈現的聲音風格。不得為空。預設：`""`（空字串）。 | STRING | 是 | 1 至 4000 個字元 |
| `lyrics` | 選填歌詞。允許使用 `[Verse]` 和 `[Chorus]` 等段落標籤。預設：`""`（空字串）。 | STRING | 是 | 0 至 8000 個字元 |
| `duration` | 歌曲長度，以秒為單位。預設：30.0。 | FLOAT | 是 | 10.0 至 360.0（步進值：0.1） |
| `rewrite_prompt` | 在生成前使用模型擴充簡短或模糊的提示詞。預設：False。 | BOOLEAN | 是 | true<br>false |
| `seed` | 取樣用的種子值。預設：42。 | INT | 是 | 0 至 2147483647 |

### Cover 輸入

當 `mode` 設為 `"cover"` 時，會顯示這些輸入。

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `source_audio` | 要翻唱的歌曲。結果長度會相同，並限制在 5 至 360 秒之間。 | AUDIO | 是 | - |
| `prompt` | 翻唱版本應呈現的聲音風格。不得為空。預設：`""`（空字串）。 | STRING | 是 | 1 至 4000 個字元 |
| `lyrics` | 選填歌詞。允許使用 `[Verse]` 和 `[Chorus]` 等段落標籤。預設：`""`（空字串）。 | STRING | 是 | 0 至 8000 個字元 |
| `rewrite_prompt` | 在生成前使用模型擴充簡短或模糊的提示詞。預設：False。 | BOOLEAN | 是 | true<br>false |
| `seed` | 取樣用的種子值。預設：42。 | INT | 是 | 0 至 2147483647 |

**限制：**

* `prompt` 必須介於 1 到 4000 個字元之間，且 `lyrics` 最多 8000 個字元。
* `"cover"` 模式會忽略 `duration`：輸出的長度會與 `source_audio` 相同，並限制在 5 至 360 秒之間。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `AUDIO` | 生成的歌曲，或所提供曲目的翻唱版本。 | AUDIO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PikaMusicNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `e3051b2d0cfff72cf7e359d7383f4e0d133df0338ff42a00f0649387f504ec28`
