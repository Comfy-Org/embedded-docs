> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceFirstLastFrameNode/zh-TW.md)

此節點使用文字提示以及首尾幀圖像來生成影片。它會根據您的描述和兩個關鍵幀，創建一個完整的影片序列，在兩者之間進行過渡。該節點提供多種選項來控制影片的解析度、長寬比、持續時間和其他生成參數。

## 輸入參數

| 參數名稱 | 資料類型 | 輸入類型 | 預設值 | 數值範圍 | 描述 |
|-----------|-----------|------------|---------|-------|-------------|
| `model` | COMBO | 下拉選單 | seedance_1_lite | seedance_1_lite | 模型名稱 |
| `prompt` | STRING | 字串 | - | - | 用於生成影片的文字提示。 |
| `first_frame` | IMAGE | 圖片 | - | - | 用於影片的首幀圖像。 |
| `last_frame` | IMAGE | 圖片 | - | - | 用於影片的尾幀圖像。 |
| `resolution` | COMBO | 下拉選單 | - | 480p, 720p, 1080p | 輸出影片的解析度。 |
| `aspect_ratio` | COMBO | 下拉選單 | - | adaptive, 16:9, 4:3, 1:1, 3:4, 9:16, 21:9 | 輸出影片的長寬比。 |
| `duration` | INT | 滑桿 | 5 | 3-12 | 輸出影片的持續時間（單位：秒）。 |
| `seed` | INT | 數字 | 0 | 0-2147483647 | 用於生成的種子值。（可選） |
| `camera_fixed` | BOOLEAN | 布林值 | False | - | 指定是否固定攝影機。平台會將固定攝影機的指令附加到您的提示詞後，但不保證實際效果。（可選） |
| `watermark` | BOOLEAN | 布林值 | True | - | 是否在影片中添加「AI 生成」浮水印。（可選） |

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `output` | VIDEO | 生成的影片檔案 |