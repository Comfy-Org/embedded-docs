# WAN 影像轉影片

WanImageToVideo 節點會為影片生成任務準備條件（conditioning）與潛在（latent）表示。它會建立一個用於影片生成的空潛在空間，並可選擇性地加入起始影像與 CLIP 視覺輸出，以引導影片生成過程。此節點會根據提供的影像與視覺資料，修改正向與負向條件輸入。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `正向` | 用於引導生成的正向條件輸入 | CONDITIONING | 是 | - |
| `負向` | 用於引導生成的負向條件輸入 | CONDITIONING | 是 | - |
| `vae` | 用於將影像編碼到潛在空間的 VAE 模型 | VAE | 是 | - |
| `寬度` | 輸出影片的寬度（預設值：832，步長：16） | INT | 是 | 16 至 MAX_RESOLUTION |
| `高度` | 輸出影片的高度（預設值：480，步長：16） | INT | 是 | 16 至 MAX_RESOLUTION |
| `長度` | 影片的幀數（預設值：81，步長：4） | INT | 是 | 1 至 MAX_RESOLUTION |
| `批次大小` | 每批生成的影片數量（預設值：1） | INT | 是 | 1 至 4096 |
| `clip_vision_output` | 選用的 CLIP 視覺輸出，用於提供額外條件 | CLIP_VISION_OUTPUT | 否 | - |
| `起始影像` | 選用的起始影像，用於初始化影片生成。提供時，影像會調整大小以符合指定的寬度和高度，影片的前幾個幀會以此影像初始化。其餘幀則填入中性灰色（0.5）數值。任何超出 `length` 的幀都會被忽略。 | IMAGE | 否 | - |

**注意：** 提供 `start_image` 時，節點會使用 VAE 對影像序列進行編碼，並對條件輸入套用遮罩。此遮罩涵蓋所有幀，但由起始影像初始化的幀除外，使生成過程能建立在所提供的影像之上。編碼時僅使用影像的前三個色彩通道（RGB）。若提供了 `clip_vision_output` 參數，則會在正向與負向輸入中加入基於視覺的條件。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `正向` | 已納入影像與視覺資料的修改後正向條件 | CONDITIONING |
| `負向` | 已納入影像與視覺資料的修改後負向條件 | CONDITIONING |
| `潛在空間` | 已準備好用於影片生成的空潛在空間張量，形狀為 [batch_size, 16, ((length-1)//4)+1, height//8, width//8] | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanImageToVideo/zh-TW.md)

---
**Source fingerprint (SHA-256):** `46779f9f2f3da16826b7b547761a96597a3b6b43ce51a9c13367987642f3d5b7`
