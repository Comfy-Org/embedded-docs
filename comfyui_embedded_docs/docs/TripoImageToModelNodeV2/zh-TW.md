# TripoImageToModelNodeV2

Tripo: Image to Model 節點使用 Tripo 的 image-to-model 服務，將單一參考影像轉換為 3D 模型。它會上傳影像、提交生成任務、等待任務完成，並傳回生成的 3D 檔案以及任務 ID。這是 API 節點，因此需要有效的 Comfy API 金鑰。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `影像` | 用於生成 3D 模型的參考影像。 | IMAGE | 是 | — |
| `模型版本` | 用於生成的模型版本。若未設定，節點會退回使用 Tripo 的 v3.1 (20260211) 版本。 | COMBO | 否 | Tripo 模型版本清單 |
| `紋理` | 生成紋理貼圖。關閉時會傳回裸幾何並忽略 `pbr`（預設：true）。 | BOOLEAN | 否 | true<br>false |
| `pbr` | PBR 材質貼圖（base color、metallic、roughness、normal）。需要 `texture`（預設：true）。 | BOOLEAN | 否 | true<br>false |
| `模型種子` | 用於幾何生成步驟的種子（預設：42）。 | INT | 否 | 0 到 2147483647 |
| `方向` | 套用至生成模型的 orientation 設定（預設：DEFAULT）。 | COMBO | 否 | Tripo orientation 選項，預設 `DEFAULT` |
| `紋理種子` | 用於紋理生成步驟的種子（預設：42）。 | INT | 否 | 0 到 2147483647 |
| `紋理品質` | detailed = HD 紋理，extreme = 8K Ultra 紋理（預設："standard"）。 | COMBO | 否 | "standard"<br>"detailed"<br>"extreme" |
| `紋理對齊` | 紋理在生成幾何上的對齊方式（預設："original_image"）。 | COMBO | 否 | "original_image"<br>"geometry" |
| `面數上限` | 最大面數。-1 讓 Tripo 自適應選擇（在 v3.x standard 上約 1.4M 面，detailed 約 2M 面）。Tripo 會默默限制：v2.5 為 500,000，quad 網格為 150,000（預設：-1）。 | INT | 否 | -1 到 2000000 |
| `四邊形網格` | 四邊形網格輸出。Tripo 以 FBX 格式提供 quad 網格，因此結果會出現在 FBX 輸出，而 GLB 輸出會保持為空（預設：false）。 | BOOLEAN | 否 | true<br>false |
| `幾何品質` | 生成幾何的品質等級（預設："standard"）。 | COMBO | 否 | "standard"<br>"detailed" |
| `智慧低多邊形` | 具有乾淨、手工風格拓撲的低多邊形網格（500-20,000 面，quad 500-10,000）。最適合簡單主體；複雜主體可能會失敗（預設：false）。 | BOOLEAN | 否 | true<br>false |
| `自動尺寸` | 將有紋理的模型縮放至以公尺為單位的實際大小。Tripo 會將大小儲存為模型的場景變換，並在模型被轉換、綁定或重新定向時將其烘焙進去；沒有紋理時會被忽略（預設：true）。 | BOOLEAN | 否 | true<br>false |

**注意事項：**

- `image` 為必填；若未提供影像，節點會引發錯誤。
- 當啟用 `smart_low_poly` 且 `face_limit` 設為 -1 以外的值時，三角形網格的上限必須介於 500 與 20,000 之間；若啟用 `quad`，則必須介於 500 與 10,000 之間。其他值會引發錯誤。
- 當停用 `texture` 時，無論 `pbr` 的設定為何，都會強制關閉，且 `auto_size` 不會產生效果。
- `face_limit` 為 -1 時，會以 "no limit" 傳送給 Tripo，讓服務自適應選擇。
- 節點無法傳回的新 3D 檔案格式（GLB 或 FBX 以外的任何格式）會導致錯誤。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `model task_id` | Tripo 生成工作的任務 ID。 | MODEL_TASK_ID |
| `GLB` | 生成模型，格式為 GLB 檔案。啟用 `quad` 時為空。 | FILE3DGLB |
| `FBX` | 生成模型，格式為 FBX 檔案。僅在啟用 `quad` 時填入。 | FILE3DFBX |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoImageToModelNodeV2/zh-TW.md)

---
**Source fingerprint (SHA-256):** `c8c069432f67a019995b9f4dedbf5ca3f7594ae4004104277068106821189c11`
