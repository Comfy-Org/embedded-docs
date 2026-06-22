# Meshy：材質模型

Meshy：紋理節點可將 AI 生成的紋理應用到 3D 模型上。它接收來自先前 Meshy 3D 生成或轉換節點的任務 ID，並使用文字描述或參考影像為模型創建新的紋理。該節點以 GLB 和 FBX 檔案格式輸出帶有紋理的模型。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `模型` | 用於紋理處理的 AI 模型版本。目前僅提供「最新」版本。 | COMBO | 是 | `"latest"` |
| `meshy_task_id` | 來自先前 Meshy 3D 生成或轉換任務的唯一識別碼（任務 ID）。這提供了要進行紋理處理的基礎 3D 模型。 | MESHY_TASK_ID | 是 | - |
| `啟用原始UV` | 使用模型的原始 UV 而非生成新的 UV。啟用時（預設值：`True`），Meshy 會保留上傳模型中的現有紋理。如果模型沒有原始 UV，輸出品質可能不佳。 | BOOLEAN | 否 | - |
| `PBR` | 為紋理模型啟用基於物理的渲染（PBR）材質輸出（預設值：`False`）。 | BOOLEAN | 否 | - |
| `文字風格提示` | 使用文字描述您期望的物體紋理風格。最多 600 個字元。不能與 `影像風格` 同時使用。 | STRING | 否 | - |
| `影像風格` | 用於引導紋理處理過程的 2D 影像。不能與 `文字風格提示` 同時使用。 | IMAGE | 否 | - |

**參數限制：**

* 您必須提供 `text_style_prompt` 或 `image_style` 其中之一，但不能同時提供兩者。
* `text_style_prompt` 最多限制為 600 個字元。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `meshy_task_id` | 生成的 GLB 模型檔案名稱。此輸出為向後相容而提供。 | STRING |
| `GLB` | 此紋理處理作業的唯一任務識別碼，可用於引用結果。 | MODEL_TASK_ID |
| `FBX` | 以 GLB 檔案格式儲存的紋理 3D 模型。 | FILE3DGLB |
| `FBX` | 以 FBX 檔案格式儲存的紋理 3D 模型。 | FILE3DFBX |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyTextureNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `380b682a8290c69e71a204c8c3d6c2d4fb2c15f4bc1679b98c7fc4fd9ec9e1b3`
