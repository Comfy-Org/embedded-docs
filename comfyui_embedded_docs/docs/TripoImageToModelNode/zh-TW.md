# Tripo：圖像轉模型

使用 Tripo 的 API，根據單一圖像同步生成 3D 模型。提供輸入圖像後，節點會據此建立完成的 3D 模型，並可選擇控制模型版本、紋理生成、細節層級與輸出格式。此為圖像轉模型節點的舊版，保留供較舊的工作流程使用。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `圖像` | 用於生成 3D 模型的輸入圖像。必須提供圖像，否則節點會引發錯誤。 | IMAGE | 是 | - |
| `模型版本` | 用於生成的模型版本。 | COMBO | 否 | `"v3.1-20260211"`<br>`"v3.0-20250812"` |
| `風格` | Tripo 已不再支援並會忽略。保留供較舊的工作流程使用。（預設值：`"None"`） | COMBO | 否 | `"None"`<br>`"realistic"`<br>`"cartoon"`<br>`"sculpture"`<br>`"low_poly"` |
| `紋理` | 生成紋理貼圖。關閉時會傳回僅含幾何的模型，並忽略 `pbr`。（預設值：True） | BOOLEAN | 否 | True<br>False |
| `PBR` | PBR 材質貼圖（基礎色、金屬度、粗糙度、法線）。需要 `texture`。（預設值：True） | BOOLEAN | 否 | True<br>False |
| `模型種子` | 模型生成用的隨機種子。（預設值：42） | INT | 否 | 0 至 2147483647 |
| `方向` | 生成模型的朝向設定。（預設值：`"default"`） | COMBO | 否 | `"default"`<br>`"front"`<br>`"back"`<br>`"left"`<br>`"right"`<br>`"top"`<br>`"bottom"` |
| `紋理種子` | 紋理生成用的隨機種子。（預設值：42） | INT | 否 | 0 至 2147483647 |
| `紋理品質` | 紋理生成的品質等級：`detailed` = HD 紋理，`extreme` = 8K Ultra 紋理。（預設值：`"standard"`） | COMBO | 否 | `"standard"`<br>`"detailed"`<br>`"extreme"` |
| `紋理對齊` | 紋理映射的對齊方法。（預設值：`"original_image"`） | COMBO | 否 | `"original_image"`<br>`"geometry"` |
| `面數限制` | 最大面數。-1 會讓 Tripo 自適應選擇（v3.x standard 約 140 萬面，detailed 約 200 萬面）。Tripo 會靜默截斷：四邊形網格為 150,000。（預設值：-1） | INT | 否 | -1 至 2000000 |
| `四邊形` | 四邊形網格輸出。Tripo 以 FBX 格式提供四邊形網格，因此結果會出現在 FBX 輸出，而 GLB 輸出會保持為空。（預設值：False） | BOOLEAN | 否 | True<br>False |
| `幾何品質` | 幾何生成的品質等級。（預設值：`"standard"`） | COMBO | 否 | `"standard"`<br>`"detailed"` |
| `smart_low_poly` | 具有乾淨、手工風格拓撲的低多邊形網格（500-20,000 面，四邊形 500-10,000）。最適合簡單主體；複雜主體可能會失敗。（預設值：False） | BOOLEAN | 否 | True<br>False |
| `auto_size` | 將帶紋理的模型縮放到以公尺為單位的真實世界尺寸。Tripo 會將尺寸儲存為模型的場景變換，並在模型轉換、綁定或重定向時將尺寸烘焙進去；沒有紋理時會忽略。（預設值：True） | BOOLEAN | 否 | True<br>False |

注意：必須提供 `image`；若缺少，節點會引發 RuntimeError。當 `texture` 為 False 時，模型僅包含裸幾何，且 `pbr` 會強制設為 False。啟用 `smart_low_poly` 時，三角形網格的 `face_limit` 必須介於 500 與 20,000 之間；若同時啟用 `quad`，則必須介於 500 與 10,000 之間；若限制值無效，節點會引發 ValueError。將 `face_limit` 設為 -1（預設值）時，不會向 API 傳送明確的面數限制，讓 Tripo 自適應選擇。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `模型檔案` | 生成的 3D 模型檔案（僅為回溯相容性保留）。 | STRING |
| `模型任務 ID` | 用於追蹤模型生成過程的任務 ID。 | MODEL_TASK_ID |
| `GLB` | GLB 格式的生成 3D 模型。啟用 `quad` 時為空。 | FILE3DGLB |
| `FBX` | FBX 格式的生成 3D 模型。僅在啟用 `quad` 時填入。 | FILE3DFBX |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoImageToModelNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `3b278abfd13329ee58ebab1bfeb47d32d09f4797f3d8628a35a028c3d15a7314`
