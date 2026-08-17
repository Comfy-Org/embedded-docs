# 套用 SeedVR2 Conditioning

此節點從 VAE 潛在變數（latent）建構正向和負向條件（conditioning），以供 SeedVR2 模型使用。它會向潛在變數新增一個遮罩通道，然後將其與模型內建的正向和負向條件嵌入配對，以產生取樣所需的條件值。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | SeedVR2 模型。 | MODEL | 是 | - |
| `vae_conditioning` | 用於建構條件的 VAE 潛在變數。顯示名稱：latent。 | LATENT | 是 | - |

`vae_conditioning` 潛在變數必須是採用 Comfy 通道優先佈局（B, C, T, H, W）的 5 維張量，且通道數需符合 SeedVR2 VAE 的預期。通道在後（channel-last）的潛在變數將被拒絕並報錯。`model` 輸入必須是具備預期內部結構的有效 SeedVR2 模型。

## 輸出

| 輸出名 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `positive` | 用於取樣的正向條件。 | CONDITIONING |
| `negative` | 用於取樣的負向條件。 | CONDITIONING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedVR2Conditioning/zh-TW.md)

---
**Source fingerprint (SHA-256):** `28e508bdd776e2e3f5f2f93bfc29a1a1d1c34a11dbdc7f421d197ddbfa85f0f5`
