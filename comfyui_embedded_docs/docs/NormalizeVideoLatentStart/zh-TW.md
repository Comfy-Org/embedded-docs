# NormalizeVideoLatentStart

此節點會調整影片潛在表示（video latent）的開頭幾幀，使其看起來更像後續的幀。它會從影片較後方的一組參考幀計算平均值與變異數，並將這些特徵套用至起始幀。這有助於在影片開頭建立更平滑且一致的視覺轉場。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `latent` | 要處理的影片潛在表示。 | LATENT | 是 | - |
| `start_frame_count` | 要從開頭開始正規化的潛在幀數（預設值：4）。 | INT | 是 | 1 至 16384（最大解析度） |
| `reference_frame_count` | 在起始幀之後用作參考的潛在幀數（預設值：5）。 | INT | 是 | 1 至 16384（最大解析度） |

**注意：** `reference_frame_count` 會自動限制為起始幀之後可用的幀數。如果影片潛在表示只有 1 幀，則不會執行任何正規化，並會原封不動地回傳原始的潛在表示。

## 輸出

| 輸出名 | 描述 | 資料類型 |
| --- | --- | --- |
| `latent` | 已處理的影片潛在表示，其起始幀已正規化。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/NormalizeVideoLatentStart/zh-TW.md)

---
**Source fingerprint (SHA-256):** `383e5a19ee4cd8bdea5983567ddbdc30bb09c373142a1a934cea985f1b9d1b0d`
