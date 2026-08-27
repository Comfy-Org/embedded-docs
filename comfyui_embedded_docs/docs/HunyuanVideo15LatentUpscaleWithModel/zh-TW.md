# Hunyuan Video 15 Latent Upscale With Model

以下是翻譯成繁體中文的結果：

---

Hunyuan Video 15 Latent Upscale With Model 節點用於增加潛在影像表示的解像度。它首先使用所選的插值方法將潛在樣本放大到指定尺寸，然後使用專門的 Hunyuan Video 1.5 放大模型對放大結果進行精煉，以提升品質。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 用於精煉放大後樣本的 Hunyuan Video 1.5 潛在放大模型。 | LATENT_UPSCALE_MODEL | 是 | 不適用 |
| `samples` | 要放大的潛在影像表示。 | LATENT | 是 | 不適用 |
| `upscale_method` | 初始放大步驟使用的插值演算法（預設值：`"bilinear"`）。 | COMBO | 否 | `"nearest-exact"`<br>`"bilinear"`<br>`"area"`<br>`"bicubic"`<br>`"bislerp"` |
| `width` | 放大後潛在表示的目標寬度（像素）。值為 0 時，將根據目標高度和原始縱橫比自動計算寬度。最終輸出寬度將是 16 的倍數（預設值：1280）。 | INT | 否 | 0 至 16384（步長：8） |
| `height` | 放大後潛在表示的目標高度（像素）。值為 0 時，將根據目標寬度和原始縱橫比自動計算高度。最終輸出高度將是 16 的倍數（預設值：720）。 | INT | 否 | 0 至 16384（步長：8） |
| `crop` | 決定放大後的潛在表示如何裁剪以符合目標尺寸。 | COMBO | 否 | `"disabled"`<br>`"center"` |

**關於尺寸的說明：** 如果同時將 `width` 和 `height` 設為 0，節點將直接傳回輸入的 `samples`，不做任何處理。如果僅將其中一個維度設為 0，另一個維度會根據原始縱橫比自動計算。最終尺寸一律調整為至少 64 像素，且為 16 的倍數。

## 輸出

| 輸出名 | 說明 | 資料類型 |
| --- | --- | --- |
| `LATENT` | 放大並經模型精煉後的潛在影像表示。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanVideo15LatentUpscaleWithModel/zh-TW.md)

---
**Source fingerprint (SHA-256):** `71af49eefb010aadd30f8699b751ad901b1ee385d6cbeedd3a83995a1a623516`
