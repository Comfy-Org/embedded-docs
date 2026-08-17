# 影片切片

Video Slice 節點允許您從影片中提取特定片段。您可以定義開始時間和持續時間來裁剪影片，或直接跳過開頭的幀。如果請求的持續時間超過剩餘影片，節點可以返回可用的部分或引發錯誤。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `video` | 要裁剪的輸入影片。 | VIDEO | 是 | - |
| `start_time` | 開始時間（秒）（預設值：0.0）。 | FLOAT | 否 | -1e5 至 1e5 |
| `duration` | 持續時間（秒），0 表示無限持續時間（預設值：0.0）。 | FLOAT | 否 | 0.0 及以上 |
| `strict_duration` | 若為 True，當無法實現指定的持續時間時，將引發錯誤（預設值：False）。 | BOOLEAN | 否 | - |

注意：當 `duration` 為 0 時，節點會從 `start_time` 裁剪到影片結尾。如果無法建立請求的片段（例如，因為 `start_time` 超過了影片結尾），節點將引發錯誤。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `video` | 裁剪後的影片片段。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Video Slice/zh-TW.md)

---
**Source fingerprint (SHA-256):** `439b76528742c1fbe230eee9502e945847ae99a58a9bd81a7a7dc3b20e15d450`
