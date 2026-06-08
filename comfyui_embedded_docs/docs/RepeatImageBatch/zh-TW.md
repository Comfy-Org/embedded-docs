RepeatImageBatch 節點旨在將指定的影像複製指定次數，從而建立一批完全相同的影像。此功能對於需要同一影像多個副本的操作非常有用，例如批次處理或資料擴增。

## 輸入

| 欄位 | 說明 | 資料類型 |
| --- | --- | --- |
| `影像` | 'image' 參數代表要複製的影像。它對於定義將在批次中重複的內容至關重要。 | `IMAGE` |
| `數量` | 'amount' 參數指定輸入影像應被複製的次數。它直接影響輸出批次的大小，允許靈活地建立批次。 | `INT` |

## 輸出

| 欄位 | 說明 | 資料類型 |
| --- | --- | --- |
| `影像` | 輸出是一個影像批次，其中每個影像都與輸入影像完全相同，並根據指定的 'amount' 進行複製。 | `IMAGE` |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RepeatImageBatch/zh-TW.md)
