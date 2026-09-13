# CFG 覆蓋

CFG Override 節點會在取樣過程的某個百分比（sigma）範圍內，將 CFG（Classifier-Free Guidance）縮放值覆寫為固定值。當使用多個 CFG Override 節點時，在重疊範圍內，最接近取樣器的覆寫設定會優先生效。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `模型` | 要套用 CFG 覆寫的模型。 | MODEL | 是 | |
| `cfg` | 在覆寫範圍內使用的固定 CFG 縮放值。預設值：1.0。 | FLOAT | 是 | 0.0 至 100.0 （步進值：0.1） |
| `起始百分比` | 覆寫範圍的起始點，以取樣過程的百分比表示。預設值：0.0。 | FLOAT | 是 | 0.0 至 1.0 （步進值：0.001） |
| `結束百分比` | 覆寫範圍的結束點，以取樣過程的百分比表示。預設值：1.0。 | FLOAT | 是 | 0.0 至 1.0 （步進值：0.001） |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `MODEL` | 已套用 CFG 覆寫包裝器的模型。 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CFGOverride/zh-TW.md)

---
**Source fingerprint (SHA-256):** `94c7d3751d90b42479f9cec4bdb3c95eeda405f51224f85d313ff12ec071ec58`
