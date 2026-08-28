# Trellis2UpsampleStage

此節點接收第一個形狀階段取樣過程產生的 512 解析度形狀 latent，將其放大到更高的目標解析度，並準備第二個形狀階段取樣過程所需的 conditioning 和 latent。它將每個階段的元數據附加到 conditioning 上，以便模型在生成期間使用。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `正向` | 已附加放大階段形狀元數據的正向 conditioning。 | CONDITIONING | 是 | |
| `負向` | 已附加放大階段形狀元數據的負向 conditioning。 | CONDITIONING | 是 | |
| `shape_latent` | 第一個形狀階段 KSampler 輸出的 512 解析度形狀 latent。 | LATENT | 是 | |
| `vae` | 用於將形狀 latent 解碼為高解析度稀疏座標的 Trellis2 VAE。 | VAE | 是 | |
| `target_resolution` | 放大後形體的體素解析度。數值越高 = 細節越多，VRAM 用量越高。預設值：1024。 | INT | 是 | 1024 - 2048 (step 128) |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `正向` | 已附加放大階段形狀元數據的正向 conditioning。 | CONDITIONING |
| `負向` | 已附加放大階段形狀元數據的負向 conditioning。 | CONDITIONING |
| `latent` | 為第二個形狀階段取樣過程準備的零填充 latent，目標解析度，並攜帶放大後的座標與解析度元數據。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Trellis2UpsampleStage/zh-TW.md)

---
**Source fingerprint (SHA-256):** `0582579bfab487718d69789de508a5ec243d98a0e06ad7165c406154a64677d6`
