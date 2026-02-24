> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingImageToVideoWithAudio/zh-TW.md)

Kling Image(First Frame) to Video with Audio 節點使用 Kling AI 模型，從單張起始圖片和文字提示生成短片。它會建立一個以提供的圖片為開頭的影片序列，並可選擇性地包含 AI 生成的音訊來搭配視覺效果。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `model_name` | COMBO | 是 | `"kling-v2-6"` | 用於影片生成的 Kling AI 模型特定版本。 |
| `start_frame` | IMAGE | 是 | - | 將作為生成影片第一幀的圖片。圖片必須至少為 300x300 像素，且長寬比需在 1:2.5 到 2.5:1 之間。 |
| `prompt` | STRING | 是 | - | 正向文字提示。這描述了您想要生成的影片內容。提示長度必須在 1 到 2500 個字元之間。 |
| `mode` | COMBO | 是 | `"pro"` | 影片生成的操作模式。 |
| `duration` | COMBO | 是 | `5`<br>`10` | 要生成的影片長度，單位為秒。 |
| `generate_audio` | BOOLEAN | 否 | - | 啟用時，節點將生成伴隨影片的音訊。停用時，影片將是靜音的。(預設值：True) |

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `video` | VIDEO | 生成的影片檔案，根據 `generate_audio` 輸入的設定，可能包含音訊。 |
