## 概述

Kling 虛擬試穿節點。輸入人物圖片和服裝圖片，即可在人物身上試穿該服裝。您可以將多張服飾商品圖片合併成一張白色背景的圖片。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `human_image` | 要進行試穿的人物圖片 | IMAGE | 是 | - |
| `cloth_image` | 要在人物身上試穿的服裝圖片 | IMAGE | 是 | - |
| `model_name` | 要使用的虛擬試穿模型（預設值："kolors-virtual-try-on-v1"） | STRING | 是 | `"kolors-virtual-try-on-v1"` |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `output` | 顯示人物穿上該服裝後的結果圖片 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingVirtualTryOnNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `bfd0da440d3ad85e15ce16851313f2e75421a8a3eb5e4c651350432955afc731`
