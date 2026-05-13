> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanVideo15LatentUpscaleWithModel/zh-TW.md)

# Hunyuan Video 1.5 潛在空間放大（搭配模型）節點

Hunyuan Video 1.5 潛在空間放大（搭配模型）節點可提高潛在影像表示法的解析度。它首先使用所選的內插方法將潛在樣本放大到指定尺寸，然後使用專門的 Hunyuan Video 1.5 放大模型來優化放大結果，以提升品質。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `model` | LATENT_UPSCALE_MODEL | 是 | 不適用 | 用於優化放大後樣本的 Hunyuan Video 1.5 潛在空間放大模型。 |
| `samples` | LATENT | 是 | 不適用 | 要進行放大的潛在影像表示法。 |
| `upscale_method` | COMBO | 否 | `"nearest-exact"`<br>`"bilinear"`<br>`"area"`<br>`"bicubic"`<br>`"bislerp"` | 用於初始放大步驟的內插演算法（預設值：`"bilinear"`）。 |
| `width` | INT | 否 | 0 至 16384 | 放大後潛在空間的目標寬度，單位為像素。設為 0 時，系統會根據目標高度和原始長寬比自動計算寬度。最終輸出寬度將為 16 的倍數（預設值：1280）。 |
| `height` | INT | 否 | 0 至 16384 | 放大後潛在空間的目標高度，單位為像素。設為 0 時，系統會根據目標寬度和原始長寬比自動計算高度。最終輸出高度將為 16 的倍數（預設值：720）。 |
| `crop` | COMBO | 否 | `"disabled"`<br>`"center"` | 決定如何裁剪放大後的潛在空間以符合目標尺寸。 |

**關於尺寸的注意事項：** 如果 `width` 和 `height` 都設為 0，則節點會直接回傳輸入的 `samples` 而不做任何變更。如果只有一個維度設為 0，則會計算另一個維度以保持原始長寬比。最終尺寸會調整為至少 64 像素，且可被 16 整除。

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `LATENT` | LATENT | 經過放大和模型優化後的潛在影像表示法。 |

---
**Source fingerprint (SHA-256):** `1de9e157c1a0433f1b3d5ff4d428a1aa392fd65da5e314e6e818ce66495d5ef4`
