> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadTrainingDataset/zh-TW.md)

此節點載入先前已儲存至磁碟的編碼訓練資料集。它會從 ComfyUI 輸出目錄內的指定資料夾中搜尋並讀取所有資料分片檔案，然後傳回合併後的潛在向量和條件資料，以供訓練工作流程使用。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `folder_name` | STRING | 否 | N/A | 包含已儲存資料集的資料夾名稱，位於 ComfyUI 輸出目錄內（預設值："training_dataset"）。 |

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `latents` | LATENT | 潛在字典的清單，其中每個字典包含一個帶有張量的 `"samples"` 鍵。 |
| `conditioning` | CONDITIONING | 條件清單的清單，其中每個內部清單包含對應樣本的條件資料。 |
