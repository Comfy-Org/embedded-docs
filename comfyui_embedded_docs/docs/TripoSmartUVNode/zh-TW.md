# Tripo: Smart UV

Tripo: Smart UV 會重新展開模型的 UV，並將其紋理、骨骼綁定與動畫重新映射到新的佈局上。當模型的原始 UV 佈局無法使用時（例如重新拓撲後，或需要重做紋理接縫時），可使用此節點。輸入模型不得超過 80,000 個三角形（一個四邊形算作兩個），因此請先使用 Tripo: Retopology 或 `face_limit` 縮減較大的模型。

> **備註：** Tripo 會在其伺服器上保留任務記錄 7 天（自 2026 年 12 月 1 日起生效）。超過該期限的任務 ID 將無法再解析，因此在該時間窗口之後重新執行已儲存的工作流程，會在此節點失敗。請再次執行先前的 Tripo 節點以建立新的任務 ID，或使用 **Tripo: Import Model** 重新匯入已下載的模型。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model_task_id` | 要重新展開 UV 的模型任務 ID。可接受來自 Tripo 生成節點的模型任務 ID，或骨骼綁定、重定向或分割任務 ID。 | MODEL_TASK_ID | 是 | Tripo 任務 ID |
| `bake` | 將現有紋理烘焙到新的 UV 佈局上。關閉時會跳過烘焙，並傳回不含色彩紋理的模型（預設：True）。 | BOOLEAN | 是 | `True`<br>`False` |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `model task_id` | 完成的 UV 任務的任務 ID。可傳遞給其他 Tripo 節點，例如 Tripo: Texture。 | MODEL_TASK_ID |
| `GLB` | 重新展開 UV 後的模型，GLB 格式。當來源模型為 FBX 時為空。 | GLB FILE |
| `FBX` | 重新展開 UV 後的模型，FBX 格式。僅當來源模型為 FBX（例如四邊形網格）時才有值。 | FBX FILE |
| `UV atlas` | 模型渲染後的 UV 佈局影像。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoSmartUVNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `55c9352c7c8129fa7a4f99f803bdc6db112830454e7d9566fa734063cb283532`
