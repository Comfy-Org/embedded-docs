此節點從指定資料夾載入一組影像及其對應的文字說明。它會搜尋影像檔案，並自動尋找檔名相同的 `.txt` 檔案作為說明文字。此節點也支援特定的資料夾結構，其中子資料夾可以數字前綴命名（例如 `10_folder_name`），表示該資料夾內的影像應在輸出中重複多次。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `資料夾` | 要載入影像的資料夾。可用的選項是 ComfyUI 輸入目錄內的子資料夾。 | COMBO | 是 | *動態從 `folder_paths.get_input_subfolders()` 載入* |

**注意：** 此節點預期特定的檔案結構。對於每個影像檔案（`.png`、`.jpg`、`.jpeg`、`.webp`），它會尋找相同名稱的 `.txt` 檔案作為說明文字。如果找不到說明檔案，則使用空字串。此節點也支援一種特殊結構：子資料夾名稱以數字和底線開頭（例如 `5_cats`），這會導致該子資料夾內的所有影像在最終輸出清單中重複該數字指定的次數。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `圖片` | 已載入影像張量的清單。 | IMAGE |
| `文字` | 對應於每個已載入影像的文字說明清單。 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageTextDataSetFromFolder/zh-TW.md)

---
**Source fingerprint (SHA-256):** `e176f35118f08ea397c63f5b6f347d9cdb3dc1a08db7ad7a5cc8255e1526e6ca`
