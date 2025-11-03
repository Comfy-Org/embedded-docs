> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PairConditioningSetDefaultAndCombine/zh-TW.md)

PairConditioningSetDefaultAndCombine 節點用於設定預設的條件設定值，並將其與輸入的條件設定資料進行合併。該節點接收正向與負向的條件設定輸入及其對應的預設值，然後透過 ComfyUI 的掛鉤系統進行處理，最終產生包含預設值的最終條件設定輸出。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | 是 | - | 要進行處理的主要正向條件設定輸入 |
| `negative` | CONDITIONING | 是 | - | 要進行處理的主要負向條件設定輸入 |
| `positive_DEFAULT` | CONDITIONING | 是 | - | 作為備用值的預設正向條件設定值 |
| `negative_DEFAULT` | CONDITIONING | 是 | - | 作為備用值的預設負向條件設定值 |
| `hooks` | HOOKS | 否 | - | 用於自訂處理邏輯的選用掛鉤群組 |

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | 已處理並包含預設值的正向條件設定 |
| `negative` | CONDITIONING | 已處理並包含預設值的負向條件設定 |