# Tripo：重新拓撲

Tripo: Retopology 會接收由先前的 Tripo 節點所生成的高多邊形 3D 模型，並將其重建為具有乾淨拓撲的低多邊形版本。它會將模型提交至 Tripo 重新拓撲服務，等待任務完成，然後下載完成的模型，並公開其任務 ID，供其他 Tripo 節點使用。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model_task_id` | 來源高多邊形模型的任務 ID。接受來自 Tripo 生成節點的模型任務 ID，或來自 Tripo: Segment Model 的分割任務 ID。 | STRING | 是 | Tripo task ID |
| `face_limit` | 目標面數：500-20,000 個三角形，或 500-10,000 個四邊形。-1 讓 Tripo 自行選擇。（預設值：-1） | INT | 是 | -1 (automatic)<br>500 至 20,000 (triangles)<br>500 至 10,000 (quads) |
| `quad` | 四邊形網格輸出。Tripo 會以 FBX 格式提供四邊形網格，因此結果會出現在 FBX 輸出，而 GLB 輸出會保持為空。（預設值：False） | BOOLEAN | 是 | True<br>False (default) |
| `bake` | 將來源紋理烘焙到低多邊形網格上。（預設值：True） | BOOLEAN | 否 | True (default)<br>False |
| `part_names` | 來自 Tripo: Segment Model 的逗號分隔部位名稱。留空則處理整個模型。（預設值：""） | STRING | 否 | Model part names or empty |

注意：當 `face_limit` 設為 -1 時，Tripo 會自動決定面數。啟用 `quad` 時，最大面數限制為 10,000 個四邊形，而非 20,000 個三角形，且結果會以 FBX 提供（GLB 輸出會保持為空）。當 `part_names` 為空時，會處理整個模型。若 `face_limit` 不是 -1 且超出允許範圍，節點會引發錯誤。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `model_file` | 向後相容的輸出，用於識別已完成的模型檔案。較新的工作流程應改用 GLB 或 FBX 輸出。 | STRING |
| `model task_id` | 完成的重新拓撲結果的任務 ID。可傳遞給其他 Tripo 節點以參照此模型。 | STRING |
| `GLB` | 重新拓撲後的低多邊形模型，採用 GLB 格式。啟用 `quad` 時為空。 | GLB FILE |
| `FBX` | 重新拓撲後的低多邊形模型，採用 FBX 格式。僅在啟用 `quad` 時填入。 | FBX FILE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoRetopologyNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `b0e967eb4987a70242b6cfce93f09e0caffb7f4bdd3e4f1439e68f33f9138bb5`
