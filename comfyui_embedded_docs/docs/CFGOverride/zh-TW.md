# CFG 覆蓋

CFG Override 節點允許您為取樣過程的特定範圍設定固定的 CFG（Classifier-Free Guidance，分類器自由引導）比例值，該範圍以總步數的百分比定義。當多個 CFG Override 節點連接時，鏈中離取樣器最近的節點在重疊範圍內具有優先權。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | 要套用 CFG override 的模型 | MODEL | 是 | |
| `cfg` | 在覆寫範圍內使用的固定 CFG 比例值（預設值：1.0） | FLOAT | 是 | 0.0 to 100.0 |
| `start_percent` | 覆寫範圍的起點，以取樣過程的百分比表示（預設值：0.0） | FLOAT | 是 | 0.0 to 1.0 |
| `end_percent` | 覆寫範圍的終點，以取樣過程的百分比表示（預設值：1.0） | FLOAT | 是 | 0.0 to 1.0 |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `MODEL` | 已套用 CFG override 包裝器的模型 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CFGOverride/zh-TW.md)

---
**Source fingerprint (SHA-256):** `94c7d3751d90b42479f9cec4bdb3c95eeda405f51224f85d313ff12ec071ec58`
