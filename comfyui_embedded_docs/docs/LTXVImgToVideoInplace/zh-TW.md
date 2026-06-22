# LTXVImgToVideoInplace

## 概述

LTXVImgToVideoInplace 節點透過將輸入影像編碼到其初始影格中，來對影片潛在表示進行條件化處理。其運作方式是使用 VAE 將影像編碼到潛在空間，然後根據指定的強度將其與現有的潛在樣本混合。這使得影像能夠作為影片生成的起點或條件化訊號。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `vae` | 用於將輸入影像編碼到潛在空間的 VAE 模型。 | VAE | 是 | - |
| `圖片` | 要編碼並用於條件化影片潛在表示的輸入影像。 | IMAGE | 是 | - |
| `latent` | 要修改的目標影片潛在表示。 | LATENT | 是 | - |
| `強度` | 控制編碼影像融入潛在表示的混合強度。值為 1.0 時完全取代初始影格，較低的值則進行混合。（預設值：1.0） | FLOAT | 否 | 0.0 - 1.0 |
| `繞過` | 繞過條件化處理。啟用時，節點會直接回傳未修改的輸入潛在表示。（預設值：False） | BOOLEAN | 否 | - |

**注意：** `image` 會根據 `latent` 輸入的寬度和高度，自動調整大小以符合 `vae` 編碼所需的空間維度。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `latent` | 修改後的影片潛在表示。包含更新後的樣本，以及一個將條件化強度應用於初始影格的 `noise_mask`。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVImgToVideoInplace/zh-TW.md)

---
**Source fingerprint (SHA-256):** `49df511591071f51e2b86f2302cfb438d18b5e1ade7ef228345f65fddf88dbcc`
