# Meshy：文字生成模型

此「Meshy: Text to Model」節點使用 Meshy API 從文字描述生成 3D 模型。它會以您的提示詞和設定向 API 發送請求，然後等待生成完成，並下載生成的模型檔案。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | 指定用於生成的 AI 模型版本。 | COMBO | 是 | `"meshy-7"`<br>`"meshy-6"`<br>`"latest"` |
| `prompt` | 您想要生成的 3D 模型的文字描述。長度必須介於 1 到 600 個字元之間。 | STRING | 是 | 1 - 600 characters |
| `style` | 生成的 3D 模型的藝術風格。 | COMBO | 是 | `"realistic"` |
| `should_remesh` | 當設定為 false 時，傳回未處理的三角網格。選擇「true」會顯示拓撲與目標多邊形數量的其他參數。 | DYNAMIC_COMBO | 是 | `"true"`<br>`"false"` |
| `topology` | 重新網格化模型的目標多邊形類型。此參數僅在 `should_remesh` 設定為「true」時可用。 | COMBO | 否* | `"triangle"`<br>`"quad"` |
| `target_polycount` | 重新網格化模型的目標多邊形數量。預設值為 300000。此參數僅在 `should_remesh` 設定為「true」時可用。 | INT | 否* | 100 - 300000 |
| `symmetry_mode` | 控制生成模型中的對稱性。這是進階參數。 | COMBO | 是 | `"auto"`<br>`"on"`<br>`"off"` |
| `pose_mode` | 指定生成模型的姿勢模式。空字串表示未要求特定姿勢。這是進階參數。 | COMBO | 是 | `""`<br>`"A-pose"`<br>`"T-pose"` |
| `seed` | 種子控制節點是否應重新執行；無論種子為何，結果都是非確定性的。預設值為 0。 | INT | 是 | 0 - 2147483647 |
| `超高模式` | 執行額外的細化處理，以獲得更高保真度且具有更精細表面細節的幾何體。預設值為 false。 | BOOLEAN | 是 | true<br>false |

*注意：`topology` 和 `target_polycount` 參數為條件可用。僅當 `should_remesh` 參數設定為「true」時才會出現。

當啟用 `ultra_mode` 時，`model` 參數必須設定為 `"meshy-7"` 或 `"latest"`。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `模型檔案` | 生成的 GLB 模型的檔案名稱。此輸出用於向後相容。 | STRING |
| `meshy_task_id` | Meshy API 任務的唯一識別碼。 | MESHY_TASK_ID |
| `GLB` | 生成的 GLB 格式 3D 模型檔案。 | FILE3DGLB |
| `FBX` | 生成的 FBX 格式 3D 模型檔案。 | FILE3DFBX |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyTextToModelNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `131f17bfb788f206e15c1d48c877e822114902fadf073a6f9fb25e8340421122`
