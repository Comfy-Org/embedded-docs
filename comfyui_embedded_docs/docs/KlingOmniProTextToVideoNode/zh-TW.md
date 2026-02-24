> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingOmniProTextToVideoNode/zh-TW.md)

此節點使用 Kling AI 模型，根據文字描述生成影片。它會將您的提示發送到遠端 API，並返回生成的影片。此節點允許您控制影片的長度、形狀和品質。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `model_name` | COMBO | 是 | `"kling-video-o1"` | 用於影片生成的特定 Kling 模型。 |
| `prompt` | STRING | 是 | 1 至 2500 個字元 | 描述影片內容的文字提示。可以包含正面和負面的描述。 |
| `aspect_ratio` | COMBO | 是 | `"16:9"`<br>`"9:16"`<br>`"1:1"` | 要生成的影片形狀或尺寸比例。 |
| `duration` | COMBO | 是 | `5`<br>`10` | 影片的長度，單位為秒。 |
| `resolution` | COMBO | 否 | `"1080p"`<br>`"720p"` | 影片的品質或像素解析度（預設值：`"1080p"`）。 |

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `output` | VIDEO | 根據提供的文字提示所生成的影片。 |
