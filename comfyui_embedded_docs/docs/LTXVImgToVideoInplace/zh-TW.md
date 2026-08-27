# LTXVImgToVideoInplace

LTXVImgToVideoInplace 會將輸入影像編碼至潛在空間，並將這些編碼幀放置在既有潛在影片的開頭。`strength` 值控制編碼影像對這些初始幀的條件化強度；當啟用 `bypass` 時，則原樣返回輸入的 latent。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `vae` | 用於將輸入影像編碼至潛在空間的 VAE 模型。 | VAE | 是 | - |
| `圖片` | 要編碼並用於條件化影片 latent 的輸入影像。 | IMAGE | 是 | - |
| `latent` | 要修改的目標潛在影片表示。 | LATENT | 是 | - |
| `強度` | 控制編碼影像對 latent 初始幀的條件化強度。值為 1.0 時，初始幀會完全由編碼影像條件化；數值越低，條件化強度越弱。初始幀的雜訊遮罩會設為 `1.0 - strength`。（預設值：1.0） | FLOAT | 否 | 0.0 - 1.0 |
| `繞過` | 繞過條件化。啟用時，節點會原樣返回輸入的 latent。（預設值：False） | BOOLEAN | 否 | True or False |

**注意：** `image` 會根據 `latent` 輸入的寬度與高度，自動調整尺寸，以符合 `vae` 編碼所需的空間維度。編碼時僅使用 `image` 的 RGB 通道。

## 輸出

| 輸出名 | 說明 | 資料類型 |
| --- | --- | --- |
| `latent` | 產生的潛在影片表示。當 bypass 停用時，其中包含更新的 `samples`，以及將條件化強度套用至初始幀的 `noise_mask`。當 bypass 啟用時，則為原樣返回的輸入 latent。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVImgToVideoInplace/zh-TW.md)

---
**Source fingerprint (SHA-256):** `69faa4b2e7b0fedeee531dc5a8809e23a79c9ce03e9760afb865160594fef30d`
