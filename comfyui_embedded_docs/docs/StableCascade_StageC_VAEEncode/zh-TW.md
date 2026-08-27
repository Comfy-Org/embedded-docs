# StableCascade 階段 C VAE 編碼

StableCascade_StageC_VAEEncode 節點會透過 VAE 編碼器處理輸入影像，為 Stable Cascade 模型產生潛在表示。它會先根據壓縮因子和 VAE 的下採樣比率調整影像大小，再對調整後的影像進行編碼。此節點輸出兩個潛在張量：一個用於階段 C（實際編碼結果），另一個用於階段 B（零填充的佔位張量）。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `影像` | 要編碼到潛在空間的輸入影像 | IMAGE | 是 | - |
| `vae` | 用於對影像進行編碼的 VAE 模型 | VAE | 是 | - |
| `壓縮` | 編碼前應用於影像的壓縮因子。影像尺寸會先除以該值，再乘以 VAE 的下採樣比率。這是一個進階參數。（預設值：42） | INT | 否 | 4-128 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `stage_c` | Stable Cascade 模型階段 C 的編碼潛在表示 | LATENT |
| `stage_b` | 階段 B 的佔位潛在表示。目前回傳一個以輸入影像尺寸計算維度的零填充張量。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_StageC_VAEEncode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `1679aaac77057fcc359e5428906d5227f6c2dde721aabbfb5a32c08738ac376c`
