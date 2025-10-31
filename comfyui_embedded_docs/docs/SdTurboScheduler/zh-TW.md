> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SDTurboScheduler/zh-TW.md)

SDTurboScheduler 專為生成圖像採樣用的 sigma 值序列而設計，能根據指定的降噪等級和步驟數量調整序列。它利用特定模型的採樣能力來產生這些 sigma 值，這些值對於控制圖像生成過程中的降噪處理至關重要。

## 輸入參數

| 參數名稱 | 資料類型 | 描述 |
| --- | --- | --- |
| `model` | `MODEL` | 此參數指定用於生成 sigma 值的生成模型，對於決定調度器的具體採樣行為和能力至關重要。 |
| `步驟` | `INT` | 此參數決定要生成的 sigma 序列長度，直接影響降噪過程的細緻程度。 |
| `去雜訊強度` | `FLOAT` | 此參數調整 sigma 序列的起始點，可對圖像生成過程中應用的降噪等級進行更精細的控制。 |

## 輸出參數

| 參數名稱 | 資料類型 | 描述 |
| --- | --- | --- |
| `sigmas` | `SIGMAS` | 根據指定模型、步驟數和降噪等級生成的 sigma 值序列，這些值對於控制圖像生成過程中的降噪處理至關重要。 |