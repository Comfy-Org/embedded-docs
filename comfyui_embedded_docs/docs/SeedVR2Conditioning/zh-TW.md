# 套用 SeedVR2 Conditioning

此節點從 VAE 潛在變量為 SeedVR2 模型建立正向和負向條件。它驗證輸入的潛在變量形狀和模型結構，然後產生引導影像或影片取樣的正向和負向條件。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | SeedVR2 模型。 | MODEL | 是 | - |
| `vae_conditioning` | 用於建立條件的 SeedVR2 VAE 潛在變量（顯示名稱：latent）。 | LATENT | 是 | - |

注意：`vae_conditioning` 潛在變量必須是 Comfy 通道優先佈局中的 5 維張量（B、C、T、H、W），其中 C 是預期的 SeedVR2 VAE 通道數。如果潛在變量不是 5 維、其通道數不匹配，或看起來是通道最後佈局，節點將引發錯誤。`model` 輸入必須是具有預期 SeedVR2 結構的模型。在內部，節點會向潛在變量附加一個常數遮罩通道，並將產生的條件同時附加到正向和負向條件池。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `positive` | 用於取樣的正向條件。 | CONDITIONING |
| `negative` | 用於取樣的負向條件。 | CONDITIONING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedVR2Conditioning/zh-TW.md)

---
**Source fingerprint (SHA-256):** `28e508bdd776e2e3f5f2f93bfc29a1a1d1c34a11dbdc7f421d197ddbfa85f0f5`
