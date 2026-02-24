> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftStyleV3VectorIllustrationNode/zh-TW.md)

此節點為 Recraft API 配置一個樣式，專門選擇 `vector_illustration` 樣式。它允許您選擇性地在該類別中選擇更具體的子樣式。此節點輸出一個樣式配置物件，可以傳遞給其他 Recraft API 節點。

## 輸入參數

| 參數 | 資料類型 | 必填 | 範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `substyle` | STRING | 否 | `"vector_illustration"`<br>`"vector_illustration_flat"`<br>`"vector_illustration_3d"`<br>`"vector_illustration_hand_drawn"`<br>`"vector_illustration_retro"`<br>`"vector_illustration_modern"`<br>`"vector_illustration_abstract"`<br>`"vector_illustration_geometric"`<br>`"vector_illustration_organic"`<br>`"vector_illustration_minimalist"`<br>`"vector_illustration_detailed"`<br>`"vector_illustration_colorful"`<br>`"vector_illustration_monochrome"`<br>`"vector_illustration_grayscale"`<br>`"vector_illustration_pastel"`<br>`"vector_illustration_vibrant"`<br>`"vector_illustration_muted"`<br>`"vector_illustration_warm"`<br>`"vector_illustration_cool"`<br>`"vector_illustration_neutral"`<br>`"vector_illustration_bold"`<br>`"vector_illustration_subtle"`<br>`"vector_illustration_playful"`<br>`"vector_illustration_serious"`<br>`"vector_illustration_elegant"`<br>`"vector_illustration_rustic"`<br>`"vector_illustration_urban"`<br>`"vector_illustration_nature"`<br>`"vector_illustration_fantasy"`<br>`"vector_illustration_sci_fi"`<br>`"vector_illustration_historical"`<br>`"vector_illustration_futuristic"`<br>`"vector_illustration_whimsical"`<br>`"vector_illustration_surreal"`<br>`"vector_illustration_realistic"`<br>`"vector_illustration_stylized"`<br>`"vector_illustration_cartoony"`<br>`"vector_illustration_anime"`<br>`"vector_illustration_comic"`<br>`"vector_illustration_pixel"`<br>`"vector_illustration_low_poly"`<br>`"vector_illustration_high_poly"`<br>`"vector_illustration_isometric"`<br>`"vector_illustration_orthographic"`<br>`"vector_illustration_perspective"`<br>`"vector_illustration_2d"`<br>`"vector_illustration_2.5d"`<br>`"vector_illustration_3d"`<br>`"vector_illustration_4d"` | 在 `vector_illustration` 類別中可選的、更具體的樣式。如果未選擇，則使用基礎的 `vector_illustration` 樣式。 |

## 輸出

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `recraft_style` | STYLEV3 | 一個 Recraft API 樣式配置物件，包含所選的 `vector_illustration` 樣式和可選的子樣式。此物件可以連接到其他 Recraft 節點。 |
