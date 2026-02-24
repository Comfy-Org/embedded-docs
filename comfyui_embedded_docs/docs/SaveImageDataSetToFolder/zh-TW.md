> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImageDataSetToFolder/zh-TW.md)

此節點將圖像清單儲存至 ComfyUI 輸出目錄內的指定資料夾。它接收多張圖像作為輸入，並以可自訂的檔案名稱前綴將其寫入磁碟。

## 輸入參數

| 參數 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `images` | IMAGE | 是 | N/A | 要儲存的圖像清單。 |
| `folder_name` | STRING | 否 | N/A | 儲存圖像的資料夾名稱（位於輸出目錄內）。預設值為 "dataset"。 |
| `filename_prefix` | STRING | 否 | N/A | 儲存圖像的檔案名稱前綴。預設值為 "image"。 |

**注意：** `images` 輸入是一個清單，這意味著它可以一次接收並處理多張圖像。`folder_name` 和 `filename_prefix` 參數是純量值；如果連接了一個清單，則只會使用該清單中的第一個值。

## 輸出結果

此節點沒有任何輸出。它是一個執行檔案系統儲存操作的輸出節點。
