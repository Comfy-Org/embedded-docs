# EmptyARVideoLatent

EmptyARVideoLatent 節點會建立用於影片生成的空白、空的潛在（latent）表示。它透過提供一個具有指定尺寸、長寬比和長度的零張量，來初始化影片生成流程。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `width` | 影片畫面的寬度（以像素為單位，預設值：832） | INT | 是 | 16 to 8192 (step: 16) |
| `height` | 影片畫面的高度（以像素為單位，預設值：480） | INT | 是 | 16 to 8192 (step: 16) |
| `length` | 影片中的影格數（預設值：81） | INT | 是 | 1 to 1024 (step: 4) |
| `batch_size` | 單一批次中要產生的影片數量（預設值：1） | INT | 是 | 1 to 64 |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `LATENT` | 一個填充為零的潛在張量，代表具有指定尺寸、長度和批次大小的空白影片潛在空間。張量形狀為 [batch_size, 16, lat_t, height/8, width/8]，其中 lat_t 是根據長度計算得出。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyARVideoLatent/zh-TW.md)

---
**Source fingerprint (SHA-256):** `02ed3c96d94f2a3df9fb5315a5312e5280b9bee280369eb1218ba10bc122e609`
