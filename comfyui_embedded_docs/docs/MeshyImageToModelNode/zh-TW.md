好的，這就為您翻譯這份 ComfyUI 節點文檔。

---

Meshy：圖片轉模型節點使用 Meshy API 從單一輸入圖片生成 3D 模型。它會上傳您的圖片，提交一個處理任務，並返回生成的 3D 模型檔案（GLB 和 FBX）以及用於參考的任務 ID。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 指定用於生成的 AI 模型版本。 | COMBO | 是 | `"latest"` |
| `image` | 要轉換為 3D 模型的輸入圖片。 | IMAGE | 是 | - |
| `should_remesh` | 決定是否處理生成的網格。設為 `"false"` 時，節點會傳回未經處理的三角形網格。 | DYNAMIC COMBO | 是 | `"true"`<br>`"false"` |
| `topology` | 重新網格化模型的目標多邊形拓撲結構。此輸入僅在 `should_remesh` 設為 `"true"` 時可用。 | COMBO | 否* | `"triangle"`<br>`"quad"` |
| `target_polycount` | 重新網格化模型的目標多邊形數量。此輸入僅在 `should_remesh` 設為 `"true"` 時可用。預設值為 300000。 | INT | 否* | 100 - 300000 |
| `symmetry_mode` | 控制應用於生成 3D 模型的對稱性。 | COMBO | 是 | `"auto"`<br>`"on"`<br>`"off"` |
| `should_texture` | 決定是否為模型生成紋理。設為 `"false"` 會跳過紋理階段，並傳回一個沒有紋理的網格。 | DYNAMIC COMBO | 是 | `"true"`<br>`"false"` |
| `enable_pbr` | 當 `should_texture` 為 `"true"` 時，此選項會在基礎顏色之外，額外生成 PBR 貼圖（金屬、粗糙度、法線）。預設值為 `False`。 | BOOLEAN | 否* | - |
| `texture_prompt` | 用於引導紋理生成過程的文字提示（最多 600 個字元）。此輸入僅在 `should_texture` 設為 `"true"` 時可用。不能與 `texture_image` 同時使用。 | STRING | 否* | - |
| `texture_image` | 用於引導紋理生成過程的圖片。此輸入僅在 `should_texture` 設為 `"true"` 時可用。不能與 `texture_prompt` 同時使用。 | IMAGE | 否* | - |
| `pose_mode` | 指定生成模型的姿勢模式。這是一個進階參數。 | COMBO | 是 | `""` (空)<br>`"A-pose"`<br>`"T-pose"` |
| `seed` | 生成過程的種子值。無論種子值為何，結果都是非確定性的。預設值為 0。 | INT | 是 | 0 - 2147483647 |

**關於參數限制的說明：**

*   `topology` 和 `target_polycount` 輸入僅在 `should_remesh` 設為 `"true"` 時可用。
*   `enable_pbr`、`texture_prompt` 和 `texture_image` 輸入僅在 `should_texture` 設為 `"true"` 時可用。
*   您不能同時使用 `texture_prompt` 和 `texture_image`。如果在 `should_texture` 為 `"true"` 時同時提供了兩者，節點將會引發錯誤。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `模型檔案` | 生成的 GLB 模型檔案名稱。（為保持向後相容性而保留）。 | STRING |
| `meshy 任務 ID` | Meshy API 任務的唯一識別碼，可用於參考或故障排除。 | MESHY_TASK_ID |
| `GLB` | 以 GLB 檔案格式生成的 3D 模型。 | FILE3DGLB |
| `FBX` | 以 FBX 檔案格式生成的 3D 模型。 | FILE3DFBX |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyImageToModelNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `134d9250d8b447bbbd2905f827e81b67f491ba355ebb93d4d256324b644100a2`
