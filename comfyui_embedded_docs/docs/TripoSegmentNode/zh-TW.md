# TripoSegmentNode

此節點會將 3D 模型分割成獨立部件。它會將模型發送到 Tripo 分割服務，等待作業完成，然後以 GLB 格式傳回分割後的模型，並附上以逗號分隔的部件名稱清單。這些部件名稱會饋送至下游步驟，例如 Tripo：完整網格部件、Tripo：重拓撲及 Tripo：轉換模型。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model_task_id` | 要分割成部件之 3D 模型的任務 ID。 | MODEL_TASK_ID | 是 | N/A |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `model_file` | 分割後 GLB 模型的輸出檔名。僅為保持向後相容性而保留。 | STRING |
| `segment task_id` | 產生此結果之分割作業的任務 ID。 | SEGMENT_TASK_ID |
| `GLB` | 分割後的 3D 模型，格式為 GLB 檔案。 | GLB |
| `part_names` | 以逗號分隔的部件名稱。 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoSegmentNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `d27580a7f2118e76cecff5e1d682c7605f966bf657d7a02b2d2ddf764d9b72d0`
