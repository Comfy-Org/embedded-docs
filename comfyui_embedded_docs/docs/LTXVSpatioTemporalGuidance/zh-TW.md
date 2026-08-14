# LTXVSpatioTemporalGuidance

此節點透過在每個取樣步驟執行額外的一次傳遞，來改善 LTXV 影片生成的空間細節與動作連貫性。在此傳遞期間，所選 transformer 區塊的自注意力會退化為值直通（value-passthrough），並引導生成遠離退化後的結果。

## 輸入
| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|---|---|---|---|---|
| `model` | 要套用時空引導的基礎模型。此模型會被複製，並以 CFG 後置引導函式進行修改。 | MODEL | 是 | — |
| `scale` | 套用於去噪結果的引導強度。設為 0 時，引導不產生任何效果。（預設值：1.0） | FLOAT | 是 | 0.0 至 100.0 (步長 0.01) |
| `blocks` | 以逗號分隔要擾動的 transformer 區塊索引。僅使用數值；任何其他字元都會被忽略。（預設值："29"） | STRING | 是 | — |
| `start_percent` | 取樣過程中開始引導所對應的比例。（預設值：0.0） | FLOAT | 是 | 0.0 至 1.0 (步長 0.001) |
| `end_percent` | 取樣過程中結束引導所對應的比例。（預設值：1.0） | FLOAT | 是 | 0.0 至 1.0 (步長 0.001) |

注意：引導僅在 `start_percent` 和 `end_percent` 之間的取樣區間內套用。如果 `scale` 為 0 或 `blocks` 不含任何數值，則引導傳遞對取樣過程沒有影響。

## 輸出
| 輸出名 | 描述 | 資料類型 |
|---|---|---|
| `MODEL` | 已附加時空引導函式的複製模型。 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVSpatioTemporalGuidance/zh-TW.md)

---
**Source fingerprint (SHA-256):** `0e14137b3bf416d36005b6b4b6db46495b1523f88b2bf574e2dc582175422a48`
