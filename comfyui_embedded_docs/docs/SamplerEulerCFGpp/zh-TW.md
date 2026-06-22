# SamplerEulerCFG++

SamplerEulerCFGpp 節點提供了一種 Euler CFG++ 取樣方法，用於生成輸出。此節點提供兩種不同實作版本的 Euler CFG++ 取樣器，可根據使用者偏好進行選擇。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `版本` | 要使用的 Euler CFG++ 取樣器實作版本（預設值："regular"） | STRING | 是 | `"regular"`<br>`"alternative"` |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `sampler` | 返回一個已配置的 Euler CFG++ 取樣器實例 | SAMPLER |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerEulerCFGpp/zh-TW.md)

---
**Source fingerprint (SHA-256):** `f01732fc39a76fca697aaddefc8cec58d54ba9761eb8d93da806ddd162d42513`
