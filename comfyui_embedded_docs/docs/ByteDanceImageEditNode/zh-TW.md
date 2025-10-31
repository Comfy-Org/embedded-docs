> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceImageEditNode/zh-TW.md)

ByteDance 圖像編輯節點允許您透過 API 使用 ByteDance 的 AI 模型來修改圖像。您提供輸入圖像和描述所需更改的文字提示，該節點會根據您的指示處理圖像。此節點會自動處理 API 通訊並返回編輯後的圖像。

## 輸入參數

| 參數名稱 | 資料類型 | 輸入類型 | 預設值 | 數值範圍 | 參數說明 |
|-----------|-----------|------------|---------|-------|-------------|
| `model` | MODEL | COMBO | seededit_3 | Image2ImageModelName 選項 | 模型名稱 |
| `image` | IMAGE | IMAGE | - | - | 要編輯的基礎圖像 |
| `prompt` | STRING | STRING | "" | - | 編輯圖像的指令 |
| `seed` | INT | INT | 0 | 0-2147483647 | 用於生成的種子值 |
| `guidance_scale` | FLOAT | FLOAT | 5.5 | 1.0-10.0 | 數值越高，圖像越緊密遵循提示 |
| `watermark` | BOOLEAN | BOOLEAN | True | - | 是否在圖像上添加「AI 生成」浮水印 |

## 輸出結果

| 輸出名稱 | 資料類型 | 輸出說明 |
|-------------|-----------|-------------|
| `IMAGE` | IMAGE | 從 ByteDance API 返回的編輯後圖像 |