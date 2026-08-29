# Meshy：材質模型

Meshy：紋理節點會將 AI 生成的紋理套用至 3D 模型。它會從先前的 Meshy 3D 生成或轉換節點取得任務 ID，並使用文字描述或參考圖像來為模型建立新的紋理。此節點會以 GLB 和 FBX 檔案格式輸出帶紋理的 3D 模型。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `模型` | 用於紋理生成的 AI 模型版本。 | COMBO | 是 | `"meshy-7"`<br>`"meshy-6"`<br>`"latest"` |
| `meshy_task_id` | 先前 Meshy 3D 生成或轉換任務的唯一識別碼（任務 ID）。這提供了要進行紋理處理的基礎 3D 模型。 | MESHY_TASK_ID | 是 | - |
| `啟用原始UV` | 使用模型的原始 UV，而不是生成新的 UV。啟用時（預設：`True`），Meshy 會保留上傳模型中的現有紋理。如果模型沒有原始 UV，輸出品質可能不會那麼好。這是一個進階選項。 | BOOLEAN | 否 | true / false |
| `PBR` | 為帶紋理的模型啟用基於物理的渲染（PBR）材質輸出（預設：`False`）。這是一個進階選項。 | BOOLEAN | 否 | true / false |
| `文字風格提示` | 使用文字描述您想要的物體紋理風格。最多 600 個字元。不能與 `image_style` 同時使用。 | STRING | 否 | - |
| `影像風格` | 用於引導紋理生成過程的 2D 圖像。不能與 `text_style_prompt` 同時使用。 | IMAGE | 否 | - |
| `紋理解析度` | 基礎顏色紋理解析度。較高的解析度可以捕捉更多表面細節。 | COMBO | 是 | `"2k"`<br>`"4k"`<br>`"8k"` |

**參數限制：**

* 您必須提供 `text_style_prompt` 或 `image_style` 其中一項，但無法同時提供兩者。
* `text_style_prompt` 最多限制為 600 個字元。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `模型檔案` | 生成的 GLB 模型的檔案名稱。此輸出僅為向後相容性而提供。 | STRING |
| `meshy_task_id` | 此紋理生成作業的唯一任務識別碼，可用於引用結果。 | MESHY_TASK_ID |
| `GLB` | 以 GLB 檔案格式儲存的帶紋理 3D 模型。 | FILE3DGLB |
| `FBX` | 以 FBX 檔案格式儲存的帶紋理 3D 模型。 | FILE3DFBX |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyTextureNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `30d51f6efe3602f27d99706840c974baf2c4397a4f9a191f3478e7eff372e319`
