# Meshy：多圖轉模型

此節點使用 Meshy API 從多張輸入圖片生成 3D 模型。它會上傳提供的圖片、提交處理任務，並回傳生成的 3D 模型檔案（GLB 和 FBX）以及用於參考的任務 ID。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 指定要使用的 AI 模型版本。 | COMBO | 是 | `"latest"` |
| `images` | 用於生成 3D 模型的一組圖片。您必須提供 2 到 4 張圖片。 | IMAGE | 是 | 2 到 4 張圖片 |
| `should_remesh` | 決定是否對生成的網格進行處理。設為 `"false"` 時，節點會回傳未經處理的三角形網格。 | COMBO | 是 | `"true"`<br>`"false"` |
| `topology` | 重新網格化輸出的目標多邊形類型。此參數僅在 `should_remesh` 設為 `"true"` 時可用且必要。 | COMBO | 否 | `"triangle"`<br>`"quad"` |
| `target_polycount` | 重新網格化模型的目標多邊形數量（預設值：300000）。此參數僅在 `should_remesh` 設為 `"true"` 時可用。 | INT | 否 | 100 到 300000 |
| `symmetry_mode` | 控制是否對生成的模型套用對稱性。 | COMBO | 是 | `"auto"`<br>`"on"`<br>`"off"` |
| `should_texture` | 決定是否生成紋理。設為 `"false"` 會跳過紋理階段，並回傳無紋理的網格。 | COMBO | 是 | `"true"`<br>`"false"` |
| `enable_pbr` | 當 `should_texture` 為 `"true"` 時，此選項會在基礎顏色之外額外生成 PBR 貼圖（金屬度、粗糙度、法線貼圖）（預設值：False）。 | BOOLEAN | 否 | True / False |
| `texture_prompt` | 用於引導紋理處理過程的文字提示（最多 600 個字元）。不能與 `texture_image` 同時使用。此參數僅在 `should_texture` 設為 `"true"` 時可用。 | STRING | 否 | - |
| `texture_image` | 用於引導紋理處理過程的圖片。`texture_image` 和 `texture_prompt` 只能同時使用其中一個。此參數僅在 `should_texture` 設為 `"true"` 時可用。 | IMAGE | 否 | - |
| `pose_mode` | 指定生成模型的姿勢模式。 | COMBO | 是 | `""` (空白)<br>`"A-pose"`<br>`"T-pose"` |
| `seed` | 生成過程的種子值（預設值：0）。無論種子為何，結果都是非確定性的，但更改種子可以觸發節點重新執行。 | INT | 是 | 0 到 2147483647 |

**參數限制：**

* 您必須為 `images` 輸入提供 2 到 4 張圖片。
* `topology` 和 `target_polycount` 參數僅在 `should_remesh` 設為 `"true"` 時才有效。
* `enable_pbr`、`texture_prompt` 和 `texture_image` 參數僅在 `should_texture` 設為 `"true"` 時才有效。
* 您不能同時使用 `texture_prompt` 和 `texture_image`；它們是互斥的。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `模型檔案` | 生成的 GLB 模型檔案名稱。此輸出是為了向後相容而提供。 | STRING |
| `meshy 任務 ID` | Meshy API 任務的唯一識別碼。 | MESHY_TASK_ID |
| `GLB` | 以 GLB 格式生成的 3D 模型。 | FILE3DGLB |
| `FBX` | 以 FBX 格式生成的 3D 模型。 | FILE3DFBX |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyMultiImageToModelNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `e6f75f50645c8b2cf5ebbe037edb077ef1eb0ea1baf67c581d60ac0033686d00`
