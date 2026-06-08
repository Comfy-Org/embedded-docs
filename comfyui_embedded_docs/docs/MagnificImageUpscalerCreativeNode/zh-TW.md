此節點使用 Magnific AI 服務來放大並創意性地增強圖像。它允許您透過文字提示引導增強過程，選擇特定風格進行最佳化，並控制創意過程的各個方面，例如細節、與原始圖像的相似度以及風格化強度。該節點會以您選擇的倍率（2x、4x、8x 或 16x）輸出放大後的圖像，最大輸出尺寸為 25.3 百萬像素。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `影像` | 要放大和增強的輸入圖像。 | IMAGE | 是 | - |
| `提示詞` | 用於引導圖像創意增強的文字描述。此為選填（預設：空白）。 | STRING | 否 | - |
| `放大倍率` | 放大圖像尺寸的倍率。 | COMBO | 是 | `"2x"`<br>`"4x"`<br>`"8x"`<br>`"16x"` |
| `最佳化目標` | 要針對哪種風格或內容類型來最佳化增強過程。 | COMBO | 是 | `"standard"`<br>`"soft_portraits"`<br>`"hard_portraits"`<br>`"art_n_illustration"`<br>`"videogame_assets"`<br>`"nature_n_landscapes"`<br>`"films_n_photography"`<br>`"3d_renders"`<br>`"science_fiction_n_horror"` |
| `創意` | 控制應用於圖像的創意詮釋程度（預設：0）。 | INT | 否 | -10 到 10 |
| `HDR` | 定義和細節的層級（預設：0）。 | INT | 否 | -10 到 10 |
| `相似度` | 與原始圖像的相似度層級（預設：0）。 | INT | 否 | -10 到 10 |
| `複雜度` | 提示強度與每平方像素的複雜度（預設：0）。 | INT | 否 | -10 到 10 |
| `引擎` | 用於處理的特定 AI 引擎。這是一個進階參數。 | COMBO | 是 | `"automatic"`<br>`"magnific_illusio"`<br>`"magnific_sharpy"`<br>`"magnific_sparkle"` |
| `自動降尺寸` | 啟用時，如果請求的放大倍率會超過最大允許輸出尺寸（25.3 百萬像素），節點將自動縮小輸入圖像。這是一個進階參數（預設：False）。 | BOOLEAN | 否 | - |

**限制條件：**

* 輸入的 `image` 必須恰好是一張圖像。
* 輸入圖像的高度和寬度最小值必須為 160 像素。
* 輸入圖像的長寬比必須介於 1:3 和 3:1 之間。
* 最終輸出尺寸（輸入尺寸乘以 `scale_factor`）不得超過 25,300,000 像素。如果停用 `auto_downscale` 且會超過此限制，節點將引發錯誤。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `影像` | 經過創意增強和放大後的輸出圖像。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MagnificImageUpscalerCreativeNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `f5f046347c2992a2589153e803de14fc23b27187864b45eb566556418ebc161c`
