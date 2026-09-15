# Tripo P1：圖片轉模型

Tripo P1：影像轉模型會使用 Tripo P1 API 將單一 2D 影像轉換成 3D 模型。它針對產生低多邊形、可直接用於遊戲的網格進行了最佳化，並讓你能在僅含幾何的網格或帶有 PBR 貼圖的紋理模型之間選擇。完成的模型會以 GLB 檔案傳回。

## 輸入

### 通用輸入

這些參數一律可用。

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `輸出模式` | 選擇結果類型。"Geometry only" 會傳回無貼圖的網格；"Textured" 會加入色彩/PBR 貼圖並顯示額外的紋理設定。 | DYNAMIC_COMBO | 是 | `"Geometry only"`<br>`"Textured"` |
| `圖片` | 用來產生 3D 模型的來源 2D 影像。必須提供單一影像；若未提供，節點會引發錯誤。 | IMAGE | 是 | - |
| `啟用圖片自動修正` | 對輸入影像進行前處理，以提升產生品質。（預設：False） | BOOLEAN | 否 | True<br>False |
| `面數上限` | 目標面數，48-20000。-1 會讓 Tripo 自適應選擇。（預設：-1） | INT | 否 | -1 至 20000 |
| `模型種子` | 用於幾何產生的種子，以便重現結果。（預設：42） | INT | 否 | 0 至 2147483647 |
| `自動尺寸` | 將輸出縮放至接近真實世界公尺。（預設：False） | BOOLEAN | 否 | True<br>False |
| `匯出 UV` | 產生期間進行 UV 展開。若僅執行幾何，關閉可加快速度。（預設：True） | BOOLEAN | 否 | True<br>False |
| `壓縮幾何` | 套用 meshopt 幾何壓縮（EXT_meshopt_compression）。檔案較小，但 ComfyUI 的 3D 預覽無法顯示它們；編輯前請先解壓縮。（預設：False） | BOOLEAN | 否 | True<br>False |

### 僅幾何輸入

沒有其他參數。輸出為無貼圖的網格。

### 紋理輸入

當 `output_mode` 設為 "Textured" 時，會顯示這些參數。

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `pbr` | 包含 PBR 貼圖。開啟時，也會強制開啟基礎貼圖。（預設：True） | BOOLEAN | 是 | True<br>False |
| `texture_quality` | detailed = HD 貼圖，extreme = 8K Ultra 貼圖。（預設："standard"） | COMBO | 是 | `"standard"`<br>`"detailed"`<br>`"extreme"` |
| `texture_alignment` | 優先考慮對來源影像的視覺保真度，或與網格幾何對齊。（預設："original_image"） | COMBO | 是 | `"original_image"`<br>`"geometry"` |
| `orientation` | 旋轉輸出以符合來源影像。僅在紋理模式下適用。（預設："default"） | COMBO | 是 | `"default"`<br>`"align_image"` |
| `texture_seed` | 用於紋理產生的種子，以便重現紋理結果。（預設：42） | INT | 是 | 0 至 2147483647 |

備註：當 `output_mode` 為 "Geometry only" 時，請求會停用紋理處理。在 "Textured" 模式下，一律會請求色彩貼圖；停用 `pbr` 會移除 PBR 貼圖，但保留基礎色彩貼圖；啟用 `pbr` 則會一併強制開啟基礎貼圖。`texture_alignment` 和 `orientation` 僅在 "Textured" 模式下可用。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `model_file` | 包含所產生模型檔案名稱（`<task_id>.glb`）的字串。僅為向後相容而保留。 | STRING |
| `model task_id` | Tripo API 針對已完成的產生工作所傳回的唯一任務 ID。 | MODEL_TASK_ID |
| `GLB` | 以 GLB 格式產生的 3D 模型。 | FILE3DGLB |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoP1ImageToModelNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `1369da2ef732556896bce3415e7b99023f310544b8077ea4c6b1730bec59ee99`
