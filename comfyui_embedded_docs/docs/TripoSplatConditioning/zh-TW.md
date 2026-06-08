# TripoSplat 條件設定

此節點使用 DINOv3 和 Flux2 VAE 對輸入影像進行編碼，為 TripoSplat 模型建立正向和負向條件設定資料。同時也會生成一個固定大小的雜訊目標（潛在空間加上相機資料），作為 KSampler 的起始點。

## ## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `clip_vision` | DINOv3 ViT-H/16+ 影像編碼器 | CLIP_VISION | 是 | - |
| `vae` | Flux2 VAE | VAE | 是 | - |
| `圖像` | 要編碼的輸入影像 | IMAGE | 是 | - |

## ## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `positive` | 包含 DINOv3 特徵和 Flux2 VAE 潛在空間的正向條件設定資料 | CONDITIONING |
| `negative` | 包含零填充 DINOv3 特徵和零填充 Flux2 VAE 潛在空間的負向條件設定資料 | CONDITIONING |
| `latent` | KSampler 使用的固定大小雜訊目標（潛在序列加上相機標記） | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoSplatConditioning/zh-TW.md)

---
**Source fingerprint (SHA-256):** `9187a4a020818b9adc762eb41e913086b59d62c47abe92d4bafdb14bc8779f51`
