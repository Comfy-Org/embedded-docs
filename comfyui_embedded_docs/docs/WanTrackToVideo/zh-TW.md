> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanTrackToVideo/zh-TW.md)

WanTrackToVideo 節點透過處理追蹤點並生成相應的影片幀，將運動追蹤資料轉換為影片序列。它接收追蹤座標作為輸入，並產生可用於影片生成的影片條件設定和潛在表示。當未提供追蹤資料時，它會回退到標準的圖像轉影片轉換。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | 是 | - | 用於影片生成的正向條件設定 |
| `negative` | CONDITIONING | 是 | - | 用於影片生成的負向條件設定 |
| `vae` | VAE | 是 | - | 用於編碼和解碼的 VAE 模型 |
| `tracks` | STRING | 是 | - | JSON 格式的追蹤資料，作為多行字串（預設值："[]"） |
| `width` | INT | 是 | 16 至 MAX_RESOLUTION | 輸出影片的寬度（像素）（預設值：832，步長：16） |
| `height` | INT | 是 | 16 至 MAX_RESOLUTION | 輸出影片的高度（像素）（預設值：480，步長：16） |
| `length` | INT | 是 | 1 至 MAX_RESOLUTION | 輸出影片的幀數（預設值：81，步長：4） |
| `batch_size` | INT | 是 | 1 至 4096 | 同時生成的影片數量（預設值：1） |
| `temperature` | FLOAT | 是 | 1.0 至 1000.0 | 用於運動修補的溫度參數（預設值：220.0，步長：0.1） |
| `topk` | INT | 是 | 1 至 10 | 用於運動修補的 top-k 值（預設值：2） |
| `start_image` | IMAGE | 否 | - | 用於影片生成的起始圖像 |
| `clip_vision_output` | CLIPVISIONOUTPUT | 否 | - | 用於額外條件設定的 CLIP 視覺輸出 |

**注意：** 當 `tracks` 包含有效的追蹤資料時，節點會處理運動軌跡以生成影片。當 `tracks` 為空時，它會切換到標準的圖像轉影片模式。如果提供了 `start_image`，它將初始化影片序列的第一幀。

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | 已應用運動追蹤資訊的正向條件設定 |
| `negative` | CONDITIONING | 已應用運動追蹤資訊的負向條件設定 |
| `latent` | LATENT | 生成的影片潛在表示 |