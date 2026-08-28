# Meshy：多圖轉模型

此節點使用 Meshy API 從多張輸入影像產生 3D 模型。它會上傳提供的影像、提交處理任務，並傳回產生的 3D 模型檔案（GLB 和 FBX）以及任務 ID 供參考。

## 輸入

### 通用輸入

| 參數 | 描述 | 資料型別 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 指定要使用的 AI 模型版本。 | COMBO | 是 | `"latest"` |
| `should_remesh` | 決定是否處理生成的網格。當設為 `"false"` 時，節點會回傳未處理的三角形網格。當設為 `"true"` 時，會顯示下方的重新網格化設定。 | DYNAMIC_COMBO | 是 | `"true"`<br>`"false"` |
| `symmetry_mode` | 控制是否對生成的模型套用對稱。 | COMBO | 是 | `"auto"`<br>`"on"`<br>`"off"` |
| `should_texture` | 決定是否生成紋理。設為 `"false"` 時會跳過紋理階段，並回傳不含紋理的網格。設為 `"true"` 時，會顯示下方的紋理設定。 | DYNAMIC_COMBO | 是 | `"true"`<br>`"false"` |
| `pose_mode` | 指定生成模型的姿勢模式。 | COMBO | 是 | `""`（空）<br>`"A-pose"`<br>`"T-pose"` |
| `seed` | 種子值控制節點是否應重新執行；無論種子為何，結果都是非確定性的。（預設：0） | INT | 是 | 0 至 2147483647 |

### 重新網格化設定（當 `should_remesh` 設為 `"true"` 時顯示）

| 參數 | 描述 | 資料型別 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `topology` | 重新網格化輸出的目標多邊形類型。 | COMBO | 否 | `"triangle"`<br>`"quad"` |
| `target_polycount` | 重新網格化模型的目標多邊形數量（預設：300000）。 | INT | 否 | 100 至 300000 |

### 紋理設定（當 `should_texture` 設為 `"true"` 時顯示）

| 參數 | 描述 | 資料型別 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `enable_pbr` | 除了基礎顏色外，是否生成 PBR 貼圖（金屬度、粗糙度、法線）。（預設：False） | BOOLEAN | 否 | True / False |
| `texture_prompt` | 提供文字提示以引導紋理生成過程。最多 600 個字元。不能與 `texture_image` 同時使用。（預設：空） | STRING | 否 | - |
| `texture_image` | `texture_image` 和 `texture_prompt` 只能同時使用其中一個。 | IMAGE | 否 | - |

### 影像輸入

| 參數 | 描述 | 資料型別 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `images` | 可擴充插槽：連接 2 到 4 張輸入影像（`image_1`、`image_2`、`image_3`、`image_4`）。這些影像用於產生 3D 模型。 | IMAGE | 是 | 2 至 4 張影像 |

**注意事項**

* 您必須為 `images` 輸入提供 2 到 4 張影像。
* `topology` 和 `target_polycount` 參數只有在 `should_remesh` 設為 `"true"` 時才有效。
* `enable_pbr`、`texture_prompt` 和 `texture_image` 參數只有在 `should_texture` 設為 `"true"` 時才有效。
* `texture_prompt` 和 `texture_image` 互斥；您不能同時使用兩者。`texture_prompt` 限制為 600 個字元。
* `seed` 值不會使結果具有確定性；更改它只是導致節點重新執行生成任務。

## 輸出

| 輸出名稱 | 描述 | 資料型別 |
| --- | --- | --- |
| `模型檔案` | 生成的 GLB 模型的檔案名稱。此輸出僅為向後相容性而提供。 | STRING |
| `meshy 任務 ID` | Meshy API 任務的唯一識別碼。 | MESHY_TASK_ID |
| `GLB` | 以 GLB 格式生成的 3D 模型。 | FILE3DGLB |
| `FBX` | 以 FBX 格式生成的 3D 模型。 | FILE3DFBX |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyMultiImageToModelNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `c2282cad611bbbc8c0a618df6a68fcd9f6e3c29c6d08b2c96a117c29765d8a7a`
