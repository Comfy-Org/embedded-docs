# Tripo P2：多視角轉模型

產生一個低多邊形 3D 模型，使用 Tripo 的 P2 模型，從同一主體的多個視圖生成具備乾淨拓撲的模型。正面視圖為必填，並可加入左、後、右視圖中的一到三個來改善結果。模型會以三角形網格 (GLB) 傳回，或在啟用 `model.quad` 時，以四邊形為主的網格 (FBX) 傳回。

## 輸入

### 通用輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `模型` | 要使用的 Tripo P 系列模型。選擇模型後，下方會顯示其專屬輸入。 | DYNAMIC_COMBO | 是 | `"P2"` |

### P2 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model.image` | 主體的正面視圖 (0°)。 | IMAGE | 是 | - |
| `model.image_left` | 左視圖 (90°)，即主體本身的左側。 | IMAGE | 否 | - |
| `model.image_back` | 背面視圖 (180°)。 | IMAGE | 否 | - |
| `model.image_right` | 右視圖 (270°)，即主體本身的右側。 | IMAGE | 否 | - |
| `quad` | 在 FBX 輸出上傳回以四邊形為主的網格，而非在 GLB 輸出上傳回三角形網格（預設：False）。 | BOOLEAN | 是 | True/False |
| `face_limit` | 目標面數。`-1` 讓 Tripo 自行選擇。啟用 `model.quad` 時，上限為 48 到 25,000；否則為 48 到 50,000（預設：-1）。 | INT | 是 | -1，或 48 至 50000 |
| `紋理` | 基礎顏色貼圖解析度：standard 為 2K、detailed 為 4K、extreme 為 8K。`"none"` 會傳回無貼圖網格（預設：`"standard"`）。 | COMBO | 是 | `"standard"`<br>`"detailed"`<br>`"extreme"`<br>`"none"` |
| `pbr` | 為基礎顏色加入金屬度、粗糙度與法線貼圖。當 `model.texture` 為 `"none"` 時忽略（預設：True）。 | BOOLEAN | 是 | True/False |
| `model_seed` | 幾何的種子（預設：42）。 | INT | 是 | 0 至 2147483647 |
| `texture_alignment` | 比對輸入影像的顏色，或將貼圖貼合至生成的幾何。當 `model.texture` 為 `"none"` 時忽略（預設：`"original_image"`）。進階設定。 | COMBO | 是 | `"original_image"`<br>`"geometry"` |
| `方向` | `"align_image"` 會將模型旋轉至輸入影像的視角。當 `model.texture` 為 `"none"` 時忽略（預設：`"default"`）。進階設定。 | COMBO | 是 | `"default"`<br>`"align_image"` |
| `texture_seed` | 貼圖的種子（預設：42）。進階設定。 | INT | 是 | 0 至 2147483647 |
| `auto_size` | 透過場景變換將模型縮放至以公尺為單位的真實世界尺寸，當 `model.texture` 為 `"none"` 時忽略（預設：False）。進階設定。 | BOOLEAN | 是 | True/False |
| `export_uv` | 當網格無貼圖時進行 UV 展開。有貼圖的網格一律會展開（預設：True）。進階設定。 | BOOLEAN | 是 | True/False |
| `compress_geometry` | 套用 meshopt 幾何壓縮：檔案會小很多，但 ComfyUI 的 3D 預覽無法顯示它們。對四邊形網格無效（預設：False）。進階設定。 | BOOLEAN | 是 | True/False |

**備註：**

- `model.image` 為必填，且必須至少連接 `model.image_left`、`model.image_back` 或 `model.image_right` 其中之一；若僅有正面視圖，節點會引發錯誤。
- 每個批次只會使用第一張影像。
- `model.face_limit` 是目標值而非硬性上限，因此結果可能包含比要求更多的面。`-1` 會讓 Tripo 自行決定。
- `model.quad` 決定由哪個輸出承載網格。啟用時，模型會出現在 FBX 輸出，而 GLB 輸出會保持空白；停用時，模型會出現在 GLB，而 FBX 會保持空白。若你連接的是空白的輸出，節點會引發錯誤。
- `model.texture`、`model.pbr`、`model.texture_seed`、`model.auto_size`、`model.texture_alignment` 與 `model.orientation` 僅適用於有貼圖的模型：使用 `"none"` 時，節點不會傳送任何貼圖設定，並傳回未貼圖的幾何。
- `model.compress_geometry` 對四邊形網格沒有影響。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `model task_id` | 模型生成請求的唯一任務 ID。 | MODEL_TASK_ID |
| `GLB` | 以 GLB 格式生成的 3D 模型。啟用 `model.quad` 時為空。 | FILE3DGLB |
| `FBX` | 以 FBX 格式生成的 3D 模型。僅在啟用 `model.quad` 時才有內容。 | FILE3DFBX |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoPSeriesMultiviewToModelNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `cea0a65ca001bc8298af9fbe2a83f592abf497987e634b0126482f3d2a18571c`
