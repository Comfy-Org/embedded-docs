# SV3D_Conditioning

SV3D_Conditioning 節點使用 SV3D 模型為 3D 視訊生成準備條件化資料。它接收一張初始影像，並透過 CLIP vision 與 VAE 編碼器進行處理，以建立正向與負向條件化資料，以及一個潛在表示。該節點會根據指定的視訊幀數，產生攝影機俯仰角與方位角序列，用於多幀視訊生成。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `clip_vision` | 用於對輸入影像進行編碼的 CLIP vision 模型 | CLIP_VISION | 是 | - |
| `初始影像` | 作為 3D 視訊生成起始點的初始影像 | IMAGE | 是 | - |
| `vae` | 用於將影像編碼至潛在空間的 VAE 模型 | VAE | 是 | - |
| `寬度` | 生成視訊幀的輸出寬度（預設值：576，必須可被 8 整除） | INT | 是 | 16 to MAX_RESOLUTION |
| `高度` | 生成視訊幀的輸出高度（預設值：576，必須可被 8 整除） | INT | 是 | 16 to MAX_RESOLUTION |
| `影片幀數` | 要生成的視訊序列幀數（預設值：21） | INT | 是 | 1 至 4096 |
| `仰角` | 3D 視圖的攝影機俯仰角（以度為單位）（預設值：0.0） | FLOAT | 是 | -90.0 至 90.0 |

注意：攝影機方位角從 0 度開始，並在每一幀增加一個固定量，使攝影機在生成的幀中圍繞物體完成完整的 360 度軌道運動。`elevation` 值在每一幀中保持不變。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `正向` | 包含影像嵌入與攝影機參數的生成用正向條件化資料 | CONDITIONING |
| `負向` | 具有歸零嵌入與潛在變數的負向條件化資料，用於對比生成 | CONDITIONING |
| `潛在空間` | 一個空的潛在張量，其維度與指定的視訊幀數和解析度相符 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SV3D_Conditioning/zh-TW.md)

---
**Source fingerprint (SHA-256):** `e28173cfa560290e66b032687088cf0b981256ca5c21f6aa608e0fdaec886665`
