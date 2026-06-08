SDTurboScheduler 旨在生成用於影像取樣的 sigma 值序列，並根據指定的去噪程度與步驟數量調整該序列。它利用特定模型的取樣能力來產生這些 sigma 值，這對於控制影像生成過程中的去噪流程至關重要。

## 輸入

| 參數 | 說明 | 資料類型 |
| --- | --- | --- |
| `model` | 此 model 參數指定用於產生 sigma 值的生成模型，對於決定排程器的特定取樣行為與能力至關重要。 | `MODEL` |
| `步驟` | 此 steps 參數決定要生成的 sigma 序列長度，直接影響去噪過程的細緻程度。 | `INT` |
| `去雜訊強度` | 此 denoise 參數調整 sigma 序列的起始點，讓您能更精細地控制影像生成時所應用的去噪程度。 | `FLOAT` |

## 輸出

| 參數 | 說明 | 資料類型 |
| --- | --- | --- |
| `sigmas` | 根據指定的 model、steps 與 denoise 程度所產生的 sigma 值序列。這些數值對於控制影像生成中的去噪過程至關重要。 | `SIGMAS` |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SDTurboScheduler/zh-TW.md)
