> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingOmniProVideoToVideoNode/zh-TW.md)

此節點使用 Kling AI 模型，根據輸入影片和可選的參考圖像生成新的影片。您提供描述所需內容的文字提示，節點會據此轉換參考影片。它還可以整合最多四張額外的參考圖像，以引導輸出的風格和內容。

## 輸入參數

| 參數 | 資料類型 | 必填 | 範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `model_name` | COMBO | 是 | `"kling-video-o1"` | 用於影片生成的特定 Kling 模型。 |
| `prompt` | STRING | 是 | N/A | 描述影片內容的文字提示。可以包含正面和負面的描述。 |
| `aspect_ratio` | COMBO | 是 | `"16:9"`<br>`"9:16"`<br>`"1:1"` | 生成影片所需的長寬比。 |
| `duration` | INT | 是 | 3 到 10 | 生成影片的長度（單位：秒，預設值：3）。 |
| `reference_video` | VIDEO | 是 | N/A | 用作參考的影片。 |
| `keep_original_sound` | BOOLEAN | 是 | N/A | 決定輸出是否保留參考影片的音訊（預設值：True）。 |
| `reference_images` | IMAGE | 否 | N/A | 最多 4 張額外的參考圖像。 |
| `resolution` | COMBO | 否 | `"1080p"`<br>`"720p"` | 生成影片的解析度（預設值："1080p"）。 |

**參數限制：**

* `prompt` 的長度必須在 1 到 2500 個字元之間。
* `reference_video` 的持續時間必須在 3.0 到 10.05 秒之間。
* `reference_video` 的尺寸必須在 720x720 到 2160x2160 像素之間。
* 最多可提供 4 張 `reference_images`。每張圖像必須至少為 300x300 像素，且長寬比在 1:2.5 到 2.5:1 之間。

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `output` | VIDEO | 新生成的影片。 |
