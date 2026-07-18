# Meshy：文字轉模型節點

Meshy：文字轉模型節點使用 Meshy API 從文字描述生成 3D 模型。它會將您的提示詞和設定發送到 API，然後等待生成完成並下載生成的模型檔案。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 指定要使用的 AI 模型版本。目前僅提供「最新」版本。 | COMBO | 是 | `"latest"` |
| `prompt` | 您想要生成的 3D 模型的文字描述。長度必須在 1 到 600 個字元之間。 | STRING | 是 | - |
| `style` | 生成 3D 模型的藝術風格。 | COMBO | 是 | `"realistic"`<br>`"sculpture"` |
| `should_remesh` | 控制是否處理生成的網格。設為「false」時，節點會傳回未經處理的三角形網格。選擇「true」會顯示拓撲和多邊形數量的額外參數。 | DYNAMIC COMBO | 是 | `"true"`<br>`"false"` |
| `topology` | 重新網格化模型的目標多邊形類型。此參數僅在 `should_remesh` 設為「true」時可用且必要。 | COMBO | 否* | `"triangle"`<br>`"quad"` |
| `target_polycount` | 重新網格化模型的目標多邊形數量。預設值為 300000。此參數僅在 `should_remesh` 設為「true」時可用且必要。 | INT | 否* | 100 - 300000 |
| `symmetry_mode` | 控制生成模型的對稱性。 | COMBO | 是 | `"auto"`<br>`"on"`<br>`"off"` |
| `pose_mode` | 指定生成模型的姿勢模式。空字串表示不要求特定姿勢。 | COMBO | 是 | `""`<br>`"A-pose"`<br>`"T-pose"` |
| `seed` | 用於生成的種子值。設定此值可控制節點是否應重新執行，但無論種子值為何，結果都是非確定性的。預設值為 0。 | INT | 是 | 0 - 2147483647 |

*注意：`topology` 和 `target_polycount` 參數是條件性必要的。它們僅在 `should_remesh` 參數設為「true」時才會顯示且必須設定。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `模型檔案` | 生成的 GLB 模型檔案名稱。此輸出提供用於向後相容。 | STRING |
| `meshy_task_id` | Meshy API 任務的唯一識別碼。 | MESHY_TASK_ID |
| `GLB` | 以 GLB 格式生成的 3D 模型檔案。 | FILE3DGLB |
| `FBX` | 以 FBX 格式生成的 3D 模型檔案。 | FILE3DFBX |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyTextToModelNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `122eee5488a89433bd1f3bf79ccd8e9c51fd23cc1dfb208c39a0628c2ad3d817`
