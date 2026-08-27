# HitPaw 通用影像增強

此節點透過將低解析度圖像放大至超解析度來增強圖像，移除偽影和雜訊。它使用外部 API 處理圖像，並可自動調整輸入大小以保持在處理限制內。最大允許輸出大小為 32 百萬像素。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `模型` | 要使用的增強模型。`generative_portrait` 模型專門針對人像最佳化，而 `generative` 是通用模型。 | COMBO | 是 | `"generative_portrait"`<br>`"generative"` |
| `影像` | 要增強的輸入圖像。 | IMAGE | 是 | - |
| `放大倍率` | 圖像尺寸的放大倍率。倍率 1 表示不放大，2 表示尺寸加倍，4 表示尺寸變為四倍。 | COMBO | 是 | `1`<br>`2`<br>`4` |
| `自動縮小` | 如果輸出會超過限制，自動縮小輸入圖像。（預設：`False`） | BOOLEAN | 否 | - |

**注意：** 如果計算出的輸出大小（輸入寬度 × 放大倍率 × 輸入高度 × 放大倍率）超過 32,000,000 像素（32MP），且 `auto_downscale` 為停用，則節點會引發錯誤。當啟用 `auto_downscale` 時，節點會自動縮小輸入圖像大小或放大倍率（或兩者），使輸出符合 32MP 限制。

## 輸出

| 輸出名 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `image` | 增強並放大後的輸出圖像。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HitPawGeneralImageEnhance/zh-TW.md)

---
**Source fingerprint (SHA-256):** `eb9adc1ac94c5fb943e3dd8f6617b21c5d3203f0d9ddb93ba1c9d4b4e63bd421`
