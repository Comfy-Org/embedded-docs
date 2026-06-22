# Tripo: 骨架模型

TripoRigNode 會根據原始模型任務 ID 生成一個已綁定骨架的 3D 模型。它會向 Tripo API 發送請求，以 Tripo 規範建立 GLB 格式的動畫骨架，然後持續輪詢 API，直到骨架生成任務完成。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `原始模型任務ID` | 要綁定骨架的原始 3D 模型任務 ID | MODEL_TASK_ID | 是 | - |
| `auth_token` | 用於存取 Comfy.org API 的驗證令牌 | AUTH_TOKEN_COMFY_ORG | 否 | - |
| `comfy_api_key` | 用於 Comfy.org 服務驗證的 API 金鑰 | API_KEY_COMFY_ORG | 否 | - |
| `unique_id` | 用於追蹤操作流程的唯一識別碼 | UNIQUE_ID | 否 | - |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `綁定任務 ID` | 生成的已綁定骨架 3D 模型檔案（為保持向下相容性而保留） | STRING |
| `GLB` | 用於追蹤骨架生成流程的任務 ID | RIG_TASK_ID |
| `GLB` | 以 GLB 格式生成的已綁定骨架 3D 模型 | FILE3DGLB |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoRigNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `621a4d08f3b8a349c3afff3dbf888b20d524eb3337685769b7a7badcb28986e4`
