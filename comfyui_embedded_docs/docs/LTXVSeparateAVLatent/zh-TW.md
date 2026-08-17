# 分離 AV 潛空間

LTXVSeparateAVLatent 節點接收組合的音訊-視覺潛在表示，並將其拆分為兩個獨立的潛在表示：一個用於影片，一個用於音訊。它可與任何音訊-視覺模型搭配使用，例如 LTXV 或 MiniMax H3。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `av_latent` | 要拆分的組合音訊-視覺潛在表示。 | LATENT | 是 | N/A |

**注意：** 輸入潛在表示的 `samples` 張量預期在第一個維度（批次維度）上至少有兩個元素。第一個元素用於影片潛在表示，第二個元素用於音訊潛在表示。如果存在 `noise_mask`，則會以相同方式拆分。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `video_latent` | 包含已拆分影片資料的潛在表示。 | LATENT |
| `audio_latent` | 包含已拆分音訊資料的潛在表示。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVSeparateAVLatent/zh-TW.md)

---
**Source fingerprint (SHA-256):** `22ed38bbc1b5716cee380c35c50455810f79c273f51bbe6a535c9ae33192afe6`
