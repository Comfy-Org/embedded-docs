# Trellis2 上採樣階段

此節點會將 512 解析度的形狀 latent 上採樣為高解析度稀疏座標，並在目標解析度下準備第二個形狀階段取樣作業。它會將各階段的中繼資料附加到條件中，讓模型可在生成期間使用。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `正向` | 要附加放大階段形狀中繼資料的正向條件。 | CONDITIONING | 是 | |
| `負向` | 要附加放大階段形狀中繼資料的負向條件。 | CONDITIONING | 是 | |
| `shape_latent` | 來自第一個形狀階段 KSampler 的 512 解析度形狀 latent 輸出。 | LATENT | 是 | |
| `vae` | 用於將形狀 latent 解碼為高解析度稀疏座標的 Trellis2 VAE。 | VAE | 是 | |
| `target_resolution` | 上採樣後形狀的體素解析度。越高 = 更多細節、更多 VRAM。預設：1024。 | INT | 是 | 1024 - 2048 （步進值：128） |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `positive` | 已附加放大階段形狀中繼資料的正向條件。 | CONDITIONING |
| `negative` | 已附加放大階段形狀中繼資料的負向條件。 | CONDITIONING |
| `latent` | 為目標解析度下的第二個形狀階段取樣作業所準備的零填充 latent，帶有上採樣後的座標、每個樣本的座標計數，以及座標解析度中繼資料。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Trellis2UpsampleStage/zh-TW.md)

---
**Source fingerprint (SHA-256):** `0582579bfab487718d69789de508a5ec243d98a0e06ad7165c406154a64677d6`
