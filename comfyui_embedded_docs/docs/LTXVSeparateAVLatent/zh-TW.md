# 分離 AV 潛空間

LTXVSeparateAVLatent 節點將合併的音訊-視覺潛在表示分割為兩個獨立的潛在表示：一個包含影片資料，一個包含音訊資料。這適用於任何音訊-視覺模型，例如 LTXV 或 MiniMax H3。`samples` 張量沿其第一個維度分割，第一個元素成為影片潛在表示，第二個元素成為音訊潛在表示；如果存在 `noise_mask`，也會以相同方式分割。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `av_latent` | 要分割為影片和音訊潛在表示的合併音訊-視覺潛在表示。 | LATENT | 是 | N/A |

**注意：** 輸入潛在表示的 `samples` 張量預期在第一個維度（批次維度）至少包含兩個元素。第一個元素用於影片潛在表示，第二個元素用於音訊潛在表示。如果存在 `noise_mask`，也會以相同方式分割。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `video_latent` | 包含分離後影片資料的潛在表示。 | LATENT |
| `audio_latent` | 包含分離後音訊資料的潛在表示。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVSeparateAVLatent/zh-TW.md)

---
**Source fingerprint (SHA-256):** `22ed38bbc1b5716cee380c35c50455810f79c273f51bbe6a535c9ae33192afe6`
