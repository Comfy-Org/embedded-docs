# SV3D_Conditioning

SV3D_Conditioning 會使用 SV3D 模型為 3D 影片生成準備條件資料。它接收初始影像，並透過 CLIP 視覺與 VAE 編碼器進行處理，以建立正向與負向條件，以及潛在表示。此節點會根據指定的影片幀數，為多幀影片生成產生相機仰角與方位角序列。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `clip_vision` | 用於編碼輸入影像的 CLIP 視覺模型 | CLIP_VISION | 是 | - |
| `初始影像` | 作為 3D 影片生成起始點的初始影像 | IMAGE | 是 | - |
| `vae` | 用於將影像編碼至潛在空間的 VAE 模型 | VAE | 是 | - |
| `寬度` | 生成影片幀的輸出寬度（預設：576，步長為 8） | INT | 是 | 16 to MAX_RESOLUTION |
| `高度` | 生成影片幀的輸出高度（預設：576，步長為 8） | INT | 是 | 16 to MAX_RESOLUTION |
| `影片幀數` | 要為影片序列生成的幀數（預設：21） | INT | 是 | 1 至 4096 |
| `仰角` | 3D 視圖的相機仰角，以度為單位（預設：0.0，步長為 0.1） | FLOAT | 是 | -90.0 至 90.0 |

注意：相機方位角從 0 度開始，並在每一幀增加固定量，使相機在生成的各幀中完整環繞物件 360 度一圈。每幀增量計算方式為 360 除以（`video_frames` - 1），當僅請求一幀時，使用最小除數 2。`elevation` 值在每一幀保持不變。

在 VAE 編碼之前，`init_image` 會縮放至指定的 `width` 和 `height`，而傳回的潛在表示使用維度 `video_frames` x 4 x (`height` // 8) x (`width` // 8)。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `positive` | 包含影像嵌入與相機參數的正向條件資料，用於生成 | CONDITIONING |
| `negative` | 具有歸零嵌入與潛在表示的負向條件資料，用於對比式生成 | CONDITIONING |
| `latent` | 空的潛在張量，其維度符合指定的影片幀數與解析度 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SV3D_Conditioning/zh-TW.md)

---
**Source fingerprint (SHA-256):** `e28173cfa560290e66b032687088cf0b981256ca5c21f6aa608e0fdaec886665`
