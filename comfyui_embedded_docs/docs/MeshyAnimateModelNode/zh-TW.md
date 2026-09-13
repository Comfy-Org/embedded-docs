# Meshy：動畫模型

此節點會使用 Meshy 服務，將特定的動畫動作套用到先前已綁定的 3D 角色。它會接收來自先前綁定操作的任務 ID，以及用於從資源庫中選擇所需動畫的動作 ID，然後以 GLB 和 FBX 兩種檔案格式傳回帶有動畫的模型。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `rig_task_id` | 來自先前已完成之 Meshy 角色綁定操作的唯一任務 ID。 | MESHY_RIGGED_TASK_ID | 是 | N/A |
| `action_id` | 要套用的動畫動作 ID 編號。請前往 https://docs.meshy.ai/en/api/animation-library 查看可用值清單。（預設值：0） | INT | 是 | 0 至 696 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `model_file` | 帶有動畫之模型的字串識別碼。此輸出僅為向後相容性而提供。 | STRING |
| `GLB` | GLB 格式的動畫 3D 模型檔案。 | FILE3DGLB |
| `FBX` | FBX 格式的動畫 3D 模型檔案。 | FILE3DFBX |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyAnimateModelNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `760e94d3a92910051d9b473545191842dc9672e6c4a59c3d1cd9cfdc5eb2589d`
