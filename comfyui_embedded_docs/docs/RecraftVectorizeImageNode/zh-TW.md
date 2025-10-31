> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftVectorizeImageNode/zh-TW.md)

從輸入圖像同步生成 SVG。此節點透過處理輸入批次中的每個圖像並將結果合併為單一 SVG 輸出，將點陣圖轉換為向量圖形格式。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `圖片` | IMAGE | 是 | - | 要轉換為 SVG 格式的輸入圖像 |
| `auth_token` | AUTH_TOKEN_COMFY_ORG | 否 | - | 用於 API 存取的驗證令牌 |
| `comfy_api_key` | API_KEY_COMFY_ORG | 否 | - | 用於 Comfy.org 服務的 API 金鑰 |

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `SVG` | SVG | 生成的向量圖形輸出，包含所有處理後的圖像 |