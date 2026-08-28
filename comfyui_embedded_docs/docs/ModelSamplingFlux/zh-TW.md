# 模型取樣 Flux

ModelSamplingFlux 節點透過根據影像尺寸計算 shift 參數，對給定模型套用 Flux 模型取樣。它會建立一個專門的取樣設定，根據指定的寬度、高度和 shift 參數調整模型行為，然後在套用新的取樣設定後，回傳修改後的模型。

## 輸入

| 參數 | 描述 | 資料型別 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 要套用 Flux 取樣的模型 | MODEL | 是 | - |
| `最大偏移` | 取樣計算的最大 shift 值（預設：1.15） | FLOAT | 是 | 0.0 - 100.0 (step 0.01) |
| `基礎偏移` | 取樣計算的基礎 shift 值（預設：0.5） | FLOAT | 是 | 0.0 - 100.0 (step 0.01) |
| `寬度` | 目標影像的寬度（像素）（預設：1024） | INT | 是 | 16 - MAX_RESOLUTION (step 8) |
| `高度` | 目標影像的高度（像素）（預設：1024） | INT | 是 | 16 - MAX_RESOLUTION (step 8) |

`max_shift` 和 `base_shift` 是進階參數。套用於取樣設定的 shift 值會根據影像尺寸計算：潛在解析度計算為 `width × height / 256`，並且 shift 值會在潛在解析度為 256 時的 `base_shift` 與潛在解析度為 4096 時的 `max_shift` 之間進行插值。

## 輸出

| 輸出名稱 | 描述 | 資料型別 |
| --- | --- | --- |
| `model` | 已套用 Flux 取樣設定的修改後模型 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingFlux/zh-TW.md)

---
**Source fingerprint (SHA-256):** `04065b54ace30a2b20476ed085df871ea89794650e98ae30c40f750357663834`
