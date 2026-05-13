> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PairConditioningSetDefaultAndCombine/zh-TW.md)

**PairConditioningSetDefaultAndCombine** 節點會設定預設的條件化數值，並將其與輸入的條件化資料結合。它接收正向與負向條件化輸入及其對應的預設值，然後透過 ComfyUI 的鉤子系統進行處理，以產生包含預設數值的最終條件化輸出。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | 是 | - | 要處理的主要正向條件化輸入 |
| `negative` | CONDITIONING | 是 | - | 要處理的主要負向條件化輸入 |
| `positive_DEFAULT` | CONDITIONING | 是 | - | 作為備用值的預設正向條件化數值 |
| `negative_DEFAULT` | CONDITIONING | 是 | - | 作為備用值的預設負向條件化數值 |
| `hooks` | HOOKS | 否 | - | 用於自訂處理邏輯的選用鉤子群組 |

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | 已處理並包含預設數值的正向條件化結果 |
| `negative` | CONDITIONING | 已處理並包含預設數值的負向條件化結果 |

---
**Source fingerprint (SHA-256):** `dfa47d0fe02e81db8b68d20ae9b765c2518773f4f7fc8caf774cb870267dbb21`
