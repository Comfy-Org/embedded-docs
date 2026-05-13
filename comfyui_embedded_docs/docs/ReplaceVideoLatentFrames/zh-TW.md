> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReplaceVideoLatentFrames/zh-TW.md)

## 概述

ReplaceVideoLatentFrames 節點會將來源潛在影片中的影格插入到目標潛在影片中，從指定的影格索引開始。如果未提供來源潛在，則直接回傳未修改的目標潛在。此節點支援負數索引，並在來源影格無法完整放入目標時發出警告。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `destination` | LATENT | 是 | - | 將被替換影格的目標潛在。 |
| `source` | LATENT | 否 | - | 提供要插入到目標潛在中的影格的來源潛在。如果未提供，則直接回傳未修改的目標潛在。 |
| `index` | INT | 是 | -MAX_RESOLUTION 至 MAX_RESOLUTION | 目標潛在中的起始潛在影格索引，來源潛在影格將放置於此。負數值從結尾開始計數（預設值：0）。 |

**限制條件：**

* `index` 必須在目標潛在的影格數量範圍內。如果超出範圍，會記錄警告並直接回傳未修改的目標潛在。
* 來源潛在影格必須能夠完整放入從指定 `index` 開始的目標潛在影格中。如果無法放入，會記錄警告並直接回傳未修改的目標潛在。

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `output` | LATENT | 影格替換操作後的結果潛在影片。 |

---
**Source fingerprint (SHA-256):** `b4e2b3dcdaa5c400fefc30262ae05cd1849896e6cb6bbb3a1bd6ce4d31583e23`
