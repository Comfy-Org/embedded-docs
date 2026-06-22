# SVD_img2vid_Conditioning

SVD_img2vid_Conditioning 節點使用 Stable Video Diffusion 為影片生成準備條件化資料。它接收初始影像，透過 CLIP 視覺編碼器和 VAE 編碼器進行處理，建立正向和負向條件化配對，以及用於影片生成的空白潛在空間。此節點設定必要的參數，用於控制生成影片中的動態、幀率和增強程度。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `clip_vision` | 用於編碼輸入影像的 CLIP 視覺模型 | CLIP_VISION | 是 | - |
| `初始影像` | 作為影片生成起始點的初始影像 | IMAGE | 是 | - |
| `vae` | 用於將影像編碼到潛在空間的 VAE 模型 | VAE | 是 | - |
| `寬度` | 輸出影片寬度（預設值：1024，步長：8） | INT | 是 | 16 至 MAX_RESOLUTION |
| `高度` | 輸出影片高度（預設值：576，步長：8） | INT | 是 | 16 至 MAX_RESOLUTION |
| `影片幀數` | 影片中要生成的幀數（預設值：14） | INT | 是 | 1 至 4096 |
| `動作分組 ID` | 控制生成影片中的動態程度（預設值：127） | INT | 是 | 1 至 1023 |
| `每秒幀數 (FPS)` | 生成影片的每秒幀數（預設值：6） | INT | 是 | 1 至 1024 |
| `增強等級` | 應用於輸入影像的噪聲增強程度（預設值：0.0，步長：0.01） | FLOAT | 是 | 0.0 至 10.0 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `負向` | 包含影像嵌入和影片參數的正向條件化資料 | CONDITIONING |
| `潛在空間` | 嵌入和影片參數歸零的負向條件化資料 | CONDITIONING |
| `latent` | 準備用於影片生成的空白潛在空間張量 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SVD_img2vid_Conditioning/zh-TW.md)

---
**Source fingerprint (SHA-256):** `33b295b6f2e459852aaa95d9dca26c724aa2e9ad0f884a1c7760766530a00a09`
