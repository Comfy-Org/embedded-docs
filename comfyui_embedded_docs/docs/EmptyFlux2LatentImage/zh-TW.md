# 空白 Flux 轉 Latent

The Empty Flux 2 Latent 節點用於建立一個空白、空值的中繼表示（latent representation）。它會產生一個充滿零的張量，作為 Flux 模型去噪過程的起點。中繼表示的尺寸由輸入的寬度與高度決定，並會以 16 為縮放因子進行縮小。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `寬度` | 要產生的最終影像寬度。中繼表示的寬度會是此數值除以 16。預設值為 1024。 | INT | 是 | 16 到 8192 |
| `高度` | 要產生的最終影像高度。中繼表示的高度會是此數值除以 16。預設值為 1024。 | INT | 是 | 16 到 8192 |
| `批次大小` | 單一批次中要產生之中繼表示樣本的數量。預設值為 1。 | INT | 否 | 1 到 4096 |

**注意：** `width` 和 `height` 輸入必須可被 16 整除，因為節點會在內部以這個因數將其相除以建立中繼表示的尺寸。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `samples` | 充滿零的中繼張量。形狀為 `[batch_size, 128, height // 16, width // 16]`。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyFlux2LatentImage/zh-TW.md)

---
**Source fingerprint (SHA-256):** `f8356568f0ab521a3f246d1f672492e74f9a2f449694961b913bd14a5f0f3878`
