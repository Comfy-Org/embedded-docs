# Meshy: Text to Model (Smart Topology)

此節點使用 Meshy T2.5 以目標面數生成可直接用於遊戲的三角網格。拓撲會依要求的多邊形數量直接建構，而不是在生成後再進行減面，因此結果可直接用於遊戲引擎，無需另外執行重拓撲流程。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | 要用於生成的 Meshy 模型版本。 | COMBO | 是 | `"meshy-t2.5"` |
| `prompt` | 要生成的 3D 模型的文字描述。 | STRING | 是 | 1 至 800 個字元 |
| `target_polycount` | 生成網格中三角形的近似數量。預設值：15000。 | INT | 是 | 100 至 30000 |
| `pose_mode` | 生成角色的姿勢。空字串表示不要求特定姿勢。此為進階設定。預設值：`""`（空字串）。 | COMBO | 是 | `""`<br>`"A-pose"`<br>`"T-pose"` |
| `seed` | `seed` 控制節點是否應重新執行；無論種子為何，結果都是不確定的。預設值：42。 | INT | 是 | 0 至 2147483647 |

**限制條件：**

* `prompt` 必須包含 1 到 800 個字元。
* `target_polycount` 是建構網格時所用的三角形數量，而不是生成後才套用的限制。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `meshy_task_id` | Meshy API 任務的唯一識別碼。 | MESHY_TASK_ID |
| `GLB` | 以 GLB 格式生成的 3D 模型。 | FILE3DGLB |
| `FBX` | 以 FBX 格式生成的 3D 模型。 | FILE3DFBX |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyTextToModelSmartTopologyNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `9fcdc846a4ba39cf3d099629637fbb0cf6d9c8d65bcee8aff5ec6ac5c76b6af3`
