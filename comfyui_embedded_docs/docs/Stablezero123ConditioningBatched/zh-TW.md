> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Stablezero123ConditioningBatched/zh-TW.md)

此節點專為處理 StableZero123 模型的批次條件化資訊而設計。其重點在於同時高效處理多組條件化資料，針對批次處理至關重要的場景最佳化工作流程。

## 輸入

| 參數 | 資料類型 | 描述 |
|----------------------|--------------|-------------|
| `clip_vision` | `CLIP_VISION` | 提供視覺背景的 CLIP 視覺嵌入，用於條件化過程。 |
| `init_image` | `IMAGE` | 作為條件化基礎的初始影像，為生成過程提供起點。 |
| `vae` | `VAE` | 用於在條件化過程中編碼和解碼影像的變分自編碼器。 |
| `width` | `INT` | 輸出影像的寬度。 |
| `height` | `INT` | 輸出影像的高度。 |
| `batch_size` | `INT` | 單一批次中要處理的條件化集合數量。 |
| `elevation` | `FLOAT` | 3D 模型條件化的俯仰角，影響生成影像的視角。 |
| `azimuth` | `FLOAT` | 3D 模型條件化的方位角，影響生成影像的方向。 |
| `elevation_batch_increment` | `FLOAT` | 批次中俯仰角的增量變化，允許產生多樣化的視角。 |
| `azimuth_batch_increment` | `FLOAT` | 批次中方位角的增量變化，允許產生多樣化的方向。 |

## 輸出

| 參數 | 資料類型 | 描述 |
|---------------|--------------|-------------|
| `positive` | `CONDITIONING` | 正向條件化輸出，專為促進生成內容中的特定特徵或面向而設計。 |
| `negative` | `CONDITIONING` | 負向條件化輸出，專為抑制生成內容中的特定特徵或面向而設計。 |
| `latent` | `LATENT` | 從條件化過程推導出的潛在表示，可供進一步處理或生成步驟使用。 |