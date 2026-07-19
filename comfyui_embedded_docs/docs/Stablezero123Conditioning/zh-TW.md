# Stablezero123Conditioning

此節點專為處理和準備用於 StableZero123 模型的條件資料而設計，重點在於將輸入轉換為與這些模型相容且經過最佳化的特定格式。

## 輸入

| 參數 | 說明 | Comfy 資料類型 |
| --- | --- | --- |
| `clip_vision` | 處理視覺資料以符合模型需求，增強模型對視覺上下文的理解。 | `CLIP_VISION` |
| `init_image` | 作為模型的初始影像輸入，為後續基於影像的操作設定基準。 | `IMAGE` |
| `vae` | 整合變分自編碼器的輸出，協助模型生成或修改影像的能力。 | `VAE` |
| `width` | 指定輸出影像的寬度，允許根據模型需求動態調整尺寸。 | `INT` |
| `height` | 決定輸出影像的高度，可自訂輸出尺寸。 | `INT` |
| `batch_size` | 控制單一批次中處理的影像數量，以最佳化計算效率。 | `INT` |
| `elevation` | 調整 3D 模型渲染的仰角，增強模型的空間理解能力。 | `FLOAT` |
| `azimuth` | 修改 3D 模型視覺化的方位角，改善模型對方向感的感知。 | `FLOAT` |

## 輸出

| 參數 | 說明 | 資料類型 |
| --- | --- | --- |
| `positive` | 生成正向條件向量，協助模型強化正向特徵。 | `CONDITIONING` |
| `negative` | 產生負向條件向量，協助模型避免特定特徵。 | `CONDITIONING` |
| `latent` | 建立潛在表示，促進模型對資料的更深層理解。 | `LATENT` |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Stablezero123Conditioning/zh-TW.md)
