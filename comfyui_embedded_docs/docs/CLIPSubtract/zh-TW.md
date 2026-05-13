> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPSubtract/zh-TW.md)

## 概述

CLIPSubtract 節點在兩個 CLIP 模型之間執行減法運算。它將第一個 CLIP 模型作為基礎，並從第二個 CLIP 模型中減去關鍵修補程式，並可透過可選的乘數來控制減法強度。這允許透過使用另一個模型移除特定特徵來進行微調的模型混合。

## 輸入

| 參數 | 資料類型 | 輸入類型 | 預設值 | 範圍 | 描述 |
|-----------|-----------|------------|---------|-------|-------------|
| `clip1` | CLIP | 必要 | - | - | 將被修改的基礎 CLIP 模型 |
| `clip2` | CLIP | 必要 | - | - | 其關鍵修補程式將從基礎模型中減去的 CLIP 模型 |
| `multiplier` | FLOAT | 必要 | 1.0 | -10.0 至 10.0，步長 0.01 | 控制減法運算的強度。正值會減去 clip2 的特徵，負值則會添加特徵。 |

## 輸出

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `CLIP` | CLIP | 減法運算後產生的 CLIP 模型 |

---
**Source fingerprint (SHA-256):** `ea7b6f838d6eb083d2d9bc07891b6ef2f3e625861ab1de9279df351e58f2a2a8`
