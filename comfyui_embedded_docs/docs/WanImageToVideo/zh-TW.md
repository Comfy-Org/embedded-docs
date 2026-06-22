# WAN 影像轉影片

WanImageToVideo 節點為影片生成任務準備條件化（conditioning）與潛在（latent）表示。它會為影片生成建立一個空的潛在空間，並可選擇性地結合起始影像與 CLIP 視覺輸出，以引導影片生成過程。此節點會根據提供的影像與視覺資料，修改正向與負向條件化輸入。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `正向` | 用於引導生成的正向條件化輸入 | CONDITIONING | 是 | - |
| `負向` | 用於引導生成的負向條件化輸入 | CONDITIONING | 是 | - |
| `vae` | 用於將影像編碼至潛在空間的 VAE 模型 | VAE | 是 | - |
| `寬度` | 輸出影片的寬度（預設值：832，步進：16） | INT | 是 | 16 至 MAX_RESOLUTION |
| `高度` | 輸出影片的高度（預設值：480，步進：16） | INT | 是 | 16 至 MAX_RESOLUTION |
| `長度` | 影片的影格數（預設值：81，步進：4） | INT | 是 | 1 至 MAX_RESOLUTION |
| `批次大小` | 每批次生成的影片數量（預設值：1） | INT | 是 | 1 至 4096 |
| `clip_vision_output` | 可選的 CLIP 視覺輸出，用於額外的條件化 | CLIP_VISION_OUTPUT | 否 | - |
| `起始影像` | 可選的起始影像，用於初始化影片生成 | IMAGE | 否 | - |

**注意：** 當提供了 `start_image` 時，節點會對影像序列進行編碼，並對條件化輸入應用遮罩。當提供了 `clip_vision_output` 參數時，它會將基於視覺的條件化添加到正向與負向輸入中。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `負向` | 已結合影像與視覺資料的修改後正向條件化 | CONDITIONING |
| `潛在空間` | 已結合影像與視覺資料的修改後負向條件化 | CONDITIONING |
| `latent` | 準備用於影片生成的空潛在空間張量 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanImageToVideo/zh-TW.md)

---
**Source fingerprint (SHA-256):** `e9f4350c43e48351523c04d82675c24f868df7b2109530c32b8e752a3ab61e8b`
