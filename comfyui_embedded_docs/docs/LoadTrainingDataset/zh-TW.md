# 載入訓練資料集

此節點載入先前已儲存至磁碟的已編碼訓練資料集（latents 與 conditioning）。它會從 datasets 目錄中選定的資料集資料夾讀取所有 `shard_*.pkl` 資料分片檔案，並回傳合併後的 latent 向量與 conditioning 資料，以供訓練工作流程使用。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `folder_name` | 要載入的已儲存資料集，來自 datasets 目錄。 | COMBO | 是 | datasets 目錄中找到的每個資料集資料夾各一個選項 |

注意：`folder_name` 選項會透過掃描 datasets 目錄自動建立。當子資料夾包含 `metadata.json` 檔案或至少一個 `.safetensors` 檔案時，該子資料夾會列為資料集（掃描不會進入符合此條件的資料夾）。系統會在所有已設定的資料集根目錄中搜尋所選的資料集資料夾，且該資料夾名稱必須解析為其中一個根目錄內的子資料夾。此節點會依排序順序讀取所選資料夾中所有名為 `shard_*.pkl` 的檔案，若找不到任何分片檔案或無法定位該資料夾，則會引發錯誤。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `latents` | latent 字典的清單（輸出的清單），其中每個字典包含一個帶有張量的 `"samples"` 鍵。 | LATENT |
| `conditioning` | conditioning 清單的清單（輸出的清單），其中每個內部清單包含對應樣本的 conditioning 資料。 | CONDITIONING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadTrainingDataset/zh-TW.md)

---
**Source fingerprint (SHA-256):** `9f914b27f067460f6f3b54f3f2a7bb793c65b99c85e8aa14ab64894be26bd816`
