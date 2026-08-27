# 儲存訓練資料集

此節點將編碼後的訓練資料集儲存到磁碟，以便在訓練期間高效載入。它接收圖像潛在變量及其對應的文字條件，將它們分割成稱為「分片」（shards）的較小檔案，並儲存在 datasets 目錄內的資料夾中。它還會寫入一個描述該資料集的 metadata 檔案。

## 輸入
| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `latents` | 來自 MakeTrainingDataset 的 latent 字典列表。 | LATENT | 是 | N/A |
| `conditioning` | 來自 MakeTrainingDataset 的 conditioning 列表的列表。 | CONDITIONING | 是 | N/A |
| `folder_name` | 在 datasets 目錄內儲存資料集的資料夾名稱。允許使用如 'project/run1' 的子資料夾。（預設值："training_dataset"） | STRING | 是 | N/A |
| `shard_size` | 每個分片檔案中的樣本數。（預設值：1000） | INT | 是 | 1 至 100000 |

**注意：** `latents` 中的項目數量必須與 `conditioning` 中的項目數量完全一致；如果數量不符，節點會引發錯誤。`folder_name` 必須指定 datasets 目錄的子資料夾（例如 `my_dataset`）——不能是 datasets 目錄本身，且解析到 datasets 目錄之外的路徑會被拒絕。

## 輸出
此節點不會產生任何輸出資料。其功能是將檔案儲存到您的磁碟。每個分片會以 `shard_XXXX.pkl` 檔案的形式儲存在所選資料夾中，而 `metadata.json` 檔案則記錄樣本總數、分片數量以及分片大小。

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveTrainingDataset/zh-TW.md)

---
**Source fingerprint (SHA-256):** `6d7b63a24ac42907b0f4a1358712cd0ed085982ecd308bce87e5376d9bbc2274`
