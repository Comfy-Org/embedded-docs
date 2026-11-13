# Tripo：分割模型

此節點會將 3D 模型分割成個別部件。它會將模型傳送至 Tripo 分割服務，等待作業完成，並以 GLB 格式回傳分割後的模型，同時附上以逗號分隔的部件名稱清單。這些部件名稱會提供給下游步驟使用，例如 Tripo: Complete Mesh Parts、Tripo: Retopology 與 Tripo: Convert model。

<Note>
Tripo 僅在其伺服器上保留任務紀錄 7 天（自 2026年12月1日起生效）。超過此期限的任務 ID 將無法再解析，因此在該期限之後重新執行已儲存的工作流程時，會在此節點失敗。若要繼續，請重新執行先前的 Tripo 節點以建立新的任務 ID，或使用 **Tripo：匯入模型** 重新匯入您已下載的模型。
</Note>

## 輸入

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `model_task_id` | 要分割成部件的 3D 模型任務 ID。 | MODEL_TASK_ID | 是 | N/A |

## 輸出

| Output Name | Description | Data Type |
|-------------|-------------|-----------|
| `model_file` | 分割後 GLB 模型的輸出檔案名稱，格式為 `<task_id>.glb`。僅為向後相容而保留。 | STRING |
| `segment task_id` | 產生該結果之分割作業的任務 ID。 | SEGMENT_TASK_ID |
| `GLB` | 分割後的 3D 模型，以 GLB 檔案形式呈現。 | GLB |
| `part_names` | 以逗號分隔的部件名稱。 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoSegmentNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `3218f87bfdc347d58b639cbe57b01cf7625c95c753bf381e35b4a28376eeb0e8`
