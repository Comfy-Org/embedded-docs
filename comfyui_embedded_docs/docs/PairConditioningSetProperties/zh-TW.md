> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PairConditioningSetProperties/zh-TW.md)

PairConditioningSetProperties 節點允許您同時修改正向和負向條件對的屬性。它會對兩個條件輸入同時套用強度調整、條件區域設定以及可選的遮罩或時序控制，並返回修改後的正向和負向條件資料。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 參數說明 |
|-----------|-----------|----------|-------|-------------|
| `positive_NEW` | CONDITIONING | 是 | - | 要修改的正向條件輸入 |
| `negative_NEW` | CONDITIONING | 是 | - | 要修改的負向條件輸入 |
| `strength` | FLOAT | 是 | 0.0 至 10.0 | 套用至條件資料的強度乘數（預設值：1.0） |
| `set_cond_area` | STRING | 是 | "default"<br>"mask bounds" | 決定條件區域的計算方式 |
| `mask` | MASK | 否 | - | 用於限制條件區域的選用遮罩 |
| `hooks` | HOOKS | 否 | - | 用於進階條件修改的選用掛鉤群組 |
| `timesteps` | TIMESTEPS_RANGE | 否 | - | 用於限制條件套用時機的選用時間步範圍 |

## 輸出結果

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | 已套用屬性的修改後正向條件資料 |
| `negative` | CONDITIONING | 已套用屬性的修改後負向條件資料 |