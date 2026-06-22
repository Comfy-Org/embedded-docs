# LTXV 條件化

## 概述

LTXVConditioning 節點會將影格率資訊新增至影片生成模型的正向與負向條件輸入中。它會接收現有的條件資料，並將指定的影格率值套用至兩組條件設定，使其適用於影片模型處理。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `正向` | 將接收影格率資訊的正向條件輸入 | CONDITIONING | 是 | - |
| `負向` | 將接收影格率資訊的負向條件輸入 | CONDITIONING | 是 | - |
| `影格率` | 要套用至兩組條件設定的影格率值（預設值：25.0） | FLOAT | 是 | 0.0 - 1000.0 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `負向` | 已套用影格率資訊的正向條件 | CONDITIONING |
| `負向` | 已套用影格率資訊的負向條件 | CONDITIONING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVConditioning/zh-TW.md)

---
**Source fingerprint (SHA-256):** `e8c18b73eb009c1b3ebcc2cb8be3dee4e065d75908607a5cf15d41f89963ee09`
