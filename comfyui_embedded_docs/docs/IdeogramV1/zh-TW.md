> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramV1/zh-TW.md)

IdeogramV1 節點透過 API 使用 Ideogram V1 模型生成圖像。它接收文字提示和各種生成設定，根據您的輸入創建一個或多個圖像。該節點支援不同的長寬比和生成模式，以自訂輸出結果。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | 是 | - | 用於圖像生成的提示詞（預設值：空） |
| `turbo` | BOOLEAN | 是 | - | 是否使用加速模式（生成速度更快，可能降低品質）（預設值：False） |
| `aspect_ratio` | COMBO | 否 | "1:1"<br>"16:9"<br>"9:16"<br>"4:3"<br>"3:4"<br>"3:2"<br>"2:3" | 圖像生成的長寬比（預設值："1:1"） |
| `magic_prompt_option` | COMBO | 否 | "AUTO"<br>"ON"<br>"OFF" | 決定是否在生成過程中使用 MagicPrompt（預設值："AUTO"） |
| `seed` | INT | 否 | 0-2147483647 | 用於生成的隨機種子值（預設值：0） |
| `negative_prompt` | STRING | 否 | - | 描述圖像中應排除的內容（預設值：空） |
| `num_images` | INT | 否 | 1-8 | 要生成的圖像數量（預設值：1） |

**注意：** `num_images` 參數在每次生成請求中最多限制為 8 張圖像。

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `output` | IMAGE | 來自 Ideogram V1 模型生成的圖像 |