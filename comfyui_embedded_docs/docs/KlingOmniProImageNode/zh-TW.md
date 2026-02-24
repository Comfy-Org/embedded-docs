> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingOmniProImageNode/zh-TW.md)

Kling Omni Image (Pro) 節點使用 Kling AI 模型生成或編輯圖像。它根據文字描述創建圖像，並允許您提供參考圖像來引導風格或內容。該節點會向外部 API 發送請求，由 API 處理任務並返回最終圖像。

## 輸入參數

| 參數 | 資料類型 | 必填 | 範圍 | 描述 |
| :--- | :--- | :--- | :--- | :--- |
| `model_name` | COMBO | 是 | `"kling-image-o1"` | 用於圖像生成的特定 Kling AI 模型。 |
| `prompt` | STRING | 是 | - | 描述圖像內容的文字提示。可以包含正向和負向描述。文字長度必須在 1 到 2500 個字元之間。 |
| `resolution` | COMBO | 是 | `"1K"`<br>`"2K"` | 生成圖像的目標解析度。 |
| `aspect_ratio` | COMBO | 是 | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"`<br>`"3:2"`<br>`"2:3"`<br>`"21:9"` | 生成圖像所需的寬高比。 |
| `reference_images` | IMAGE | 否 | - | 最多 10 張額外的參考圖像。每張圖像的寬度和高度都必須至少為 300 像素，且其寬高比必須在 1:2.5 到 2.5:1 之間。 |

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
| :--- | :--- | :--- |
| `image` | IMAGE | 由 Kling AI 模型生成或編輯的最終圖像。 |
