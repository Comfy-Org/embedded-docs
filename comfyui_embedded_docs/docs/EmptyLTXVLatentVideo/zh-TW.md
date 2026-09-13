# EmptyLTXVLatentVideo

EmptyLTXVLatentVideo 節點會使用你指定的 `width`、`height`、`length` 和 `batch_size` 建立一個空的（以零填充的）潛在影片張量。它為 LTXV 影片生成工作流程提供空白起始點，且潛在維度會相對於請求的影片尺寸自動壓縮。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `寬度` | 潛在影片張量的寬度（預設：768，步長：32） | INT | 是 | 64 to MAX_RESOLUTION |
| `高度` | 潛在影片張量的高度（預設：512，步長：32） | INT | 是 | 64 to MAX_RESOLUTION |
| `長度` | 潛在影片中的影格數量（預設：97，步長：8） | INT | 是 | 1 to MAX_RESOLUTION |
| `批次大小` | 一個批次中要生成的潛在影片數量（預設：1） | INT | 是 | 1 至 4096 |

注意：與請求的尺寸相比，潛在影片會經過壓縮：空間維度（`width` 和 `height`）會除以 32，而影格數量（`length`）會除以 8 並向上取整至最接近的整數。`width`、`height` 和 `length` 的步長值有助於讓這些除法的結果保持為整數。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `samples` | 生成的空白潛在張量，在指定維度中具有零值，並附帶空間下縮放比例 32 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyLTXVLatentVideo/zh-TW.md)

---
**Source fingerprint (SHA-256):** `0b1e57baf9730d852b03b6bccbb8a033e2be9b9cd2420a0aa3638c31f6d3cd26`
