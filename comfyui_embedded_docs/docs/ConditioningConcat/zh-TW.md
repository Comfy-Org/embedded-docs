# 條件（串接）

ConditioningConcat 節點旨在串接條件向量，具體是將 'conditioning_from' 向量合併到 'conditioning_to' 向量中。此操作在需要將來自兩個來源的條件資訊組合成單一統一表示時至關重要。

## 輸入

| 參數 | 說明 | Comfy 資料類型 |
| --- | --- | --- |
| `conditioning_to` | 代表主要的條件向量集合，'conditioning_from' 向量將被串接到此集合中。它作為串接過程的基礎。 | `CONDITIONING` |
| `conditioning_from` | 包含將被串接到 'conditioning_to' 向量的條件向量。此參數允許將額外的條件資訊整合到現有集合中。 | `CONDITIONING` |

## 輸出

| 參數 | 說明 | Comfy 資料類型 |
| --- | --- | --- |
| `conditioning` | 輸出為統一的條件向量集合，由 'conditioning_from' 向量串接到 'conditioning_to' 向量後產生。 | `CONDITIONING` |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningConcat/zh-TW.md)
