# 手動 Sigma

ManualSigmas 節點允許您手動定義取樣過程中自訂的噪聲水平（sigma 值）序列。您輸入一串以字串表示的數字，節點會將其轉換為可供其他取樣節點使用的張量。這對於測試或建立特定的噪聲調度非常有用。

## 輸入

| 參數 | 描述 | 資料型別 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `sigmas` | 包含 sigma 值的字串。節點會從此字串中提取所有數字，包括小數和負值。例如："1, 0.5, 0.1" 或 "1 0.5 0.1"。預設值："1, 0.5"。 | STRING | 是 | 任何以逗號或空格分隔的數值 |

注意：此節點標記為實驗性。

## 輸出

| 輸出名稱 | 描述 | 資料型別 |
| --- | --- | --- |
| `sigmas` | 包含從輸入字串中提取的 sigma 值序列的張量。 | SIGMAS |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ManualSigmas/zh-TW.md)

---
**Source fingerprint (SHA-256):** `19d938ef0eac7343a3138393a039f63632b0763e3884636653c06b91b6f44ed6`
