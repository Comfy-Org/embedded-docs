# EmptyARVideoLatent

## 概述

EmptyARVideoLatent 節點會建立一個用於影片生成的空白潛在表示。它透過提供具有指定尺寸、長寬比和長度的零張量來初始化影片生成過程。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `寬度` | 影片幀的寬度（像素）（預設值：832） | INT | 是 | 16 至 8192 (步長：16) |
| `高度` | 影片幀的高度（像素）（預設值：480） | INT | 是 | 16 至 8192 (步長：16) |
| `長度` | 影片的幀數（預設值：81） | INT | 是 | 1 至 1024 (步長：4) |
| `批次大小` | 單一批次中生成的影片數量（預設值：1） | INT | 是 | 1 至 64 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `LATENT` | 一個填充零的潛在張量，代表具有指定尺寸、長度和批次大小的空白影片潛在空間。張量形狀為 [batch_size, 16, lat_t, height/8, width/8]，其中 lat_t 是根據長度計算得出。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyARVideoLatent/zh-TW.md)

---
**Source fingerprint (SHA-256):** `5ae25e2ccb24e627eae583d14c5bcba8b576a227b7a489f3cd4bc56738928513`
