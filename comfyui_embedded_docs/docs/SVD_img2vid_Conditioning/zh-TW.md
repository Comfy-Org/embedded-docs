> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SVD_img2vid_Conditioning/zh-TW.md)

# SVD_img2vid_Conditioning 節點

SVD_img2vid_Conditioning 節點使用 Stable Video Diffusion 為影片生成準備條件化資料。它接收初始影像，透過 CLIP 視覺編碼器和 VAE 編碼器進行處理，建立正向和負向條件化配對，以及用於影片生成的空白潛在空間。此節點設定必要的參數，用於控制生成影片中的動態、幀率和增強程度。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `clip_vision` | CLIP_VISION | 是 | - | 用於編碼輸入影像的 CLIP 視覺模型 |
| `初始影像` | IMAGE | 是 | - | 作為影片生成起始點的初始影像 |
| `vae` | VAE | 是 | - | 用於將影像編碼到潛在空間的 VAE 模型 |
| `寬度` | INT | 是 | 16 至 MAX_RESOLUTION | 輸出影片寬度（預設值：1024，步長：8） |
| `高度` | INT | 是 | 16 至 MAX_RESOLUTION | 輸出影片高度（預設值：576，步長：8） |
| `影片幀數` | INT | 是 | 1 至 4096 | 影片中要生成的幀數（預設值：14） |
| `動作分組 ID` | INT | 是 | 1 至 1023 | 控制生成影片中的動態程度（預設值：127） |
| `每秒幀數 (FPS)` | INT | 是 | 1 至 1024 | 生成影片的每秒幀數（預設值：6） |
| `增強等級` | FLOAT | 是 | 0.0 至 10.0 | 應用於輸入影像的噪聲增強程度（預設值：0.0，步長：0.01） |

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `負向` | CONDITIONING | 包含影像嵌入和影片參數的正向條件化資料 |
| `潛在空間` | CONDITIONING | 嵌入和影片參數歸零的負向條件化資料 |
| `latent` | LATENT | 準備用於影片生成的空白潛在空間張量 |

---
**Source fingerprint (SHA-256):** `33b295b6f2e459852aaa95d9dca26c724aa2e9ad0f884a1c7760766530a00a09`
