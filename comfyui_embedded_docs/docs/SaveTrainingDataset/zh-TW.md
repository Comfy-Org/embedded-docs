> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveTrainingDataset/zh-TW.md)

此節點將準備好的訓練資料集儲存到電腦硬碟中。它接收已編碼的資料（包含圖像潛在表示及其對應的文字條件），並將它們組織成多個較小的檔案（稱為分片）以便於管理。節點會自動在輸出目錄中建立資料夾，並儲存資料檔案以及描述資料集的中繼資料檔案。

## 輸入參數

| 參數 | 資料類型 | 必填 | 範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `latents` | LATENT | 是 | N/A | 來自 MakeTrainingDataset 的潛在字典列表。 |
| `conditioning` | CONDITIONING | 是 | N/A | 來自 MakeTrainingDataset 的條件列表。 |
| `folder_name` | STRING | 否 | N/A | 儲存資料集的資料夾名稱（位於輸出目錄內）。(預設："training_dataset") |
| `shard_size` | INT | 否 | 1 至 100000 | 每個分片檔案包含的樣本數量。(預設：1000) |

**注意：** `latents` 列表中的項目數量必須與 `conditioning` 列表中的項目數量完全一致。如果數量不符，節點將引發錯誤。

## 輸出結果

此節點不產生任何輸出資料。其功能是將檔案儲存到您的磁碟。
