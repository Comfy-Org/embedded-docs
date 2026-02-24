> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVEmptyLatentAudio/zh-TW.md)

LTXV Empty Latent Audio 節點會建立一批空的（以零填充的）潛在音訊張量。它使用提供的 Audio VAE 模型的配置來確定潛在空間的正確維度，例如通道數和頻率區間數。這個空的潛在張量可作為 ComfyUI 內音訊生成或處理工作流程的起點。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `frames_number` | INT | 是 | 1 至 1000 | 幀數。預設值為 97。 |
| `frame_rate` | INT | 是 | 1 至 1000 | 每秒幀數。預設值為 25。 |
| `batch_size` | INT | 是 | 1 至 4096 | 批次中的潛在音訊樣本數量。預設值為 1。 |
| `audio_vae` | VAE | 是 | N/A | 用於獲取配置的 Audio VAE 模型。此參數為必填項。 |

**注意：** `audio_vae` 輸入是強制性的。如果未提供，節點將引發錯誤。

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `Latent` | LATENT | 一個空的潛在音訊張量，其結構（樣本數、取樣率、類型）已配置為與輸入的 Audio VAE 相匹配。 |
