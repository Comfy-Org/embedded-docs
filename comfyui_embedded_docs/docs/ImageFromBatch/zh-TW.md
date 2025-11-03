> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageFromBatch/zh-TW.md)

{heading_overview}

`ImageFromBatch` 節點旨在根據提供的索引和長度，從批次中提取特定的圖像區段。它允許對批次圖像進行更精細的控制，便於在較大批次中對個別或子集圖像進行操作。

{heading_inputs}

| 欄位 | 資料類型 | 描述 |
|------|----------|------|
| `image` | `IMAGE` | 將從中提取區段的圖像批次。此參數對於指定來源批次至關重要。 |
| `batch_index` | `INT` | 批次中開始提取的起始索引。它決定了要從批次中提取的區段的起始位置。 |
| `length` | `INT` | 從 batch_index 開始從批次中提取的圖像數量。此參數定義了要提取的區段大小。 |

{heading_outputs}

| 欄位 | 資料類型 | 描述 |
|------|----------|------|
| `image` | `IMAGE` | 從指定批次中提取的圖像區段。此輸出代表原始批次的一個子集，由 batch_index 和 length 參數決定。 |