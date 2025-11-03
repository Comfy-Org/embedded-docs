> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxProUltraImageNode/zh-TW.md)

使用 Flux Pro 1.1 Ultra 透過 API 根據提示詞和解析度生成圖像。此節點連接外部服務，根據您的文字描述和指定尺寸建立圖像。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 參數說明 |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | 是 | - | 用於圖像生成的提示詞（預設：空字串） |
| `prompt_upsampling` | BOOLEAN | 否 | - | 是否對提示詞進行上採樣處理。啟用時會自動修改提示詞以實現更具創意的生成，但結果具有不確定性（相同種子不會產生完全相同的結果）。（預設：False） |
| `seed` | INT | 否 | 0 到 18446744073709551615 | 用於建立雜訊的隨機種子。（預設：0） |
| `aspect_ratio` | STRING | 否 | - | 圖像的長寬比；必須介於 1:4 到 4:1 之間。（預設："16:9"） |
| `raw` | BOOLEAN | 否 | - | 設為 True 時，生成較少處理、更自然外觀的圖像。（預設：False） |
| `image_prompt` | IMAGE | 否 | - | 用於引導生成的可選參考圖像 |
| `image_prompt_strength` | FLOAT | 否 | 0.0 到 1.0 | 在提示詞和圖像提示之間的混合程度。（預設：0.1） |

**注意：** `aspect_ratio` 參數必須介於 1:4 到 4:1 之間。當提供 `image_prompt` 時，`image_prompt_strength` 將變為啟用狀態，並控制參考圖像對最終輸出的影響程度。

## 輸出結果

| 輸出名稱 | 資料類型 | 輸出說明 |
|-------------|-----------|-------------|
| `output_image` | IMAGE | 由 Flux Pro 1.1 Ultra 生成的圖像 |