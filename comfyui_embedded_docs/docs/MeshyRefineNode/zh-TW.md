# Meshy：精修草稿模型

Meshy：Refine Draft Model 節點接收來自先前 Meshy 任務的 3D 草稿模型並加以改良，可選擇使用文字提示或參考圖片來添加紋理。它會將精修任務提交給 Meshy API，並在任務完成後以 GLB 和 FBX 檔案形式回傳完成後的模型。

## 輸入

| 參數 | 描述 | 資料型別 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | 用於精修草稿模型的 AI 模型。 | COMBO | 是 | `"meshy-7"`<br>`"meshy-6"`<br>`"latest"` |
| `meshy_task_id` | 您要精修的草稿模型的唯一任務 ID。 | MESHY_TASK_ID | 是 | - |
| `enable_pbr` | 在基礎顏色之外，生成 PBR 貼圖（金屬度、粗糙度、法線）。請注意：使用 Sculpture 風格時應將其設為 false，因為 Sculpture 風格會生成自己的一套 PBR 貼圖。（預設：False） | BOOLEAN | 是 | - |
| `texture_prompt` | 提供文字提示以引導紋理生成過程。最多 600 個字元。不能與 `texture_image` 同時使用。（預設：空字串） | STRING | 是 | - |
| `texture_image` | `texture_image` 和 `texture_prompt` 兩者只能同時使用其中一個。 | IMAGE | 否 | - |
| `紋理解析度` | 基礎顏色紋理解析度。較高的解析度能捕捉更多表面細節。 | COMBO | 是 | `"2k"`<br>`"4k"`<br>`"8k"` |

**注意：** `texture_prompt` 和 `texture_image` 輸入彼此互斥。您不能在同一次操作中同時提供文字提示和用於紋理化的圖片。

## 輸出

| 輸出名 | 描述 | 資料型別 |
|-------------|-------------|-----------|
| `模型檔案` | 生成的 GLB 模型的檔案名稱。（僅用於向後相容） | STRING |
| `meshy 任務 ID` | 已提交精修工作的唯一任務 ID。 | MESHY_TASK_ID |
| `GLB` | 最終精修後的 3D 模型，格式為 GLB。 | FILE3DGLB |
| `FBX` | 最終精修後的 3D 模型，格式為 FBX。 | FILE3DFBX |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyRefineNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `73c9d712c4fd9fdd2792600ce874916ce9447d386407353c886f624641fa0e0f`
