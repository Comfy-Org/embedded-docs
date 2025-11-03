> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewImage/zh-TW.md)

PreviewImage 節點專為建立臨時預覽影像而設計。它會自動為每個影像產生唯一的臨時檔案名稱，將影像壓縮至指定等級，並將其儲存至臨時目錄。此功能在處理過程中生成影像預覽時特別有用，且不會影響原始檔案。

## 輸入參數

| 參數名稱 | 資料類型 | 描述 |
|-----------|-------------|-------------|
| `images`  | IMAGE     | 此 'images' 輸入參數指定了要處理並儲存為臨時預覽影像的影像內容。這是節點的主要輸入，決定了哪些影像將進行預覽生成流程。 |

## 輸出結果

本節點沒有輸出類型。