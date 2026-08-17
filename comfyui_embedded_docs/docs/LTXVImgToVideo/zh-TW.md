# LTXV 圖片轉影片

LTXVImgToVideo 節點準備一個潛在表示，用於從輸入影像生成影片。影像會調整為指定的寬度和高度，使用 VAE 進行編碼，並放置在第一個潛在影格中。使用 `strength` 建立雜訊遮罩，以控制原始影像內容的保留或修改程度，而正向與負向條件資料則原封不動地傳遞。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `positive` | 作為輸入提供並原樣返回的正向條件資料。 | CONDITIONING | 是 | - |
| `negative` | 作為輸入提供並原樣返回的負向條件資料。 | CONDITIONING | 是 | - |
| `vae` | 用於將輸入影像編碼到潛在空間的 VAE 模型。 | VAE | 是 | - |
| `image` | 輸入影像，會調整大小並編碼以構成影片潛在序列的開頭。 | IMAGE | 是 | - |
| `width` | 輸出影片的寬度（像素）（預設：768，步進：32）。 | INT | 是 | 64 to MAX_RESOLUTION |
| `height` | 輸出影片的高度（像素）（預設：512，步進：32）。 | INT | 是 | 64 to MAX_RESOLUTION |
| `length` | 生成的影片中的影格數（預設：97，步進：8）。 | INT | 是 | 9 to MAX_RESOLUTION |
| `batch_size` | 一個潛在批次中要生成的影片數量（預設：1）。 | INT | 是 | 1 to 4096 |
| `strength` | 控制第一個潛在影格中保留多少已編碼的影像內容。值為 1.0 時完全保留原始影像，而 0.0 則允許最大程度的修改（預設：1.0）。 | FLOAT | 是 | 0.0 to 1.0 |

注意：`MAX_RESOLUTION` 是 ComfyUI 安裝所允許的最大解析度。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `positive` | 未經修改直接傳遞的正向條件。 | CONDITIONING |
| `negative` | 未經修改直接傳遞的負向條件。 | CONDITIONING |
| `latent` | 影片潛在序列，包含序列開頭的已編碼輸入影像，以及基於 `strength` 的雜訊遮罩。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVImgToVideo/zh-TW.md)

---
**Source fingerprint (SHA-256):** `4ebc7f80b4d9ac3329e3349c7048885de22b827b5bdd102976687afd7e07a16b`
