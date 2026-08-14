# Wan 2.7 影片續接

The Wan 2.7 Video Continuation 節點會生成一段新的影片片段，從輸入影片剪輯的結尾繼續延伸。它使用 Wan 2.7 模型，根據文字提示詞合成接續內容，並可選擇性地將結尾引導至特定的目標幀。

## 輸入

### 通用輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | 要使用的影片生成模型。 | COMBO | 是 | `"wan2.7-i2v"` |
| `first_clip` | 要接續的輸入影片。持續時間：2 秒至 10 秒。輸出長寬比由該影片決定。 | VIDEO | 是 | 2s to 10s |
| `last_frame` | 最後一幀的圖像。接續內容將過渡到此幀。 | IMAGE | 否 | - |
| `seed` | 用於生成的種子。(預設值：0) | INT | 是 | 0 至 2147483647 |
| `prompt_extend` | 是否使用 AI 輔助增強提示詞。(預設值：True) | BOOLEAN | 是 | - |
| `watermark` | 是否在結果中加入 AI 生成的浮水印。(預設值：False) | BOOLEAN | 是 | - |

### wan2.7-i2v 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model.prompt` | 描述元素和視覺特徵的提示詞。支援英文和中文。(預設值：空字串) | STRING | 是 | - |
| `model.negative_prompt` | 描述應避免內容的負面提示詞。(預設值：空字串) | STRING | 是 | - |
| `model.resolution` | 輸出影片的解析度。 | COMBO | 是 | `"720P"`<br>`"1080P"` |
| `model.duration` | 輸出總持續時間（秒）。模型會生成接續內容，以填補輸入影片剪輯之後的剩餘時間。(預設值：5) | INT | 是 | 2 至 15 |

**注意：** `first_clip` 輸入影片的持續時間必須介於 2 秒到 10 秒之間。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `output` | 生成的影片接續內容。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan2VideoContinuationApi/zh-TW.md)

---
**Source fingerprint (SHA-256):** `591e551676969bc1fedb5f820f6866512c132bb98ee8ef1766d1e0b389e2dc11`
