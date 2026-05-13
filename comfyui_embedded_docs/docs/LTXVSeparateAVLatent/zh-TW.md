> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVSeparateAVLatent/zh-TW.md)

## 概述

LTXVSeparateAVLatent 節點接收一個合併的音訊-視覺潛在表示，並將其拆分為兩個獨立的部分：一個用於影片，一個用於音訊。它會將樣本以及輸入潛在表示中的噪聲遮罩（若存在）分離，從而建立兩個新的潛在物件。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `av_latent` | LATENT | 是 | N/A | 待拆分的合併音訊-視覺潛在表示。 |

**注意：** 輸入潛在表示的 `samples` 張量在第一個維度（批次維度）上預期至少包含兩個元素。第一個元素用於影片潛在表示，第二個元素用於音訊潛在表示。如果存在 `noise_mask`，則會以相同方式進行拆分。

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `video_latent` | LATENT | 包含拆分後影片資料的潛在表示。 |
| `audio_latent` | LATENT | 包含拆分後音訊資料的潛在表示。 |

---
**Source fingerprint (SHA-256):** `55bce5d768e7fe13f885cc32d34ecdac5cdcbb667b03743004866ea4b6d58d46`
