# Wan攝影機圖像轉影片

WanCameraImageToVideo 為從圖像生成影片準備條件化與潛在資料。它接收正向與負向條件化提示詞，以及可選的起始圖像與攝影機控制，並輸出修改後的條件化資料，以及一個可供影片模型填入的空潛在張量。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `positive` | 正向條件化提示詞，用於影片生成 | CONDITIONING | 是 | - |
| `negative` | 負向條件化提示詞，用於避免在影片生成中出現的內容 | CONDITIONING | 是 | - |
| `vae` | VAE 模型，用於將圖像編碼至潛在空間 | VAE | 是 | - |
| `width` | 輸出影片寬度（像素），預設值：832，步長：16 | INT | 是 | 16 to MAX_RESOLUTION |
| `height` | 輸出影片高度（像素），預設值：480，步長：16 | INT | 是 | 16 to MAX_RESOLUTION |
| `length` | 影片序列中的幀數，預設值：81，步長：4 | INT | 是 | 1 to MAX_RESOLUTION |
| `batch_size` | 同時生成的影片數量，預設值：1 | INT | 是 | 1 to 4096 |
| `clip_vision_output` | 可選的 CLIP 視覺輸出，用於額外的條件化 | CLIP_VISION_OUTPUT | 否 | - |
| `start_image` | 可選的起始圖像，用於初始化影片序列。提供時，影片的前幾幀將基於此圖像，並套用遮罩以將起始幀與生成的內容混合。圖像會調整大小以符合指定的寬度和高度。 | IMAGE | 否 | - |
| `camera_conditions` | 可選的攝影機嵌入條件，用於影片生成。提供時，這些條件會同時套用於正向與負向條件化。 | WAN_CAMERA_EMBEDDING | 否 | - |

**注意：** 當提供 `start_image` 時，節點會使用它來初始化影片序列，並套用遮罩以將起始幀與生成的內容混合。`camera_conditions` 與 `clip_vision_output` 參數為選用，但提供時會修改正向與負向提示詞的條件化。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `positive` | 修改後的正向條件化，已套用攝影機條件、CLIP 視覺輸出及/或起始圖像資料 | CONDITIONING |
| `negative` | 修改後的負向條件化，已套用攝影機條件、CLIP 視覺輸出及/或起始圖像資料 | CONDITIONING |
| `latent` | 生成的空影片潛在表示，供影片模型使用。潛在張量的維度為 `[batch_size, 16, frames, height/8, width/8]`，其中 `frames` 的計算方式為 `((length - 1) // 4) + 1`。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanCameraImageToVideo/zh-TW.md)

---
**Source fingerprint (SHA-256):** `467a82be0dfd6ac1c3b2dd2a6cb02e0d0749de4536a7fbdb000456b817b20ebb`
