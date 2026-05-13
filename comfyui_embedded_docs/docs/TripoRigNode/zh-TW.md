> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoRigNode/zh-TW.md)

TripoRigNode 會根據原始模型任務 ID 生成一個已綁定骨架的 3D 模型。它會向 Tripo API 發送請求，以 Tripo 規範建立 GLB 格式的動畫骨架，然後持續輪詢 API，直到骨架生成任務完成。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `original_model_task_id` | MODEL_TASK_ID | 是 | - | 要綁定骨架的原始 3D 模型任務 ID |
| `auth_token` | AUTH_TOKEN_COMFY_ORG | 否 | - | 用於存取 Comfy.org API 的驗證令牌 |
| `comfy_api_key` | API_KEY_COMFY_ORG | 否 | - | 用於 Comfy.org 服務驗證的 API 金鑰 |
| `unique_id` | UNIQUE_ID | 否 | - | 用於追蹤操作流程的唯一識別碼 |

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `model_file` | STRING | 生成的已綁定骨架 3D 模型檔案（為保持向下相容性而保留） |
| `rig task_id` | RIG_TASK_ID | 用於追蹤骨架生成流程的任務 ID |
| `GLB` | FILE3DGLB | 以 GLB 格式生成的已綁定骨架 3D 模型 |

---
**Source fingerprint (SHA-256):** `621a4d08f3b8a349c3afff3dbf888b20d524eb3337685769b7a7badcb28986e4`
