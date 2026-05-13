> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ChromaRadianceOptions/zh-TW.md)

## 概述

ChromaRadianceOptions 節點可讓您為 Chroma Radiance 模型配置進階設定。它會包裝現有模型，並根據 sigma 值在去噪過程中套用特定選項，從而實現對 NeRF 區塊大小及其他輻射相關參數的精細控制。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | 是 | - | 要套用 Chroma Radiance 選項的模型 |
| `preserve_wrapper` | BOOLEAN | 否 | - | 啟用時，若存在現有模型函數包裝器，將委派給該包裝器。通常應保持啟用。（預設值：True） |
| `start_sigma` | FLOAT | 否 | 0.0 至 1.0 | 這些選項開始生效的第一個 sigma 值。（預設值：1.0） |
| `end_sigma` | FLOAT | 否 | 0.0 至 1.0 | 這些選項結束生效的最後一個 sigma 值。（預設值：0.0） |
| `nerf_tile_size` | INT | 否 | -1 及以上 | 允許覆寫預設的 NeRF 區塊大小。-1 表示使用預設值 (32)。0 表示使用非區塊模式（可能需要大量 VRAM）。（預設值：-1） |

**注意：** Chroma Radiance 選項僅在當前 sigma 值落在 `end_sigma` 與 `start_sigma` 之間（含邊界值）時才會生效。`nerf_tile_size` 參數僅在設定為 0 或更高數值時才會套用。

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `model` | MODEL | 已套用 Chroma Radiance 選項的修改後模型 |

---
**Source fingerprint (SHA-256):** `b49a12e9aba59e4669c59e05a6aeff6d4ae5a4b656ca5b0de4bdf71291dca095`
