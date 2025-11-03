> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetPropertiesAndCombine/zh-TW.md)

此節點透過將新條件輸入的屬性應用到現有條件輸入來修改條件資料。它結合了兩個條件集，同時控制新條件的強度並指定條件區域的應用方式。

## 輸入參數

| 參數名稱 | 資料類型 | 輸入類型 | 預設值 | 範圍 | 描述 |
|-----------|-----------|------------|---------|-------|-------------|
| `cond` | CONDITIONING | 必填 | - | - | 要被修改的原始條件資料 |
| `cond_NEW` | CONDITIONING | 必填 | - | - | 提供要應用屬性的新條件資料 |
| `強度` | FLOAT | 必填 | 1.0 | 0.0 - 10.0 | 控制新條件屬性的強度 |
| `設定條件區域` | STRING | 必填 | default | ["default", "mask bounds"] | 決定條件區域的應用方式 |
| `遮罩` | MASK | 選填 | - | - | 用於定義特定條件區域的選用遮罩 |
| `hooks` | HOOKS | 選填 | - | - | 用於自訂處理的選用掛鉤函數 |
| `時間步驟` | TIMESTEPS_RANGE | 選填 | - | - | 用於控制條件應用時機的選用時間步範圍 |

**注意：** 當提供 `mask` 時，`set_cond_area` 參數可以使用 "mask bounds" 來將條件應用限制在遮罩區域內。

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `CONDITIONING` | CONDITIONING | 具有修改後屬性的合併條件資料 |