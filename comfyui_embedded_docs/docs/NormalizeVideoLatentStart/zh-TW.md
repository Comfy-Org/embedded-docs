# NormalizeVideoLatentStart

此節點調整影片潛在表示的前幾幀，使其看起來更類似於後續的幀。它會計算影片後段一組參考幀的平均值與變異程度，並將這些相同的特徵套用到起始幀。這有助於在影片開頭創造更平滑且一致的視覺過渡。

## 輸入

| 參數 | 描述 | 資料型別 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `latent` | 要處理的影片潛在表示。 | LATENT | 是 | - |
| `start_frame_count` | 要正規化的潛在幀數，從開頭起算（預設：4）。 | INT | 是 | 1 至 16384 (max resolution) |
| `reference_frame_count` | 起始幀之後用作參考的潛在幀數（預設：5）。 | INT | 是 | 1 至 16384 (max resolution) |

**注意：** `reference_frame_count` 會自動限制為起始幀之後可用的幀數。如果影片潛在只有 1 幀長，則不會執行正規化，並回傳原始的潛在表示。

## 輸出

| 輸出名稱 | 描述 | 資料型別 |
| --- | --- | --- |
| `latent` | 已處理的影片潛在表示，其起始幀已正規化。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/NormalizeVideoLatentStart/zh-TW.md)

---
**Source fingerprint (SHA-256):** `383e5a19ee4cd8bdea5983567ddbdc30bb09c373142a1a934cea985f1b9d1b0d`
