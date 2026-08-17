# 儲存訓練資料集

此節點會將準備好的訓練資料集儲存到電腦的硬碟中。它接收編碼後的資料（包含影像潛在變數及其對應的文字條件），並將其整理為多個較小的檔案（稱為 shard）以便管理。節點會自動在 datasets 目錄中建立資料夾，並同時儲存 shard 資料檔與描述該資料集的中繼資料檔。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `latents` | 來自 MakeTrainingDataset 的潛在變數 dict 清單。 | LATENT | 是 | N/A |
| `conditioning` | 來自 MakeTrainingDataset 的 conditioning 清單清單。 | CONDITIONING | 是 | N/A |
| `folder_name` | 要在 datasets 目錄中儲存資料集的資料夾名稱。允許使用如 'project/run1' 的子資料夾。（預設值："training_dataset"） | STRING | 是 | N/A |
| `shard_size` | 每個 shard 檔案中的樣本數量。（預設值：1000） | INT | 是 | 1 至 100000 |

**注意：** `latents` 清單中的項目數量必須與 `conditioning` 清單中的項目數量完全相符。若兩者數量不符，節點會回報錯誤。`folder_name` 必須指定 datasets 目錄下的子資料夾：datasets 根目錄本身，以及任何逸出該目錄的路徑（例如 '..' 或絕對路徑），都會被拒絕。

## 輸出

此節點不會產生任何輸出資料。它會將資料集儲存為編號的 shard 檔案（例如 `shard_0000.pkl`）以及 `metadata.json` 檔案，儲存在 datasets 目錄中所選的資料夾內。

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveTrainingDataset/zh-TW.md)

---
**Source fingerprint (SHA-256):** `6d7b63a24ac42907b0f4a1358712cd0ed085982ecd308bce87e5376d9bbc2274`
