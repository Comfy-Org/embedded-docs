# Meshy：動畫模型

此節點使用 Meshy 服務，將特定的動畫動作套用至先前已綁定骨架的 3D 角色。它接收先前綁定操作的工作任務 ID，以及從動畫庫中選擇所需動畫的動作 ID，然後以 GLB 和 FBX 兩種檔案格式回傳動畫模型。

## 輸入

| 參數 | 描述 | 資料型別 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `rig_task_id` | 先前完成的 Meshy 角色綁定操作的唯一任務 ID。 | STRING | 是 | N/A |
| `action_id` | 要套用的動畫動作 ID 號碼。請參閱 https://docs.meshy.ai/en/api/animation-library 以取得可用值清單。（預設值：0） | INT | 是 | 0 至 696 |

## 輸出

| 輸出名 | 描述 | 資料型別 |
|-------------|-------------|-----------|
| `模型檔案` | 動畫模型的字串識別碼。此輸出僅為向後相容性提供。 | STRING |
| `GLB` | GLB 格式的動畫 3D 模型檔案。 | FILE3DGLB |
| `FBX` | FBX 格式的動畫 3D 模型檔案。 | FILE3DFBX |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyAnimateModelNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `760e94d3a92910051d9b473545191842dc9672e6c4a59c3d1cd9cfdc5eb2589d`
