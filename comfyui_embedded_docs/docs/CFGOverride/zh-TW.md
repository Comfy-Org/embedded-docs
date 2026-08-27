# CFG 覆蓋

CFG Override 節點可讓您為取樣流程的特定範圍設定固定的 CFG（無分類器引導，Classifier-Free Guidance）強度值，該範圍以總步數的百分比定義。當連接多個 CFG Override 節點時，在鏈中離取樣器最近的節點對重疊範圍具有優先權。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `模型` | 要套用 CFG 覆寫的模型 | MODEL | 是 | |
| `cfg` | 在覆寫範圍內使用的固定 CFG 強度值（預設值：1.0） | FLOAT | 是 | 0.0 至 100.0 |
| `起始百分比` | 覆寫範圍的起點，以取樣流程的百分比表示（預設值：0.0） | FLOAT | 是 | 0.0 至 1.0 |
| `結束百分比` | 覆寫範圍的終點，以取樣流程的百分比表示（預設值：1.0） | FLOAT | 是 | 0.0 至 1.0 |

## 輸出

| 輸出名 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `MODEL` | 已套用 CFG 覆寫包裝器的模型 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CFGOverride/zh-TW.md)

---
**Source fingerprint (SHA-256):** `94c7d3751d90b42479f9cec4bdb3c95eeda405f51224f85d313ff12ec071ec58`
