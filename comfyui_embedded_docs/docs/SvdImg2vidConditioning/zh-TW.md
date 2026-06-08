此節點專為生成影片生成任務的條件資料而設計，特別針對 SVD_img2vid 模型進行了最佳化。它接收多種輸入，包括初始影像、影片參數和 VAE 模型，以產生可用於引導影片幀生成的條件資料。

## 輸入

| 參數 | 說明 | Comfy dtype |
| --- | --- | --- |
| `clip_vision` | 代表用於從初始影像編碼視覺特徵的 CLIP 視覺模型，在理解影像內容與背景以進行影片生成方面扮演關鍵角色。 | `CLIP_VISION` |
| `init_image` | 將從此初始影像生成影片，作為影片生成過程的起點。 | `IMAGE` |
| `vae` | 一個變分自編碼器（VAE）模型，用於將初始影像編碼到潛在空間，有助於生成連貫且連續的影片幀。 | `VAE` |
| `width` | 欲生成影片幀的寬度，允許自訂影片的解析度。 | `INT` |
| `height` | 欲生成影片幀的高度，可控制影片的長寬比與解析度。 | `INT` |
| `video_frames` | 指定要為影片生成的幀數，決定影片的長度。 | `INT` |
| `motion_bucket_id` | 用於分類影片生成中要應用的動作類型的識別碼，有助於創建動態且引人入勝的影片。 | `INT` |
| `fps` | 影片的每秒幀數（fps）速率，影響生成影片的流暢度與真實感。 | `INT` |
| `augmentation_level` | 控制應用於初始影像的增強程度的參數，影響生成影片幀的多樣性與變異性。 | `FLOAT` |

## 輸出

| 參數 | 說明 | Comfy dtype |
| --- | --- | --- |
| `positive` | 正向條件資料，包含編碼後的特徵與參數，用於引導影片生成過程朝向期望方向。 | `CONDITIONING` |
| `negative` | 負向條件資料，提供與正向條件相對比的內容，可用於避免生成影片中出現特定模式或特徵。 | `CONDITIONING` |
| `latent` | 為影片的每一幀生成的潛在表示，作為影片生成過程的基礎組成部分。 | `LATENT` |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SvdImg2vidConditioning/zh-TW.md)
