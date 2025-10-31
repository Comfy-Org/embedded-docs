> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceImageReferenceNode/zh-TW.md)

ByteDance Image Reference 節點使用文字提示和一至四張參考圖片來生成影片。它會將圖片和提示發送到外部 API 服務，該服務會建立符合您描述的影片，同時融入參考圖片的視覺風格和內容。該節點提供多種控制項，用於調整影片解析度、長寬比、持續時間和其他生成參數。

## 輸入參數

| 參數名稱 | 資料類型 | 輸入類型 | 預設值 | 範圍 | 描述 |
|-----------|-----------|------------|---------|-------|-------------|
| `model` | MODEL | COMBO | seedance_1_lite | seedance_1_lite | 模型名稱 |
| `prompt` | STRING | STRING | - | - | 用於生成影片的文字提示。 |
| `images` | IMAGE | IMAGE | - | - | 一至四張圖片。 |
| `resolution` | STRING | COMBO | - | 480p, 720p | 輸出影片的解析度。 |
| `aspect_ratio` | STRING | COMBO | - | adaptive, 16:9, 4:3, 1:1, 3:4, 9:16, 21:9 | 輸出影片的長寬比。 |
| `duration` | INT | INT | 5 | 3-12 | 輸出影片的持續時間（單位：秒）。 |
| `seed` | INT | INT | 0 | 0-2147483647 | 用於生成的種子值。 |
| `watermark` | BOOLEAN | BOOLEAN | True | - | 是否在影片上添加「AI 生成」浮水印。 |

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `output` | VIDEO | 根據輸入提示和參考圖片生成的影片檔案。 |