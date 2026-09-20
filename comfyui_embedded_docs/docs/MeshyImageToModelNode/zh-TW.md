# Meshy：圖片轉模型

Meshy: Image to Model 節點使用 Meshy API 從單一輸入圖像生成 3D 模型。它會上傳您的圖像，提交處理任務，並返回生成的 3D 模型檔案（GLB 和 FBX）以及任務 ID 以供參考。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 指定用於生成的 AI 模型版本。 | COMBO | 是 | `"meshy-7.1"`<br>`"meshy-7"`<br>`"meshy-6"`<br>`"latest"` |
| `image` | 要轉換為 3D 模型的輸入圖像。 | IMAGE | 是 | - |
| `should_remesh` | 當設定為 `"false"` 時，返回未處理的三角網格。 | DYNAMIC_COMBO | 是 | `"true"`<br>`"false"` |
| `topology` | 重新網格化模型的目標多邊形拓撲。此輸入僅在 `should_remesh` 設定為 `"true"` 時可用。 | COMBO | 否* | `"triangle"`<br>`"quad"` |
| `target_polycount` | 重新網格化模型的目標多邊形數量。此輸入僅在 `should_remesh` 設定為 `"true"` 時可用。預設值：300000。 | INT | 否* | 100 - 300000 |
| `symmetry_mode` | 控制應用於生成之 3D 模型的對稱性。 | COMBO | 是 | `"auto"`<br>`"on"`<br>`"off"` |
| `should_texture` | 決定是否生成紋理。將其設定為 `"false"` 會跳過紋理階段，並返回不帶紋理的網格。 | DYNAMIC_COMBO | 是 | `"true"`<br>`"false"` |
| `enable_pbr` | 除了基礎顏色外，生成 PBR 貼圖（金屬、粗糙度、法線）。此輸入僅在 `should_texture` 設定為 `"true"` 時可用。預設值：`False`。 | BOOLEAN | 否* | - |
| `texture_prompt` | 提供文字提示以引導紋理生成過程。最多 600 個字元。不能與 `texture_image` 同時使用。此輸入僅在 `should_texture` 設定為 `"true"` 時可用。預設值：空字串。 | STRING | 否* | - |
| `texture_image` | `texture_image` 或 `texture_prompt` 僅能同時使用其中一個。此輸入僅在 `should_texture` 設定為 `"true"` 時可用。 | IMAGE | 否* | - |
| `texture_resolution` | 基礎顏色紋理解析度。較高的解析度能捕捉更多表面細節。此輸入僅在 `should_texture` 設定為 `"true"` 時可用。 | COMBO | 否* | `"2k"`<br>`"4k"`<br>`"8k"` |
| `pose_mode` | 指定生成模型的姿勢模式。這是一個進階參數。 | COMBO | 是 | `""`（空）<br>`"A-pose"`<br>`"T-pose"` |
| `seed` | 種子控制節點是否應重新執行；無論種子為何，結果均為非確定性。預設值：0。 | INT | 是 | 0 - 2147483647 |
| `超高模式` | 執行額外的精煉過程，以獲得具有更精細表面細節的高保真幾何形狀。預設值：`False`。 | BOOLEAN | 是 | - |
| `ultra_resolution` | 超高模式的解析度：`"2k"` 以 2048³ 執行，`"4k"` 以 4096³ 執行，以獲得最精細的表面細節。`"4k"` 需要 `"meshy-7.1"` 或 `"latest"` 模型。僅在啟用 `ultra_mode` 時使用（預設：`"2k"`）。 | COMBO | 否 | `"2k"`<br>`"4k"` |

**參數約束注意事項：**

* `topology` 和 `target_polycount` 輸入僅在 `should_remesh` 設定為 `"true"` 時可用。
* `enable_pbr`、`texture_prompt`、`texture_image` 和 `texture_resolution` 輸入僅在 `should_texture` 設定為 `"true"` 時可用。
* 當 `should_texture` 設定為 `"true"` 時，`texture_prompt` 和 `texture_image` 不能同時使用。如果同時提供，節點會拋出錯誤。
* `texture_prompt` 最大長度為 600 個字元。
* 啟用 `ultra_mode` 時，`model` 參數必須設為 `"meshy-7.1"`、`"meshy-7"` 或 `"latest"`；選取任何其他模型都會引發錯誤。使用 `"meshy-7"` 時，超高模式一律以 2048³ 執行，而 `"4k"` 的超高解析度需要 `"meshy-7.1"` 或 `"latest"`。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `模型檔案` | 生成的 GLB 模型的檔案名稱。僅為向後相容性保留。 | STRING |
| `meshy 任務 ID` | Meshy API 任務的唯一識別碼，可用於參考或問題排除。 | MESHY_TASK_ID |
| `GLB` | 以 GLB 檔案格式生成的 3D 模型。 | FILE3DGLB |
| `FBX` | 以 FBX 檔案格式生成的 3D 模型。 | FILE3DFBX |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyImageToModelNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `38528b48c3f792a459008a52f65fae248ef1dadafb37fe4dc6b697d25bc89f4f`
