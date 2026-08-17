# 從資料夾載入圖片與文字資料集

此節點會從指定資料夾載入由影像與文字說明配對組成的資料集，並以清單形式回傳。支援的格式：PNG、JPG、JPEG、WEBP。對於每個影像檔案，節點會自動尋找相同主檔名的對應 `.txt` 檔案，作為該影像的文字說明。此節點也支援一種資料夾結構：子資料夾名稱以數字前綴開頭（例如 `10_folder_name`），這會使該子資料夾內的影像在輸出中重複該數字指定的次數。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `folder` | 要從中載入影像與文字說明的資料夾。可用選項為 ComfyUI 輸入目錄下的子資料夾。 | COMBO | 是 | *Dynamically loaded from `folder_paths.get_input_subfolders()`* |

**注意：** 此節點預期特定的檔案結構。對於每個影像檔案（`.png`、`.jpg`、`.jpeg`、`.webp`），它會尋找同名的 `.txt` 檔案作為文字說明。如果找不到文字說明檔案，則使用空字串。此節點也支援一種特殊結構：子資料夾名稱以數字和底線開頭（例如 `5_cats`），這會使該子資料夾內的所有影像在最終輸出清單中重複該數字指定的次數。所選資料夾必須位於 ComfyUI 的輸入目錄內；任何解析到該目錄之外的資料夾名稱都會被拒絕。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `images` | 已載入影像張量的清單。 | IMAGE |
| `texts` | 對應於每張已載入影像的文字說明清單。 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageTextDataSetFromFolder/zh-TW.md)

---
**Source fingerprint (SHA-256):** `d34494d59a65edb38d7e6a5f12c241fb0093371db0b0bf1e52789e84209ad3f5`
