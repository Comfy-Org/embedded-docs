# Tripo P2：文字轉模型

使用 Tripo 的 P2 模型，從文字提示生成具有乾淨拓撲的低多邊形 3D 模型。結果會以三角形網格 (GLB) 傳回；當啟用 `model.quad` 時，則以四邊形為主的網格 (FBX) 傳回。

## 輸入

### 通用輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `模型` | 要使用的 Tripo P 系列模型。選取模型後，下方會顯示其專屬輸入。 | DYNAMIC_COMBO | 是 | `"P2"` |

### P2 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `提示詞` | 要生成之 3D 模型的文字描述。不得為空，最多 1024 個字元（預設：空）。 | STRING | 是 | 最多 1024 個字元 |
| `negative_prompt` | 要避免在生成模型中出現之內容的文字描述（預設：空）。 | STRING | 否 | 最多 255 個字元 |
| `四邊形` | 在 FBX 輸出上傳回以四邊形為主的網格，而非在 GLB 輸出上傳回三角形網格（預設：False）。 | BOOLEAN | 是 | True/False |
| `face_limit` | 目標面數。`-1` 讓 Tripo 自行選擇。啟用 `model.quad` 時，限制為 48 到 25,000，否則為 48 到 50,000（預設：-1）。 | INT | 是 | -1，或 48 到 50000 |
| `紋理` | 基礎顏色貼圖解析度：standard 為 2K、detailed 為 4K、extreme 為 8K。`"none"` 會傳回無貼圖網格（預設：`"standard"`）。 | COMBO | 是 | `"standard"`<br>`"detailed"`<br>`"extreme"`<br>`"none"` |
| `pbr` | 為基礎顏色加入金屬度、粗糙度與法線貼圖。當 `model.texture` 為 `"none"` 時忽略（預設：True）。 | BOOLEAN | 是 | True/False |
| `model_seed` | 幾何的種子（預設：42）。 | INT | 是 | 0 到 2147483647 |
| `image_seed` | Tripo 在建模前根據提示所生成影像的種子（預設：42）。進階設定。 | INT | 是 | 0 到 2147483647 |
| `texture_seed` | 貼圖的種子（預設：42）。進階設定。 | INT | 是 | 0 到 2147483647 |
| `auto_size` | 透過場景變換將模型縮放至以公尺為單位的實際尺寸（預設：False）。進階設定。 | BOOLEAN | 是 | True/False |
| `export_uv` | 當網格無貼圖時，對其進行 UV 展開。有貼圖的網格一律會展開（預設：True）。進階設定。 | BOOLEAN | 是 | True/False |
| `compress_geometry` | 套用 meshopt 幾何壓縮：檔案會小很多，但 ComfyUI 的 3D 預覽無法顯示它們。四邊形網格會忽略此設定（預設：False）。進階設定。 | BOOLEAN | 是 | True/False |

**注意：**

- `model.prompt` 為必填；`model.negative_prompt` 為選填，且限制為 255 個字元。
- `model.face_limit` 是目標值而非硬性上限，因此結果可能包含比要求更多的面數。`-1` 會將選擇權留給 Tripo。
- `model.quad` 決定哪個輸出會帶有網格。啟用時，模型會出現在 FBX 輸出上，而 GLB 輸出會保持空白；停用時，模型會出現在 GLB 上，而 FBX 會保持空白。若你連接的是空白輸出，節點會引發錯誤。
- `model.texture`、`model.pbr`、`model.texture_seed` 和 `model.auto_size` 僅適用於有貼圖的模型：設為 `"none"` 時，節點不會傳送貼圖設定，並傳回裸幾何。
- `model.compress_geometry` 對四邊形網格沒有影響。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `model task_id` | 模型生成請求的唯一任務 ID。 | MODEL_TASK_ID |
| `GLB` | 以 GLB 格式生成的 3D 模型。啟用 `model.quad` 時為空。 | FILE3DGLB |
| `FBX` | 以 FBX 格式生成的 3D 模型。僅在啟用 `model.quad` 時填入。 | FILE3DFBX |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoPSeriesTextToModelNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `e55596c1a237cf6b92e3bdead4359f380c6cba60992dcc61b5ee4e6b1bdd843b`
