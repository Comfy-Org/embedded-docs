> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingOmniProFirstLastFrameNode/zh-TW.md)

此節點使用 Kling AI 模型來生成影片。它需要一張起始圖片和一段文字提示。您可以選擇性地提供一張結束圖片或最多六張參考圖片，以引導影片的內容和風格。該節點處理這些輸入，以創建指定時長和解析度的影片。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `model_name` | COMBO | 是 | `"kling-video-o1"` | 用於影片生成的特定 Kling AI 模型。 |
| `prompt` | STRING | 是 | - | 描述影片內容的文字提示。可以包含正面和負面的描述。 |
| `duration` | INT | 是 | 3 到 10 | 生成影片的期望長度，單位為秒（預設值：5）。 |
| `first_frame` | IMAGE | 是 | - | 影片序列的起始圖片。 |
| `end_frame` | IMAGE | 否 | - | 影片的可選結束畫面。此參數不能與 `reference_images` 同時使用。 |
| `reference_images` | IMAGE | 否 | - | 最多 6 張額外的參考圖片。 |
| `resolution` | COMBO | 否 | `"1080p"`<br>`"720p"` | 生成影片的輸出解析度（預設值："1080p"）。 |

**重要限制：**

* `end_frame` 輸入不能與 `reference_images` 輸入同時使用。
* 如果您沒有提供 `end_frame` 或任何 `reference_images`，則 `duration` 只能設定為 5 或 10 秒。
* 所有輸入圖片（`first_frame`、`end_frame` 以及任何 `reference_images`）的寬度和高度都必須至少為 300 像素。
* 所有輸入圖片的長寬比必須在 1:2.5 到 2.5:1 之間。
* 透過 `reference_images` 輸入最多可提供 6 張圖片。
* `prompt` 文字的長度必須在 1 到 2500 個字元之間。

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `output` | VIDEO | 生成的影片檔案。 |
