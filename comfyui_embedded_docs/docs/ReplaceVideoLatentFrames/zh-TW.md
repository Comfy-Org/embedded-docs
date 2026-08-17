# ReplaceVideoLatentFrames

ReplaceVideoLatentFrames 節點會將來源潛在影片的幀插入到目標潛在影片中，從指定的幀索引開始。如果未提供來源潛在，則原樣返回目標潛在。此節點支援負索引，並在來源幀無法放入目標時發出警告。

## 輸入

| 參數 | 描述 | 資料型態 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `destination` | 目標潛在，幀將被替換到此處。 | LATENT | 是 | - |
| `source` | 提供要插入到目標潛在中的幀的來源潛在。若未提供，則原樣返回目標潛在。 | LATENT | 否 | - |
| `index` | 目標潛在中用於放置來源潛在幀的起始潛在幀索引。負值從末尾開始計數（預設值：0）。 | INT | 是 | -MAX_RESOLUTION to MAX_RESOLUTION (step: 1) |

**約束：**

* `index` 必須在目標潛在的幀數範圍內。若超出範圍，系統會記錄警告並原樣返回目標。
* 來源潛在幀必須能從指定的 `index` 開始放入目標潛在幀中。若無法容納，系統會記錄警告並原樣返回目標。

## 輸出

| 輸出名稱 | 描述 | 資料型態 |
| --- | --- | --- |
| `output` | 幀替換操作後產生的潛在影片。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReplaceVideoLatentFrames/zh-TW.md)

---
**Source fingerprint (SHA-256):** `5b98d875bdeaec63521bff19fecbc5510036c8b4f90322d8296b216688b557bf`
