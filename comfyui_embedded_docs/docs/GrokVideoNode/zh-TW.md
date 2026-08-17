# Grok 影片

Grok Video 節點可根據文字描述生成短片。它可以使用提示詞從零開始建立影片，或將單一輸入圖片製成動畫，並可選擇以提示詞引導。此節點會向外部 API 傳送請求，並回傳生成的影片。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | 用於影片生成的模型。 | COMBO | 是 | "grok-imagine-video"<br>"grok-imagine-video-1.5" |
| `prompt` | 所需影片的文字描述。當提供輸入圖片時，對 grok-imagine-video-1.5 為可選。 | STRING | 是 | - |
| `resolution` | 輸出影片的解析度。1080p 僅適用於 grok-imagine-video-1.5。 | COMBO | 是 | "480p"<br>"720p"<br>"1080p" |
| `aspect_ratio` | 輸出影片的長寬比（預設值："auto"）。 | COMBO | 是 | "auto"<br>"16:9"<br>"4:3"<br>"3:2"<br>"1:1"<br>"2:3"<br>"3:4"<br>"9:16" |
| `duration` | 輸出影片的持續時間（秒）（預設值：6）。 | INT | 是 | 1 to 15 |
| `seed` | 用於決定節點是否重新執行的種子；無論種子值為何，實際結果都是非確定性的（預設值：0）。 | INT | 是 | 0 to 2147483647 |
| `image` | 可選的起始圖片。如果省略，則僅根據文字提示詞生成影片。 | IMAGE | 否 | - |

**注意：**
- 「1080p」解析度僅適用於 `grok-imagine-video-1.5` 模型。若搭配 `grok-imagine-video` 選用此解析度會引發錯誤。
- 僅支援單一輸入圖片。提供多張圖片會引發錯誤。
- 除非模型設定為 `grok-imagine-video-1.5` 且提供了輸入圖片，否則 `prompt` 為必填。當為必填時，提示詞在去除空白後至少需要 1 個字元。
- `seed` 僅決定節點是否重新執行；無論種子值為何，生成的結果都是非確定性的。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `output` | 生成的影片。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokVideoNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `c708c8cd78749aa533db63e2bc5938ef14fa78cf95f8ba4628d0c586f8723297`
