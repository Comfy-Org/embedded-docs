# 垂直負向引導器

## 概述

PerpNegGuider 節點建立了一個引導系統，用於透過垂直負面條件化來控制影像生成。它接收正面、負面和空條件化輸入，並應用專門的引導演算法來引導生成過程。此節點專為實驗性測試而設計，並提供對引導強度和負面縮放的精細控制。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 用於引導生成的模型 | MODEL | 是 | - |
| `正向` | 正面條件化，引導生成朝向期望的內容 | CONDITIONING | 是 | - |
| `負向` | 負面條件化，引導生成遠離不想要的內容 | CONDITIONING | 是 | - |
| `空條件` | 空或中性的條件化，用作基準參考 | CONDITIONING | 是 | - |
| `cfg` | 無分類器引導尺度，控制條件化影響生成的程度（預設值：8.0） | FLOAT | 是 | 0.0 - 100.0 |
| `負向比例` | 負面縮放因子，調整負面條件化的強度（預設值：1.0） | FLOAT | 是 | 0.0 - 100.0 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `guider` | 一個已配置的引導系統，可直接用於生成流程中 | GUIDER |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PerpNegGuider/zh-TW.md)

---
**Source fingerprint (SHA-256):** `efd3f78d461ade9d16885923875bacffb5afeafcbe32fc2d207598e0efe3a8c6`
