# VOIDWarpedNoise

為 VOID 影片精煉流程的第二階段產生具時間相關性的雜訊。它會接收 Pass 1 輸出影片，並沿著光流向量扭曲高斯雜訊，使雜訊的移動與影片內容保持一致。產生的扭曲雜訊會用作 Pass 2 的起始 latent，從而改善最終輸出的時間一致性。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `optical_flow` | 來自 OpticalFlowLoader (RAFT-large) 的光流模型。 | OPTICAL_FLOW | 是 | - |
| `video` | Pass 1 輸出影片影格 [T, H, W, 3]。 | IMAGE | 是 | - |
| `width` | 目標寬度，單位為像素（預設：672）。在產生雜訊之前，會先將輸入影片縮放到此寬度，而 latent 寬度則由 `width` ÷ 8 得出。 | INT | 是 | 16 to MAX_RESOLUTION （步進值：8） |
| `height` | 目標高度，單位為像素（預設：384）。在產生雜訊之前，會先將輸入影片縮放到此高度，而 latent 高度則由 `height` ÷ 8 得出。 | INT | 是 | 16 to MAX_RESOLUTION （步進值：8） |
| `length` | 像素影格數量。會向下取整以使 `latent_t` 為偶數（`patch_size_t=2` 的要求），例如 49 變成 45（預設：45）。 | INT | 是 | 1 to MAX_RESOLUTION （步進值：1） |
| `batch_size` | 要產生的相同扭曲雜訊序列數量（預設：1）。產生的雜訊會沿批次維度重複 `batch_size` 次。 | INT | 是 | 1 至 64 |

**關於 `length` 參數的注意事項：** `length` 值會自動向下取整至最接近且能產生偶數 `latent_t` 維度的值，這是 CogVideoX-Fun-V1.5 模型的 `patch_size_t=2` 限制所要求的（例如 49 會變成 45）。當發生此取整時，節點會記錄一則警告。超出調整後 `length` 的影格會被忽略，且雜訊會重新取樣為產生的 latent 影格數量。

**關於 `width` 與 `height` 的注意事項：** 這些值同時用於調整輸入影片影格的大小（雙線性插值、中心裁切），以及決定最終 latent 解析度（除以 8）。如果產生的雜訊與要求的 latent 大小不符，則會調整大小以配合。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `warped_noise` | 一個 5D 張量 (B, C, T, H, W)，包含經光流扭曲的高斯雜訊，可作為 VOID Pass 2 的初始 latent 使用。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDWarpedNoise/zh-TW.md)

---
**Source fingerprint (SHA-256):** `f46b0a73b09a5d2d0bc25676f9571563c6bb8bad8d835e7564ac092c72136107`
