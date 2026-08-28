# 儲存影像與文字資料集到資料夾

Save Image-Text (to Folder) 會將圖像列表及其對應的文字說明保存到 ComfyUI 輸出目錄內的指定資料夾。對於每個以 PNG 格式保存的圖像，會建立一個具有相同主檔名的 TXT 檔案來儲存其說明文字，這使其非常適合建立由生成圖像及其描述配對而成的有組織資料集。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `images` | 要保存的圖像列表。 | IMAGE | 是 | - |
| `texts` | 要保存的文字說明列表。此輸入為可選。 | STRING | 否 | - |
| `folder_name` | 要保存圖像的資料夾名稱（位於輸出目錄內）。（預設值："dataset"） | STRING | 是 | - |
| `filename_prefix` | 已保存圖像檔案名稱的前綴。（預設值："image"） | STRING | 是 | - |
| `模式` | 是否覆蓋現有檔案或增加編號以避免覆蓋。（預設值："overwrite"） | COMBO | 是 | "overwrite"<br>"increment" |

**注意：** `images` 輸入是一個列表。`texts` 輸入為可選；如果提供，則應為文字說明列表，且應包含與 `images` 相同數量的項目。每個說明都會被保存為與其配對圖像對應的 `.txt` 檔案。在 `overwrite` 模式下，檔案命名為 `{filename_prefix}_{index}.png`，並會取代任何同名現有檔案。在 `increment` 模式下，檔案名稱中會加入唯一計數器，因此不會覆蓋現有檔案。`folder_name` 必須解析為輸出目錄內的路徑；試圖跳出該目錄的資料夾名稱（例如使用 `..`）將被拒絕。

## 輸出

| 輸出名 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| - | 此節點不返回任何資料。它直接將檔案保存到檔案系統。 | - |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImageTextDataSetToFolder/zh-TW.md)

---
**Source fingerprint (SHA-256):** `46c5a04ba1befedf62b75abbff2442dde934048f365fa7e2604ea37e70d8fdcb`
