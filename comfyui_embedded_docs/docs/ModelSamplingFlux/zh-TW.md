# 模型取樣 Flux

ModelSamplingFlux 節點會根據影像尺寸計算 shift 參數，將 Flux 模型取樣套用至指定的模型。它會建立專門的取樣設定，根據指定的 width、height 與 shift 參數調整模型行為，然後傳回已套用新取樣設定的修改後模型。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 要套用 Flux 取樣的模型 | MODEL | 是 | - |
| `max_shift` | 取樣計算的最大偏移值（預設值：1.15） | FLOAT | 是 | 0.0 - 100.0 |
| `base_shift` | 取樣計算的基礎偏移值（預設值：0.5） | FLOAT | 是 | 0.0 - 100.0 |
| `width` | 目標影像的寬度（像素，預設值：1024） | INT | 是 | 16 - MAX_RESOLUTION |
| `height` | 目標影像的高度（像素，預設值：1024） | INT | 是 | 16 - MAX_RESOLUTION |

有效偏移值會根據由 `width` 和 `height` 推導出的潛在尺寸（latent size），在 `base_shift` 與 `max_shift` 之間進行插值。`step` 值對於 `max_shift` 和 `base_shift` 為 0.01，對於 `width` 和 `height` 則為 8。`max_shift` 和 `base_shift` 參數在使用者介面中標記為進階選項。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `model` | 已套用 Flux 取樣設定的修改後模型 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingFlux/zh-TW.md)

---
**Source fingerprint (SHA-256):** `04065b54ace30a2b20476ed085df871ea89794650e98ae30c40f750357663834`
