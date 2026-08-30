# Meshy：多圖轉模型

此節點使用 Meshy API 從多張輸入影像產生 3D 模型。它會上傳提供的影像、提交處理任務，並回傳產生的 3D 模型檔案（GLB 與 FBX）以及任務 ID 以供參考。

## 輸入

### 通用輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 指定要使用的 AI 模型版本。 | COMBO | 是 | `"meshy-7"`<br>`"meshy-6"`<br>`"latest"` |
| `should_remesh` | 決定產生的網格是否進行處理。設為 `"false"` 時，節點會回傳未經處理的三角形網格；設為 `"true"` 時，會顯示下方的重新網格化設定。 | DYNAMIC_COMBO | 是 | `"true"`<br>`"false"` |
| `symmetry_mode` | 控制是否對產生的模型套用對稱。 | COMBO | 是 | `"auto"`<br>`"on"`<br>`"off"` |
| `should_texture` | 決定是否產生紋理。設為 `"false"` 時會跳過紋理階段，回傳不含紋理的網格；設為 `"true"` 時，會顯示下方的紋理設定。 | DYNAMIC_COMBO | 是 | `"true"`<br>`"false"` |
| `pose_mode` | 指定產生模型的姿勢模式。 | COMBO | 是 | `""`（空）<br>`"A-pose"`<br>`"T-pose"` |
| `seed` | `seed` 控制節點是否重新執行；無論 seed 為何，結果皆不具確定性。（預設值：0） | INT | 是 | 0 至 2147483647 |

### 重新網格化設定（當 `should_remesh` 為 `"true"` 時顯示）

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `topology` | 重新網格化輸出的目標多邊形類型。 | COMBO | 否 | `"triangle"`<br>`"quad"` |
| `target_polycount` | 重新網格化模型的目標多邊形數量（預設值：300000）。 | INT | 否 | 100 至 300000 |

### 紋理設定（當 `should_texture` 為 `"true"` 時顯示）

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `enable_pbr` | 除了基礎色彩外，還會產生 PBR 貼圖（金屬度、粗糙度、法線）。（預設值：False） | BOOLEAN | 否 | True / False |
| `texture_prompt` | 提供文字提示以引導紋理生成過程。最多 600 個字元。無法與 `texture_image` 同時使用。（預設值：空） | STRING | 否 | 最多 600 個字元 |
| `texture_image` | 同一時間只能使用 `texture_image` 或 `texture_prompt` 其中一個。 | IMAGE | 否 | - |
| `texture_resolution` | 基礎色彩紋理的解析度。較高的解析度能捕捉更多表面細節。 | COMBO | 否 | `"2k"`<br>`"4k"`<br>`"8k"` |

### 影像輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `images` | 可擴充插槽：連接 2 至 4 張輸入影像（`image_1`、`image_2`、`image_3`、`image_4`）。這些影像用於產生 3D 模型。 | IMAGE | 是 | 2 至 4 張影像 |

**注意事項**

* `images` 輸入必須提供 2 至 4 張影像。
* `topology` 和 `target_polycount` 參數僅在 `should_remesh` 設為 `"true"` 時啟用。
* `enable_pbr`、`texture_prompt`、`texture_image` 和 `texture_resolution` 參數僅在 `should_texture` 設為 `"true"` 時啟用。
* `texture_prompt` 和 `texture_image` 互斥；兩者無法同時使用。`texture_prompt` 限制為 600 個字元。
* `seed` 值不會使結果具有確定性；變更 seed 只是讓節點重新執行生成任務。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `模型檔案` | 所產生 GLB 模型的檔案名稱。此輸出僅為回溯相容而提供。 | STRING |
| `meshy 任務 ID` | Meshy API 任務的唯一識別碼。 | MESHY_TASK_ID |
| `GLB` | 以 GLB 格式產生的 3D 模型。 | FILE3DGLB |
| `FBX` | 以 FBX 格式產生的 3D 模型。 | FILE3DFBX |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyMultiImageToModelNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `a8b2fc23ef8a8a4af097489c15beb3e0ed205dfdc8309afc95207d7a5616d37a`
