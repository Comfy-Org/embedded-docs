# 後處理 SeedVR2 輸出

此節點會將生成的影像與原始調整尺寸後的影像對齊，並套用可選的色彩校正。它接收 SeedVR2 放大流程的輸出，並調整其以符合原始參考影像的色彩與尺寸。

## 輸入
| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `images` | 要處理的生成影像。 | IMAGE | 是 | - |
| `original_resized_images` | 預處理前的原始調整尺寸影像，作為參考。 | IMAGE | 是 | - |
| `color_correction_method` | 用於將生成影像的色彩比對至原始影像的方法。`lab`：在 CIELAB 色彩空間中轉移色彩，保留細節（最忠實）。`wavelet`：轉移低頻色彩，保留放大後的高頻細節。`adain`：比對每個通道的平均值/標準差（最快，整體色偏）。`none`：跳過色彩轉移（僅進行幾何對齊）。（預設值：`"lab"`） | COMBO | 是 | `"lab"`<br>`"wavelet"`<br>`"adain"`<br>`"none"` |

**備註：** 兩個輸入可能都是 4-D（批次、高度、寬度、通道）或 5-D（批次、幀數、高度、寬度、通道）張量。節點會將兩者裁切為最小的批次、幀數、高度和寬度，因此兩者不需完全一致。輸出的高度和寬度會向下取整為偶數。如果參考影像具有 Alpha 通道（4 個通道），該 Alpha 通道會被保留並套用至輸出。

## 輸出
| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `images` | 已對齊並完成色彩校正的影像。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedVR2PostProcessing/zh-TW.md)

---
**Source fingerprint (SHA-256):** `00a3a3ef06edc7e0eca8f67a96095920a3e0e885dac3fb676d081e4c4c30bec5`
