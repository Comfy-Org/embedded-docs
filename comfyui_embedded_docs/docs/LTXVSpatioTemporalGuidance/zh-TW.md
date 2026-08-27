# LTXV 時空引導（STG）

此節點透過在每個取樣步驟執行額外的一次傳遞，來改善 LTXV 影片生成的空間細節與運動一致性。在此傳遞過程中，所選 Transformer 區塊的自注意力會被降級為值直通（value-passthrough），並引導生成結果遠離降級後的結果。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | 要套用時空引導的基礎模型。該模型會被複製，並以 CFG 後引導函式進行修改。 | MODEL | 是 | — |
| `scale` | 套用於去噪結果的引導強度。設為 0 時，引導不產生任何效果。（預設值：1.0） | FLOAT | 是 | 0.0 至 100.0 (step 0.01) |
| `blocks` | 以逗號分隔的 Transformer 區塊索引，用於擾動。僅使用數值；任何其他字元都會被忽略。（預設值："29"） | STRING | 是 | — |
| `start_percent` | 引導開始時的取樣過程比例。這是一個進階參數。（預設值：0.0） | FLOAT | 是 | 0.0 至 1.0 (step 0.001) |
| `end_percent` | 引導結束時的取樣過程比例。這是一個進階參數。（預設值：1.0） | FLOAT | 是 | 0.0 至 1.0 (step 0.001) |

注意：引導僅在 `start_percent` 與 `end_percent` 之間的取樣區間內套用。如果 `scale` 為 0，或 `blocks` 中不含任何數值，則引導傳遞對取樣過程不產生任何影響。

## 輸出

| 輸出名 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `MODEL` | 帶有附加時空引導函式的複製模型。 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVSpatioTemporalGuidance/zh-TW.md)

---
**Source fingerprint (SHA-256):** `0e14137b3bf416d36005b6b4b6db46495b1523f88b2bf574e2dc582175422a48`
