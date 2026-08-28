# VOIDWarpedNoise

為 VOID 影片精化流程的第二遍處理產生時間相關的雜訊。它接收來自 Pass 1 的輸出影片，並沿著光流向量扭曲高斯雜訊，產生與影片內容一致移動的雜訊。此扭曲雜訊用作 Pass 2 的起始潛在變量，以改善最終輸出的時間一致性。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `optical_flow` | 來自 OpticalFlowLoader (RAFT-large) 的光流模型。 | OPTICAL_FLOW | 是 | - |
| `video` | Pass 1 的輸出影片幀 [T, H, W, 3]。 | IMAGE | 是 | - |
| `width` | 輸出潛在變量的寬度（預設值：672）。 | INT | 是 | 16 to MAX_RESOLUTION (step 8) |
| `height` | 輸出潛在變量的高度（預設值：384）。 | INT | 是 | 16 to MAX_RESOLUTION (step 8) |
| `length` | 像素幀數。向下取整以使 `latent_t` 為偶數（`patch_size_t=2` 要求），例如 49 → 45（預設值：45）。 | INT | 是 | 1 to MAX_RESOLUTION (step 1) |
| `batch_size` | 要產生的相同雜訊序列數量（預設值：1）。 | INT | 是 | 1 至 64 |

**關於 `length` 參數的說明：** `length` 值會自動向下取整至最接近的有效值，以產生偶數的 `latent_t` 維度。這是 CogVideoX-Fun-V1.5 模型 `patch_size_t=2` 約束所要求的。發生取整時會記錄警告。

## 輸出

| 輸出名 | 描述 | 資料類型 |
| --- | --- | --- |
| `warped_noise` | 一個 5D 張量 (B, C, T, H, W)，包含經光流扭曲的高斯雜訊，可直接用作 VOID Pass 2 的初始潛在變量。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDWarpedNoise/zh-TW.md)

---
**Source fingerprint (SHA-256):** `f46b0a73b09a5d2d0bc25676f9571563c6bb8bad8d835e7564ac092c72136107`
