> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingOmniProEditVideoNode/zh-TW.md)

Kling Omni Edit Video (Pro) 節點使用 AI 模型，根據文字描述編輯現有影片。您提供原始影片和提示詞，該節點會生成一個相同長度、包含所要求修改的新影片。它可以選擇性地使用參考圖片來引導風格，並保留原始影片的音訊。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `model_name` | COMBO | 是 | `"kling-video-o1"` | 用於影片編輯的 AI 模型。 |
| `prompt` | STRING | 是 | | 描述影片內容的文字提示詞。可以包含正面和負面描述。 |
| `video` | VIDEO | 是 | | 用於編輯的影片。輸出影片的長度將與之相同。 |
| `keep_original_sound` | BOOLEAN | 是 | | 決定是否在輸出中保留輸入影片的原始音訊（預設值：True）。 |
| `reference_images` | IMAGE | 否 | | 最多 4 張額外的參考圖片。 |
| `resolution` | COMBO | 否 | `"1080p"`<br>`"720p"` | 輸出影片的解析度（預設值："1080p"）。 |

**限制與約束：**

* `prompt` 的長度必須在 1 到 2500 個字元之間。
* 輸入的 `video` 時長必須在 3.0 到 10.05 秒之間。
* 輸入的 `video` 尺寸必須在 720x720 到 2160x2160 像素之間。
* 使用影片時，最多可以提供 4 張 `reference_images`。
* 每張 `reference_image` 必須至少為 300x300 像素。
* 每張 `reference_image` 的長寬比必須在 1:2.5 到 2.5:1 之間。

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `video` | VIDEO | 由 AI 模型生成的編輯後影片。 |
