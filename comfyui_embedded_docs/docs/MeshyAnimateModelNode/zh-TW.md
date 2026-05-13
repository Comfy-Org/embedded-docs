> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyAnimateModelNode/zh-TW.md)

此節點將特定的動畫套用至已使用 Meshy 服務完成骨架綁定的 3D 角色模型。它接收先前骨架綁定操作的任務 ID，以及從動畫庫中選取所需動畫的動作 ID。接著，節點會處理請求，並以 GLB 和 FBX 兩種檔案格式回傳動畫模型。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `rig_task_id` | STRING | 是 | 不適用 | 先前完成的 Meshy 角色骨架綁定操作的唯一任務 ID。 |
| `action_id` | INT | 是 | 0 至 696 | 要套用的動畫動作 ID 編號。請造訪 <https://docs.meshy.ai/en/api/animation-library> 以取得可用值清單。（預設值：0） |

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `model_file` | STRING | 動畫模型的字串識別碼。此輸出僅為向下相容性而提供。 |
| `GLB` | FILE3DGLB | GLB 格式的動畫 3D 模型檔案。 |
| `FBX` | FILE3DFBX | FBX 格式的動畫 3D 模型檔案。 |

---
**Source fingerprint (SHA-256):** `3b7610b5f6f763dde86a52f9212b3fc98f41e54bda30097fcb8f5f0bd020899e`
