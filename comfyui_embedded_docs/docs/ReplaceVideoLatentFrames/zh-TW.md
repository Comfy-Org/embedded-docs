# ReplaceVideoLatentFrames

ReplaceVideoLatentFrames 會使用來源潛在影片中的幀替換目標潛在影片中的一系列幀，從指定的幀索引開始。若未提供來源潛在，目標潛在將原樣返回。此節點支援負數索引，並在來源幀無法容納於目標中時記錄警告。

## 輸入
| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `destination` | 作為幀替換目標的潛在。 | LATENT | 是 | - |
| `source` | 提供要插入目標潛在之幀的來源潛在。若未提供，目標潛在將原樣返回。 | LATENT | 否 | - |
| `index` | 目標潛在中要放置來源潛在幀的起始幀索引。負數值從末尾倒數計算（預設：0）。 | INT | 是 | -MAX_RESOLUTION to MAX_RESOLUTION |

**約束條件：**

* 負數的 `index` 會加上目標幀數來調整，因此會從目標潛在的末尾倒數計算。
* 如果 `index` 指向超出目標幀數的位置，或來源幀在從 `index` 開始的範圍內無法容納於目標中，則會記錄警告並原樣返回目標潛在。

## 輸出
| 輸出名 | 描述 | 資料類型 |
| --- | --- | --- |
| `output` | 幀替換操作後產生的潛在影片。若無法執行替換，目標潛在將原樣返回。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReplaceVideoLatentFrames/zh-TW.md)

---
**Source fingerprint (SHA-256):** `5b98d875bdeaec63521bff19fecbc5510036c8b4f90322d8296b216688b557bf`
