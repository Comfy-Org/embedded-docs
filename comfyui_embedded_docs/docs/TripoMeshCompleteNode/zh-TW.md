# TripoMeshCompleteNode

此節點用於補全已分割 3D 模型中缺失或不完整的部分，並修復網格的損壞區域。它接收 Tripo 網格分割結果的任務 ID，請求 Tripo 補全模型，然後等待工作完成。補全的部分會以 GLB 檔案形式傳回，您也可以選擇僅補全指定的部分名稱。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `segment_task_id` | Tripo 網格分割任務的任務 ID。此任務中分割模型的部分會被補全。請連接先前 Tripo 網格分割節點的 SEGMENT_TASK_ID 輸出。 | SEGMENT_TASK_ID | 是 | Single task ID |
| `part_names` | 以逗號分隔、要補全的部分名稱。留空則補全所有部分。預設為空字串。名稱周圍的多餘空格會被移除，重複名稱會被忽略。 | STRING | 否 | Free text or empty |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `model_file` | 補全後模型的檔案名稱。此輸出僅為向後相容性而存在。 | STRING |
| `模型 task_id` | 已完成的 Tripo 網格補全任務的任務 ID。可作為其他預期接收模型任務 ID 之 Tripo 節點的輸入。 | MODEL_TASK_ID |
| `GLB` | 已修復部分的完整 3D 模型，以 GLB 檔案形式下載。 | GLB |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoMeshCompleteNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `aa7173f25f54d9fca9605e246a93fe319cf46c07d8d3aacc214a24a60c92e611`
