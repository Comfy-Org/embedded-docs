# 影片切片

Video Slice 節點可讓您從影片中提取特定片段。您可以定義開始時間和持續時間來裁剪影片，或直接跳過開頭幀。如果要求的持續時間超過剩餘影片長度，節點可以回傳可用的部分，或引發錯誤。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `影片` | 要進行切片處理的輸入影片。 | VIDEO | 是 | - |
| `起始時間` | 開始時間（秒），預設為 0.0。 | FLOAT | 是 | -1e5 至 1e5 |
| `時長` | 持續時間（秒），或 0 表示無限制（預設為 0.0）。 | FLOAT | 是 | 0.0 及以上 |
| `嚴格時長` | 若為 True，當無法達到指定的持續時間時，將引發錯誤（預設為 False）。 | BOOLEAN | 是 | - |

**注意：** 如果影片無法根據給定的 `start_time` 和 `duration` 進行切片，節點會引發錯誤。當 `strict_duration` 為 False 時，若要求的持續時間超過剩餘長度，節點會回傳影片的可用部分；當其為 True 時，則會改為引發錯誤。

## 輸出

| 輸出名 | 說明 | 資料類型 |
| --- | --- | --- |
| `video` | 裁剪後的影片片段。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Video Slice/zh-TW.md)

---
**Source fingerprint (SHA-256):** `439b76528742c1fbe230eee9502e945847ae99a58a9bd81a7a7dc3b20e15d450`
