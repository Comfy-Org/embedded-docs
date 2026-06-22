# ByteDance Seed

## 概述

使用 ByteDance 的 Seed 2.0 模型生成文字回應。提供文字提示，並可選擇包含圖片或影片以提供多模態上下文。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `提示詞` | 輸入至模型的文字。 | STRING | 是 | 不適用 |
| `模型` | 用於生成回應的 Seed 模型。 | COMBO | 是 | `"Seed 2.0 Pro"`<br>`"Seed 2.0 Lite"`<br>`"Seed 2.0 Mini"` |
| `隨機種子` | Seed 控制節點是否應重新執行；無論 seed 為何，結果皆非確定性。（預設值：0） | INT | 是 | 0 至 2147483647 |
| `系統提示` | 決定模型行為的基礎指令。（預設值：""） | STRING | 否 | 不適用 |

**關於 `model` 參數的說明：** `model` 參數是一個動態組合，也可接受圖片和影片。您可以將圖片和影片輸入連接到此參數，以提供多模態上下文。每個請求最多支援 20 張圖片和 4 部影片。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `output` | 從 Seed 模型生成的文字回應。 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `d1ef73cf72e88216d40c0cf727f90c40cf783cecabe3be0e7530fe72dba6c172`
