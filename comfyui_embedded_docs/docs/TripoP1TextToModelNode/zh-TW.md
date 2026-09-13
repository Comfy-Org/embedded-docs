# Tripo P1：文字轉模型

Tripo P1 文字轉 3D。此節點使用 Tripo P1 API 從文字描述生成 3D 模型。它針對建立低多邊形、遊戲就緒且拓撲穩定的網格進行了最佳化，適合即時應用程式。

## 輸入

### 通用輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `輸出模式` | 控制生成的模型僅包含幾何圖形，還是也包含顏色/PBR 貼圖。"Geometry only" 會傳回無貼圖的網格。"Textured" 會新增顏色/PBR 貼圖，並顯示下方的貼圖選項。 | DYNAMIC_COMBO | 是 | `"Geometry only"`<br>`"Textured"` |
| `提示詞` | 您要生成的 3D 模型的文字描述。最多 1024 個字元。必填且不能為空。 | STRING | 是 | 最多 1024 個字元 |
| `負面提示詞` | 您不希望在生成的模型中出現的內容的文字描述。最多 255 個字元。預設：未設定。 | STRING | 否 | 最多 255 個字元 |
| `圖像種子` | 用於控制隨機性的種子值。預設：42。 | INT | 否 | 0 到 2147483647 |
| `面數上限` | 目標面數，48-20000。-1 讓 Tripo 自適應選擇。預設：-1。 | INT | 否 | -1 到 20000 |
| `模型種子` | 用於控制隨機性的種子值。預設：42。 | INT | 否 | 0 到 2147483647 |
| `自動尺寸` | 將輸出縮放至接近真實世界的公尺。預設：False。 | BOOLEAN | 否 | True / False |
| `匯出 UV` | 生成期間進行 UV 展開。關閉可加快僅幾何圖形的執行速度。預設：True。 | BOOLEAN | 否 | True / False |
| `壓縮幾何` | 套用 meshopt 幾何壓縮 (EXT_meshopt_compression)。檔案較小，但 ComfyUI 的 3D 預覽無法顯示它們；編輯前請先解壓縮。預設：False。 | BOOLEAN | 否 | True / False |

### Geometry only 輸入

當 `output_mode` 設為 `"Geometry only"` 時，沒有額外的輸入可用。在此模式下，與貼圖相關的參數不會傳送給 Tripo。

### Textured 輸入

這些輸入僅在 `output_mode` 設為 `"Textured"` 時出現。

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `pbr` | 包含 PBR 貼圖。開啟時，基礎貼圖也會強制開啟。預設：True。 | BOOLEAN | 是 | True / False |
| `texture_quality` | 貼圖品質預設集。detailed = HD 貼圖，extreme = 8K Ultra 貼圖。預設："standard"。 | COMBO | 是 | `"standard"`<br>`"detailed"`<br>`"extreme"` |
| `texture_seed` | 用於貼圖生成以控制隨機性的種子值。預設：42。 | INT | 是 | 0 到 2147483647 |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `model_file` | 生成的模型檔案名稱，僅保留以向後相容。 | STRING |
| `model task_id` | 模型生成請求的唯一任務 ID。 | MODEL_TASK_ID |
| `GLB` | 生成的 3D 模型，格式為 GLB。 | FILE3DGLB |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoP1TextToModelNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `53a5573384294612b912558436e82f3481717d2ba3d50b73f1e40c3065aff2a0`
