# WAN 影像轉影片

WanImageToVideo 節點為影片生成任務準備 conditioning 與 latent 表示。它建立一個用於影片生成的空 latent 空間，並可選擇性地納入起始影像與 CLIP 視覺輸出，以引導影片生成過程。此節點會根據提供的影像與視覺資料，修改正面與負面 conditioning 輸入。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `positive` | 用於引導生成的正面 conditioning 輸入 | CONDITIONING | 是 | - |
| `negative` | 用於引導生成的負面 conditioning 輸入 | CONDITIONING | 是 | - |
| `vae` | 用於將影像編碼至 latent 空間的 VAE 模型 | VAE | 是 | - |
| `width` | 輸出影片的寬度（預設：832，步長：16） | INT | 是 | 16 至 MAX_RESOLUTION |
| `height` | 輸出影片的高度（預設：480，步長：16） | INT | 是 | 16 至 MAX_RESOLUTION |
| `length` | 影片中的幀數（預設：81，步長：4） | INT | 是 | 1 至 MAX_RESOLUTION |
| `batch_size` | 每批生成的影片數量（預設：1） | INT | 是 | 1 至 4096 |
| `clip_vision_output` | 可選的 CLIP 視覺輸出，用於額外 conditioning | CLIP_VISION_OUTPUT | 否 | - |
| `start_image` | 可選的起始影像，用於初始化影片生成。提供時，此影像會被調整大小以符合指定的寬度與高度，影片的前幾幀會以此影像初始化，剩餘幀則填入中性灰色（0.5）值。僅使用影像的前 `length` 幀。 | IMAGE | 否 | - |

**注意：** 當提供 `start_image` 時，節點會使用 VAE 將影像序列編碼，並對 conditioning 輸入套用遮罩。此遮罩涵蓋除起始影像初始化的幀以外的所有幀，讓生成能建立在所提供的影像上。當提供 `clip_vision_output` 參數時，會向正面與負面輸入添加基於視覺的 conditioning。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `positive` | 已整合影像與視覺資料的修改後正面 conditioning | CONDITIONING |
| `negative` | 已整合影像與視覺資料的修改後負面 conditioning | CONDITIONING |
| `latent` | 已準備好用於影片生成的空 latent 空間張量，形狀為 [batch_size, 16, ((length-1)//4)+1, height//8, width//8] | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanImageToVideo/zh-TW.md)

---
**Source fingerprint (SHA-256):** `46779f9f2f3da16826b7b547761a96597a3b6b43ce51a9c13367987642f3d5b7`
