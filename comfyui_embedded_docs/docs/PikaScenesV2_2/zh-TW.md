PikaScenes v2.2 節點結合多張圖片，以建立一個包含所有輸入圖片中物件的影片。您可以上傳最多五張不同的圖片作為素材，並生成將它們無縫融合在一起的高品質影片。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `prompt_text` | 要生成內容的文字描述 | STRING | 是 | - |
| `negative_prompt` | 在生成中要避免的內容的文字描述 | STRING | 是 | - |
| `seed` | 用於生成的隨機種子值 | INT | 是 | - |
| `resolution` | 影片的輸出解析度 | STRING | 是 | - |
| `duration` | 生成影片的持續時間 | INT | 是 | - |
| `ingredients_mode` | 結合素材的模式（預設值："creative"） | STRING | 否 | "creative"<br>"precise" |
| `aspect_ratio` | 寬高比（寬度 / 高度）（預設值：1.778） | FLOAT | 否 | 0.4 - 2.5 |
| `image_ingredient_1` | 將用作素材以建立影片的圖片 | IMAGE | 否 | - |
| `image_ingredient_2` | 將用作素材以建立影片的圖片 | IMAGE | 否 | - |
| `image_ingredient_3` | 將用作素材以建立影片的圖片 | IMAGE | 否 | - |
| `image_ingredient_4` | 將用作素材以建立影片的圖片 | IMAGE | 否 | - |
| `image_ingredient_5` | 將用作素材以建立影片的圖片 | IMAGE | 否 | - |

**注意：** 您最多可以提供 5 個圖片素材，但至少需要一張圖片才能生成影片。該節點將使用所有提供的圖片來建立最終的影片合成。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `output` | 結合所有輸入圖片後生成的影片 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PikaScenesV2_2/zh-TW.md)

---
**Source fingerprint (SHA-256):** `dda8f10a58527c2b9037744f59f30821cdde37ad23427b856ba5e699a05acafd`
