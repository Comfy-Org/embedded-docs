> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoRetargetNode/zh-TW.md)

TripoRetargetNode 透過重新定向動作資料，將預先定義的動畫套用至 3D 角色模型。它接收先前處理過的 3D 模型並套用多種預設動畫之一，生成一個帶有動畫的 3D 模型檔案作為輸出。此節點會與 Tripo API 通訊以處理動畫重新定向操作。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 參數說明 |
|-----------|-----------|----------|-------|-------------|
| `original_model_task_id` | RIG_TASK_ID | 是 | - | 先前處理過、要套用動畫的 3D 模型之任務 ID |
| `animation` | STRING | 是 | "preset:idle"<br>"preset:walk"<br>"preset:climb"<br>"preset:jump"<br>"preset:slash"<br>"preset:shoot"<br>"preset:hurt"<br>"preset:fall"<br>"preset:turn" | 要套用至 3D 模型的預設動畫 |
| `auth_token` | AUTH_TOKEN_COMFY_ORG | 否 | - | 用於存取 Comfy.org API 的驗證權杖 |
| `comfy_api_key` | API_KEY_COMFY_ORG | 否 | - | 用於存取 Comfy.org 服務的 API 金鑰 |
| `unique_id` | UNIQUE_ID | 否 | - | 用於追蹤操作的唯一識別碼 |

## 輸出結果

| 輸出名稱 | 資料類型 | 輸出說明 |
|-------------|-----------|-------------|
| `model_file` | STRING | 已生成的帶有動畫的 3D 模型檔案 |
| `retarget task_id` | RETARGET_TASK_ID | 用於追蹤重新定向操作的任務 ID |