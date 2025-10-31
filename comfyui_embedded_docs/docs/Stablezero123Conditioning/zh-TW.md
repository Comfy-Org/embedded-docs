> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Stablezero123Conditioning/zh-TW.md)

此節點專為處理和調節 StableZero123 模型所需的資料而設計，重點在於以特定格式準備輸入內容，確保與這些模型相容並進行最佳化。

## 輸入參數

| 參數名稱             | Comfy 資料類型     | 描述 |
|-----------------------|--------------------|-------------|
| `clip_vision`         | `CLIP_VISION`      | 處理視覺資料以符合模型要求，增強模型對視覺上下文的理解。 |
| `init_image`          | `IMAGE`            | 作為模型的初始影像輸入，為後續影像操作設定基準。 |
| `vae`                 | `VAE`              | 整合變分自編碼器輸出，促進模型生成或修改影像的能力。 |
| `width`               | `INT`              | 指定輸出影像的寬度，允許根據模型需求進行動態調整。 |
| `height`              | `INT`              | 決定輸出影像的高度，實現輸出尺寸的客製化。 |
| `batch_size`          | `INT`              | 控制單一批次處理的影像數量，優化計算效率。 |
| `elevation`           | `FLOAT`            | 調整 3D 模型渲染的仰角，增強模型的空間理解能力。 |
| `azimuth`             | `FLOAT`            | 修改 3D 模型可視化的方位角，提升模型對方向感知的準確性。 |

## 輸出參數

| 參數名稱     | 資料類型          | 描述 |
|---------------|--------------|-------------|
| `positive`    | `CONDITIONING` | 生成正向調節向量，協助模型強化正面特徵。 |
| `negative`    | `CONDITIONING` | 產生負向調節向量，幫助模型避免特定不良特徵。 |
| `latent`      | `LATENT`     | 建立潛在表示，促進模型對資料的深層理解。 |