> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PhotoMakerLoader/zh-TW.md)

PhotoMakerLoader 節點會從可用的模型檔案中載入 PhotoMaker 模型。它會讀取指定的模型檔案，並準備好用於基於身份識別的影像生成任務的 PhotoMaker ID 編碼器。此節點標記為實驗性，僅供測試用途。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 參數說明 |
|-----------|-----------|----------|-------|-------------|
| `photomaker_model_name` | STRING | 是 | 提供多個選項 | 要載入的 PhotoMaker 模型檔案名稱。可用選項由 photomaker 資料夾中的模型檔案決定。 |

## 輸出結果

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `photomaker_model` | PHOTOMAKER | 已載入的 PhotoMaker 模型，包含 ID 編碼器，準備用於身份編碼操作。 |