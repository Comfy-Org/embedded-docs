# Wan 追蹤轉影片

WanTrackToVideo 節點使用運動追蹤資料（點軌跡）來引導影片生成。它處理軌跡資料，可選擇與起始影像結合，並為 Wan 影片模型產生有條件的正向與負向輸出，以及一個潛在張量。當未提供有效的軌跡資料時，它會回退到標準的影像轉影片轉換。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `positive` | 用於影片生成的正向條件 | CONDITIONING | 是 | - |
| `negative` | 用於影片生成的負向條件 | CONDITIONING | 是 | - |
| `vae` | 用於編碼影片幀的 VAE 模型 | VAE | 是 | - |
| `tracks` | 以多行字串表示的 JSON 格式追蹤資料（預設值："[]"） | STRING | 是 | - |
| `width` | 輸出影片的寬度（像素）（預設值：832，間距：16） | INT | 是 | 16 至 MAX_RESOLUTION |
| `height` | 輸出影片的高度（像素）（預設值：480，間距：16） | INT | 是 | 16 至 MAX_RESOLUTION |
| `length` | 輸出影片的幀數（預設值：81，間距：4） | INT | 是 | 1 至 MAX_RESOLUTION |
| `batch_size` | 同時生成的影片數量（預設值：1） | INT | 是 | 1 至 4096 |
| `temperature` | 用於運動修補的進階溫度參數（預設值：220.0，間距：0.1） | FLOAT | 是 | 1.0 至 1000.0 |
| `topk` | 用於運動修補的進階 top-k 值（預設值：2） | INT | 是 | 1 至 10 |
| `start_image` | 用於影片生成第一幀的起始影像 | IMAGE | 是 | - |
| `clip_vision_output` | 用於額外條件化的 CLIP 視覺輸出 | CLIP_VISION_OUTPUT | 否 | - |

**注意事項：**
- `tracks` 輸入預期接收包含點追蹤資料的 JSON 字串或 JSON 字串清單。若 `tracks` 為空或無法解析，節點將回退至 WanImageToVideo 行為。
- 當提供 `start_image` 時，它會被調整大小以符合 `width` 和 `height`，並用作影片序列的第一幀。
- 當提供 `clip_vision_output` 時，它會被添加到正向與負向條件化中。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `positive` | 已套用運動軌跡與可選影像資訊的正向條件化 | CONDITIONING |
| `negative` | 已套用運動軌跡與可選影像資訊的負向條件化 | CONDITIONING |
| `latent` | 零填充的潛在張量，尺寸符合請求的影片尺寸、長度與批次大小 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanTrackToVideo/zh-TW.md)

---
**Source fingerprint (SHA-256):** `e67fe326dd7e5ae63ddc35946d8144138d04d9523ec1ad2e08ea6bc1dc9325da`
