# 條件集屬性

ConditioningSetProperties 節點透過調整強度、區域設定以及應用可選遮罩、鉤子或時間步範圍來修改條件資料的屬性。它允許您透過設定特定參數來控制條件如何影響生成過程，這些參數會影響條件資料在圖像生成期間的應用方式。

## 輸入

| 參數 | 說明 | 資料類型 | 輸入類型 | 預設值 | 範圍 |
| --- | --- | --- | --- | --- | --- |
| `cond_NEW` | 要修改的條件資料 | CONDITIONING | 必要 | - | - |
| `強度` | 控制條件效果的強度 | FLOAT | 必要 | 1.0 | 0.0 - 10.0 (步長: 0.01) |
| `設定條件區域` | 決定條件區域的應用方式。選擇 "default" 使用標準行為，或選擇 "mask bounds" 限制在遮罩區域內 | STRING | 必要 | default | ["default", "mask bounds"] |
| `遮罩` | 可選遮罩，用於限制條件應用的區域 | MASK | 可選 | - | - |
| `hooks` | 用於自訂處理的可選鉤子函數 | HOOKS | 可選 | - | - |
| `時間步驟` | 可選時間步範圍，用於限制條件生效的時間 | TIMESTEPS_RANGE | 可選 | - | - |

**注意：** 當提供 `mask` 時，可以將 `set_cond_area` 參數設定為 "mask bounds"，以將條件應用限制在遮罩區域內。`hooks` 參數允許透過鉤子函數進行自訂處理，而 `timesteps` 則將條件效果限制在生成過程中的特定時間步範圍內。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `CONDITIONING` | 已更新屬性的修改後條件資料 | CONDITIONING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetProperties/zh-TW.md)

---
**Source fingerprint (SHA-256):** `5e3f5348f6df8f2fa1c1d42b883efcab3ee07d933e219f11fa48730aacc168d7`
