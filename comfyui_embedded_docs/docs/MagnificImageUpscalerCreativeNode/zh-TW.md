# Magnific 影像放大（創意）

此節點使用 Magnific AI 服務來放大並創意增強影像。您可以透過文字提示引導增強過程，選擇要最佳化的特定樣式，並控制創作過程的各個方面，例如細節、與原圖的相似度以及風格化強度。節點會以您選擇的倍數（2 倍、4 倍、8 倍或 16 倍）輸出放大後的影像，最大輸出尺寸為 25.3 百萬像素。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `影像` | 要放大和增強的輸入影像。 | IMAGE | 是 | - |
| `提示詞` | 用於引導影像創意增強的文字描述。此為選填（預設：空）。 | STRING | 否 | - |
| `放大倍率` | 放大影像尺寸的倍數。 | COMBO | 是 | `"2x"`<br>`"4x"`<br>`"8x"`<br>`"16x"` |
| `最佳化目標` | 要最佳化增強過程的樣式或內容類型。 | COMBO | 是 | `"standard"`<br>`"soft_portraits"`<br>`"hard_portraits"`<br>`"art_n_illustration"`<br>`"videogame_assets"`<br>`"nature_n_landscapes"`<br>`"films_n_photography"`<br>`"3d_renders"`<br>`"science_fiction_n_horror"` |
| `創意` | 控制套用於影像的創意詮釋程度（預設：0）。 | INT | 否 | -10 到 10 |
| `HDR` | 清晰度與細節的程度（預設：0）。 | INT | 否 | -10 到 10 |
| `相似度` | 與原始影像的相似度（預設：0）。 | INT | 否 | -10 到 10 |
| `複雜度` | 提示詞的強度以及每平方像素的精細度（預設：0）。 | INT | 否 | -10 到 10 |
| `引擎` | 要用於處理的特定 AI 引擎。這是進階參數。 | COMBO | 是 | `"automatic"`<br>`"magnific_illusio"`<br>`"magnific_sharpy"`<br>`"magnific_sparkle"` |
| `自動降尺寸` | 若輸出會超過最大像素限制，自動縮小輸入影像（預設：False）。這是進階參數。 | BOOLEAN | 否 | - |

**約束條件：**

* 輸入的 `image` 必須恰好是一張影像。
* 輸入影像的高度和寬度最低必須為 160 像素。
* 輸入影像的長寬比必須介於 1:3 和 3:1 之間。
* 最終輸出尺寸（輸入尺寸乘以 `scale_factor`）不得超過 25,300,000 像素。若將超過此限制：
  - 啟用 `auto_downscale` 時，節點會自動縮小輸入影像尺寸（不超過 2 倍）或使用較低的 `scale_factor`，使輸出維持在限制內。
  - 停用 `auto_downscale` 時，節點會產生錯誤。

## 輸出

| 輸出名 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `image` | 經創意增強並放大的輸出影像。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MagnificImageUpscalerCreativeNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `36c38e87f9f1e568c78cf794aeb0a268c6d25d639006eb2cf18ee040d3071ad4`
