# 條件設定（影片區域百分比）

ConditioningSetAreaPercentageVideo 節點透過定義特定區域和時間區段來修改 conditioning 資料，以進行影片生成。它允許您使用相對於整體尺寸的百分比值，來設定 conditioning 套用區域的位置、大小和持續時間。這對於將生成聚焦在影片序列的特定部分非常有用。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `conditioning` | 要修改的 conditioning 資料 | CONDITIONING | 是 | - |
| `width` | 區域寬度，以總寬度的百分比表示（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `height` | 區域高度，以總高度的百分比表示（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `temporal` | 區域的時間持續時間，以總影片長度的百分比表示（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `x` | 區域的水平起始位置，以百分比表示（預設值：0.0） | FLOAT | 是 | 0.0 - 1.0 |
| `y` | 區域的垂直起始位置，以百分比表示（預設值：0.0） | FLOAT | 是 | 0.0 - 1.0 |
| `z` | 區域在影片時間軸上的時間起始位置，以百分比表示（預設值：0.0） | FLOAT | 是 | 0.0 - 1.0 |
| `strength` | 套用至所定義區域內 conditioning 的強度乘數（預設值：1.0） | FLOAT | 是 | 0.0 - 10.0 |

注意：所有大小和位置值皆為相對於整體影片尺寸與時間軸的正規化百分比（0.0 至 1.0）。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `conditioning` | 已套用指定區域與強度設定的修改後 conditioning 資料 | CONDITIONING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetAreaPercentageVideo/zh-TW.md)

---
**Source fingerprint (SHA-256):** `9c5ddae6a2b1da5907fb52ef625eefb12b0b228fd3bd52c3033b5c4226d76150`
