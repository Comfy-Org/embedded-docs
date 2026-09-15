# EmptyARVideoLatent

EmptyARVideoLatent 節點會建立用於影片生成的空白潛在表徵。它會使用指定的 `width`、`height`、影格數與批次大小來建立一個零張量，之後可用來初始化影片生成流程。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `寬度` | 影片影格的寬度，單位為像素（預設：832） | INT | 是 | 16 至 8192 （步進值：16） |
| `高度` | 影片影格的高度，單位為像素（預設：480） | INT | 是 | 16 至 8192 （步進值：16） |
| `長度` | 影片中的影格數（預設：81） | INT | 是 | 1 至 1024 （步進值：4） |
| `批次大小` | 單一批次中要生成的影片數量（預設：1） | INT | 是 | 1 至 64 |

注意：內部潛在大小會根據這些輸入推導而來。`width` 和 `height` 會除以 8，而潛在時間步數的計算方式為 `((length - 1) // 4) + 1`。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `LATENT` | 一個填滿零的潛在張量，代表具有指定尺寸、長度與批次大小的空白影片潛在空間。張量形狀為 [batch_size, 16, lat_t, height/8, width/8]，其中 lat_t = ((length - 1) // 4) + 1，是根據所要求長度推導出的潛在時間步數。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyARVideoLatent/zh-TW.md)

---
**Source fingerprint (SHA-256):** `02ed3c96d94f2a3df9fb5315a5312e5280b9bee280369eb1218ba10bc122e609`
