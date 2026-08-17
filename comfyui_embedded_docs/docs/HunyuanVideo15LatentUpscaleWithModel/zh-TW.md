# Hunyuan Video 15 Latent Upscale With Model

Hunyuan Video 15 Latent Upscale With Model 節點用於提高潛在影像表示（latent image representation）的解析度。它首先使用所選的插值方法將潛在樣本（latent samples）放大到指定尺寸，然後使用專門的 Hunyuan Video 1.5 放大模型來最佳化放大結果，以提升品質。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 用於最佳化放大後樣本的 Hunyuan Video 1.5 潛在放大模型。 | LATENT_UPSCALE_MODEL | 是 | N/A |
| `samples` | 要放大的潛在影像表示。 | LATENT | 是 | N/A |
| `upscale_method` | 用於初始放大步驟的插值演算法（預設：`"bilinear"`）。 | COMBO | 否 | `"nearest-exact"`<br>`"bilinear"`<br>`"area"`<br>`"bicubic"`<br>`"bislerp"` |
| `width` | 放大後潛在影像的目標寬度（像素）。若設為 0，則會根據目標高度和原始縱橫比自動計算寬度。最終輸出寬度將是 16 的倍數（預設：1280）。 | INT | 否 | 0 至 16384（步長 8） |
| `height` | 放大後潛在影像的目標高度（像素）。若設為 0，則會根據目標寬度和原始縱橫比自動計算高度。最終輸出高度將是 16 的倍數（預設：720）。 | INT | 否 | 0 至 16384（步長 8） |
| `crop` | 決定如何裁切放大後的潛在影像以符合目標尺寸。 | COMBO | 否 | `"disabled"`<br>`"center"` |

**尺寸說明：** 如果 `width` 和 `height` 都設為 0，節點會直接回傳輸入的 `samples`。如果只有一個維度設為 0，則會計算另一個維度以保持原始縱橫比。最終尺寸一律會調整為至少 64 像素，且為 16 的倍數。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `LATENT` | 經放大並以模型最佳化的潛在影像表示。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanVideo15LatentUpscaleWithModel/zh-TW.md)

---
**Source fingerprint (SHA-256):** `71af49eefb010aadd30f8699b751ad901b1ee385d6cbeedd3a83995a1a623516`
