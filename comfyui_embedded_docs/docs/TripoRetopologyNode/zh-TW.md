# Tripo：重新拓撲

Tripo: Retopology 會取得由較早的 Tripo 節點所生成的高多邊形 3D 模型，並將其重建為具有乾淨拓撲結構的低多邊形版本。它會將模型提交至 Tripo 重拓撲服務，等待任務完成，然後下載完成的模型，並將其任務 ID 提供給其他 Tripo 節點使用。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model_task_id` | 來源高多邊形模型的任務 ID。可接受來自 Tripo 生成節點的模型任務 ID，或來自 Tripo: Segment Model 的分割任務 ID。 | STRING | 是 | Tripo 任務 ID |
| `face_limit` | 目標面數：500 至 20,000 個三角形，或 500 至 10,000 個四邊形。設為 -1 時由 Tripo 自動選擇。（預設：-1） | INT | 是 | -1 (自動)<br>500 至 20,000 (三角形)<br>500 至 10,000 (四邊形) |
| `quad` | 四邊形網格輸出。Tripo 以 FBX 格式提供四邊形網格，因此結果會出現在 FBX 輸出，而 GLB 輸出保持空白。（預設：False） | BOOLEAN | 是 | True<br>False (預設) |
| `bake` | 將來源紋理烘焙到低多邊形網格上。（預設：True） | BOOLEAN | 否 | True (預設)<br>False |
| `part_names` | 來自 Tripo: Segment Model 的零件名稱，以逗號分隔。留空則處理整個模型。（預設：""） | STRING | 否 | 模型零件名稱或空白 |

注意：將 `face_limit` 設為 -1 時，Tripo 會自動決定面數。啟用 `quad` 時，面數上限為 10,000 個四邊形，而非 20,000 個三角形，且結果以 FBX 格式提供（GLB 輸出保持空白）。`part_names` 為空時，會處理整個模型。

## 輸出

| 輸出名 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `model_file` | 向後相容的輸出，用於識別已完成的模型檔案。較新的工作流程應改用 GLB 或 FBX 輸出。 | STRING |
| `model task_id` | 已完成重拓撲結果的任務 ID。可傳遞給其他 Tripo 節點以引用此模型。 | STRING |
| `GLB` | 以 GLB 格式提供已完成重拓撲的低多邊形模型。啟用 `quad` 時為空白。 | GLB FILE |
| `FBX` | 以 FBX 格式提供已完成重拓撲的低多邊形模型。僅在啟用 `quad` 時有內容。 | FBX FILE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoRetopologyNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `dc15f469b160a1d738e8089cf18de4a8262721bc77ebafa45bf194f04c7726b6`
