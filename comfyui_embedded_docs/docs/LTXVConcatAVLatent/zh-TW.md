# 串接 AV 潛空間

LTXVConcatAVLatent 節點將視訊潛在與音訊潛在合併為單一聯合潛在，供 LTXV 或 MiniMax H3 等音訊視訊模型使用。它將兩個輸入的 `samples` 捆綁在一起，如果任一輸入包含 `noise_mask`，這些遮罩也會一併捆綁。如果視訊潛在已經是 AV 潛在，此節點會保留其視訊流，並以提供的音訊潛在取代其音訊流。

## 輸入

| 參數 | 說明 | 資料型別 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `video_latent` | 視訊資料的潛在表示。 | LATENT | 是 |  |
| `audio_latent` | 要與視訊潛在結合的音訊資料潛在表示。 | LATENT | 是 |  |

**關於音訊長度的說明：** 當 `video_latent` 已經是 AV 潛在時，`audio_latent` 必須在除一個維度外的所有維度上與內嵌音訊流相符。此節點會沿該維度修剪或零填充音訊，以符合現有流的長度。填充的尾部會保持未遮罩狀態，以便模型可以生成它。

## 輸出

| 輸出名稱 | 說明 | 資料型別 |
| --- | --- | --- |
| `latent` | 包含配對的視訊與音訊 `samples` 的潛在。如果任一輸入提供 `noise_mask`，輸出也會包含配對的 `noise_mask`；缺少的遮罩會以 1 取代。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVConcatAVLatent/zh-TW.md)

---
**Source fingerprint (SHA-256):** `0231f9db2ce73132d8555fbb33f295b68aa68a0c1c54e4a0c5d2e1f67b5611cb`
