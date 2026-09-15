# 儲存影像與文字資料集到資料夾

Save Image-Text (to Folder) 會將影像與文字標註配對的資料集儲存到 ComfyUI 輸出目錄內的資料夾。每張影像會寫入為 PNG 檔案，而與其配對的標註會寫入為具有相同主檔名的 TXT 檔案，因此每張影像最終都會與其描述配對。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `images` | 要儲存的影像清單。 | IMAGE | 是 | - |
| `texts` | 要儲存的文字標註清單。此輸入為選填。 | STRING | 否 | - |
| `folder_name` | 要儲存影像的資料夾名稱（位於輸出目錄內）。（預設值："dataset"） | STRING | 是 | - |
| `filename_prefix` | 儲存影像檔名的前綴。（預設值："image"） | STRING | 是 | - |
| `模式` | 要覆寫現有檔案，或遞增檔名以避免覆寫。（預設值："overwrite"） | COMBO | 是 | "overwrite"<br>"increment" |

**注意：** `images` 輸入是一個清單，且節點會同時將 `images` 和 `texts` 作為清單接收。`texts` 輸入為選填；若提供，它應為文字標註清單，且項目數量應與 `images` 相同。每個標註會儲存為與其配對影像相對應的 `.txt` 檔案。在 `overwrite` 模式下，檔案會命名為 `{filename_prefix}_{index}.png`，並取代任何同名現有檔案。在 `increment` 模式下，檔名會加入唯一計數器，因此不會覆寫現有檔案。`folder_name` 必須解析為輸出目錄內的路徑；試圖逃逸該目錄的資料夾名稱（例如使用 `..`）會被拒絕。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| - | 此節點不會回傳任何資料。它會直接將檔案儲存到檔案系統。 | - |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImageTextDataSetToFolder/zh-TW.md)

---
**Source fingerprint (SHA-256):** `46c5a04ba1befedf62b75abbff2442dde934048f365fa7e2604ea37e70d8fdcb`
