> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MagnificImageSkinEnhancerNode/zh-TW.md)

## 概述

Magnific Image Skin Enhancer 節點對人像圖片應用專門的 AI 處理，以改善皮膚外觀。它提供三種不同的模式以滿足不同的增強目標：`creative` 用於藝術效果，`faithful` 用於保留原始外觀，`flexible` 用於針對性改善（如光線或真實感）。該節點會將圖片上傳至外部 API 進行處理，並返回增強後的結果。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | 是 | - | 要增強的人像圖片。 |
| `sharpen` | INT | 否 | 0 至 100 | 銳化強度等級（預設值：0）。 |
| `smart_grain` | INT | 否 | 0 至 100 | 智慧顆粒強度等級（預設值：2）。 |
| `mode` | COMBO | 是 | `"creative"`<br>`"faithful"`<br>`"flexible"` | 要使用的處理模式。`"creative"` 用於藝術增強，`"faithful"` 用於保留原始外觀，`"flexible"` 用於針對性最佳化。 |
| `skin_detail` | INT | 否 | 0 至 100 | 皮膚細節增強等級。此輸入僅在 `mode` 設定為 `"faithful"` 時可用且必要（預設值：80）。 |
| `optimized_for` | COMBO | 否 | `"enhance_skin"`<br>`"improve_lighting"`<br>`"enhance_everything"`<br>`"transform_to_real"`<br>`"no_make_up"` | 增強最佳化目標。此輸入僅在 `mode` 設定為 `"flexible"` 時可用且必要。 |

**限制條件：**

* 此節點僅接受一張輸入圖片。
* 輸入圖片的最小高度和寬度必須為 160 像素。
* 輸入圖片的長寬比必須介於 1:3 與 3:1 之間（非嚴格驗證）。
* `skin_detail` 參數僅在 `mode` 設定為 `"faithful"` 時生效。
* `optimized_for` 參數僅在 `mode` 設定為 `"flexible"` 時生效。

## 輸出

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `image` | IMAGE | 增強後的人像圖片。 |

---
**Source fingerprint (SHA-256):** `e02cae2e119ddab931b790865889adf53f47a2ebb03d488477c289dfda7204f5`
