# 應用 SeedVR2 條件設定

此節點從 VAE 潛在空間建立正向與負向條件設定，以供 SeedVR2 模型使用。它會準備引導影像或影片生成過程所需的條件資料。

## ## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | SeedVR2 模型。 | MODEL | 是 | - |
| `vae_conditioning` | 用於建立條件設定的 VAE 潛在空間。 | LATENT | 是 | - |

## ## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `model` | SeedVR2 模型。 | MODEL |
| `positive` | 用於引導生成過程的正向條件設定。 | CONDITIONING |
| `negative` | 用於引導生成過程的負向條件設定。 | CONDITIONING |
| `latent` | 處理後的潛在空間樣本。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedVR2Conditioning/zh-TW.md)

---
**Source fingerprint (SHA-256):** `8f99c0e712c5c6fc76261d6d72c5c08b7202c77827ecf2549240fc530c1b65bd`
