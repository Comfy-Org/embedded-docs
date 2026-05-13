> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveTrainingDataset/zh-TW.md)

## 概述

此節點將準備好的訓練資料集儲存到電腦的硬碟中。它接收編碼後的資料（包含影像潛在表示及其對應的文字條件），並將它們組織成多個較小的檔案（稱為分片），以便於管理。節點會自動在輸出目錄中建立一個資料夾，並同時儲存資料檔案與描述該資料集的中繼資料檔案。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `latents` | LATENT | 是 | 無 | 來自 MakeTrainingDataset 的潛在字典列表。 |
| `conditioning` | CONDITIONING | 是 | 無 | 來自 MakeTrainingDataset 的條件列表列表。 |
| `folder_name` | STRING | 否 | 無 | 用於儲存資料集的資料夾名稱（位於輸出目錄內）。（預設值："training_dataset"） |
| `shard_size` | INT | 否 | 1 至 100000 | 每個分片檔案中的樣本數量。（預設值：1000） |

**注意：** `latents` 列表中的項目數量必須與 `conditioning` 列表中的項目數量完全相符。如果數量不符，節點將會引發錯誤。

## 輸出

此節點不會產生任何輸出資料。其功能是將檔案儲存到您的磁碟中。

---
**Source fingerprint (SHA-256):** `1b0108be7362c0cb8ba16ffbf94cf42be2d04159aacbabe1ff0890083d1733b3`
