# TripoSplat 條件編碼

此節點使用 DINOv3 影像編碼器和 Flux2 VAE 對輸入影像進行編碼，為 TripoSplat 模型建立正向與負向條件資料。它還會產生固定大小的雜訊目標（潛在變數加相機資料），作為 KSampler 的起點。

## 輸入

| 參數 | 說明 | 資料型別 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `clip_vision` | DINOv3 ViT-H/16+ 影像編碼器 | CLIP_VISION | 是 | - |
| `vae` | Flux2 VAE | VAE | 是 | - |
| `圖像` | 要編碼的輸入影像 | IMAGE | 是 | - |

## 輸出

| 輸出名 | 說明 | 資料型別 |
|-------------|-------------|-----------|
| `正向` | 包含 DINOv3 特徵和 Flux2 VAE 潛在變數的正向條件資料 | CONDITIONING |
| `負向` | 包含零填充 DINOv3 特徵和零填充 Flux2 VAE 潛在變數的負向條件資料 | CONDITIONING |
| `latent` | 供 KSampler 使用的固定大小雜訊目標（潛在變數 + 相機） | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoSplatConditioning/zh-TW.md)

---
**Source fingerprint (SHA-256):** `59ebeef272d125a2cc2045f4ff54f99268b1273d0a1fd46f7462e6d312f3a805`
