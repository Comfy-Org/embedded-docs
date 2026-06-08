## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `clip_vision` | 用於編碼輸入圖像的 CLIP 視覺模型 | CLIP_VISION | 是 | - |
| `初始影像` | 作為 3D 影片生成起點的初始圖像 | IMAGE | 是 | - |
| `vae` | 用於將圖像編碼到潛在空間的 VAE 模型 | VAE | 是 | - |
| `寬度` | 生成影片畫面的輸出寬度（預設值：576，必須為 8 的倍數） | INT | 否 | 16 至 MAX_RESOLUTION |
| `高度` | 生成影片畫面的輸出高度（預設值：576，必須為 8 的倍數） | INT | 否 | 16 至 MAX_RESOLUTION |
| `影片幀數` | 影片序列要生成的影格數（預設值：21） | INT | 否 | 1 至 4096 |
| `仰角` | 3D 視角的相機俯仰角度（預設值：0.0） | FLOAT | 否 | -90.0 至 90.0 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `負向` | 正向條件化資料，包含用於生成的圖像嵌入和相機參數 | CONDITIONING |
| `潛在空間` | 負向條件化資料，嵌入值歸零，用於對比生成 | CONDITIONING |
| `latent` | 空白的潛在張量，其維度與指定的影片影格數和解析度相符 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SV3D_Conditioning/zh-TW.md)

---
**Source fingerprint (SHA-256):** `be02939aa4cdd1785eb445034a27d08a90e390a497fa9697fb769f0ce26e6d2f`
