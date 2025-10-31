> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceTextToVideoNode/zh-TW.md)

ByteDance Text to Video 節點透過 API 使用 ByteDance 模型，根據文字提示生成影片。它接收文字描述和各種影片設定作為輸入，然後創建符合提供規格的影片。該節點負責處理 API 通訊，並將生成的影片作為輸出返回。

## 輸入參數

| 參數名稱 | 資料類型 | 輸入類型 | 預設值 | 數值範圍 | 描述 |
|-----------|-----------|------------|---------|-------|-------------|
| `model` | STRING | 下拉選單 | seedance_1_pro | Text2VideoModelName 選項 | 模型名稱 |
| `prompt` | STRING | 字串 | - | - | 用於生成影片的文字提示。 |
| `resolution` | STRING | 下拉選單 | - | ["480p", "720p", "1080p"] | 輸出影片的解析度。 |
| `aspect_ratio` | STRING | 下拉選單 | - | ["16:9", "4:3", "1:1", "3:4", "9:16", "21:9"] | 輸出影片的長寬比。 |
| `duration` | INT | 整數 | 5 | 3-12 | 輸出影片的持續時間（單位：秒）。 |
| `seed` | INT | 整數 | 0 | 0-2147483647 | 用於生成的種子值。（可選） |
| `camera_fixed` | BOOLEAN | 布林值 | False | - | 指定是否固定攝影機。平台會將固定攝影機的指令附加到您的提示詞中，但不保證實際效果。（可選） |
| `watermark` | BOOLEAN | 布林值 | True | - | 是否在影片中添加「AI 生成」浮水印。（可選） |

**參數限制：**

- `prompt` 參數在移除空白字元後必須至少包含 1 個字元
- `prompt` 參數不能包含以下文字參數："resolution"、"ratio"、"duration"、"seed"、"camerafixed"、"watermark"
- `duration` 參數限制在 3 到 12 秒之間的值
- `seed` 參數接受從 0 到 2,147,483,647 的值

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `output` | VIDEO | 生成的影片檔案 |