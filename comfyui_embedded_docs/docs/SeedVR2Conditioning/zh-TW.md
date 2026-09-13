# 套用 SeedVR2 Conditioning

從 VAE latent 建立正向與負向條件，以供 SeedVR2 模型使用。它會驗證輸入 latent 與模型結構，將遮罩通道加入 latent，並回傳兩個條件輸出。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | SeedVR2 模型。 | MODEL | 是 | - |
| `vae_conditioning` | 要用來建立條件的 SeedVR2 VAE latent（顯示名稱：latent）。 | LATENT | 是 | - |

注意：`vae_conditioning` latent 必須是採用 Comfy channel-first 佈局的 5-D 張量（B, C, T, H, W），其中 C 是 SeedVR2 VAE 預期的通道數。如果 latent 不是 5-D、通道數不符，或張量似乎採用 channel-last 佈局，此節點會引發錯誤。`model` 輸入必須具有 SeedVR2 預期的結構；此節點會解析其內部的擴散模型，並讀取其正向與負向條件。在內部，此節點會將一個固定遮罩通道附加到 latent，並將產生的條件附加到正向與負向條件輸出。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `positive` | 用於取樣的正向條件。 | CONDITIONING |
| `negative` | 用於取樣的負向條件。 | CONDITIONING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedVR2Conditioning/zh-TW.md)

---
**Source fingerprint (SHA-256):** `28e508bdd776e2e3f5f2f93bfc29a1a1d1c34a11dbdc7f421d197ddbfa85f0f5`
