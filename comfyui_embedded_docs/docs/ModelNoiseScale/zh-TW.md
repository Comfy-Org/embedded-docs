# 模型雜訊尺度

## 概述

此節點調整模型取樣期間所使用的雜訊比例。它允許您設定特定的雜訊比例值，以控制套用至模型取樣過程的雜訊量。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `模型` | 要套用雜訊比例調整的模型。 | MODEL | 是 | - |
| `雜訊尺度` | 絕對訓練雜訊比例。例如 HiDream-O1 base：8.0，dev：7.5。（預設值：1.0） | FLOAT | 是 | 0.0 至 64.0 (step: 0.01) |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `MODEL` | 已套用新雜訊比例的修改後模型。 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelNoiseScale/zh-TW.md)

---
**Source fingerprint (SHA-256):** `75b0b99323fc15ff3cafc23de05a9d6b52d059494fbc229e5fb685d2908dd5d3`
