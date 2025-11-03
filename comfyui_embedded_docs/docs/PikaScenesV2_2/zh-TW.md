> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PikaScenesV2_2/zh-TW.md)

PikaScenes v2.2 節點可將多張圖片組合起來，建立一個融合所有輸入圖片物件的影片。您最多可以上傳五張不同的圖片作為素材，並生成高品質的無縫融合影片。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `prompt_text` | STRING | 是 | - | 生成內容的文字描述 |
| `negative_prompt` | STRING | 是 | - | 生成過程中應避免內容的文字描述 |
| `seed` | INT | 是 | - | 用於生成的隨機種子值 |
| `resolution` | STRING | 是 | - | 影片的輸出解析度 |
| `duration` | INT | 是 | - | 生成影片的持續時間 |
| `ingredients_mode` | COMBO | 否 | "creative"<br>"precise" | 組合素材的模式（預設："creative"） |
| `aspect_ratio` | FLOAT | 否 | 0.4 - 2.5 | 寬高比（寬度 / 高度）（預設：1.778） |
| `image_ingredient_1` | IMAGE | 否 | - | 將用作影片製作素材的圖片 |
| `image_ingredient_2` | IMAGE | 否 | - | 將用作影片製作素材的圖片 |
| `image_ingredient_3` | IMAGE | 否 | - | 將用作影片製作素材的圖片 |
| `image_ingredient_4` | IMAGE | 否 | - | 將用作影片製作素材的圖片 |
| `image_ingredient_5` | IMAGE | 否 | - | 將用作影片製作素材的圖片 |

**注意：** 您最多可以提供 5 個圖片素材，但至少需要一張圖片才能生成影片。該節點將使用所有提供的圖片來建立最終的影片合成。

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `output` | VIDEO | 融合所有輸入圖片後生成的影片 |