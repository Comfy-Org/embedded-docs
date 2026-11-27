# Meshy: Texture Model (N1)

此節點會使用 Meshy N1 貼圖模型，為先前建立的 3D 模型加上貼圖；過程中會使用同一個物件的 1 至 4 個參考視圖。請連接原始模型的任務 ID 及這些視圖；節點會將它們傳送給 Meshy，等待作業完成，並以 GLB 和 FBX 檔案形式回傳已貼圖的模型，以及新的任務 ID。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `模型` | 用於貼圖作業的 AI 模型。目前僅提供 `"meshy-n1"`。 | COMBO | 是 | `"meshy-n1"` |
| `meshy_任務_id` | 先前建立且應進行貼圖的 3D 模型任務 ID。 | MESHY_TASK_ID, STRING | 是 | N/A |
| `正面視角` | Meshy 視為正面的視圖。單張圖片會為正面貼圖，背面則保持空白；在 `額外視角` 中加入背面與側面視圖，可讓背面也忠實呈現。 | IMAGE | 是 | 單張圖片 |
| `額外視角` | 同一物件的其他視圖，順序不拘。可擴充插槽：連接 0 至 3 張圖片（`view_1` ... `view_3`）。與 `正面視角` 合計最多 4 張圖片。 | IMAGE | 否 | 0 至 3 張影像 |
| `啟用原始 UV` | 使用模型的原始 UV，而非產生新的 UV。啟用時，Meshy 會保留所上傳模型中既有的貼圖。若模型沒有原始 UV，輸出品質可能較不理想。（預設：True；進階選項） | BOOLEAN | 否 | True 或 False |

**注意：** `正面視角` 與 `額外視角` 合計最多可容納 4 張圖片；若連接超過此數量，節點會引發錯誤。若連接的圖片帶有批次，批次中的每張圖片都會計入該上限。貼圖解析度固定為 2K，且不會產生 PBR 貼圖。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `meshy_task_id` | 貼圖作業的任務 ID，可供後續的 Meshy 節點使用。 | MESHY_TASK_ID, STRING |
| `GLB` | 以 GLB 格式下載的已貼圖 3D 模型。 | FILE3DGLB |
| `FBX` | 以 FBX 格式下載的已貼圖 3D 模型。 | FILE3DFBX |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyTextureN1Node/zh-TW.md)

---
**Source fingerprint (SHA-256):** `be4191fd091839cfdce82b4f41fc6ae9e70f7b5b5504eb14a3c0d741d25ac8fd`
