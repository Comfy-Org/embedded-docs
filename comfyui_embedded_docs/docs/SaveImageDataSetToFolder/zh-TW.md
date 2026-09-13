# 儲存影像資料集到資料夾

此節點會將影像清單儲存到 ComfyUI 輸出目錄內的指定資料夾。它會使用可設定的檔案名稱前綴，將每張影像以 PNG 檔案寫入磁碟。此節點已棄用，並由現有的 Save Image 節點取代；在這些節點中，目標資料夾可於檔案名稱前綴中指定。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|------|------|----------|------|------|
| `images` | 要儲存的影像清單。 | IMAGE | 是 | N/A |
| `folder_name` | 要將影像儲存至其中的資料夾名稱（位於輸出目錄內）。預設："dataset"。 | STRING | 否 | N/A |
| `filename_prefix` | 儲存影像檔案名稱的前綴。預設："image"。進階參數。 | STRING | 否 | N/A |
| `模式` | 是否覆寫現有檔案，或遞增檔案名稱以避免覆寫。預設："overwrite"。 | COMBO | 否 | "overwrite"<br>"increment" |

**備註：**

- `images` 輸入是清單，因此可在單次執行中儲存多張影像。
- `folder_name`、`filename_prefix` 和 `mode` 參數是純量值；若連接的是清單，則只會使用該清單中的第一個值。
- `folder_name` 必須解析到 ComfyUI 輸出目錄內的位置。任何逃逸輸出目錄的值（例如包含 `..` 的路徑、絕對路徑、磁碟機代號或符號連結逃逸）都會被拒絕並產生錯誤。
- 在 "overwrite" 模式中，檔案會儲存為 `{prefix}_00000.png`、`{prefix}_00001.png` 等等，並取代任何現有檔案。在 "increment" 模式中，檔案名稱會插入計數器，因此不會覆寫現有檔案。
- 僅支援 PNG 輸出。

## 輸出

此節點沒有任何輸出。它是一個輸出節點，會執行將資料儲存至檔案系統的操作。

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImageDataSetToFolder/zh-TW.md)

---
**Source fingerprint (SHA-256):** `ee92340ca1581edcfe1cc1d5659ee705ad53425bed6658161a56e6d130680e50`
