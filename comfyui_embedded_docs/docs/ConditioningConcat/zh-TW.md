> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningConcat/zh-TW.md)

{heading_overview}

ConditioningConcat 節點專門用於串接條件向量，特別是將 'conditioning_from' 向量合併到 'conditioning_to' 向量中。此操作在需要將來自兩個來源的條件資訊合併為單一統一表示的場景中至關重要。

{heading_inputs}

| 參數名稱             | Comfy 資料類型     | 描述 |
|-----------------------|--------------------|-------------|
| `conditioning_to`     | `CONDITIONING`     | 代表主要的條件向量集合，'conditioning_from' 向量將被串接至此。它作為串接過程的基礎。 |
| `conditioning_from`   | `CONDITIONING`     | 包含將被串接到 'conditioning_to' 向量的條件向量。此參數允許將額外的條件資訊整合到現有集合中。 |

{heading_outputs}

| 參數名稱            | Comfy 資料類型     | 描述 |
|----------------------|--------------------|-------------|
| `conditioning`       | `CONDITIONING`     | 輸出為統一的條件向量集合，由 'conditioning_from' 向量串接到 'conditioning_to' 向量的結果。 |