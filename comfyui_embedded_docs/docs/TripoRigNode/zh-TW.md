> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoRigNode/zh-TW.md)

TripoRigNode 可根據原始模型任務 ID 生成帶有骨架綁定的 3D 模型。它會向 Tripo API 發送請求，使用 Tripo 規格建立 GLB 格式的動畫骨架，然後持續輪詢 API 直到骨架生成任務完成。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 參數說明 |
|-----------|-----------|----------|-------|-------------|
| `original_model_task_id` | MODEL_TASK_ID | 是 | - | 要進行骨架綁定的原始 3D 模型任務 ID |
| `auth_token` | AUTH_TOKEN_COMFY_ORG | 否 | - | 用於 Comfy.org API 存取的身份驗證令牌 |
| `comfy_api_key` | API_KEY_COMFY_ORG | 否 | - | 用於 Comfy.org 服務身份驗證的 API 金鑰 |
| `unique_id` | UNIQUE_ID | 否 | - | 用於追蹤操作的唯一識別碼 |

## 輸出結果

| 輸出名稱 | 資料類型 | 輸出說明 |
|-------------|-----------|-------------|
| `model_file` | STRING | 生成的帶有骨架綁定的 3D 模型檔案 |
| `rig task_id` | RIG_TASK_ID | 用於追蹤骨架生成過程的任務 ID |