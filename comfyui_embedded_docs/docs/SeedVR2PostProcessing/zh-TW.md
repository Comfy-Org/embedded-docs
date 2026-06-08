# 後處理 SeedVR2 輸出

此節點將生成的圖像與原始調整大小後的圖像進行對齊，並套用可選的色彩校正。它接收來自 SeedVR2 放大流程的輸出，並進行調整以匹配原始參考圖像的色彩和尺寸。

## ## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `images` | 要處理的生成圖像。 | IMAGE | 是 | - |
| `original_resized_images` | 預處理前的原始調整大小圖像，用作參考。 | IMAGE | 是 | - |
| `color_correction_method` | 將生成圖像色彩匹配到原始圖像的方法。lab：在 CIELAB 色彩空間中轉移色彩，保留細節（最忠實）。wavelet：轉移低頻色彩，保留放大後的高頻細節。adain：匹配每個通道的平均值/標準差（最快，全域色調）。none：跳過色彩轉移（僅進行幾何對齊）。（預設值："lab"） | COMBO | 是 | `"lab"`<br>`"wavelet"`<br>`"adain"`<br>`"none"` |

**注意：** `images` 和 `original_resized_images` 輸入必須具有匹配的尺寸。如果原始圖像具有 Alpha 通道（4 個通道），則該通道將被保留並套用至輸出。

## ## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `images` | 已套用色彩校正且尺寸與參考圖像對齊的處理後圖像。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedVR2PostProcessing/zh-TW.md)

---
**Source fingerprint (SHA-256):** `befbe8ccd591c8064a07ae4bb8df853c7ce10f3de83ebfa9214755c22faf28b0`
