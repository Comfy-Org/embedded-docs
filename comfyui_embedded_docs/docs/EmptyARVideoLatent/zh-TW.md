# EmptyARVideoLatent

## 總覽

EmptyARVideoLatent 節點會建立一個空白、空的潛在表示，用於影片生成。它透過提供一個具有指定尺寸、長寬比和長度的零張量來初始化影片生成程序。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `寬度` | 影片幀的寬度（像素）（預設值：832） | INT | 是 | 16 至 8192 (step: 16) |
| `高度` | 影片幀的高度（像素）（預設值：480） | INT | 是 | 16 至 8192 (step: 16) |
| `長度` | 影片中的幀數（預設值：81） | INT | 是 | 1 至 1024 (step: 4) |
| `批次大小` | 單一批次中要生成的影片數量（預設值：1） | INT | 是 | 1 至 64 |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `LATENT` | 一個以零填充的潛在張量，代表具有指定尺寸、長度和批次大小的空影片潛在空間。張量形狀為 [batch_size, 16, lat_t, height/8, width/8]，其中 lat_t = ((length - 1) // 4) + 1 是根據請求的長度得出的潛在時間步數。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyARVideoLatent/zh-TW.md)

---
**Source fingerprint (SHA-256):** `02ed3c96d94f2a3df9fb5315a5312e5280b9bee280369eb1218ba10bc122e609`
