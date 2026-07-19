# ImageMorphology

## 概述

形態學節點對影像應用各種形態學運算，這些是用於處理和分析影像中形狀的數學運算。它可以執行侵蝕、膨脹、開運算、閉運算等操作，並使用可自訂的核心大小來控制效果強度。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `影像` | 要處理的輸入影像 | IMAGE | 是 | - |
| `操作` | 要套用的形態學運算（預設值："erode"） | STRING | 是 | `"erode"`<br>`"dilate"`<br>`"open"`<br>`"close"`<br>`"gradient"`<br>`"bottom_hat"`<br>`"top_hat"` |
| `核心大小` | 結構元素核心的大小（預設值：3）。必須為奇數。 | INT | 是 | 3-999 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `影像` | 應用形態學運算後處理完成的影像 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Morphology/zh-TW.md)

---
**Source fingerprint (SHA-256):** `7f6224a0e58fbb7263267b377394e119c6f8d65d16af4ce492ca9504654af7b4`
