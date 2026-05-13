> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SkipLayerGuidanceSD3/zh-TW.md)

## 概述

SkipLayerGuidanceSD3 節點透過在跳層的情況下應用額外的無分類器引導，來增強對詳細結構的引導效果。此實驗性實作受到擾動注意力引導（Perturbed Attention Guidance）的啟發，其運作原理是在負面條件化過程中選擇性地繞過特定層，以改善生成輸出中的結構細節。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | 是 | - | 要套用跳層引導的模型 |
| `layers` | STRING | 是 | - | 要跳過的層索引，以逗號分隔（預設值："7, 8, 9"） |
| `scale` | FLOAT | 是 | 0.0 - 10.0 | 跳層引導效果的強度（預設值：3.0） |
| `start_percent` | FLOAT | 是 | 0.0 - 1.0 | 引導應用起始點，以總步數的百分比表示（預設值：0.01） |
| `end_percent` | FLOAT | 是 | 0.0 - 1.0 | 引導應用結束點，以總步數的百分比表示（預設值：0.15） |

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `model` | MODEL | 已套用跳層引導的修改後模型 |

---
**Source fingerprint (SHA-256):** `97c8220abd223bd35b4d0274c2b4536ffb6be7954ccd917943905bd22f60c1a5`
