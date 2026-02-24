> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Veo3FirstLastFrameNode/zh-TW.md)

Veo3FirstLastFrameNode 使用 Google 的 Veo 3 模型來生成影片。它根據文字提示建立影片，並使用提供的首尾畫面來引導序列的開始與結束。

## 輸入參數

| 參數 | 資料類型 | 必填 | 範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | 是 | N/A | 影片的文字描述（預設：空字串）。 |
| `negative_prompt` | STRING | 否 | N/A | 負向文字提示，用於引導影片中應避免的內容（預設：空字串）。 |
| `resolution` | COMBO | 是 | `"720p"`<br>`"1080p"` | 輸出影片的解析度。 |
| `aspect_ratio` | COMBO | 否 | `"16:9"`<br>`"9:16"` | 輸出影片的長寬比（預設："16:9"）。 |
| `duration` | INT | 否 | 4 到 8 | 輸出影片的持續時間（單位：秒，預設：8）。 |
| `seed` | INT | 否 | 0 到 4294967295 | 影片生成的隨機種子（預設：0）。 |
| `first_frame` | IMAGE | 是 | N/A | 影片的起始畫面。 |
| `last_frame` | IMAGE | 是 | N/A | 影片的結束畫面。 |
| `model` | COMBO | 否 | `"veo-3.1-generate"`<br>`"veo-3.1-fast-generate"` | 用於生成的特定 Veo 3 模型（預設："veo-3.1-fast-generate"）。 |
| `generate_audio` | BOOLEAN | 否 | N/A | 為影片生成音訊（預設：True）。 |

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `output` | VIDEO | 生成的影片檔案。 |
