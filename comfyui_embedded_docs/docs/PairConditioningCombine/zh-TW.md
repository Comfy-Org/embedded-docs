> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PairConditioningCombine/zh-TW.md)

PairConditioningCombine 節點將兩組條件資料（正面與負面）合併為單一組。它接收兩個獨立的條件配對作為輸入，並使用 ComfyUI 的內部條件組合邏輯進行合併。此節點屬於實驗性功能，主要用於進階條件操作工作流程。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `positive_A` | CONDITIONING | 是 | - | 第一組正面條件輸入 |
| `negative_A` | CONDITIONING | 是 | - | 第一組負面條件輸入 |
| `positive_B` | CONDITIONING | 是 | - | 第二組正面條件輸入 |
| `negative_B` | CONDITIONING | 是 | - | 第二組負面條件輸入 |

## 輸出結果

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | 合併後的正面條件輸出 |
| `negative` | CONDITIONING | 合併後的負面條件輸出 |