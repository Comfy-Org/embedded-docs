# 模型雜訊尺度

此節點調整模型取樣期間使用的雜訊比例。您可以設定特定的雜訊比例值，以控制套用至模型取樣過程的雜訊量。此節點會複製模型，並以新的雜訊比例更新其取樣配置，同時保留現有的偏移（shift）與乘數（multiplier）設定。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 要套用雜訊比例調整的模型。 | MODEL | 是 | - |
| `noise_scale` | 絕對訓練雜訊比例。例如 HiDream-O1 base：8.0，dev：7.5。（預設值：1.0） | FLOAT | 是 | 0.0 至 64.0（步長：0.01） |

## 輸出

| 輸出名 | 說明 | 資料類型 |
| --- | --- | --- |
| `MODEL` | 套用新雜訊比例後的修改模型。 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelNoiseScale/zh-TW.md)

---
**Source fingerprint (SHA-256):** `75b0b99323fc15ff3cafc23de05a9d6b52d059494fbc229e5fb685d2908dd5d3`
