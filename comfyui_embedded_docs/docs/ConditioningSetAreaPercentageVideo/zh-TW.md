> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetAreaPercentageVideo/zh-TW.md)

## 概述

ConditioningSetAreaPercentageVideo 節點透過定義影片生成的特定區域與時間範圍來修改 conditioning 資料。您可以使用相對於整體尺寸的百分比值，設定 conditioning 將套用的區域位置、大小與持續時間。這對於將生成重點聚焦在影片序列的特定部分非常有用。

## 輸入

| 參數 | 資料類型 | 輸入類型 | 預設值 | 範圍 | 說明 |
|-----------|-----------|------------|---------|-------|-------------|
| `conditioning` | CONDITIONING | 必要 | - | - | 要修改的 conditioning 資料 |
| `width` | FLOAT | 必要 | 1.0 | 0.0 - 1.0 | 區域寬度佔總寬度的百分比 |
| `height` | FLOAT | 必要 | 1.0 | 0.0 - 1.0 | 區域高度佔總高度的百分比 |
| `temporal` | FLOAT | 必要 | 1.0 | 0.0 - 1.0 | 區域的時間持續時間佔總影片長度的百分比 |
| `x` | FLOAT | 必要 | 0.0 | 0.0 - 1.0 | 區域的水平起始位置百分比 |
| `y` | FLOAT | 必要 | 0.0 | 0.0 - 1.0 | 區域的垂直起始位置百分比 |
| `z` | FLOAT | 必要 | 0.0 | 0.0 - 1.0 | 區域在影片時間軸上的時間起始位置百分比 |
| `strength` | FLOAT | 必要 | 1.0 | 0.0 - 10.0 | 套用於定義區域內 conditioning 的強度乘數 |

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `conditioning` | CONDITIONING | 已套用指定區域與強度設定的修改後 conditioning 資料 |

---
**Source fingerprint (SHA-256):** `72d4bef4f8ddc4765cf69863f7ad03d34992f0ff30a963dbe2dc1b7d69815410`
