# NormalizeVideoLatentStart

此節點會調整影片 latent 的開頭幾個影格，使其看起來更接近後續的影格。它會從影片後段的一組參考影格計算平均值與變異，並將相同的特徵套用到起始影格上。這有助於減少起始影格與影片其餘部分之間的差異，打造更平滑、更一致的轉場。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `latent` | 要處理的影片 latent 表示。 | LATENT | 是 | - |
| `start_frame_count` | 要進行正規化的 latent 影格數量，從開頭開始計算（預設：4）。 | INT | 是 | 1 到 16384（最大解析度） |
| `reference_frame_count` | 起始影格之後用作參考的 latent 影格數量（預設：5）。 | INT | 是 | 1 到 16384（最大解析度） |

**注意：** 參考影格是緊接在 `start_frame_count` 個影格之後開始取用。若可用影格數少於 `reference_frame_count` 所要求，節點會使用所有可用影格（最多為該 latent 總影格數減一）。若影片 latent 只有 1 個影格，則不執行任何正規化，並原樣回傳原始 latent。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `latent` | 已將起始影格正規化後的處理完成影片 latent。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/NormalizeVideoLatentStart/zh-TW.md)

---
**Source fingerprint (SHA-256):** `383e5a19ee4cd8bdea5983567ddbdc30bb09c373142a1a934cea985f1b9d1b0d`
