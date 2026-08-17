# 模型取樣 Stable Cascade

ModelSamplingStableCascade 節點透過調整取樣參數與 shift 值，對模型套用穩定級聯取樣。此節點會建立一個輸入模型的修改克隆，並為穩定級聯生成設定自訂的取樣配置。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 要套用穩定級聯取樣的輸入模型 | MODEL | 是 | - |
| `shift` | 套用至取樣參數的位移值（預設值：2.0） | FLOAT | 是 | 0.0 - 100.0（間距：0.01） |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `model` | 已套用穩定級聯取樣的修改後模型 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingStableCascade/zh-TW.md)

---
**Source fingerprint (SHA-256):** `358681a7c698d4335cde60780d5a8b134b75df4ea40102bf51544c53bbb08c42`
