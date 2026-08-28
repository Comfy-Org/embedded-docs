# 串接 AV 潛空間

此節點將影片潛在表示（video latent）與音訊潛在表示（audio latent）合併為單一的聯合影音（AV）潛在表示，可供 LTXV 或 MiniMax H3 等 AV 模型使用。若影片輸入本身已是 AV 潛在表示，則保留其影片串流，僅以所提供的音訊潛在表示取代音訊串流。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `video_latent` | 影片資料的潛在表示。當它已同時包含影片與音訊串流時，節點會保留其影片串流，並以 `audio_latent` 中的音訊進行替換。 | LATENT | 是 |  |
| `audio_latent` | 音訊資料的潛在表示。其長度會調整以配合影片串流：較長的音訊會被截短，較短的音訊則以零填補。 | LATENT | 是 |  |

**注意：** 兩個輸入的樣本會以巢狀張量（nested tensor）中的一對影片與音訊串流形式結合。若任一輸入包含 `noise_mask`，輸出會包含合併後的遮罩；缺少的遮罩會以形狀與其樣本相符的全 1 遮罩取代。當較短的音訊被填補時，填補區域會保持未遮蓋狀態，以便模型產生該區域。若音訊潛在表示無法配合影片潛在表示，節點會引發錯誤，例如當兩個潛在表示在多個維度上不同，或是在批次或通道維度上不同時。

## 輸出

| 輸出名 | 說明 | 資料類型 |
| --- | --- | --- |
| `latent` | 包含影片與音訊樣本以兩條串流形式打包在一起的潛在表示，且當至少一個輸入提供 `noise_mask` 時，也包含合併後的 `noise_mask`。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVConcatAVLatent/zh-TW.md)

---
**Source fingerprint (SHA-256):** `0231f9db2ce73132d8555fbb33f295b68aa68a0c1c54e4a0c5d2e1f67b5611cb`
