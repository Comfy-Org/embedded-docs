# Wan攝影機圖像轉影片

以下為翻譯結果：

WanCameraImageToVideo 節點準備用於從圖像生成視頻的 conditioning 和 latent 數據。它接收正向和負向的 conditioning 提示，以及可選的起始圖像和可選的相機控制項，並輸出修改後的 conditioning 以及一個空的潛在張量，供視頻模型填充。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `正面提示詞` | 用於視頻生成的正向 conditioning 提示 | CONDITIONING | 是 | - |
| `負面提示詞` | 用於避免在視頻生成中出現的負向 conditioning 提示 | CONDITIONING | 是 | - |
| `VAE` | 用於將圖像編碼到潛在空間的 VAE 模型 | VAE | 是 | - |
| `寬度` | 輸出視頻的寬度（像素）（預設值：832，步長：16） | INT | 是 | 16 至 MAX_RESOLUTION |
| `高度` | 輸出視頻的高度（像素）（預設值：480，步長：16） | INT | 是 | 16 至 MAX_RESOLUTION |
| `長度` | 視頻序列中的幀數（預設值：81，步長：4） | INT | 是 | 1 至 MAX_RESOLUTION |
| `批次大小` | 同時生成的視頻數量（預設值：1） | INT | 是 | 1 至 4096 |
| `CLIP視覺輸出` | 可選的 CLIP 視覺輸出，用於附加的 conditioning | CLIP_VISION_OUTPUT | 否 | - |
| `起始圖像` | 可選的起始圖像，用於初始化視頻序列。提供時，視頻的前幾幀將基於此圖像，並套用遮罩將起始幀與生成的內容混合。圖像會調整大小以符合指定的寬度和高度。 | IMAGE | 否 | - |
| `攝影機條件` | 可選的相機嵌入條件，用於視頻生成。提供時，這些條件會套用於正向和負向 conditioning。 | WAN_CAMERA_EMBEDDING | 否 | - |

**注意：** 當提供 `start_image` 時，僅使用輸入圖像的前 `length` 幀來初始化視頻序列，節點會套用遮罩將這些起始幀與生成的內容混合。`camera_conditions` 和 `clip_vision_output` 參數是可選的，但提供時，它們會修改正向和負向提示的 conditioning。

## 輸出

| 輸出名 | 描述 | 資料類型 |
| --- | --- | --- |
| `正面提示詞` | 已套用相機條件、CLIP 視覺輸出和/或起始圖像資料的修改後正向 conditioning | CONDITIONING |
| `負面提示詞` | 已套用相機條件、CLIP 視覺輸出和/或起始圖像資料的修改後負向 conditioning | CONDITIONING |
| `潛在空間` | 生成的空白視頻潛在表示，用於視頻模型。潛在張量的維度為 [batch_size, 16, frames, height/8, width/8]，其中 frames 計算方式為 ((length - 1) // 4) + 1。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanCameraImageToVideo/zh-TW.md)

---
**Source fingerprint (SHA-256):** `467a82be0dfd6ac1c3b2dd2a6cb02e0d0749de4536a7fbdb000456b817b20ebb`
