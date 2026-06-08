此節點用於設定 Recraft API 使用的樣式，專門選擇「digital_illustration」（數位插畫）風格。您可以選擇一個可選的子風格，進一步調整生成圖像的藝術方向。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `子風格` | 可選的子風格，用於指定特定類型的數位插畫。若未選擇，則使用基礎的「digital_illustration」風格。 | STRING | 否 | `"digital_illustration"`<br>`"digital_illustration_anime"`<br>`"digital_illustration_cartoon"`<br>`"digital_illustration_comic"`<br>`"digital_illustration_concept_art"`<br>`"digital_illustration_fantasy"`<br>`"digital_illustration_futuristic"`<br>`"digital_illustration_graffiti"`<br>`"digital_illustration_graphic_novel"`<br>`"digital_illustration_hyperrealistic"`<br>`"digital_illustration_ink"`<br>`"digital_illustration_manga"`<br>`"digital_illustration_minimalist"`<br>`"digital_illustration_pixel_art"`<br>`"digital_illustration_pop_art"`<br>`"digital_illustration_retro"`<br>`"digital_illustration_sci_fi"`<br>`"digital_illustration_sticker"`<br>`"digital_illustration_street_art"`<br>`"digital_illustration_surreal"`<br>`"digital_illustration_vector"` |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `recraft_style` | 一個已設定的樣式物件，包含所選的「digital_illustration」風格及可選的子風格，準備傳遞給其他 Recraft API 節點使用。 | STYLEV3 |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftStyleV3DigitalIllustration/zh-TW.md)

---
**Source fingerprint (SHA-256):** `e52790a670839608ee1cb576e802a54d3bf2ca879ec288a24acd4ac7db27021a`
