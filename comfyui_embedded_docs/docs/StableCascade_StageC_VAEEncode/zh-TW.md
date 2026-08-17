# StableCascade 階段 C VAE 編碼

StableCascade_StageC_VAEEncode 節點透過 VAE 編碼器處理輸入影像，以產生 Stable Cascade 模型的潛在表示。它首先根據壓縮因子和 VAE 的下採樣比例調整影像大小，然後對調整後的影像進行編碼。此節點輸出兩個潛在張量：一個用於 stage C（實際編碼結果），另一個用於 stage B（一個填零的佔位張量）。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `image` | 要編碼到潛在空間的輸入影像 | IMAGE | 是 | - |
| `vae` | 用於編碼影像的 VAE 模型 | VAE | 是 | - |
| `compression` | 編碼前套用於影像的壓縮因子。影像尺寸除以該值，再乘以 VAE 的下採樣比例。（預設值：42） | INT | 否 | 4-128 |

## 輸出

| 輸出名 | 描述 | 資料類型 |
| --- | --- | --- |
| `stage_c` | 用於 Stable Cascade 模型 stage C 的編碼潛在表示 | LATENT |
| `stage_b` | stage B 的佔位潛在表示。目前回傳一個填零的張量，其維度根據輸入影像尺寸計算。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_StageC_VAEEncode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `1679aaac77057fcc359e5428906d5227f6c2dde721aabbfb5a32c08738ac376c`
