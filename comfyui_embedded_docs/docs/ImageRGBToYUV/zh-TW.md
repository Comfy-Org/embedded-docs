# RGB 轉 YUV

ImageRGBToYUV 節點會使用 RGB 轉 YCbCr 的色彩轉換，將 RGB 影像轉換為 YUV 形式的色彩分量。它會將結果拆分為三張獨立的影像 —— Y（亮度，或稱明度）、U（藍色差色度）與 V（紅色差色度）—— 並以與輸入相同的寬度和高度回傳每個分量。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `影像` | 要轉換為 Y、U、V 分量的輸入 RGB 影像。若影像包含 alpha 通道，則只會使用前三個（RGB）通道。 | IMAGE | 是 | - |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `Y` | YUV 色彩空間的亮度（明度）分量，以三通道影像回傳 | IMAGE |
| `U` | YUV 色彩空間的藍色差色度分量，以三通道影像回傳 | IMAGE |
| `V` | YUV 色彩空間的紅色差色度分量，以三通道影像回傳 | IMAGE |

每個輸出的寬度和高度都與輸入影像相同。對應的 Y、U 或 V 分量會在所有三個通道中重複，因此每個輸出都會以標準的三通道影像回傳。

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageRGBToYUV/zh-TW.md)

---
**Source fingerprint (SHA-256):** `1a75ce64dfaec316a8f4b3a210cede388c9ba12d3ab3ec5ec14b0027be383744`
