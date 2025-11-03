> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftRemoveBackgroundNode/zh-TW.md)

此節點使用 Recraft API 服務來移除圖像背景。它會處理輸入批次中的每個圖像，並返回具有透明背景的處理後圖像，以及標示已移除背景區域的對應 Alpha 遮罩。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | 是 | - | 要進行背景移除處理的輸入圖像 |
| `auth_token` | STRING | 否 | - | 用於 Recraft API 存取的身份驗證令牌 |
| `comfy_api_key` | STRING | 否 | - | 用於 Comfy.org 服務整合的 API 金鑰 |

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `image` | IMAGE | 具有透明背景的處理後圖像 |
| `mask` | MASK | 標示已移除背景區域的 Alpha 通道遮罩 |