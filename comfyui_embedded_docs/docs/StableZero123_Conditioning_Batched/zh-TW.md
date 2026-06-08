# StableZero123_Conditioning_Batched 節點

StableZero123_Conditioning_Batched 節點處理輸入影像，並為 3D 模型生成生成條件數據。它使用 CLIP vision 和 VAE 模型對影像進行編碼，然後根據仰角和方位角創建相機嵌入，以生成正向和負向條件，以及用於批次處理的潛在表示。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `clip_vision` | 用於編碼輸入影像的 CLIP vision 模型 | CLIP_VISION | 是 | - |
| `初始影像` | 要處理和編碼的初始輸入影像 | IMAGE | 是 | - |
| `vae` | 用於將影像像素編碼為潛在空間的 VAE 模型 | VAE | 是 | - |
| `寬度` | 處理後影像的輸出寬度（預設：256，必須能被 8 整除） | INT | 否 | 16 至 MAX_RESOLUTION |
| `高度` | 處理後影像的輸出高度（預設：256，必須能被 8 整除） | INT | 否 | 16 至 MAX_RESOLUTION |
| `批次大小` | 批次中生成的條件樣本數量（預設：1） | INT | 否 | 1 至 4096 |
| `仰角` | 初始相機仰角，單位為度（預設：0.0） | FLOAT | 否 | -180.0 至 180.0 |
| `方位角` | 初始相機方位角，單位為度（預設：0.0） | FLOAT | 否 | -180.0 至 180.0 |
| `仰角批次遞增` | 每個批次項目的仰角增量（預設：0.0） | FLOAT | 否 | -180.0 至 180.0 |
| `方位角批次遞增` | 每個批次項目的方位角增量（預設：0.0） | FLOAT | 否 | -180.0 至 180.0 |

**注意：** `width` 和 `height` 參數必須能被 8 整除，因為節點內部會將這些維度除以 8 以生成潛在空間。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `負向` | 包含影像嵌入和相機參數的正向條件數據 | CONDITIONING |
| `潛在空間` | 嵌入初始化為零的負向條件數據 | CONDITIONING |
| `latent` | 包含批次索引資訊的處理後影像潛在表示 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableZero123_Conditioning_Batched/zh-TW.md)

---
**Source fingerprint (SHA-256):** `2b770f7a168a0d3e33da8bfa63383080709fa5d53846dbf6a4374bd1ef1746aa`
