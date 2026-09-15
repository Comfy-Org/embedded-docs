# Meshy：骨架綁定模型

Meshy: Rig Model 節點會取得先前 Meshy 任務中的 3D 模型，並自動為其建立骨架，產生可擺姿勢與製作動畫的已綁定骨骼角色。此節點會以 GLB 與 FBX 兩種檔案格式輸出已綁定骨骼的模型。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `meshy_task_id` | 來自先前 Meshy 操作的唯一任務 ID（例如文字轉 3D 或圖像轉 3D），該操作產生了要綁定骨骼的模型。 | MESHY_TASK_ID | 是 | N/A |
| `height_meters` | 角色模型的大約高度，以公尺為單位。這有助於提升縮放與骨骼綁定的準確度（預設值：1.7）。 | FLOAT | 是 | 0.1 至 15.0 |
| `texture_image` | 模型的 UV 展開基礎色紋理影像。 | IMAGE | 否 | N/A |

**注意：** 自動骨骼綁定程序目前不適合未貼紋理的網格、非人形資產，或肢體與身體結構不明確的人形資產。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `model_file` | 僅為了向後相容而保留的舊版輸出，包含 GLB 模型的檔案名稱。 | STRING |
| `rig_task_id` | 此骨骼綁定操作的唯一任務 ID，可用於在後續 Meshy 節點中參照結果。 | MESHY_RIGGED_TASK_ID |
| `GLB` | 以 GLB 檔案格式儲存的已綁定骨骼 3D 角色模型。 | FILE3DGLB |
| `FBX` | 以 FBX 檔案格式儲存的已綁定骨骼 3D 角色模型。 | FILE3DFBX |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyRigModelNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `6ae79359fa54f36dd2491a952fe54fa56866038758e8cd475a2d2f8e9e47e3b3`
