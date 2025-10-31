> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetDefaultAndCombine/zh-TW.md)

此節點使用基於掛鉤的系統將條件化資料與預設條件化資料結合。它接收主要條件化輸入和預設條件化輸入，然後根據指定的掛鉤配置將它們合併。結果是包含兩個來源的單一條件化輸出。

## 輸入參數

| 參數名稱 | 資料類型 | 輸入類型 | 預設值 | 數值範圍 | 描述 |
|-----------|-----------|------------|---------|-------|-------------|
| `cond` | CONDITIONING | 必填 | - | - | 要處理的主要條件化輸入 |
| `cond_DEFAULT` | CONDITIONING | 必填 | - | - | 要與主要條件化結合的預設條件化資料 |
| `hooks` | HOOKS | 選填 | - | - | 控制條件化資料處理和合併方式的選填掛鉤配置 |

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `CONDITIONING` | CONDITIONING | 合併主要和預設條件化輸入後產生的組合條件化資料 |