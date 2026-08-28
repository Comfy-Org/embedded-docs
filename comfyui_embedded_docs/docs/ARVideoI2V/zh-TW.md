# ARVideoI2V

## 概覽

此節點為使用因果強制（Causal Forcing）或自強制（Self-Forcing）的 AR（自回歸）影片模型準備圖像轉影片的生成設定。它使用 VAE 將起始圖像編碼到潛在空間，並將其儲存在模型的 transformer 選項中，以便影片採樣過程可以在去噪之前為 KV 快取注入初始值。它使用與文字轉影片相同的模型檢查點，因此不需要單獨的圖像轉影片架構。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 用於生成的 AR 影片模型。 | MODEL | 是 | - |
| `vae` | 用於將起始圖像編碼到潛在空間的 VAE 模型。 | VAE | 是 | - |
| `起始圖像` | 作為生成影片第一幀的初始圖像。僅使用輸入批次中的第一張圖像，且僅編碼其 RGB 通道。 | IMAGE | 是 | - |
| `寬度` | 生成影片幀的寬度（預設值：832）。 | INT | 是 | 16 至 8192 (step: 16) |
| `高度` | 生成影片幀的高度（預設值：480）。 | INT | 是 | 16 至 8192 (step: 16) |
| `長度` | 生成影片的總幀數（預設值：81）。 | INT | 是 | 1 至 1024 (step: 4) |
| `批次大小` | 單一批次中要生成的影片序列數量（預設值：1）。 | INT | 是 | 1 至 64 |

注意：起始圖像在編碼前會調整為指定的 `width` 和 `height`。潛在時間維度計算為 `((length - 1) // 4) + 1`，潛在空間維度為 `height / 8` 和 `width / 8`。

## 輸出

| 輸出名 | 描述 | 資料類型 |
| --- | --- | --- |
| `MODEL` | 具有編碼後起始圖像的克隆模型，儲存在其 transformer 選項中（`ar_config.initial_latent`），採樣器用它來在去噪前為 KV 快取注入初始值。 | MODEL |
| `LATENT` | 一個形狀為 `[batch_size, 16, lat_t, height // 8, width // 8]` 的零填充潛在張量，其中 `lat_t = ((length - 1) // 4) + 1`。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ARVideoI2V/zh-TW.md)

---
**Source fingerprint (SHA-256):** `984834951b9d5a22aef51c85a5019fd8ba58cdb2d6fff235371ed29f316896d8`
