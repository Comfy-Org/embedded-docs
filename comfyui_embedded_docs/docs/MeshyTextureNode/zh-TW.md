# Meshy：材質模型

Meshy: Texture Model 節點會將 AI 生成的紋理套用到既有的 3D 模型。它會使用先前 Meshy 3D 生成或轉換任務的任務 ID，並透過文字風格提示詞或參考影像來引導紋理貼圖過程。此節點會傳回 GLB 與 FBX 檔案格式的紋理貼圖後模型。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `模型` | 用於紋理貼圖的 AI 模型版本。 | COMBO | 是 | `"meshy-7"`<br>`"meshy-6"`<br>`"latest"` |
| `meshy_task_id` | 來自先前 Meshy 3D 生成或轉換任務的唯一識別碼（任務 ID）。這會提供要進行紋理貼圖的基礎 3D 模型。 | MESHY_TASK_ID | 是 | - |
| `啟用原始UV` | 使用模型的原始 UV，而不是產生新的 UV。啟用時（預設：`True`），Meshy 會保留上傳模型既有的紋理。如果模型沒有原始 UV，輸出品質可能不會那麼好。這是進階選項。 | BOOLEAN | 是 | true / false |
| `PBR` | 為紋理貼圖後的模型啟用基於物理的渲染（PBR）材質輸出（預設：`False`）。這是進階選項。 | BOOLEAN | 是 | true / false |
| `文字風格提示` | 使用文字描述您想要的物件紋理風格（預設：空字串）。最多 600 個字元。不能與 `image_style` 同時使用。 | STRING | 是 | - |
| `影像風格` | 用來引導紋理貼圖過程的 2D 影像。不能與 `text_style_prompt` 同時使用。 | IMAGE | 否 | - |
| `紋理解析度` | 基礎顏色紋理解析度。較高的解析度可捕捉更多表面細節。 | COMBO | 是 | `"2k"`<br>`"4k"`<br>`"8k"` |

**參數限制：**

* 您必須提供 `text_style_prompt` 或 `image_style` 其中一個，但不能同時提供兩者。
* `text_style_prompt` 限制最多 600 個字元。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `model_file` | 所產生 GLB 模型的檔案名稱。此輸出僅為了向後相容而提供。 | STRING |
| `meshy_task_id` | 此紋理貼圖工作的唯一任務識別碼，可用於參照結果。 | MESHY_TASK_ID |
| `GLB` | 以 GLB 檔案格式儲存的紋理貼圖後 3D 模型。 | FILE3DGLB |
| `FBX` | 以 FBX 檔案格式儲存的紋理貼圖後 3D 模型。 | FILE3DFBX |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyTextureNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `30d51f6efe3602f27d99706840c974baf2c4397a4f9a191f3478e7eff372e319`
