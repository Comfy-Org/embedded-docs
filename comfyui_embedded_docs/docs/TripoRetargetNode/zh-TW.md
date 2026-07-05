# Tripo: 重新定位骨架模型

TripoRetargetNode 透過重新定位動作資料，將預先定義的動畫應用於 3D 角色模型。它接收先前已綁定骨架的 3D 模型，並套用多種預設動畫之一，產生動畫化的 3D 模型檔案作為輸出。此節點與 Tripo API 通訊以處理動畫重新定位操作。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `original_model_task_id` | 要套用動畫的先前已處理綁定 3D 模型的任務 ID | RIG_TASK_ID | 是 | - |
| `animation` | 要套用於 3D 模型的動畫預設。選項包括人形動畫（待機、行走、跑步、潛水、攀爬、跳躍、揮砍、射擊、受傷、墜落、轉身）和生物動畫（四足行走、六足行走、八足行走、蛇形行進、水生行進）。 | STRING | 是 | "preset:idle"<br>"preset:walk"<br>"preset:run"<br>"preset:dive"<br>"preset:climb"<br>"preset:jump"<br>"preset:slash"<br>"preset:shoot"<br>"preset:hurt"<br>"preset:fall"<br>"preset:turn"<br>"preset:quadruped:walk"<br>"preset:hexapod:walk"<br>"preset:octopod:walk"<br>"preset:serpentine:march"<br>"preset:aquatic:march" |
| `auth_token_comfy_org` | 用於 Comfy.org API 存取的驗證令牌（隱藏參數） | AUTH_TOKEN_COMFY_ORG | 否 | - |
| `api_key_comfy_org` | 用於 Comfy.org 服務存取的 API 金鑰（隱藏參數） | API_KEY_COMFY_ORG | 否 | - |
| `unique_id` | 用於追蹤操作的唯一識別碼（隱藏參數） | UNIQUE_ID | 否 | - |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `模型檔案` | 產生的動畫化 3D 模型檔案（僅為向後相容性保留） | STRING |
| `重定向任務 ID` | 用於追蹤重新定位操作的任務 ID | RETARGET_TASK_ID |
| `GLB` | 以 GLB 格式輸出的動畫化 3D 模型 | FILE3DGLB |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoRetargetNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `304326afdc1fa3e8c3593f151f771f93520e061802c831838c58ebc401b9e9e2`
