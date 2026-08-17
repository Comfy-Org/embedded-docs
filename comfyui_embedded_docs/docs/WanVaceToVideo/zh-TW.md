# WAN 人臉轉影片

WanVaceToVideo 節點處理視訊生成模型的視訊條件資料。它接收正向與負向條件輸入以及視訊控制資料，並為視訊生成準備潛在表示。此節點處理視訊放大、遮罩和 VAE 編碼，以建立適用於視訊模型的條件結構。

## 輸入

| 參數 | 說明 | 資料型別 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `positive` | 用於引導生成的正向條件輸入 | CONDITIONING | 是 | - |
| `negative` | 用於引導生成的負向條件輸入 | CONDITIONING | 是 | - |
| `vae` | 用於編碼影像和視訊畫面的 VAE 模型 | VAE | 是 | - |
| `width` | 輸出視訊寬度（像素）（預設：832，步長：16） | INT | 是 | 16 to MAX_RESOLUTION |
| `height` | 輸出視訊高度（像素）（預設：480，步長：16） | INT | 是 | 16 to MAX_RESOLUTION |
| `length` | 視訊中的幀數（預設：81，步長：4） | INT | 是 | 1 to MAX_RESOLUTION |
| `batch_size` | 同時生成的視訊數量（預設：1） | INT | 是 | 1 to 4096 |
| `strength` | VACE 控制的條件強度（預設：1.0，步長：0.01）。這不是 LoRA 強度。LoRA 權重是透過獨立的 LoRA 節點套用的。 | FLOAT | 是 | 0.0 to 1000.0 |
| `control_video` | 用於控制條件的選用輸入視訊。如果未提供，會自動建立中性灰色視訊。若提供，則會放大至 `width` × `height`，並限制為前 `length` 幀；如果幀數較少，缺少的幀會以中性灰色填補。 | IMAGE | 否 | - |
| `control_masks` | 用於控制要修改視訊哪些部分的選用遮罩。如果未提供，會使用全白遮罩。若提供，遮罩會放大至 `width` × `height`，限制為 `length` 幀，若幀數較少則以白色填補。 | MASK | 否 | - |
| `reference_image` | 用於額外條件的選用參考影像。若提供，會放大至 `width` × `height`，由 VAE 編碼，並前置到潛在序列中。 | IMAGE | 否 | - |

**注意：** 當提供 `control_video` 時，它會被放大至指定的 `width` 和 `height`。若提供 `control_masks`，則會放大以比照相同尺寸。`reference_image` 若提供，會經 VAE 編碼並前置到潛在序列中。`length` 參數決定幀數，潛在長度計算為 `((length - 1) // 4) + 1`。

## 輸出

| 輸出名稱 | 說明 | 資料型別 |
| --- | --- | --- |
| `positive` | 套用視訊控制資料（vace_frames、vace_mask、vace_strength）的正向條件 | CONDITIONING |
| `negative` | 套用視訊控制資料（vace_frames、vace_mask、vace_strength）的負向條件 | CONDITIONING |
| `latent` | 準備用於視訊生成的空潛在張量，形狀為 [batch_size, 16, latent_length, height/8, width/8] | LATENT |
| `trim_latent` | 使用參考影像時要修剪的潛在幀數（若未提供參考影像則為 0） | INT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanVaceToVideo/zh-TW.md)

---
**Source fingerprint (SHA-256):** `2039b7509ce5b731e9e41d9cd2dad022d4c5004751f571a4cf88c1ba0cae405b`
