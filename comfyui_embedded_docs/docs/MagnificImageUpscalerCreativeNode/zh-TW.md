# Magnific 影像放大（創意）

此節點使用 Magnific AI 服務來放大並創意增強影像。它允許您透過文字提示引導增強，選擇要最佳化的特定風格，並控制創意流程的各個方面，例如細節、與原圖的相似度以及風格化強度。此節點會以您選擇的倍率（2x、4x、8x 或 16x）輸出放大後的影像，最大輸出尺寸為 25.3 百萬像素。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `影像` | 要放大並增強的輸入影像。 | IMAGE | 是 | - |
| `提示詞` | 用於引導影像創意增強的文字描述。預設為空字串（在該情況下不會傳送提示）。 | STRING | 是 | - |
| `放大倍率` | 將影像尺寸放大的倍率。 | COMBO | 是 | `"2x"`<br>`"4x"`<br>`"8x"`<br>`"16x"` |
| `最佳化目標` | 要為增強流程最佳化的風格或內容類型。 | COMBO | 是 | `"standard"`<br>`"soft_portraits"`<br>`"hard_portraits"`<br>`"art_n_illustration"`<br>`"videogame_assets"`<br>`"nature_n_landscapes"`<br>`"films_n_photography"`<br>`"3d_renders"`<br>`"science_fiction_n_horror"` |
| `創意` | 控制套用到影像的創意詮釋程度（預設：0）。 | INT | 是 | -10 至 10 |
| `HDR` | 清晰度與細節的程度（預設：0）。 | INT | 是 | -10 至 10 |
| `相似度` | 與原始影像的相似程度（預設：0）。 | INT | 是 | -10 至 10 |
| `複雜度` | 提示的強度以及每平方像素的精細複雜程度（預設：0）。 | INT | 是 | -10 至 10 |
| `引擎` | 用於處理的特定 AI 引擎。這是進階參數。 | COMBO | 是 | `"automatic"`<br>`"magnific_illusio"`<br>`"magnific_sharpy"`<br>`"magnific_sparkle"` |
| `自動降尺寸` | 若輸出會超過最大像素限制，則自動縮小輸入影像（預設：False）。這是進階參數。 | BOOLEAN | 是 | - |

**限制條件：**

* 輸入 `image` 必須恰好是一張影像。
* 輸入影像的高度和寬度必須至少為 160 像素。
* 輸入影像的長寬比必須介於 1:3 與 3:1 之間。
* 最終輸出尺寸（輸入尺寸乘以 `scale_factor`）不得超過 25,300,000 像素。如果會超過此限制：
  - 當啟用 `auto_downscale` 時，節點會自動縮小輸入影像尺寸（額外縮小最多維持在 2x）或使用較低的 `scale_factor`，使輸出維持在限制內。
  - 當停用 `auto_downscale` 時，節點會引發錯誤。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `image` | 經過創意增強並放大的輸出影像。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MagnificImageUpscalerCreativeNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `36c38e87f9f1e568c78cf794aeb0a268c6d25d639006eb2cf18ee040d3071ad4`
