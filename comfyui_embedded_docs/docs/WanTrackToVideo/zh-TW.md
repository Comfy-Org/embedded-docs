> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanTrackToVideo/zh-TW.md)

# WanTrackToVideo 節點

WanTrackToVideo 節點透過處理軌跡點並生成對應的視訊幀，將運動追蹤資料轉換為視訊序列。它接收追蹤座標作為輸入，並產生可用於視訊生成的視訊條件化與潛在表示。當未提供任何軌跡時，它會回退為標準的影像轉視訊轉換。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | 是 | - | 用於視訊生成的正向條件化 |
| `negative` | CONDITIONING | 是 | - | 用於視訊生成的負向條件化 |
| `vae` | VAE | 是 | - | 用於編碼與解碼的 VAE 模型 |
| `tracks` | STRING | 是 | - | JSON 格式的追蹤資料，以多行字串表示（預設值："[]"） |
| `width` | INT | 是 | 16 至 MAX_RESOLUTION | 輸出視訊的寬度（像素）（預設值：832，步進值：16） |
| `height` | INT | 是 | 16 至 MAX_RESOLUTION | 輸出視訊的高度（像素）（預設值：480，步進值：16） |
| `length` | INT | 是 | 1 至 MAX_RESOLUTION | 輸出視訊的幀數（預設值：81，步進值：4） |
| `batch_size` | INT | 是 | 1 至 4096 | 同時生成的視訊數量（預設值：1） |
| `temperature` | FLOAT | 是 | 1.0 至 1000.0 | 運動修補的溫度參數（預設值：220.0，步進值：0.1） |
| `topk` | INT | 是 | 1 至 10 | 運動修補的 top-k 值（預設值：2） |
| `start_image` | IMAGE | 否 | - | 用於視訊生成的起始影像 |
| `clip_vision_output` | CLIPVISIONOUTPUT | 否 | - | 用於額外條件化的 CLIP 視覺輸出 |

**注意：** 當 `tracks` 包含有效的追蹤資料時，節點會處理運動軌跡以生成視訊。當 `tracks` 為空時，則切換為標準的影像轉視訊模式。如果提供了 `start_image`，它會初始化視訊序列的第一幀。

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | 已套用運動軌跡資訊的正向條件化 |
| `negative` | CONDITIONING | 已套用運動軌跡資訊的負向條件化 |
| `latent` | LATENT | 生成的視訊潛在表示 |

---
**Source fingerprint (SHA-256):** `b3e12492d3dafa100266f6be8fe05e4d62b827f1a2bdb4029f804b107dc691ed`
