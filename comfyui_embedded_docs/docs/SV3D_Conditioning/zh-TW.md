# SV3D_Conditioning

SV3D_Conditioning 節點使用 SV3D 模型為 3D 影片生成準備 conditioning 資料。它接受一張初始影像，並透過 CLIP vision 與 VAE 編碼器進行處理，以建立正向與負向 conditioning，以及潛在表示。節點會根據指定的影片幀數，為多幀影片生成生成相機仰角與方位角序列。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `clip_vision` | 用於編碼輸入影像的 CLIP vision 模型 | CLIP_VISION | 是 | - |
| `init_image` | 作為 3D 影片生成起點的初始影像 | IMAGE | 是 | - |
| `vae` | 用於將影像編碼到潛在空間的 VAE 模型 | VAE | 是 | - |
| `width` | 生成影片幀的輸出寬度（預設值：576，必須為 8 的倍數） | INT | 是 | 16 to MAX_RESOLUTION (step of 8) |
| `height` | 生成影片幀的輸出高度（預設值：576，必須為 8 的倍數） | INT | 是 | 16 to MAX_RESOLUTION (step of 8) |
| `video_frames` | 影片序列要生成的幀數（預設值：21） | INT | 是 | 1 to 4096 |
| `elevation` | 3D 視圖的相機仰角（度），套用於每一幀（預設值：0.0） | FLOAT | 是 | -90.0 to 90.0 (step of 0.1) |

注意：相機方位角從 0 度開始，每一幀增加 360 / (video_frames - 1) 度，因此相機會在整個序列中環繞物體一圈。相同的 `elevation` 值會套用於所有幀。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `positive` | 包含影像嵌入與相機參數的正向 conditioning 資料，用於生成 | CONDITIONING |
| `negative` | 嵌入歸零的負向 conditioning 資料，用於對比生成 | CONDITIONING |
| `latent` | 一個空的潛在張量，其維度與指定的影片幀數和解析度相符 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SV3D_Conditioning/zh-TW.md)

---
**Source fingerprint (SHA-256):** `e28173cfa560290e66b032687088cf0b981256ca5c21f6aa608e0fdaec886665`
