# Tripo: Smart UV

Tripo: Smart UV 會重新展開模型的 UV，並將其紋理、骨架和動畫重新對應到新的配置。當模型的原始 UV 配置無法使用時（例如重新拓撲後，或需要重做紋理接縫時），即可使用此節點。輸入模型不得超過 80,000 個三角形（一個四邊形算作兩個），因此較大的模型請先使用 Tripo: Retopology 或 `face_limit` 進行簡化。

> **注意：** Tripo 會在其伺服器上保留任務記錄 7 天（自 2026 年 12 月 1 日起生效）。超過該期限的任務 ID 將無法再解析，因此在期限過後重新執行已儲存的工作流程時，此節點會失敗。請重新執行產生該任務的上游 Tripo 節點，或使用 **Tripo: Import Model** 重新匯入已下載的模型。請在期限結束前下載模型：過期的資產無法從任務記錄中復原。

## 輸入

| 參數 | 描述 | 資料類型 | 是否必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model_task_id` | 要重新展開 UV 的模型任務 ID。可接受來自 Tripo 生成節點的模型任務 ID，或骨架、重定向或分割任務 ID。 | MODEL_TASK_ID | 是 | Tripo 任務 ID |
| `烘焙` | 將現有紋理烘焙到新的 UV 配置上。關閉時會略過烘焙，並傳回不含顏色紋理的模型（預設：True）。 | BOOLEAN | 是 | `True`<br>`False` |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `model task_id` | 完成的 UV 任務的任務 ID。可傳遞給其他 Tripo 節點，例如 Tripo: Texture。 | MODEL_TASK_ID |
| `GLB` | 以 GLB 格式重新展開 UV 的模型。當來源模型為 FBX 時為空。 | FILE_3D_GLB |
| `FBX` | 以 FBX 格式重新展開 UV 的模型。僅當來源模型為 FBX（例如四邊形網格）時才有內容。 | FILE_3D_FBX |
| `UV atlas` | 模型渲染後的 UV 配置圖像。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoSmartUVNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `55c9352c7c8129fa7a4f99f803bdc6db112830454e7d9566fa734063cb283532`
