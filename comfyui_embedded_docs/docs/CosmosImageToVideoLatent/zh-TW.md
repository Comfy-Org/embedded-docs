CosmosImageToVideoLatent 節點從輸入圖像建立影片潛在表示。它會生成一個空白的影片潛在，並可選擇性地將起始和/或結束圖像編碼到影片序列的開頭和/或結尾影格中。當提供圖像時，它也會建立相應的雜訊遮罩，以指示在生成過程中應保留潛在的哪些部分。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `vae` | 用於將圖像編碼到潛在空間的 VAE 模型 | VAE | 是 | - |
| `寬度` | 輸出影片的寬度（像素），預設值：1280 | INT | 是 | 16 至 MAX_RESOLUTION |
| `高度` | 輸出影片的高度（像素），預設值：704 | INT | 是 | 16 至 MAX_RESOLUTION |
| `長度` | 影片序列中的影格數量，預設值：121 | INT | 是 | 1 至 MAX_RESOLUTION |
| `批次大小` | 要生成的潛在批次數量，預設值：1 | INT | 是 | 1 至 4096 |
| `起始影像` | 可選，編碼至影片序列開頭的圖像 | IMAGE | 否 | - |
| `結束圖片` | 可選，編碼至影片序列結尾的圖像 | IMAGE | 否 | - |

**注意：** 當未提供 `start_image` 和 `end_image` 時，節點會返回一個不帶任何雜訊遮罩的空白潛在。當提供任一圖像時，潛在的對應部分會被編碼並相應地進行遮罩處理。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `latent` | 生成的影片潛在表示，包含可選的編碼圖像及相應的雜訊遮罩 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CosmosImageToVideoLatent/zh-TW.md)

---
**Source fingerprint (SHA-256):** `31ce4dc577c672e0b3dc0bfb6644b2ef7ab737f6c4ee5e0677973b6a4efdd66d`
