> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PairConditioningSetPropertiesAndCombine/zh-TW.md)

PairConditioningSetPropertiesAndCombine 節點透過將新的調節資料應用到現有的正向和負向調節輸入，來修改並組合調節對。它允許您調整所應用調節的強度，並控制調節區域的設定方式。此節點在需要混合多個調節來源的進階調節操作工作流程中特別有用。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | 是 | - | 原始的正向調節輸入 |
| `negative` | CONDITIONING | 是 | - | 原始的負向調節輸入 |
| `positive_NEW` | CONDITIONING | 是 | - | 要應用的新正向調節 |
| `negative_NEW` | CONDITIONING | 是 | - | 要應用的新負向調節 |
| `strength` | FLOAT | 是 | 0.0 至 10.0 | 應用新調節的強度係數（預設值：1.0） |
| `set_cond_area` | STRING | 是 | "default"<br>"mask bounds" | 控制調節區域的應用方式 |
| `mask` | MASK | 否 | - | 用於限制調節應用區域的選用遮罩 |
| `hooks` | HOOKS | 否 | - | 用於進階控制的選用掛鉤群組 |
| `timesteps` | TIMESTEPS_RANGE | 否 | - | 選用的時間步範圍規格 |

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | 組合後的正向調節輸出 |
| `negative` | CONDITIONING | 組合後的負向調節輸出 |