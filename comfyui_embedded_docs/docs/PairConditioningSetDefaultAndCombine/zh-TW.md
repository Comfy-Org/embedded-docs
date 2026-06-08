**PairConditioningSetDefaultAndCombine** 節點會設定預設的條件化數值，並將其與輸入的條件化資料結合。它接收正向與負向條件化輸入及其對應的預設值，然後透過 ComfyUI 的鉤子系統進行處理，以產生包含預設數值的最終條件化輸出。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `positive` | 要處理的主要正向條件化輸入 | CONDITIONING | 是 | - |
| `negative` | 要處理的主要負向條件化輸入 | CONDITIONING | 是 | - |
| `positive_DEFAULT` | 作為備用值的預設正向條件化數值 | CONDITIONING | 是 | - |
| `negative_DEFAULT` | 作為備用值的預設負向條件化數值 | CONDITIONING | 是 | - |
| `hooks` | 用於自訂處理邏輯的選用鉤子群組 | HOOKS | 否 | - |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `positive` | 已處理並包含預設數值的正向條件化結果 | CONDITIONING |
| `negative` | 已處理並包含預設數值的負向條件化結果 | CONDITIONING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PairConditioningSetDefaultAndCombine/zh-TW.md)

---
**Source fingerprint (SHA-256):** `dfa47d0fe02e81db8b68d20ae9b765c2518773f4f7fc8caf774cb870267dbb21`
