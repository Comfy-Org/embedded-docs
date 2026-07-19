# CFGGuider

## 概述

CFGGuider 節點建立了一個引導系統，用於控制影像生成過程中的取樣流程。它接收一個模型以及正向與負向條件輸入，然後應用無分類器引導尺度，將生成過程導向期望內容，同時避免產生不需要的元素。此節點輸出一個引導器物件，可供取樣節點用於控制影像生成方向。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 用於引導的模型 | MODEL | 是 | - |
| `正向` | 正向條件，用於引導生成朝向期望內容 | CONDITIONING | 是 | - |
| `負向` | 負向條件，用於引導生成遠離不需要的內容 | CONDITIONING | 是 | - |
| `cfg` | 無分類器引導尺度，控制條件對生成的影響強度（預設值：8.0） | FLOAT | 是 | 0.0 至 100.0 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `GUIDER` | 一個引導器物件，可傳遞給取樣節點以控制生成過程 | GUIDER |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CFGGuider/zh-TW.md)

---
**Source fingerprint (SHA-256):** `80c1f733dc26717c5762655404b9c36b53bb9059ceb6a8531ef1a853e2fe2380`
