# 載入訓練資料集

此節點從磁碟載入已編碼的訓練資料集（潛在變數與條件資料），以供訓練使用。在您選取先前儲存的資料集資料夾後，它會讀取其中所有分片檔案，並傳回合併後的潛在向量與條件資料。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `folder_name` | 要載入的已儲存資料集，來自資料集目錄。 | COMBO | 是 | 動態填入在已註冊資料集目錄中找到的所有資料集資料夾。僅列出包含 `metadata.json` 檔案或 `.safetensors` 檔案的資料夾。 |

**注意：** 所選的資料集資料夾必須是已註冊資料集目錄的子資料夾，且必須包含至少一個名為 `shard_*.pkl` 的分片檔案；否則節點會產生錯誤。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `latents` | 從資料集分片載入的潛在字典清單，每個字典包含一個 `samples` 張量。 | LATENT |
| `conditioning` | 從資料集分片載入的條件清單，每個樣本一個。 | CONDITIONING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadTrainingDataset/zh-TW.md)

---
**Source fingerprint (SHA-256):** `9f914b27f067460f6f3b54f3f2a7bb793c65b99c85e8aa14ab64894be26bd816`
