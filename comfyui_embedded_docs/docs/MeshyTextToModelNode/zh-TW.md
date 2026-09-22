# Meshy：文字生成模型

Meshy: Text to Model 節點使用 Meshy API 根據文字描述生成 3D 模型。它會使用你的提示詞與設定向 API 傳送請求，然後等待生成完成，並下載產生的模型檔案。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | 指定要用於生成的 AI 模型版本。 | COMBO | 是 | `"meshy-7.1"`<br>`"meshy-7"`<br>`"meshy-6"`<br>`"latest"` |
| `prompt` | 你想生成之 3D 模型的文字描述。長度必須介於 1 到 600 個字元之間。預設為空字串。 | STRING | 是 | 1 - 600 characters |
| `style` | 產生的 3D 模型之藝術風格。 | COMBO | 是 | `"realistic"` |
| `should_remesh` | 設為 false 時，會傳回未處理的三角網格。選取 "true" 會顯示 `topology` 與 `target_polycount` 這兩個額外參數。 | DYNAMIC_COMBO | 是 | `"true"`<br>`"false"` |
| `topology` | 重新網格化模型的目標多邊形類型。此參數僅在 `should_remesh` 設為 "true" 時可用。 | COMBO | 否* | `"triangle"`<br>`"quad"` |
| `target_polycount` | 重新網格化模型的目標多邊形數量。預設為 300000。此參數僅在 `should_remesh` 設為 "true" 時可用。 | INT | 否* | 100 - 300000 |
| `symmetry_mode` | 控制產生模型中的對稱性。這是進階參數。選項為 `"auto"`、`"on"` 和 `"off"`。 | COMBO | 是 | `"auto"`<br>`"on"`<br>`"off"` |
| `pose_mode` | 指定產生模型的姿勢模式。空字串表示未要求特定姿勢。這是進階參數。 | COMBO | 是 | `""`<br>`"A-pose"`<br>`"T-pose"` |
| `seed` | `seed` 控制節點是否應重新執行；無論 `seed` 為何，結果皆不具確定性。預設為 0。 | INT | 是 | 0 - 2147483647 |
| `超高模式` | 執行額外細化處理，以獲得更精細表面細節的高保真幾何。預設為 false。 | BOOLEAN | 是 | true<br>false |
| `ultra_resolution` | 超高模式的解析度：`"2k"` 以 2048³ 執行，`"4k"` 以 4096³ 執行，以獲得最精細的表面細節。`"4k"` 需要 `"meshy-7.1"` 或 `"latest"` 模型。僅在啟用 `ultra_mode` 時使用（預設：`"2k"`）。 | COMBO | 否 | `"2k"`<br>`"4k"` |

*注意：`topology` 與 `target_polycount` 參數為有條件可用。它們僅在 `should_remesh` 參數設為 "true" 時出現。

啟用 `ultra_mode` 時，`model` 參數必須設為 `"meshy-7.1"`、`"meshy-7"` 或 `"latest"`；選取任何其他模型都會引發錯誤。使用 `"meshy-7"` 時，超高模式一律以 2048³ 執行，而 `"4k"` 的超高解析度需要 `"meshy-7.1"` 或 `"latest"`。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `model_file` | 產生的 GLB 模型檔案名稱。此輸出是為了向後相容而提供。 | STRING |
| `meshy_task_id` | Meshy API 任務的唯一識別碼。 | MESHY_TASK_ID |
| `GLB` | 產生的 GLB 格式 3D 模型檔案。 | FILE3DGLB |
| `FBX` | 產生的 FBX 格式 3D 模型檔案。 | FILE3DFBX |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyTextToModelNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `a02a5ae28bcae343c628d11ba3efa952b61b8bdf867669f58f1beb0f7c9e49f9`
