> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokVideoReferenceNode/zh-TW.md)

Grok Reference-to-Video 節點根據文字提示生成影片，並使用最多七張參考圖像來引導輸出的風格和內容。它會連接到外部 API 來創建影片，然後下載並返回該影片。

## 輸入參數

| 參數 | 資料類型 | 必填 | 範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | 是 | N/A | 期望影片的文字描述。 |
| `model` | COMBO | 是 | `"grok-imagine-video"` | 用於影片生成的模型。 |
| `model.reference_images` | IMAGE | 是 | 1 到 7 張圖像 | 最多 7 張用於引導影片生成的參考圖像。 |
| `model.resolution` | COMBO | 是 | `"480p"`<br>`"720p"` | 輸出影片的解析度。 |
| `model.aspect_ratio` | COMBO | 是 | `"16:9"`<br>`"4:3"`<br>`"3:2"`<br>`"1:1"`<br>`"2:3"`<br>`"3:4"`<br>`"9:16"` | 輸出影片的長寬比。 |
| `model.duration` | INT | 是 | 2 到 10 | 輸出影片的持續時間（單位：秒，預設值：6）。 |
| `seed` | INT | 否 | 0 到 2147483647 | 用於決定節點是否應重新執行的種子值；無論種子為何，實際結果都是非確定性的（預設值：0）。 |

**注意：** `model` 參數是一個包含 `reference_images`、`resolution`、`aspect_ratio` 和 `duration` 的群組。您必須提供至少一張參考圖像，最多可提供七張。

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `video` | VIDEO | 生成的影片檔案。 |