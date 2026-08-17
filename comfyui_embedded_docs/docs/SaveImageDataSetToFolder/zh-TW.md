# 儲存影像資料集到資料夾

此節點會將影像清單以 PNG 檔案格式儲存至 ComfyUI 輸出目錄內的指定資料夾。此節點已棄用：它並非必要功能，且已被現有的 Save Image 節點所取代，因為現有節點可在檔案名稱前綴中指定目標資料夾。此節點使用可自訂的檔案名稱前綴，將接收到的每張影像寫入磁碟，並且可以選擇覆寫既有檔案，或產生遞增的檔案名稱以避免覆寫。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `images` | 要儲存的影像清單。 | IMAGE | 是 | N/A |
| `folder_name` | 要儲存影像的資料夾名稱（位於輸出目錄內）。預設值為 "dataset"。 | STRING | 否 | N/A |
| `filename_prefix` | 已儲存影像檔案名稱的前綴。預設值為 "image"。 | STRING | 否 | N/A |
| `mode` | 選擇要覆寫既有檔案，還是遞增檔案名稱以避免覆寫。預設值為 "overwrite"。 | COMBO | 否 | "overwrite"<br>"increment" |

**注意：** `images` 輸入是一個清單，表示它可以一次接收並處理多張影像。所有輸入皆以清單形式接收；對於 `folder_name`、`filename_prefix` 和 `mode`，僅會使用所連接清單中的第一個值。`folder_name` 必須解析為 ComfyUI 輸出目錄內的資料夾——若資料夾名稱試圖逸出該目錄（例如使用 ".."、絕對路徑或磁碟機代號），將會被拒絕並回報錯誤。影像一律以 PNG 格式儲存。`filename_prefix` 參數為進階選項。

## 輸出

此節點沒有任何資料輸出。它是一個執行檔案系統儲存操作的輸出節點。

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImageDataSetToFolder/zh-TW.md)

---
**Source fingerprint (SHA-256):** `ee92340ca1581edcfe1cc1d5659ee705ad53425bed6658161a56e6d130680e50`
