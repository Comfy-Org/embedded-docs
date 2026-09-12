# TripoSmartSegmentNode

將 3D 模型拆分為語意上具有意義的部分，並為每個部分命名。它可以分割現有模型（透過任務 ID 提供），或先從圖像生成模型再進行分割。產生的 `segment task_id` 可供其他 Tripo 節點使用，例如 Complete Mesh Parts、Retopology、Texture model 和 Convert model，用法與 Tripo: Segment Model 結果相同。

## 輸入

### 通用輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `來源` | 分割現有模型，或先從圖像生成模型再進行分割。所選選項會決定顯示哪些額外輸入。 | DYNAMIC_COMBO | 是 | `"model"`<br>`"image"` |

### 模型輸入

當 `source` 設為 `"model"` 時顯示。

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model_task_id` | GLB 結果。四邊面（FBX）網格必須先經過 Tripo: Convert model (GLTF) 處理。 | MODEL_TASK_ID | 是 | - |
| `granularity` | 模型拆分為各部分的精細程度（預設："medium"）。 | COMBO | 否 | `"coarse"`<br>`"medium"`<br>`"fine"` |
| `hint` | 選填文字，用於指定要尋找的部分名稱，例如「手持劍與身穿盔甲的遊戲角色」（預設：空）。 | STRING | 否 | - |

### 圖像輸入

當 `source` 設為 `"image"` 時顯示。Tripo 會先從圖像生成模型，再將其分割。

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `image` | 用於生成待分割模型的圖像。 | IMAGE | 是 | - |
| `granularity` | 模型拆分為各部分的精細程度（預設："medium"）。 | COMBO | 否 | `"coarse"`<br>`"medium"`<br>`"fine"` |
| `hint` | 選填文字，用於指定要尋找的部分名稱，例如「手持劍與身穿盔甲的遊戲角色」（預設：空）。 | STRING | 否 | - |

**注意事項：**

- `granularity` 和 `hint` 由兩個 `source` 選項共用，且皆為選填。當 `hint` 留空時，不會向服務傳送任何提示。
- 當 `source` 為 `"model"` 時，僅接受 GLB 模型。其他格式（例如四邊面（FBX）網格）必須先使用 Tripo: Convert model (GLTF) 轉換。
- 系統會輪詢任務直到其達到最終狀態，預估耗時約 180 秒。若 Tripo 傳回不完整的分割結果，此節點會回報錯誤。
- 價格標記：當 `source` 為 `"image"` 時約為 0.85 USD，當 `source` 為 `"model"` 時約為 0.55 USD（顯示值為近似值）。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `分割 task_id` | 分割任務的任務 ID，可作為其他 Tripo 節點的輸入。 | SEGMENT_TASK_ID |
| `模型 task_id` | 被分割的模型（從圖像生成，或匯入的模型）。 | MODEL_TASK_ID |
| `GLB` | 分割後的 3D 模型檔案。 | FILE3DGLB |
| `part_names` | 以逗號分隔的部分名稱。 | STRING |
| `零件` | Tripo 對其找到之部分的描述。 | STRING |
| `遮罩` | 分割所產生的遮罩圖像。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoSmartSegmentNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `ba041da49e20b1ac085770078cce6ac87ef70eee927ba0ee9e5655a058893f1c`
