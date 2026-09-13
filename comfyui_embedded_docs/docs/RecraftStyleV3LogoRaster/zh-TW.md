# Recraft Style - 標誌點陣圖

此節點會為生成標誌圖片選擇標誌點陣風格與特定子風格。它專門用於建立採用點陣視覺處理的標誌設計。所選風格會以 Recraft 風格設定形式回傳，可傳遞至其他 Recraft 節點。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `子風格` | 要用於標誌生成的特定標誌點陣子風格 | COMBO | 是 | `"bold"`<br>`"minimal"`<br>`"vibrant"`<br>`"handdrawn"`<br>`"geometric"`<br>`"vintage"`<br>`"neon"`<br>`"gradient"`<br>`"flat"`<br>`"outline"`<br>`"mascot"`<br>`"badge"`<br>`"abstract"`<br>`"retro"`<br>`"modern"`<br>`"playful"`<br>`"luxury"`<br>`"tech"`<br>`"nature"`<br>`"food"`<br>`"sport"`<br>`"fashion"`<br>`"music"`<br>`"travel"`<br>`"education"`<br>`"health"`<br>`"finance"`<br>`"realestate"`<br>`"nonprofit"` |

注意：必須一律選擇子風格；沒有 "none" 選項。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `recraft_style` | 所選的 Recraft 風格設定，包含標誌點陣風格與所選子風格 | CUSTOM |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftStyleV3LogoRaster/zh-TW.md)

---
**Source fingerprint (SHA-256):** `59c3af980261d2b20b6d401980639c6bbc3a8b7c4e2370ca048ccb07535b10e7`
