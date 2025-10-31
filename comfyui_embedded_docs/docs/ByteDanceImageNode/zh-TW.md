> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceImageNode/zh-TW.md)

ByteDance Image 節點透過基於文字提示的 API，使用 ByteDance 模型來生成圖像。它允許您選擇不同的模型、指定圖像尺寸，並控制各種生成參數，如種子值和引導尺度。該節點會連接到 ByteDance 的圖像生成服務並返回創建的圖像。

## 輸入參數

| 參數名稱 | 資料類型 | 輸入類型 | 預設值 | 數值範圍 | 描述 |
|-----------|-----------|------------|---------|-------|-------------|
| `model` | MODEL | COMBO | seedream_3 | Text2ImageModelName 選項 | 模型名稱 |
| `prompt` | STRING | STRING | - | - | 用於生成圖像的文字提示 |
| `size_preset` | STRING | COMBO | - | RECOMMENDED_PRESETS 標籤 | 選擇推薦尺寸。選擇 Custom 以使用下方的寬度和高度 |
| `width` | INT | INT | 1024 | 512-2048 (間隔 64) | 圖像的自訂寬度。僅在 `size_preset` 設為 `Custom` 時生效 |
| `height` | INT | INT | 1024 | 512-2048 (間隔 64) | 圖像的自訂高度。僅在 `size_preset` 設為 `Custom` 時生效 |
| `seed` | INT | INT | 0 | 0-2147483647 (間隔 1) | 用於生成的種子值（可選） |
| `guidance_scale` | FLOAT | FLOAT | 2.5 | 1.0-10.0 (間隔 0.01) | 數值越高，圖像會更緊密地遵循提示（可選） |
| `watermark` | BOOLEAN | BOOLEAN | True | - | 是否在圖像上添加「AI 生成」浮水印（可選） |

## 輸出參數

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `IMAGE` | IMAGE | 從 ByteDance API 生成的圖像 |