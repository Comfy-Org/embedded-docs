# LTXV 空 latent 音訊

LTXV 空白潛在音訊節點會建立一批空的（零填充）潛在音訊張量。它使用所提供的 Audio VAE 模型的設定來決定潛在空間的正確維度，例如通道數和頻率區間數，並根據幀數與幀率計算音訊潛在數量。此空白潛在張量可作為 ComfyUI 中音訊生成或處理工作流程的起點。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `frames_number` | 幀數。預設值為 97。 | INT | 是 | 1 至 1000 |
| `frame_rate` | 每秒幀數。預設值為 25.0。接受 FLOAT 或 INT 值。 | FLOAT | 是 | 1.0 至 1000.0 |
| `batch_size` | 批次中的潛在音訊樣本數量。預設值為 1。 | INT | 是 | 1 至 4096 |
| `audio_vae` | 用於取得設定的 Audio VAE 模型。此參數為必要項目。 | VAE | 是 | N/A |

**注意：** `audio_vae` 輸入為必填。若未提供，節點將產生錯誤。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `Latent` | 一個空的潛在音訊張量，結構為 (batch_size, z_channels, num_audio_latents, audio_freq)，並設定為與輸入的 Audio VAE 相符。輸出也包含一個設定為 "audio" 的 `type` 欄位。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVEmptyLatentAudio/zh-TW.md)

---
**Source fingerprint (SHA-256):** `3ac1bf17ebdba7c3a73bdd795f561b7bee31798d8a1efc11b972db1944f873a4`
