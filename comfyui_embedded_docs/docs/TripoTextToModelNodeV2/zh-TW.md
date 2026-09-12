# TripoTextToModelNodeV2

使用 Tripo 服務從文字描述生成 3D 模型。此節點會將提示詞與設定傳送至 Tripo，等待生成任務完成，並回傳完成的 3D 檔案以及任務識別碼。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 要生成之模型的文字描述。不得為空。 | STRING | 是 | 多行文字 |
| `negative_prompt` | 描述生成模型中不應出現內容的文字。最多 255 個字元。 | STRING | 否 | 多行文字，最大 255 個字元 |
| `model_version` | 用於生成的 Tripo 模型版本（預設：`v3.1_20260211`）。 | COMBO | 否 | 支援的 Tripo 模型版本清單 |
| `texture` | 生成材質貼圖。關閉時會回傳不含材質的幾何圖形，並忽略 `pbr`（預設：True）。 | BOOLEAN | 否 | True<br>False |
| `pbr` | PBR 材質貼圖（基礎顏色、金屬度、粗糙度、法線）。需要 `texture`（預設：True）。 | BOOLEAN | 否 | True<br>False |
| `image_seed` | 影像生成的種子值（預設：42）。 | INT | 否 | 0 到 2147483647 |
| `model_seed` | 模型生成的種子值（預設：42）。 | INT | 否 | 0 到 2147483647 |
| `texture_seed` | 材質生成的種子值（預設：42）。 | INT | 否 | 0 到 2147483647 |
| `texture_quality` | 材質細節等級（預設："standard"）。"detailed" = HD 材質，"extreme" = 8K Ultra 材質。 | COMBO | 否 | `"standard"`<br>`"detailed"`<br>`"extreme"` |
| `face_limit` | 最大面數。-1 讓 Tripo 自適應選擇（v3.x 標準約 140 萬面，detailed 約 200 萬面）。Tripo 會靜默限制：v2.5 為 500,000，四邊形網格為 150,000（預設：-1）。 | INT | 否 | -1 到 2000000 |
| `quad` | 四邊形網格輸出。Tripo 會以 FBX 交付四邊形網格，因此結果會出現在 FBX 輸出，而 GLB 輸出會保持空白（預設：False）。 | BOOLEAN | 否 | True<br>False |
| `geometry_quality` | 幾何細節等級（預設："standard"）。 | COMBO | 否 | `"standard"`<br>`"detailed"` |
| `smart_low_poly` | 具有乾淨、手工風格拓撲的低多邊形網格（500-20,000 面，四邊形 500-10,000）。最適合簡單主體；複雜主體可能會失敗（預設：False）。 | BOOLEAN | 否 | True<br>False |
| `auto_size` | 將有材質的模型縮放到其真實世界尺寸（以公尺為單位）。Tripo 會將尺寸儲存為模型的場景變換，並在模型轉換、綁定或重新定向時烘烤進去；沒有材質時會被忽略（預設：True）。 | BOOLEAN | 否 | True<br>False |

### 備註

- `prompt` 為必填，且不能為空或僅有空白。
- 當 `texture` 設為 False 時，`pbr` 會強制關閉，且 `auto_size` 不會生效。
- 當啟用 `smart_low_poly` 且 `face_limit` 不是 -1 時，三角形網格的 `face_limit` 必須介於 500 到 20,000 之間，或者啟用 `quad` 時介於 500 到 10,000 之間。
- 啟用 `quad` 時，Tripo 會回傳 FBX 檔案，因此 `GLB` 輸出會保持空白，而 `FBX` 輸出會被填入。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `model task_id` | 產生該模型的 Tripo 生成任務識別碼。 | MODEL_TASK_ID |
| `GLB` | 以 GLB 格式生成的模型。啟用 `quad` 時為空。 | FILE3D_GLB |
| `FBX` | 以 FBX 格式生成的模型。僅在啟用 `quad` 時填入。 | FILE3D_FBX |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoTextToModelNodeV2/zh-TW.md)

---
**Source fingerprint (SHA-256):** `8af7044188c6dbb87d23298bf7b99fe826bdc7bd7ba0948db2066887274faa00`
