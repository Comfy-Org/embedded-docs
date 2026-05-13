> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoRetargetNode/zh-TW.md)

# TripoRetargetNode

TripoRetargetNode 透過重新定位動作資料，將預先定義的動畫應用於 3D 角色模型。它接收先前已綁定骨架的 3D 模型，並套用多種預設動畫之一，產生動畫化的 3D 模型檔案作為輸出。此節點與 Tripo API 通訊以處理動畫重新定位操作。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `original_model_task_id` | RIG_TASK_ID | 是 | - | 要套用動畫的先前已處理綁定 3D 模型的任務 ID |
| `animation` | STRING | 是 | "preset:idle"<br>"preset:walk"<br>"preset:run"<br>"preset:dive"<br>"preset:climb"<br>"preset:jump"<br>"preset:slash"<br>"preset:shoot"<br>"preset:hurt"<br>"preset:fall"<br>"preset:turn"<br>"preset:quadruped:walk"<br>"preset:hexapod:walk"<br>"preset:octopod:walk"<br>"preset:serpentine:march"<br>"preset:aquatic:march" | 要套用於 3D 模型的動畫預設。選項包括人形動畫（待機、行走、跑步、潛水、攀爬、跳躍、揮砍、射擊、受傷、墜落、轉身）和生物動畫（四足行走、六足行走、八足行走、蛇形行進、水生行進）。 |
| `auth_token_comfy_org` | AUTH_TOKEN_COMFY_ORG | 否 | - | 用於 Comfy.org API 存取的驗證令牌（隱藏參數） |
| `api_key_comfy_org` | API_KEY_COMFY_ORG | 否 | - | 用於 Comfy.org 服務存取的 API 金鑰（隱藏參數） |
| `unique_id` | UNIQUE_ID | 否 | - | 用於追蹤操作的唯一識別碼（隱藏參數） |

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `model_file` | STRING | 產生的動畫化 3D 模型檔案（僅為向後相容性保留） |
| `retarget task_id` | RETARGET_TASK_ID | 用於追蹤重新定位操作的任務 ID |
| `GLB` | FILE3DGLB | 以 GLB 格式輸出的動畫化 3D 模型 |

---
**Source fingerprint (SHA-256):** `304326afdc1fa3e8c3593f151f771f93520e061802c831838c58ebc401b9e9e2`
