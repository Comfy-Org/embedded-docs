# Meshy：骨架綁定模型

Meshy: Rig Model 節點會從先前的 Meshy 任務中取得 3D 模型，並自動為其建立骨架，產生可擺姿勢及動畫化的綁定角色。此節點會以 GLB 和 FBX 兩種檔案格式輸出綁定後的模型。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `meshy_task_id` | 先前 Meshy 操作（例如文字轉 3D 或影像轉 3D）所產生待綁定模型的唯一任務 ID。 | STRING | 是 | N/A |
| `height_meters` | 角色模型的近似高度（以公尺為單位）。這有助於比例縮放和綁定準確性（預設值：1.7）。 | FLOAT | 是 | 0.1 至 15.0 |
| `texture_image` | 模型的 UV 展開基礎顏色紋理影像。 | IMAGE | 否 | N/A |

**注意：** 自動綁定流程目前不適用於無紋理網格、非人形資產，或肢體與身體結構不明確的人形資產。

## 輸出

| 輸出名 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `模型檔案` | 向後相容的舊版輸出，包含 GLB 模型的檔案名稱。 | STRING |
| `rig 任務 ID` | 此綁定操作的唯一任務 ID，可用於參照結果。 | STRING |
| `GLB` | 以 GLB 檔案格式儲存的已綁定 3D 角色模型。 | FILE3DGLB |
| `FBX` | 以 FBX 檔案格式儲存的已綁定 3D 角色模型。 | FILE3DFBX |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyRigModelNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `6ae79359fa54f36dd2491a952fe54fa56866038758e8cd475a2d2f8e9e47e3b3`
