> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Stablezero123ConditioningBatched/zh-TW.md)

此節點專為 StableZero123 模型設計，以批次方式處理條件資訊。它專注於同時高效處理多組條件數據，針對需要批次處理的場景優化工作流程。

## 輸入參數

| 參數名稱                   | 資料類型      | 描述 |
|--------------------------|---------------|------|
| `clip_vision`            | `CLIP_VISION` | 為條件化過程提供視覺上下文的 CLIP 視覺嵌入 |
| `init_image`             | `IMAGE`       | 作為生成過程起點的初始圖像，將以此為基礎進行條件化處理 |
| `vae`                    | `VAE`         | 在條件化過程中用於圖像編碼和解碼的變分自編碼器 |
| `width`                  | `INT`         | 輸出圖像的寬度 |
| `height`                 | `INT`         | 輸出圖像的高度 |
| `batch_size`             | `INT`         | 單一批次中要處理的條件化集合數量 |
| `elevation`              | `FLOAT`       | 用於 3D 模型條件化的仰角，影響生成圖像的視角 |
| `azimuth`                | `FLOAT`       | 用於 3D 模型條件化的方位角，影響生成圖像的方向 |
| `elevation_batch_increment` | `FLOAT`    | 在批次中各項目間仰角的增量變化，允許不同的視角 |
| `azimuth_batch_increment` | `FLOAT`     | 在批次中各項目間方位角的增量變化，允許不同的方向 |

## 輸出參數

| 參數名稱     | 資料類型        | 描述 |
|-------------|-----------------|------|
| `positive`  | `CONDITIONING`  | 正向條件化輸出，專門用於在生成內容中增強特定特徵或方面 |
| `negative`  | `CONDITIONING`  | 負向條件化輸出，專門用於在生成內容中抑制特定特徵或方面 |
| `latent`    | `LATENT`        | 從條件化過程推導出的潛在表示，準備用於進一步處理或生成步驟 |