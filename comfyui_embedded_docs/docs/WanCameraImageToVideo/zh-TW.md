# Wan攝影機圖像轉影片

WanCameraImageToVideo 節點會為基於影像的相機控制影片生成準備條件與潛在資料。它接收正向與負向條件提示詞，以及可選輸入，例如起始影像、CLIP vision 輸出與相機條件，並輸出更新後的條件，以及可供影片模型填入的空潛在張量。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `正面提示詞` | 用於影片生成的正向條件提示詞 | CONDITIONING | 是 | - |
| `負面提示詞` | 影片生成中要避免的負向條件提示詞 | CONDITIONING | 是 | - |
| `VAE` | 用於將影像編碼至潛在空間的 VAE 模型 | VAE | 是 | - |
| `寬度` | 輸出影片寬度，單位為像素（預設：832，步長：16） | INT | 是 | 16 to MAX_RESOLUTION |
| `高度` | 輸出影片高度，單位為像素（預設：480，步長：16） | INT | 是 | 16 to MAX_RESOLUTION |
| `長度` | 影片序列中的影格數（預設：81，步長：4） | INT | 是 | 1 to MAX_RESOLUTION |
| `批次大小` | 同時生成的影片數量（預設：1） | INT | 是 | 1 至 4096 |
| `CLIP視覺輸出` | 可選的 CLIP vision 輸出，用於額外條件 | CLIP_VISION_OUTPUT | 否 | - |
| `起始圖像` | 可選的起始影像，用於初始化影片序列。提供時，只會使用前 `length` 個影格，並將影像調整大小以符合指定的 `width` 與 `height`。序列的前幾個影格會被編碼至潛在空間，並套用遮罩，將起始影格與生成內容混合。 | IMAGE | 否 | - |
| `攝影機條件` | 可選的相機嵌入條件，用於影片生成。提供時，這些條件會套用至正向與負向條件。 | WAN_CAMERA_EMBEDDING | 否 | - |

**注意：** 提供 `start_image` 時，節點會在 `positive` 與 `negative` 條件上設定 `concat_latent_image` 與 `concat_mask` 值。`camera_conditions` 與 `clip_vision_output` 參數為可選，但提供時，它們會修改正向與負向提示詞的條件。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `positive` | 套用了相機條件、CLIP vision 輸出及/或起始影像資料後，修改過的正向條件 | CONDITIONING |
| `negative` | 套用了相機條件、CLIP vision 輸出及/或起始影像資料後，修改過的負向條件 | CONDITIONING |
| `latent` | 供影片模型使用的空影片潛在表示。潛在張量維度為 `[batch_size, 16, frames, height/8, width/8]`，其中 frames 的計算方式為 `((length - 1) // 4) + 1`。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanCameraImageToVideo/zh-TW.md)

---
**Source fingerprint (SHA-256):** `467a82be0dfd6ac1c3b2dd2a6cb02e0d0749de4536a7fbdb000456b817b20ebb`
