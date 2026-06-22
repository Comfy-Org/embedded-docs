# 條件設定（Stable Audio）

## 概述

ConditioningStableAudio 節點會為音訊生成的正向與負向條件輸入添加時間資訊。它設定開始時間與總持續時間參數，有助於控制音訊內容應在何時生成以及生成多長時間。此節點透過附加音訊特定的時間元資料來修改現有條件資料。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `正向` | 將被添加音訊時間資訊的正向條件輸入 | CONDITIONING | 是 | - |
| `負向` | 將被添加音訊時間資訊的負向條件輸入 | CONDITIONING | 是 | - |
| `起始秒數` | 音訊生成的開始時間（秒），預設值：0.0 | FLOAT | 是 | 0.0 至 1000.0 |
| `總秒數` | 音訊生成的總持續時間（秒），預設值：47.0 | FLOAT | 是 | 0.0 至 1000.0 |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `負向` | 已套用音訊時間資訊的修改後正向條件 | CONDITIONING |
| `負向` | 已套用音訊時間資訊的修改後負向條件 | CONDITIONING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningStableAudio/zh-TW.md)

---
**Source fingerprint (SHA-256):** `ad4fdb2ac536e4f9cc23c044a7a63333e3f3530cc782937eaedc1565cc7c5d0e`
