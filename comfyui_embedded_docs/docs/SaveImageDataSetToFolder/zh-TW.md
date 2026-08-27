# 儲存影像資料集到資料夾

此節點會將影像清單儲存到 ComfyUI 輸出目錄內的指定資料夾中。它會使用可設定的檔名前綴，將每張影像以 PNG 檔案格式寫入磁碟。此節點已棄用，並由現有的 Save Image 節點取代；在現有節點中，目標資料夾可直接在檔名前綴中指定。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `images` | 要儲存的影像清單。 | IMAGE | 是 | N/A |
| `folder_name` | 要儲存影像的資料夾名稱（位於輸出目錄內）。預設值："dataset"。 | STRING | 否 | N/A |
| `filename_prefix` | 儲存影像檔名的前綴。預設值："image"。進階參數。 | STRING | 否 | N/A |
| `模式` | 是否覆寫現有檔案，或遞增檔名以避免覆寫。預設值："overwrite"。 | COMBO | 否 | "overwrite"<br>"increment" |

**注意事項：**

- `images` 輸入是一個清單，因此可在單次執行中儲存多張影像。
- `folder_name`、`filename_prefix` 和 `mode` 參數是純量值；如果連接的是清單，則只使用該清單中的第一個值。
- `folder_name` 必須解析為 ComfyUI 輸出目錄內的位置。任何會逸出輸出目錄的值（例如包含 `..` 的路徑或絕對路徑）都會被拒絕並產生錯誤。
- 在 "overwrite" 模式下，檔案會儲存為 `{prefix}_00000.png`、`{prefix}_00001.png` 等，並取代任何現有檔案。在 "increment" 模式下，檔名中會插入一個計數器，因此不會覆寫現有檔案。

## 輸出

此節點沒有任何輸出。它是一個執行儲存作業至檔案系統的輸出節點。

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImageDataSetToFolder/zh-TW.md)

---
**Source fingerprint (SHA-256):** `ee92340ca1581edcfe1cc1d5659ee705ad53425bed6658161a56e6d130680e50`
