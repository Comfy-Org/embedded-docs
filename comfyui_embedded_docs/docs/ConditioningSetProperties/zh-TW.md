> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetProperties/zh-TW.md)

## 概述

ConditioningSetProperties 節點透過調整強度、區域設定以及應用可選的遮罩或時間步範圍，來修改條件化資料的屬性。它允許您設定特定參數來控制條件化資料在圖像生成過程中的應用方式，從而影響條件化對生成過程的作用。

## 輸入

| 參數名稱 | 資料類型 | 輸入類型 | 預設值 | 範圍 | 描述 |
|-----------|-----------|------------|---------|-------|-------------|
| `cond_NEW` | CONDITIONING | 必填 | - | - | 要修改的條件化資料 |
| `強度` | FLOAT | 必填 | 1.0 | 0.0-10.0 | 控制條件化效果的強度 |
| `設定條件區域` | STRING | 必填 | default | ["default", "mask bounds"] | 決定條件化區域的應用方式 |
| `遮罩` | MASK | 可選 | - | - | 用於限制條件化應用區域的可選遮罩 |
| `hooks` | HOOKS | 可選 | - | - | 用於自定義處理的可選掛鉤函數 |
| `時間步驟` | TIMESTEPS_RANGE | 可選 | - | - | 用於限制條件化生效時間的可選時間步範圍 |

**注意：** 當提供 `mask` 時，可將 `set_cond_area` 參數設定為 "mask bounds"，以將條件化應用限制在遮罩區域內。

## 輸出

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `CONDITIONING` | CONDITIONING | 具有更新屬性的修改後條件化資料 |