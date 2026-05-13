> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ManualSigmas/zh-TW.md)

## 概述

ManualSigmas 節點允許您手動定義取樣過程的自訂噪聲等級（sigma）序列。您以字串形式輸入數字列表，節點會將其轉換為可供其他取樣節點使用的張量。這對於測試或建立特定的噪聲排程非常有用。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `sigmas` | STRING | 是 | 任何以逗號或空格分隔的數字 | 包含 sigma 值的字串。節點會從此字串中提取所有數字。例如："1, 0.5, 0.1" 或 "1 0.5 0.1"。預設值為 "1, 0.5"。 |

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `sigmas` | SIGMAS | 包含從輸入字串中提取的 sigma 值序列的張量。 |

---
**Source fingerprint (SHA-256):** `b815633dfea8f529f487f46b2d0464fa8c1045df8c4d4ef586bd36ad6f4a28db`
