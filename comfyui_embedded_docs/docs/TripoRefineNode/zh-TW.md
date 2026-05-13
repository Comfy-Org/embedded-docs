> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoRefineNode/zh-TW.md)

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `model_task_id` | MODEL_TASK_ID | 是 | - | 必須是 v1.4 Tripo 模型 |

**注意：** 此節點僅接受由 Tripo v1.4 模型建立的草稿模型。使用其他版本的模型可能會導致錯誤。

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `模型任務 ID` | STRING | 精煉後模型的檔案路徑或參考（僅為向後相容性保留） |
| `GLB` | MODEL_TASK_ID | 精煉模型操作的任務識別碼 |
| `GLB` | FILE3DGLB | 精煉後的 GLB 格式 3D 模型 |

---
**Source fingerprint (SHA-256):** `136093c7cdd7eb33b55e862f4b8c0554de7bde656a7e0139efb63323ad041c32`
