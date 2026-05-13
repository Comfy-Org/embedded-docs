> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImageDataSetToFolder/zh-TW.md)

## 概述

此節點將影像列表儲存到 ComfyUI 輸出目錄中的指定資料夾。它接收多張影像作為輸入，並使用可自訂的檔案名稱前綴將其寫入磁碟。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `images` | IMAGE | 是 | N/A | 要儲存的影像列表。 |
| `folder_name` | STRING | 否 | N/A | 儲存影像的資料夾名稱（位於輸出目錄內）。預設值為 "dataset"。 |
| `filename_prefix` | STRING | 否 | N/A | 儲存影像檔案名稱的前綴。預設值為 "image"。 |

**注意：** `images` 輸入是一個列表，表示它可以同時接收和處理多張影像。`folder_name` 和 `filename_prefix` 參數是純量值；如果連接的是列表，則只會使用該列表中的第一個值。

## 輸出

此節點沒有任何輸出。它是一個執行儲存操作到檔案系統的輸出節點。

---
**Source fingerprint (SHA-256):** `65c7905caa8ff2811054bec2830c1359d0c441b5d93f50bc4d0bf10645046556`
