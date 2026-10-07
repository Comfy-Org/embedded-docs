# Clarity AI Crystal Upscale

使用 Clarity AI 的 Crystal Upscaler 放大影像；這是一款高保真放大器，能在忠實保留原圖的同時，修復臉部、皮膚與細緻紋理。影像會傳送至 Clarity AI 的 API，並以影像形式回傳放大後的結果。

選擇 `model` 後會顯示該模型專屬的參數。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | 要使用的模型。選擇模型後會顯示其專屬參數：`image`、`scale_factor` 與 `creativity`。 | DYNAMIC_COMBO | 是 | `"crystal-upscaler"` |
| `image` | 要放大的影像。必須恰好包含一張影像；不支援影像批次。 | IMAGE | 是 | N/A |
| `scale_factor` | 用來乘以影像寬度與高度的倍率。輸出限制為 100 百萬像素（預設值：2.0）。 | FLOAT | 是 | 1.0 至 200.0（步長 0.1） |
| `creativity` | 數值越高，模型會重建更多細節，而非嚴格保留原始內容。對短邊為 256 像素或以下的影像沒有作用（預設值：0）。 | INT | 是 | 0 至 10 |

**注意：** 輸入影像必須至少為 2x2 像素。輸出上限為 100 百萬像素，且每邊最多 65535 像素；若結果更大會引發錯誤，因此請使用較小的影像或較低的 `scale_factor`。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `IMAGE` | 放大後的影像。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ClarityCrystalUpscaleNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `38c90cf7054a93477ee63c356c3fdf8ba38c7edaf1a337da7ac366cd9d746d9e`
