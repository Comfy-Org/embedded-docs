# TextEncodeAceStepAudio1.5

TextEncodeAceStepAudio1.5 節點準備文字與音訊相關的中繼資料，以供 AceStepAudio 1.5 模型使用。它接受描述性標籤、歌詞與音樂參數，然後使用 CLIP 模型將它們轉換為適合音訊生成的 conditioning 格式。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `clip` | 用於對輸入文字進行標記化與編碼的 CLIP 模型。 | CLIP | 是 | N/A |
| `tags` | 音訊的描述性標籤，例如類型、情緒或樂器。支援多行輸入與動態提示。 | STRING | 是 | N/A |
| `lyrics` | 音訊軌道的歌詞。支援多行輸入與動態提示。 | STRING | 是 | N/A |
| `seed` | 用於可重現生成的隨機種子值。具有 control_after_generate 元件。預設值：0。 | INT | 否 | 0 至 18446744073709551615 |
| `bpm` | 生成音訊的每分鐘拍數 (BPM)。預設值：120。 | INT | 否 | 10 至 300 |
| `duration` | 所需的音訊長度（以秒為單位）。預設值：120.0。 | FLOAT | 否 | 0.0 至 2000.0 |
| `timesignature` | 音樂拍號。 | COMBO | 否 | `"2"`<br>`"3"`<br>`"4"`<br>`"6"` |
| `language` | 輸入文字的语言。預設值："en"。 | COMBO | 否 | `"ar"`<br>`"az"`<br>`"bg"`<br>`"bn"`<br>`"ca"`<br>`"cs"`<br>`"da"`<br>`"de"`<br>`"el"`<br>`"en"`<br>`"es"`<br>`"fa"`<br>`"fi"`<br>`"fr"`<br>`"he"`<br>`"hi"`<br>`"hr"`<br>`"ht"`<br>`"hu"`<br>`"id"`<br>`"is"`<br>`"it"`<br>`"ja"`<br>`"ko"`<br>`"la"`<br>`"lt"`<br>`"ms"`<br>`"ne"`<br>`"nl"`<br>`"no"`<br>`"pa"`<br>`"pl"`<br>`"pt"`<br>`"ro"`<br>`"ru"`<br>`"sa"`<br>`"sk"`<br>`"sr"`<br>`"sv"`<br>`"sw"`<br>`"ta"`<br>`"te"`<br>`"th"`<br>`"tl"`<br>`"tr"`<br>`"uk"`<br>`"ur"`<br>`"vi"`<br>`"yue"`<br>`"zh"`<br>`"unknown"` |
| `keyscale` | 音樂的調性與音階（大調或小調）。 | COMBO | 否 | `"C major"`<br>`"C# major"`<br>`"Db major"`<br>`"D major"`<br>`"D# major"`<br>`"Eb major"`<br>`"E major"`<br>`"F major"`<br>`"F# major"`<br>`"Gb major"`<br>`"G major"`<br>`"G# major"`<br>`"Ab major"`<br>`"A major"`<br>`"A# major"`<br>`"Bb major"`<br>`"B major"`<br>`"C minor"`<br>`"C# minor"`<br>`"Db minor"`<br>`"D minor"`<br>`"D# minor"`<br>`"Eb minor"`<br>`"E minor"`<br>`"F minor"`<br>`"F# minor"`<br>`"Gb minor"`<br>`"G minor"`<br>`"G# minor"`<br>`"Ab minor"`<br>`"A minor"`<br>`"A# minor"`<br>`"Bb minor"`<br>`"B minor"` |
| `generate_audio_codes` | 啟用生成音訊代碼的 LLM。這可能會較慢，但會提高生成音訊的品質。如果你為模型提供音訊參考，請關閉此選項。預設值：True。 | BOOLEAN | 否 | N/A |
| `cfg_scale` | 無分類器指導（Classifier-free guidance）尺度。數值越高，輸出越貼近提示。預設值：2.0。 | FLOAT | 否 | 0.0 至 100.0 |
| `temperature` | 取樣溫度。數值越低，輸出越具確定性。預設值：0.85。 | FLOAT | 否 | 0.0 至 2.0 |
| `top_p` | 核取樣機率 (top-p)。預設值：0.9。 | FLOAT | 否 | 0.0 至 2000.0 |
| `top_k` | 要考慮的最高機率 token 數量 (top-k)。預設值：0。 | INT | 否 | 0 至 100 |
| `min_p` | token 取樣的最低機率門檻 (min-p)。預設值：0.000。 | FLOAT | 否 | 0.0 至 1.0 |

## 輸出

| 輸出名 | 說明 | 資料類型 |
| --- | --- | --- |
| `CONDITIONING` | conditioning 資料，包含供 AceStepAudio 1.5 模型使用的編碼後文字與音訊參數。 | CONDITIONING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeAceStepAudio1.5/zh-TW.md)

---
**Source fingerprint (SHA-256):** `4bc97ec6220514b71fafde610339f2dca4ded26f68b541ed43ea492f127321f8`
