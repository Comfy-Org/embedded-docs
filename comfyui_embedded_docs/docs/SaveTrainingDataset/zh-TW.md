# 儲存訓練資料集

此節點會將編碼後的訓練資料集儲存至磁碟，以便在訓練期間有效率地載入。它會接收影像 latent 及其對應的文字 conditioning，將它們分割成稱為 shard 的較小檔案，並儲存在 datasets 目錄內的資料夾中。它也會寫入一個描述該資料集的 metadata 檔案。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `latents` | 來自 MakeTrainingDataset 的 latent 字典清單。 | LATENT | 是 | N/A |
| `conditioning` | 來自 MakeTrainingDataset 的 conditioning 清單列表。 | CONDITIONING | 是 | N/A |
| `folder_name` | 要將資料集儲存至 datasets 目錄內的資料夾名稱。允許使用如 'project/run1' 的子資料夾。（預設值："training_dataset"） | STRING | 是 | N/A |
| `shard_size` | 每個 shard 檔案的樣本數量。（預設值：1000） | INT | 是 | 1 至 100000 |

**注意：** `latents` 中的項目數量必須與 `conditioning` 中的項目數量完全相符；如果這些計數不相符，節點會擲回錯誤。`folder_name` 必須命名為 datasets 目錄的子資料夾（例如 `my_dataset`）——它不能是 datasets 目錄本身，且會解析到 datasets 目錄外部的資料夾名稱會被拒絕。`shard_size` 參數是進階設定。

## 輸出

此節點不會產生任何輸出資料。其功能是將檔案儲存到你的磁碟。每個 shard 會以 `shard_XXXX.pkl` 檔案儲存在所選資料夾中，並由 `metadata.json` 檔案記錄樣本總數、shard 數量以及 shard 大小。

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveTrainingDataset/zh-TW.md)

---
**Source fingerprint (SHA-256):** `6d7b63a24ac42907b0f4a1358712cd0ed085982ecd308bce87e5376d9bbc2274`
