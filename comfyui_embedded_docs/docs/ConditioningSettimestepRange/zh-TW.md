> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetTimestepRange/zh-TW.md)

{heading_overview}

此節點旨在透過設定特定的時間步長範圍來調整條件化的時間維度。它允許精確控制條件化過程的開始和結束點，從而實現更具針對性和效率的生成。

{heading_inputs}

| 參數 | 資料類型 | 描述 |
| --- | --- | --- |
| `CONDITIONING` | CONDITIONING | 條件化輸入代表生成過程的當前狀態，此節點透過設定特定的時間步長範圍來修改此狀態。 |
| `start` | `FLOAT` | start 參數指定時間步長範圍的起始點，以總生成過程的百分比表示，允許精細控制條件化效果開始的時間。 |
| `end` | `FLOAT` | end 參數定義時間步長範圍的結束點，以百分比表示，可精確控制條件化效果的持續時間和結束點。 |

{heading_outputs}

| 參數 | 資料類型 | 描述 |
| --- | --- | --- |
| `CONDITIONING` | CONDITIONING | 輸出是應用指定時間步長範圍後的修改條件化，準備進行進一步處理或生成。 |