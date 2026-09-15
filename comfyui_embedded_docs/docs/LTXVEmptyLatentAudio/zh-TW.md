# LTXV 空 latent 音訊

LTXV Empty Latent Audio 節點會建立一批空的（填零）潛在音訊張量。它會讀取所連接 Audio VAE 模型的組態，以判斷正確的潛在維度，例如通道數與頻率區間，並根據影格數與影格率計算所需的音訊潛在數量。產生的空潛在可作為音訊生成或操作工作流程的起點。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `frames_number` | 影格數。預設值為 97。 | INT | 是 | 1 至 1000 |
| `frame_rate` | 每秒影格數。預設值為 25.0。此輸入可接受 FLOAT 或 INT 值。 | FLOAT | 是 | 1.0 至 1000.0 |
| `batch_size` | 批次中的潛在音訊樣本數。預設值為 1。 | INT | 是 | 1 至 4096 |
| `audio_vae` | 用於取得組態的 Audio VAE 模型。顯示為 "Audio VAE"。 | VAE | 是 | N/A |

**注意：**`audio_vae` 輸入為必填。若未提供，節點會引發錯誤。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `Latent` | 一個空的潛在音訊張量，形狀為 (batch_size, z_channels, num_audio_latents, audio_freq)，其中通道數與頻率區間來自 Audio VAE，而音訊潛在數量則由 `frames_number` 與 `frame_rate` 推導而來。輸出也包含一個設為 "audio" 的 `type` 欄位。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVEmptyLatentAudio/zh-TW.md)

---
**Source fingerprint (SHA-256):** `3ac1bf17ebdba7c3a73bdd795f561b7bee31798d8a1efc11b972db1944f873a4`
