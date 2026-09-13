# WAN 影像轉影片

WanImageToVideo 節點會準備用於影片生成的條件與潛在表示。它會為影片建立一個空的潛在空間，並可選擇性地納入起始影像與 CLIP vision 輸出以引導生成。`positive` 與 `negative` 條件輸入都會使用提供的影像與 CLIP vision 資料進行更新。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `正向` | 用於引導生成的正向條件輸入 | CONDITIONING | 是 | - |
| `負向` | 用於引導生成的負向條件輸入 | CONDITIONING | 是 | - |
| `vae` | 用於將影像編碼到潛在空間的 VAE 模型 | VAE | 是 | - |
| `寬度` | 生成影片的寬度（預設：832，步長：16） | INT | 是 | 16 to MAX_RESOLUTION |
| `高度` | 生成影片的高度（預設：480，步長：16） | INT | 是 | 16 to MAX_RESOLUTION |
| `長度` | 影片中的影格數（預設：81，步長：4） | INT | 是 | 1 to MAX_RESOLUTION |
| `批次大小` | 一次批次中生成的影片數量（預設：1） | INT | 是 | 1 至 4096 |
| `clip_vision_output` | 可選的 CLIP vision 輸出，會作為額外條件加入 `positive` 與 `negative` 輸入 | CLIP_VISION_OUTPUT | 否 | - |
| `起始影像` | 可選的起始影像，用於初始化影片。提供時，會將其縮放至指定的 `width` 與 `height`，並放置在影格序列的開頭；超過 `length` 的影格會被忽略。其餘影格會以中性灰（0.5）值填充。 | IMAGE | 否 | - |

**注意：** 當提供 `start_image` 時，影格序列會使用 VAE 編碼，並對條件套用遮罩。遮罩在起始影像涵蓋的影格設為 0，其餘影格設為 1，因此生成會從提供的影像繼續。編碼期間只會使用影像的前三個色彩通道（RGB）。`positive` 與 `negative` 條件都會接收相同的串接潛在影像、遮罩，以及（若有提供）CLIP vision 輸出。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `positive` | 正向條件，已使用影像與 CLIP vision 資料更新 | CONDITIONING |
| `negative` | 負向條件，已使用影像與 CLIP vision 資料更新 | CONDITIONING |
| `latent` | 可供影片生成使用的空潛在張量，形狀為 [batch_size, 16, ((length-1)//4)+1, height//8, width//8] | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanImageToVideo/zh-TW.md)

---
**Source fingerprint (SHA-256):** `46779f9f2f3da16826b7b547761a96597a3b6b43ce51a9c13367987642f3d5b7`
