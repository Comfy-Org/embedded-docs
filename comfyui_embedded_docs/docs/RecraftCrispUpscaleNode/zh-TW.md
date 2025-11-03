> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftCrispUpscaleNode/zh-TW.md)

同步放大影像。使用「清晰放大」工具增強給定的點陣圖影像，提高影像解析度，使影像更清晰、更乾淨。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 參數說明 |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | 是 | - | 要進行放大的輸入影像 |
| `auth_token` | STRING | 否 | - | Recraft API 的驗證令牌 |
| `comfy_api_key` | STRING | 否 | - | Comfy.org 服務的 API 金鑰 |

## 輸出結果

| 輸出名稱 | 資料類型 | 輸出說明 |
|-------------|-----------|-------------|
| `image` | IMAGE | 經過放大並增強解析度和清晰度的影像 |