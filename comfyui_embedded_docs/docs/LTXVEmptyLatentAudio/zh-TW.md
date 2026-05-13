> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVEmptyLatentAudio/zh-TW.md)

## 概述

LTXV 空潛在音訊節點會建立一批空的（零填充）潛在音訊張量。它使用提供的音訊 VAE 模型中的配置來確定潛在空間的正確維度，例如通道數和頻率區間。這個空的潛在張量可作為 ComfyUI 中音訊生成或處理工作流程的起點。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `frames_number` | INT | 是 | 1 至 1000 | 影格數量。預設值為 97。 |
| `frame_rate` | INT | 是 | 1 至 1000 | 每秒影格數。預設值為 25。 |
| `batch_size` | INT | 是 | 1 至 4096 | 批次中的潛在音訊樣本數量。預設值為 1。 |
| `audio_vae` | VAE | 是 | 不適用 | 用於獲取配置的音訊 VAE 模型。此參數為必要項目。 |

**注意：** `audio_vae` 輸入為強制性參數。若未提供，節點將會引發錯誤。

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `Latent` | LATENT | 一個空的潛在音訊張量，其結構為 (batch_size, z_channels, num_audio_latents, audio_freq)，配置為與輸入的音訊 VAE 相符。輸出還包含一個設為 "audio" 的 `type` 欄位。 |

---
**Source fingerprint (SHA-256):** `1a8bfea98f14de014069016652b39542cfd9290cae2d870ab4e381e46aa1e08f`
