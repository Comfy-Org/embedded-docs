# Meshy：圖片轉模型

Meshy: Image to Model 節點使用 Meshy API 從單一輸入影像生成 3D 模型。節點會上傳您的影像、提交處理任務，並傳回生成的 3D 模型檔案（GLB 和 FBX），以及可供參考的任務 ID。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 指定要用於生成的 AI 模型版本。 | COMBO | 是 | `"latest"` |
| `image` | 要轉換成 3D 模型的輸入影像。 | IMAGE | 是 | - |
| `should_remesh` | 設為 `"false"` 時，會傳回未處理的三角形網格。 | DYNAMIC_COMBO | 是 | `"true"`<br>`"false"` |
| `topology` | 重新網格化模型的目標多邊形拓撲。此輸入僅在 `should_remesh` 設為 `"true"` 時可用。 | COMBO | 否* | `"triangle"`<br>`"quad"` |
| `target_polycount` | 重新網格化模型的目標多邊形數量。此輸入僅在 `should_remesh` 設為 `"true"` 時可用。預設值：300000。 | INT | 否* | 100 - 300000 |
| `symmetry_mode` | 控制套用至生成 3D 模型的對稱設定。 | COMBO | 是 | `"auto"`<br>`"on"`<br>`"off"` |
| `should_texture` | 決定是否生成紋理。設為 `"false"` 時，會跳過紋理階段並傳回不含紋理的網格。 | DYNAMIC_COMBO | 是 | `"true"`<br>`"false"` |
| `enable_pbr` | 在基礎顏色之外，生成 PBR 貼圖（金屬、粗糙度、法線）。此輸入僅在 `should_texture` 設為 `"true"` 時可用。預設值：`False`。 | BOOLEAN | 否* | - |
| `texture_prompt` | 提供文字提示來引導紋理生成過程。最多 600 個字元。不能與 `texture_image` 同時使用。此輸入僅在 `should_texture` 設為 `"true"` 時可用。預設值：空字串。 | STRING | 否* | - |
| `texture_image` | `texture_image` 與 `texture_prompt` 同一時間只能使用其中一個。此輸入僅在 `should_texture` 設為 `"true"` 時可用。 | IMAGE | 否* | - |
| `pose_mode` | 指定生成模型的姿勢模式。此為進階參數。 | COMBO | 是 | `""`（空字串）<br>`"A-pose"`<br>`"T-pose"` |
| `seed` | `seed` 控制節點是否應重新執行；無論種子值為何，結果皆不具確定性。預設值：0。 | INT | 是 | 0 - 2147483647 |

**參數限制注意事項：**

* `topology` 和 `target_polycount` 輸入僅在 `should_remesh` 設為 `"true"` 時可用。
* `enable_pbr`、`texture_prompt` 和 `texture_image` 輸入僅在 `should_texture` 設為 `"true"` 時可用。
* 當 `should_texture` 設為 `"true"` 時，`texture_prompt` 和 `texture_image` 不能同時使用。若同時提供兩者，節點會拋出錯誤。
* `texture_prompt` 的最大長度為 600 個字元。

## 輸出

| 輸出名 | 說明 | 資料類型 |
| --- | --- | --- |
| `模型檔案` | 生成的 GLB 模型的檔案名稱。僅為維持向後相容性而保留。 | STRING |
| `meshy 任務 ID` | Meshy API 任務的唯一識別碼，可用於參考或疑難排解。 | MESHY_TASK_ID |
| `GLB` | 以 GLB 檔案格式生成的 3D 模型。 | FILE3DGLB |
| `FBX` | 以 FBX 檔案格式生成的 3D 模型。 | FILE3DFBX |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyImageToModelNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `9f7abcb0db3c78715e4ba7370efe294caf186590f7ab62da8568778848fc838c`
