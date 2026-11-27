# Tripo：文字轉模型

此舊版節點使用 Tripo 的 API，根據文字描述生成完成的 3D 模型。它會等待生成完成，然後傳回模型檔案，並可選擇附帶紋理與 PBR 材質。此節點已標記為棄用，保留供較舊的工作流程使用。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `提示詞` | 要生成之 3D 模型的文字描述（多行）。此參數為必填，且不能為空。 | STRING | 是 | - |
| `負向提示詞` | 要避免在生成模型中出現之內容的文字描述（多行）。最多 255 個字元。僅在非空時傳送給 API。 | STRING | 否 | 最多 255 個字元 |
| `模型版本` | 用於生成的 Tripo 模型版本（預設：v3_1_20260211）。 | COMBO | 否 | 有多個選項可用 |
| `風格` | Tripo 已不再支援且會忽略。保留供較舊的工作流程使用（預設："None"）。 | COMBO | 否 | 有多個選項可用 |
| `紋理` | 生成紋理貼圖。關閉時會傳回不含紋理的幾何，並忽略 `pbr`（預設：True）。 | BOOLEAN | 否 | true / false |
| `PBR材質` | PBR 材質貼圖（基礎顏色、金屬度、粗糙度、法線）。需要 `texture`；當 `texture` 關閉時會強制關閉（預設：True）。 | BOOLEAN | 否 | true / false |
| `圖片種子` | 用於圖像生成階段的種子（預設：42）。 | INT | 否 | 0 至 2147483647 |
| `模型種子` | 用於模型生成階段的種子（預設：42）。 | INT | 否 | 0 至 2147483647 |
| `紋理種子` | 用於紋理生成階段的種子（預設：42）。 | INT | 否 | 0 至 2147483647 |
| `紋理品質` | 生成紋理的品質。detailed = HD 紋理，extreme = 8K Ultra 紋理（預設：standard）。 | COMBO | 否 | "standard"<br>"detailed"<br>"extreme" |
| `面數限制` | 最大面數。-1 讓 Tripo 自適應選擇（v3.x standard 約 1.4M 面，detailed 約 2M 面）。Tripo 會默默限制：四邊形網格為 150,000。（預設：-1） | INT | 否 | -1 至 2000000 |
| `四邊形` | 四邊形網格輸出。Tripo 會以 FBX 格式提供四邊形網格，因此結果會出現在 FBX 輸出，而 GLB 輸出會保持空白。（預設：False） | BOOLEAN | 否 | true / false |
| `幾何品質` | 生成幾何的品質（預設：standard）。 | COMBO | 否 | "standard"<br>"detailed" |
| `smart_low_poly` | 具有乾淨、手工風格拓撲的低多邊形網格（500-20,000 面，四邊形 500-10,000）。最適合簡單主體；複雜主體可能會失敗。（預設：False） | BOOLEAN | 否 | true / false |
| `auto_size` | 將帶有紋理的模型縮放到其以公尺為單位的真實世界尺寸。Tripo 會將尺寸儲存為模型的場景變換，並在模型轉換、綁定骨架或重定向時將其烘焙進去；沒有 `texture` 時會被忽略。（預設：True） | BOOLEAN | 否 | true / false |

**備註：**
- 此節點已棄用，並標記為舊版節點。保留它是為了與較舊的工作流程維持向後相容性。
- `prompt` 參數為必填：空的 `prompt` 會導致節點引發錯誤。
- `pbr` 需要 `texture`。當 `texture` 關閉時，節點會強制將 `pbr` 關閉並忽略其值。沒有 `texture` 時，`auto_size` 也沒有效果。
- 當啟用 `smart_low_poly` 且 `face_limit` 設為 -1 以外的值時，若為三角形輸出，面數限制必須介於 500 與 20,000 之間；若啟用 `quad`，則必須介於 500 與 10,000 之間；否則節點會引發錯誤。
- 當啟用 `quad` 時，生成的四邊形網格會以 FBX 格式交付，因此 FBX 輸出會有內容，而 GLB 輸出會保持空白。
- 接受 `style` 參數，但會忽略它。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `模型檔案` | 生成的 3D 模型檔案名稱，格式為 `<task_id>.<format>`，僅為了向後相容性而保留。 | STRING |
| `模型任務 ID` | 模型生成程序的唯一任務識別碼。 | MODEL_TASK_ID |
| `GLB` | 以 GLB 格式生成的 3D 模型。啟用 `quad` 時為空。 | FILE3DGLB |
| `FBX` | 以 FBX 格式生成的 3D 模型。僅在啟用 `quad` 時才會有內容。 | FILE3DFBX |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoTextToModelNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `c26c8437ea66d08f7f39865fedeaaf4cf8583ca64b368f3b767ea18918dd6c08`
