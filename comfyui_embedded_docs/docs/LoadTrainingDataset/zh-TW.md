# 載入訓練資料集

此節點載入先前儲存到磁碟的編碼訓練資料集（潛在變數與條件資料）。它會從 datasets 目錄中選定的資料集資料夾讀取所有資料分片檔案，並傳回合併後的潛在變數向量與條件資料，以供訓練工作流程使用。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `folder_name` | 要載入的已儲存資料集，來自 datasets 目錄。 | COMBO | 是 | 在 datasets 目錄中找到的每個資料集資料夾對應一個選項 |

注意：`folder_name` 的選項會透過掃描 datasets 目錄自動建立。當一個子資料夾包含 `metadata.json` 檔案或至少一個 `.safetensors` 檔案時，就會被列為資料集。選定的資料集資料夾會在所有已設定的資料集根目錄中搜尋。此節點會讀取所選資料夾中所有名為 `shard_*.pkl` 的檔案，如果找不到任何分片檔案，則會引發錯誤。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `latents` | 潛在變數字典的清單，其中每個字典包含一個帶有張量的 `"samples"` 鍵。 | LATENT |
| `conditioning` | 條件清單的清單，其中每個內部清單包含對應樣本的條件資料。 | CONDITIONING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadTrainingDataset/zh-TW.md)

---
**Source fingerprint (SHA-256):** `9f914b27f067460f6f3b54f3f2a7bb793c65b99c85e8aa14ab64894be26bd816`
