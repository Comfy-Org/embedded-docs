# Tripo P2：影像轉模型

生成具備乾淨拓撲的低多邊形 3D 模型，使用 Tripo 的 P2 模型從單一影像生成。結果會以三角形網格 (GLB) 傳回，或者當啟用 `model.quad` 時，以四邊形為主的網格 (FBX) 傳回。

## 輸入

### 通用輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `模型` | 要使用的 Tripo P 系列模型。選擇模型後，會在其下方顯示該模型自身的輸入。 | DYNAMIC_COMBO | 是 | `"P2"` |

### P2 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model.image` | 用來生成模型的影像。 | IMAGE | 是 | - |
| `quad` | 在 FBX 輸出上傳回以四邊形為主的網格，而非 GLB 輸出上的三角形網格（預設：False）。 | BOOLEAN | 是 | True/False |
| `face_limit` | 目標面數。`-1` 讓 Tripo 自行選擇。啟用 `model.quad` 時，限制為 48 到 25,000；否則為 48 到 50,000（預設：-1）。 | INT | 是 | -1，或 48 至 50000 |
| `紋理` | 基礎顏色紋理解析度：standard 為 2K，detailed 為 4K，extreme 為 8K。`"none"` 會傳回無紋理的網格（預設：`"standard"`）。 | COMBO | 是 | `"standard"`<br>`"detailed"`<br>`"extreme"`<br>`"none"` |
| `pbr` | 將金屬度、粗糙度和法線貼圖加入基礎顏色。當 `model.texture` 為 `"none"` 時忽略（預設：True）。 | BOOLEAN | 是 | True/False |
| `model_seed` | 幾何的種子（預設：42）。 | INT | 是 | 0 至 2147483647 |
| `texture_alignment` | 比對輸入影像的顏色，或將紋理貼合至生成的幾何。當 `model.texture` 為 `"none"` 時忽略（預設：`"original_image"`）。進階設定。 | COMBO | 是 | `"original_image"`<br>`"geometry"` |
| `方向` | `"align_image"` 會將模型旋轉至輸入影像的視角。當 `model.texture` 為 `"none"` 時忽略（預設：`"default"`）。進階設定。 | COMBO | 是 | `"default"`<br>`"align_image"` |
| `enable_image_autofix` | 讓 Tripo 在建模前增強低解析度或低品質的影像（預設：False）。進階設定。 | BOOLEAN | 是 | True/False |
| `texture_seed` | 紋理的種子（預設：42）。進階設定。 | INT | 是 | 0 至 2147483647 |
| `auto_size` | 透過場景變換將模型縮放至其以公尺為單位的真實世界尺寸（預設：False）。進階設定。 | BOOLEAN | 是 | True/False |
| `export_uv` | 當網格無紋理時，對其進行 UV 展開。有紋理的網格一律會展開（預設：True）。進階設定。 | BOOLEAN | 是 | True/False |
| `compress_geometry` | 套用 meshopt 幾何壓縮：檔案會小得多，但 ComfyUI 的 3D 預覽無法顯示它們。對四邊形網格無效（預設：False）。進階設定。 | BOOLEAN | 是 | True/False |

**備註：**

- `model.image` 為必填，且僅使用批次中的第一張影像。
- `model.face_limit` 是目標值而非硬性上限，因此結果可能包含比要求更多的面。`-1` 會將選擇權留給 Tripo。
- `model.quad` 會決定由哪個輸出攜帶網格。啟用時，模型會出現在 FBX 輸出上，GLB 輸出則保持空白；停用時，模型會出現在 GLB 輸出上，FBX 保持空白。若你連接的是空白的那個輸出，此節點會引發錯誤。
- `model.texture`、`model.pbr`、`model.texture_seed`、`model.auto_size`、`model.texture_alignment` 和 `model.orientation` 僅適用於有紋理的模型：當 `"none"` 時，此節點不會傳送任何紋理設定，並傳回裸幾何。
- `model.compress_geometry` 對四邊形網格沒有作用。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `model task_id` | 模型生成請求的唯一任務 ID。 | MODEL_TASK_ID |
| `GLB` | 生成的 3D 模型，格式為 GLB。啟用 `model.quad` 時為空白。 | FILE3DGLB |
| `FBX` | 生成的 3D 模型，格式為 FBX。僅在啟用 `model.quad` 時填入。 | FILE3DFBX |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoPSeriesImageToModelNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `9bfad31ee00546d0603ce3273502cfc93c79e3b125941fed255866aa83f770a5`
