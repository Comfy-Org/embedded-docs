# Wan 2.7 圖像轉影片

Wan 2.7 影像轉視訊節點會根據首幀影像產生影片。您可以選擇性地提供尾幀影像，以建立兩者之間的轉場，或提供音訊檔案來引導影片的動作與節奏。此節點使用 AI 模型，根據您的文字描述來為場景製作動畫。

## 輸入

### 通用輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 用於影片生成的 AI 模型。 | DYNAMIC_COMBO | 是 | `"wan2.7-i2v"` |
| `first_frame` | 首幀影像。輸出影片的長寬比由此影像決定。 | IMAGE | 是 | - |
| `last_frame` | 尾幀影像。模型會生成從首幀轉場到尾幀的影片。 | IMAGE | 否 | - |
| `audio` | 用於驅動影片生成的音訊（例如：唇形同步、節拍對齊動作）。時長：2 秒至 30 秒。若未提供，模型會自動生成相符的背景音樂或音效。 | AUDIO | 否 | - |
| `seed` | 用於生成的隨機種子（預設值：0）。 | INT | 是 | 0 至 2147483647 |
| `prompt_extend` | 是否使用 AI 輔助增強提示詞（預設值：True）。此為進階設定。 | BOOLEAN | 是 | True<br>False |
| `watermark` | 是否在結果中加入 AI 生成的水印（預設值：False）。此為進階設定。 | BOOLEAN | 是 | True<br>False |

### wan2.7-i2v 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `prompt` | 描述元素與視覺特徵的提示詞。支援英文與中文。（預設值：空白） | STRING | 是 | - |
| `negative_prompt` | 描述應避免內容的負面提示詞。（預設值：空白） | STRING | 是 | - |
| `resolution` | 輸出影片的解析度。 | COMBO | 是 | `"720P"`<br>`"1080P"` |
| `duration` | 生成影片的長度，以秒為單位（預設值：5）。 | INT | 是 | 2 至 15 |

**注意：** `audio` 輸入有時間長度限制。若提供音訊，檔案長度必須介於 2 至 30 秒之間。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `output` | 生成的影片檔案。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan2ImageToVideoApi/zh-TW.md)

---
**Source fingerprint (SHA-256):** `81b0dc9500ff00e1428422d3d9c8df8f790c1d9dec547dcba0d1aa239f8a8beb`
