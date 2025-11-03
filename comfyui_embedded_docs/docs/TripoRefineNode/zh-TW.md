> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoRefineNode/zh-TW.md)

TripoRefineNode 專門用於精煉由 v1.4 Tripo 模型創建的 3D 草稿模型。它接收一個模型任務 ID，並透過 Tripo API 進行處理，以生成模型的改進版本。此節點專門設計用於處理由 Tripo v1.4 模型產生的草稿模型。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `model_task_id` | MODEL_TASK_ID | 是 | - | 必須是 v1.4 Tripo 模型 |
| `auth_token` | AUTH_TOKEN_COMFY_ORG | 否 | - | 用於 Comfy.org API 的驗證令牌 |
| `comfy_api_key` | API_KEY_COMFY_ORG | 否 | - | 用於 Comfy.org 服務的 API 金鑰 |
| `unique_id` | UNIQUE_ID | 否 | - | 操作的唯一識別碼 |

**注意：** 此節點僅接受由 Tripo v1.4 模型創建的草稿模型。使用其他版本的模型可能會導致錯誤。

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `model_file` | STRING | 精煉後模型的檔案路徑或參考 |
| `model task_id` | MODEL_TASK_ID | 精煉模型操作的任務識別碼 |