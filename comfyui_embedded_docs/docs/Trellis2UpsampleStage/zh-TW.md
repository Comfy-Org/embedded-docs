# Trellis2UpsampleStage

此節點接收第一個形狀階段取樣過程產生的 512 解析度形狀潛在變數，將其放大至較高的目標解析度，並準備第二個形狀階段取樣過程所需的條件與潛在變數。它會將每個階段的後設資料附加到條件，以便模型在生成期間使用。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `positive` | 附加了放大階段形狀後設資料的正向條件。 | CONDITIONING | 是 | |
| `negative` | 附加了放大階段形狀後設資料的負向條件。 | CONDITIONING | 是 | |
| `shape_latent` | 來自第一個形狀階段 KSampler 輸出的 512 解析度形狀潛在變數。 | LATENT | 是 | |
| `vae` | 用於將形狀潛在變數解碼為高解析度稀疏座標的 Trellis2 VAE。 | VAE | 是 | |
| `target_resolution` | 放大後形狀的體素解析度。數值越高細節越多，但需要更多 VRAM。預設值：1024。 | INT | 是 | 1024 - 2048 (step 128) |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `positive` | 附加了放大階段形狀後設資料的正向條件。 | CONDITIONING |
| `negative` | 附加了放大階段形狀後設資料的負向條件。 | CONDITIONING |
| `latent` | 為目標解析度下的第二個形狀階段取樣過程準備的零填充潛在變數，攜帶放大後的座標與解析度後設資料。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Trellis2UpsampleStage/zh-TW.md)

---
**Source fingerprint (SHA-256):** `0582579bfab487718d69789de508a5ec243d98a0e06ad7165c406154a64677d6`
