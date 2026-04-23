> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan2ReferenceVideoApi/zh-TW.md)

此節點根據提供的參考素材生成以人物或物體為特色的影片。它使用 Wan 2.7 模型，根據文字提示建立影片，支援單一角色表演與多角色互動。您必須提供至少一個參考影片或圖像，生成功能才能運作。

## 輸入參數

| 參數 | 資料類型 | 必填 | 範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | 是 | `"wan2.7-r2v"` | 用於影片生成的特定模型。 |
| `model.prompt` | STRING | 是 | - | 描述影片的提示詞。使用如 'character1' 和 'character2' 等識別符來指代參考角色。 |
| `model.negative_prompt` | STRING | 否 | - | 描述在生成影片中應避免內容的負向提示詞（預設為空）。 |
| `model.resolution` | COMBO | 是 | `"720P"`<br>`"1080P"` | 輸出影片的解析度。 |
| `model.ratio` | COMBO | 是 | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"` | 輸出影片的長寬比。 |
| `model.duration` | INT | 是 | 2 到 10 | 生成影片的長度，單位為秒（預設值：5）。 |
| `model.reference_videos` | VIDEO | 否 | - | 參考影片清單。最多可新增 3 個影片。 |
| `model.reference_images` | IMAGE | 否 | - | 參考圖像清單。最多可新增 5 個圖像。 |
| `seed` | INT | 否 | 0 到 2147483647 | 用於生成的種子值，有助於控制輸出的隨機性（預設值：0）。 |
| `watermark` | BOOLEAN | 否 | - | 是否在結果中添加 AI 生成浮水印（預設值：False）。此為進階設定。 |

**重要限制：**
*   您必須在 `model.reference_videos` 或 `model.reference_images` 輸入中提供至少一個參考影片或參考圖像。
*   參考影片和圖像的總數合計不得超過 5 個。

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `output` | VIDEO | 生成的影片檔案。 |