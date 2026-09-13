# Tripo：補全網格部件

補全已分割 3D 模型的部件，並修復網格中缺失或損壞的區域。它會取得 Tripo 網格分割結果的任務 ID，向 Tripo 請求補全作業，並等待其完成。您可以選擇將工作限制在特定的部件名稱。完成的模型會以 GLB 檔案回傳。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `segment_task_id` | Tripo 網格分割任務的任務 ID。來自此任務的已分割模型部件會被補全。連接先前 Tripo 網格分割節點的 SEGMENT_TASK_ID 輸出。 | SEGMENT_TASK_ID | 是 | 單一任務 ID |
| `part_names` | 以逗號分隔要補全的部件名稱。留空則補全每個部件。預設值：空字串。名稱前後的多餘空格會被移除，重複的名稱會被忽略。 | STRING | 否 | 自由文字或留空 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `model_file` | 已完成模型的檔案名稱。此輸出僅為了向後相容性而存在。 | STRING |
| `model task_id` | 已完成 Tripo 網格補全任務的任務 ID。可供其他預期模型任務 ID 的 Tripo 節點作為輸入使用。 | MODEL_TASK_ID |
| `GLB` | 已完成且部件已修復的 3D 模型，會以 GLB 檔案下載。 | GLB |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoMeshCompleteNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `c5709231fa2e33e6f3c9b25669acca1d4ae9adb882b90210d703aeddc0d11ecc`
