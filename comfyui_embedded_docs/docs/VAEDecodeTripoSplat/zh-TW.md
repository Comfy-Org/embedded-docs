# TripoSplat 解碼

將 TripoSplat 的潛在表示解碼為 3D 高斯潑濺。此節點接收來自 TripoSplat 模型的取樣潛在，並將其重建為一組 3D 高斯，可透過調整產生的高斯數量來改變密度。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `samples` | 要解碼的潛在樣本 | LATENT | 是 | - |
| `vae` | TripoSplat VAE 解碼器 | VAE | 是 | - |
| `num_gaussians` | 要產生的高斯數量（四捨五入至 32 的倍數）。262144 符合八叉樹的點密度；更高的值會對相同點進行過度取樣（更密集，但不會新增細節），並按比例消耗更多 VRAM/時間。預設：262144 | INT | 是 | 32 至 1048576（步驟：32） |
| `seed` | 為八叉樹點取樣器（全域 RNG）設定種子，以進行確定性解碼。預設：0 | INT | 是 | 0 至 18446744073709551615 |

**注意：** `num_gaussians` 值會自動四捨五入為 VAE 解碼器的 gaussians-per-point 設定的倍數。實際使用的數量可能與輸入值略有不同。

## 輸出

| 輸出名 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `splat` | 包含位置、縮放、旋轉、不透明度與球諧係數的解碼 3D 高斯潑濺 | SPLAT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEDecodeTripoSplat/zh-TW.md)

---
**Source fingerprint (SHA-256):** `5c2b21cee31c68a6440ab4c7156e0d5c041ce7264f6467a508dc41e2eb0dc598`
