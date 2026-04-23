> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan2VideoEditApi/zh-TW.md)

Wan2VideoEditApi 節點使用 Wan 2.7 模型，根據文字指令、參考圖像或風格遷移來編輯影片。它會處理輸入影片，並根據指定的解析度、持續時間和長寬比等參數生成新的影片。

## 輸入參數

| 參數 | 資料類型 | 必填 | 範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | 是 | `"wan2.7-videoedit"` | 用於影片編輯的模型。 |
| `model.prompt` | STRING | 是 | - | 編輯指令或風格遷移要求。(預設值：空字串) |
| `model.resolution` | COMBO | 是 | `"720P"`<br>`"1080P"` | 輸出影片的解析度。 |
| `model.ratio` | COMBO | 是 | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"` | 輸出影片的長寬比。如果未更改，則會近似於輸入影片的長寬比。 |
| `model.duration` | COMBO | 是 | `"auto"`<br>`"2"`<br>`"3"`<br>`"4"`<br>`"5"`<br>`"6"`<br>`"7"`<br>`"8"`<br>`"9"`<br>`"10"` | 輸出影片的持續時間（秒）。'auto' 表示與輸入影片持續時間一致。指定具體數值會從影片開頭截取對應長度。(預設值："auto") |
| `model.reference_images` | IMAGE | 否 | - | 用於引導編輯的參考圖像清單，最多 4 張。 |
| `video` | VIDEO | 是 | - | 要編輯的影片。 |
| `seed` | INT | 否 | 0 到 2147483647 | 用於生成的種子值。(預設值：0) |
| `audio_setting` | COMBO | 否 | `"auto"`<br>`"origin"` | 'auto'：模型根據提示詞決定是否重新生成音訊。'origin'：保留輸入影片的原始音訊。(預設值："auto") |
| `watermark` | BOOLEAN | 否 | - | 是否在結果中添加 AI 生成的水印。(預設值：False) |

**限制條件：**
*   `model.prompt` 的長度必須至少為 1 個字元。
*   輸入的 `video` 持續時間必須在 2 到 10 秒之間。
*   `model.reference_images` 輸入最多可接受 4 張圖像。

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `output` | VIDEO | 由模型生成的編輯後影片。 |