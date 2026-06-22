# Cond Pair 組合

## 概述

PairConditioningCombine 節點將兩個獨立的條件配對（每個配對包含一個正向條件與一個負向條件）合併為單一組合配對。它從兩個不同來源取得正向與負向條件，並使用 ComfyUI 的內部邏輯進行合併，最終輸出一個正向條件與一個負向條件。此節點為實驗性功能，專為進階條件操控工作流程而設計。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `positive_A` | 第一個正向條件輸入 | CONDITIONING | 是 | - |
| `negative_A` | 第一個負向條件輸入 | CONDITIONING | 是 | - |
| `positive_B` | 第二個正向條件輸入 | CONDITIONING | 是 | - |
| `negative_B` | 第二個負向條件輸入 | CONDITIONING | 是 | - |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `負向` | 合併後的正向條件輸出 | CONDITIONING |
| `negative` | 合併後的負向條件輸出 | CONDITIONING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PairConditioningCombine/zh-TW.md)

---
**Source fingerprint (SHA-256):** `34c14207930ba31fea054b2e641e9666e738ed786aa117449c4a27667bde41b1`
