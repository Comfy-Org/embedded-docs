# Meshy：骨架綁定模型節點

Meshy：骨架綁定模型節點會從先前的 Meshy 任務中獲取 3D 模型，並自動為其建立骨架，產生一個可進行姿勢調整和動畫製作的綁定角色。此節點會以 GLB 和 FBX 兩種檔案格式輸出綁定後的模型。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `meshy_task_id` | 先前 Meshy 操作（例如文字轉 3D 或圖片轉 3D）所產生的唯一任務 ID，用於指定要進行骨架綁定的模型。 | STRING | 是 | 不適用 |
| `height_meters` | 角色模型的近似高度（單位：公尺）。這有助於提高縮放和骨架綁定的準確性（預設值：1.7）。 | FLOAT | 是 | 0.1 至 15.0 |
| `texture_image` | 模型的 UV 展開基礎顏色紋理圖片。 | IMAGE | 否 | 不適用 |

**注意：** 自動骨架綁定流程目前不適用於無紋理網格、非人形資產，或四肢與身體結構不明確的人形資產。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `rig 任務 ID` | 為向後相容性保留的舊版輸出，包含 GLB 模型的檔案名稱。 | STRING |
| `GLB` | 此骨架綁定操作的唯一任務 ID，可用於引用結果。 | STRING |
| `FBX` | 以 GLB 檔案格式儲存的已綁定 3D 角色模型。 | FILE3DGLB |
| `FBX` | 以 FBX 檔案格式儲存的已綁定 3D 角色模型。 | FILE3DFBX |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyRigModelNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `91e06e3465d3d309d2267ae307ec5a704af3903b7a6d7fb6011217dd58a63973`
