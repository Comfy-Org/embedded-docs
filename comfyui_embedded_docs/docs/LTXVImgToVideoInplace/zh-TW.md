# LTXVImgToVideoInplace

LTXVImgToVideoInplace 節點透過將輸入影像編碼到其初始影格，對影片潛在表示進行條件化。其運作方式是使用 VAE 將影像編碼到潛在空間，然後將潛在影片樣本的初始影格替換為此編碼影像。套用雜訊遮罩，使得條件化強度控制在生成過程中影像對這些初始影格的影響程度。

## 輸入

| 參數 | 描述 | 資料型別 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `vae` | 用於將輸入影像編碼到潛在空間的 VAE 模型。 | VAE | 是 | - |
| `image` | 要編碼並用於對影片潛在表示進行條件化的輸入影像。 | IMAGE | 是 | - |
| `latent` | 要修改的目標影片潛在表示。 | LATENT | 是 | - |
| `strength` | 控制編碼影像對初始潛在影格的條件化強度。值為 1.0 時，初始影格會被完全條件化；數值較低時則套用較弱的條件化。（預設值：1.0） | FLOAT | 否 | 0.0 - 1.0 |
| `bypass` | 繞過條件化。啟用時，節點會回傳未變更的輸入潛在表示。（預設值：False） | BOOLEAN | 否 | - |

**注意：** 系統會根據 `latent` 輸入的寬度和高度，自動調整 `image` 的大小（使用雙線性插值），以符合 `vae` 編碼所需的空間維度。僅使用影像的前 3 個色彩通道（RGB）；任何 Alpha 通道都會被忽略。

## 輸出

| 輸出名稱 | 描述 | 資料型別 |
| --- | --- | --- |
| `latent` | 修改後的影片潛在表示。其中包含更新後的樣本，以及一個將條件化強度套用至初始影格的 `noise_mask`。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVImgToVideoInplace/zh-TW.md)

---
**Source fingerprint (SHA-256):** `69faa4b2e7b0fedeee531dc5a8809e23a79c9ce03e9760afb865160594fef30d`
