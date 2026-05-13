> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadTrainingDataset/zh-TW.md)

# 載入訓練資料集

此節點載入先前已儲存至磁碟的編碼訓練資料集。它會在 ComfyUI 輸出目錄中指定的資料夾內搜尋並讀取所有資料分片檔案，然後傳回合併後的潛在向量與條件化資料，以供訓練工作流程使用。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `folder_name` | STRING | 是 | 不適用 | 包含已儲存資料集的資料夾名稱，位於 ComfyUI 輸出目錄內（預設值："training_dataset"）。 |

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `latents` | LATENT | 潛在字典的清單，其中每個字典包含一個帶有張量的 `"samples"` 鍵。 |
| `conditioning` | CONDITIONING | 條件化清單的清單，其中每個內部清單包含對應樣本的條件化資料。 |

---
**Source fingerprint (SHA-256):** `0a07c97e2c6a32f77cd21ea7dbdd33e06fad82285696b88122fef369307e133d`
