# HitPaw 通用影像增強

此節點透過將低解析度影像放大至超解析度，同時移除偽影和雜訊來增強低解析度影像。它會將影像傳送至外部 API 進行處理，並可自動調整輸入尺寸，以維持在允許的輸出限制內。允許的最大輸出尺寸為 32 百萬像素。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `模型` | 要使用的增強模型。`generative_portrait` 模型專為人像最佳化，而 `generative` 則是通用模型。 | COMBO | 是 | `"generative_portrait"`<br>`"generative"` |
| `影像` | 要增強的輸入影像。 | IMAGE | 是 | - |
| `放大倍率` | 用來放大影像尺寸的倍率。倍率為 1 表示不放大，2 會將尺寸加倍，4 則會將其變為四倍。 | COMBO | 是 | `1`<br>`2`<br>`4` |
| `自動縮小` | 若輸出會超過限制，則自動縮小輸入影像。（預設：`False`） | BOOLEAN | 否 | - |

**注意：** 如果計算出的輸出尺寸（輸入寬度 × `upscale_factor` × 輸入高度 × `upscale_factor`）超過 32,000,000 像素（32MP），且 `auto_downscale` 已停用，則此節點會引發錯誤。當 `auto_downscale` 啟用時，此節點會自動縮小輸入影像尺寸或降低放大倍率（或兩者），使輸出符合 32MP 限制。所選的 `model` 與 `upscale_factor` 會合併成傳送至服務的模型名稱。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `image` | 增強並放大後的輸出影像。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HitPawGeneralImageEnhance/zh-TW.md)

---
**Source fingerprint (SHA-256):** `eb9adc1ac94c5fb943e3dd8f6617b21c5d3203f0d9ddb93ba1c9d4b4e63bd421`
