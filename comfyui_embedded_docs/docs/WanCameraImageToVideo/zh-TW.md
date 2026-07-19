# Wan攝影機圖像轉影片

WanCameraImageToVideo 節點透過生成用於影片生成的潛在表示，將影像轉換為影片序列。它處理條件化輸入和可選的起始影像，以建立可與影片模型搭配使用的影片潛在變數。該節點支援攝影機條件和 CLIP 視覺輸出，以增強對影片生成的控制。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `正面提示詞` | 用於影片生成的正向條件化提示 | CONDITIONING | 是 | - |
| `負面提示詞` | 用於影片生成中要避免的負向條件化提示 | CONDITIONING | 是 | - |
| `VAE` | 用於將影像編碼到潛在空間的 VAE 模型 | VAE | 是 | - |
| `寬度` | 輸出影片寬度（像素）（預設值：832，步進值：16） | INT | 是 | 16 至 MAX_RESOLUTION |
| `高度` | 輸出影片高度（像素）（預設值：480，步進值：16） | INT | 是 | 16 至 MAX_RESOLUTION |
| `長度` | 影片序列中的影格數（預設值：81，步進值：4） | INT | 是 | 1 至 MAX_RESOLUTION |
| `批次大小` | 同時生成的影片數量（預設值：1） | INT | 是 | 1 至 4096 |
| `CLIP視覺輸出` | 可選的 CLIP 視覺輸出，用於額外的條件化處理 | CLIP_VISION_OUTPUT | 否 | - |
| `起始圖像` | 可選的起始影像，用於初始化影片序列。當提供此參數時，影片的前幾個影格將基於此影像，並套用遮罩來混合起始影格與生成的內容。該影像會調整大小以符合指定的寬度和高度。 | IMAGE | 否 | - |
| `攝影機條件` | 可選的攝影機嵌入條件，用於影片生成。當提供此參數時，這些條件會同時應用於正向和負向條件化處理。 | WAN_CAMERA_EMBEDDING | 否 | - |

**注意：** 當提供 `start_image` 時，節點會使用它來初始化影片序列，並套用遮罩來混合起始影格與生成的內容。`camera_conditions` 和 `clip_vision_output` 參數為可選項，但當提供時，它們會修改正向和負向提示的條件化處理。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `正面提示詞` | 已套用攝影機條件和 CLIP 視覺輸出的修改後正向條件化處理 | CONDITIONING |
| `負面提示詞` | 已套用攝影機條件和 CLIP 視覺輸出的修改後負向條件化處理 | CONDITIONING |
| `潛在空間` | 生成的影片潛在表示，用於與影片模型搭配使用。潛在張量的維度為 [batch_size, 16, frames, height/8, width/8]，其中 frames 的計算方式為 ((length - 1) // 4) + 1。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanCameraImageToVideo/zh-TW.md)

---
**Source fingerprint (SHA-256):** `19d76097d580b14663afd0aab58810f9dc1685cd32e8f67aa43c820be65239e7`
