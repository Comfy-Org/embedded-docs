> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceImageToVideoNode/zh-TW.md)

ByteDance Image to Video 節點透過 API 使用 ByteDance 模型，根據輸入圖像和文字提示生成影片。它接收一個起始圖像幀，並根據提供的描述創建影片序列。該節點提供多種自訂選項，包括影片解析度、長寬比、時長和其他生成參數。

## 輸入參數

| 參數名稱 | 資料類型 | 輸入類型 | 預設值 | 數值範圍 | 描述 |
|-----------|-----------|------------|---------|-------|-------------|
| `model` | STRING | COMBO | seedance_1_pro | Image2VideoModelName 選項 | 模型名稱 |
| `prompt` | STRING | STRING | - | - | 用於生成影片的文字提示。 |
| `image` | IMAGE | IMAGE | - | - | 用於影片生成的起始圖像幀。 |
| `resolution` | STRING | COMBO | - | ["480p", "720p", "1080p"] | 輸出影片的解析度。 |
| `aspect_ratio` | STRING | COMBO | - | ["adaptive", "16:9", "4:3", "1:1", "3:4", "9:16", "21:9"] | 輸出影片的長寬比。 |
| `duration` | INT | INT | 5 | 3-12 | 輸出影片的時長（單位：秒）。 |
| `seed` | INT | INT | 0 | 0-2147483647 | 用於生成的隨機種子。 |
| `camera_fixed` | BOOLEAN | BOOLEAN | False | - | 指定是否固定攝影機視角。平台會在您的提示詞後附加固定攝影機的指令，但不保證實際效果。 |
| `watermark` | BOOLEAN | BOOLEAN | True | - | 是否在影片中添加「AI 生成」浮水印。 |

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `output` | VIDEO | 根據輸入圖像和提示參數生成的影片檔案。 |