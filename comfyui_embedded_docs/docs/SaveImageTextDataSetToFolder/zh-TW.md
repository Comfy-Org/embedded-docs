# 儲存影像與文字資料集到資料夾

Save Image-Text (to Folder) 是一個輸出節點，可將成對的圖像與文字說明資料集儲存到 ComfyUI 輸出目錄內的資料夾中。每張圖像會儲存為 PNG 檔案，當提供文字說明時，每張圖像會產生一個相同主檔名的 TXT 檔案。這對於建立由生成圖像及其描述組成的有組織資料集非常有用。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `images` | 要儲存的圖像列表。 | IMAGE | 是 | - |
| `texts` | 要儲存的文字說明列表。此輸入為可選。 | STRING | 否 | - |
| `folder_name` | 要儲存圖像的資料夾名稱（位於輸出目錄內）。（預設值："dataset"） | STRING | 是 | - |
| `filename_prefix` | 已儲存圖像檔案名稱的前綴。（預設值："image"） | STRING | 是 | - |
| `mode` | 是否覆寫現有檔案，或遞增檔案名稱以避免覆寫。（預設值："overwrite"） | COMBO | 是 | "overwrite"<br>"increment" |

**注意：** `images` 輸入是一個列表。`texts` 輸入為可選；如果提供，應為文字說明列表。文字說明會按順序與圖像配對，每個說明會以 UTF-8 `.txt` 檔案儲存，並與其配對的圖像具有相同的主檔名（例如，`image_00000.txt` 對應 `image_00000.png`）。如果文字說明少於圖像，則剩餘圖像會在不帶說明的情況下儲存；任何多餘的說明將被忽略。

具有預設值的輸入（`folder_name`、`filename_prefix`、`mode`）無需連接；系統會自動使用其預設值。

當 `mode` 設定為 `overwrite`（預設值）時，圖像會以類似 `image_00000.png` 的名稱儲存，並取代任何具有相同名稱的現有檔案。當 `mode` 設定為 `increment` 時，會自動在檔案名稱中增加遞增計數器，因此不會覆寫現有檔案。

`folder_name` 的值必須解析為 ComfyUI 輸出目錄內的位置。嘗試逃離輸出目錄的資料夾名稱（例如使用 `..`）將被拒絕。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| - | 此節點沒有輸出。它直接將檔案儲存到檔案系統。 | - |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImageTextDataSetToFolder/zh-TW.md)

---
**Source fingerprint (SHA-256):** `46c5a04ba1befedf62b75abbff2442dde934048f365fa7e2604ea37e70d8fdcb`
