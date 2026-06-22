# TextEncodeAceStepAudio1.5

## 概述

TextEncodeAceStepAudio1.5 節點負責準備文字與音訊相關的元數據，以供 AceStepAudio 1.5 模型使用。它接收描述性標籤、歌詞及音樂參數，然後利用 CLIP 模型將其轉換為適合音訊生成的條件格式。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `clip` | 用於對輸入文字進行分詞和編碼的 CLIP 模型。 | CLIP | 是 | 不適用 |
| `tags` | 音訊的描述性標籤，例如類型、情緒或樂器。支援多行輸入和動態提示。 | STRING | 是 | 不適用 |
| `lyrics` | 音軌的歌詞。支援多行輸入和動態提示。 | STRING | 是 | 不適用 |
| `seed` | 用於可重現生成的隨機種子值。具有 control_after_generate 小工具。預設值：0。 | INT | 否 | 0 至 18446744073709551615 |
| `bpm` | 生成音訊的每分鐘節拍數 (BPM)。預設值：120。 | INT | 否 | 10 至 300 |
| `duration` | 音訊的期望時長（以秒為單位）。預設值：120.0。 | FLOAT | 否 | 0.0 至 2000.0 |
| `timesignature` | 音樂拍號。 | COMBO | 否 | `"2"`<br>`"3"`<br>`"4"`<br>`"6"` |
| `language` | 輸入文字的語言。預設值："en"。 | COMBO | 否 | `"ar"`<br>`"az"`<br>`"bg"`<br>`"bn"`<br>`"ca"`<br>`"cs"`<br>`"da"`<br>`"de"`<br>`"el"`<br>`"en"`<br>`"es"`<br>`"fa"`<br>`"fi"`<br>`"fr"`<br>`"he"`<br>`"hi"`<br>`"hr"`<br>`"ht"`<br>`"hu"`<br>`"id"`<br>`"is"`<br>`"it"`<br>`"ja"`<br>`"ko"`<br>`"la"`<br>`"lt"`<br>`"ms"`<br>`"ne"`<br>`"nl"`<br>`"no"`<br>`"pa"`<br>`"pl"`<br>`"pt"`<br>`"ro"`<br>`"ru"`<br>`"sa"`<br>`"sk"`<br>`"sr"`<br>`"sv"`<br>`"sw"`<br>`"ta"`<br>`"te"`<br>`"th"`<br>`"tl"`<br>`"tr"`<br>`"uk"`<br>`"ur"`<br>`"vi"`<br>`"yue"`<br>`"zh"`<br>`"unknown"` |
| `keyscale` | 音樂調性與音階（大調或小調）。 | COMBO | 否 | `"C major"`<br>`"C minor"`<br>`"C# major"`<br>`"C# minor"`<br>`"Db major"`<br>`"Db minor"`<br>`"D major"`<br>`"D minor"`<br>`"D# major"`<br>`"D# minor"`<br>`"Eb major"`<br>`"Eb minor"`<br>`"E major"`<br>`"E minor"`<br>`"F major"`<br>`"F minor"`<br>`"F# major"`<br>`"F# minor"`<br>`"Gb major"`<br>`"Gb minor"`<br>`"G major"`<br>`"G minor"`<br>`"G# major"`<br>`"G# minor"`<br>`"Ab major"`<br>`"Ab minor"`<br>`"A major"`<br>`"A minor"`<br>`"A# major"`<br>`"A# minor"`<br>`"Bb major"`<br>`"Bb minor"`<br>`"B major"`<br>`"B minor"` |
| `generate_audio_codes` | 啟用生成音訊編碼的 LLM。此過程可能較慢，但會提升生成音訊的品質。若您提供音訊參考給模型，請關閉此選項。預設值：True。 | BOOLEAN | 否 | 不適用 |
| `cfg_scale` | 無分類器引導尺度。數值越高，輸出越貼近提示。預設值：2.0。 | FLOAT | 否 | 0.0 至 100.0 |
| `temperature` | 取樣溫度。數值越低，輸出越具確定性。預設值：0.85。 | FLOAT | 否 | 0.0 至 2.0 |
| `top_p` | 核心取樣機率 (top-p)。預設值：0.9。 | FLOAT | 否 | 0.0 至 2000.0 |
| `top_k` | 要考慮的機率最高 token 數量 (top-k)。預設值：0。 | INT | 否 | 0 至 100 |
| `min_p` | token 取樣的最低機率閾值 (min-p)。預設值：0.000。 | FLOAT | 否 | 0.0 至 1.0 |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `CONDITIONING` | 條件數據，包含為 AceStepAudio 1.5 模型編碼的文字與音訊參數。 | CONDITIONING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeAceStepAudio1.5/zh-TW.md)

---
**Source fingerprint (SHA-256):** `df70a55024812d8c77a3b618cbff6d3148a3f3f5fc4d17dd3c4282ce7f3cbc2c`
