# Hunyuan Video 15 Latent Upscale With Model

Hunyuan Video 15 Latent Upscale With Model 節點會提高潛在影像表示的解析度。它會先使用選定的插值方法，將潛在樣本放大至指定尺寸，然後使用專門的 Hunyuan Video 1.5 放大模型來精修放大後的結果，以提升品質。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 用於精修放大後樣本的 Hunyuan Video 1.5 潛在放大模型。 | LATENT_UPSCALE_MODEL | 是 | N/A |
| `samples` | 要放大的潛在影像表示。 | LATENT | 是 | N/A |
| `upscale_method` | 用於初始放大步驟的插值演算法（預設：`"bilinear"`）。 | COMBO | 是 | `"nearest-exact"`<br>`"bilinear"`<br>`"area"`<br>`"bicubic"`<br>`"bislerp"` |
| `width` | 放大後潛在表示的目標寬度，以像素為單位。值為 0 時，會根據目標高度與原始長寬比自動計算寬度。最終輸出寬度會是 16 的倍數（預設：1280）。 | INT | 是 | 0 至 16384 （步進值：8） |
| `height` | 放大後潛在表示的目標高度，以像素為單位。值為 0 時，會根據目標寬度與原始長寬比自動計算高度。最終輸出高度會是 16 的倍數（預設：720）。 | INT | 是 | 0 至 16384 （步進值：8） |
| `crop` | 決定如何裁剪放大後的潛在表示，以符合目標尺寸。 | COMBO | 是 | `"disabled"`<br>`"center"` |

**關於尺寸的注意事項：** 如果 `width` 與 `height` 都設為 0，節點會原樣回傳輸入的 `samples`。如果只有其中一個維度設為 0，則會計算另一個維度以保留原始長寬比。兩個值都會被限制為最小值 64，而傳遞給插值步驟的放大目標是 `width // 16` 乘以 `height // 16`，因此請求的尺寸實際上會向下捨入為 16 的倍數。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `LATENT` | 放大並經模型精修後的潛在影像表示，以 CPU 上的 float 張量形式回傳。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanVideo15LatentUpscaleWithModel/zh-TW.md)

---
**Source fingerprint (SHA-256):** `71af49eefb010aadd30f8699b751ad901b1ee385d6cbeedd3a83995a1a623516`
