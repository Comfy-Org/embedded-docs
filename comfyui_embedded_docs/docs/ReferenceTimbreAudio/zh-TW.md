# ReferenceTimbreAudio

此節點會為「ace step 1.5」流程設定參考音訊。它接收一個 `conditioning` 輸入，並可選擇性地接收音訊的 latent 表示，然後將該 latent 資料附加到 `conditioning`，讓後續節點可將其用作參考音訊音色 latent。此節點標記為實驗性。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `條件` | 要附加參考音訊資訊的 conditioning 資料。 | CONDITIONING | 是 |  |
| `latent` | 參考音訊的選用 latent 表示（預設：None）。提供時，其樣本會作為參考音訊音色 latent 附加到 conditioning。 | LATENT | 否 |  |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `conditioning` | 修改後的 conditioning 資料；若提供了選用的 `latent` 輸入，現在會包含參考音訊音色 latent。 | CONDITIONING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReferenceTimbreAudio/zh-TW.md)

---
**Source fingerprint (SHA-256):** `2ddccb7676fc45a5324ba32dde0cd2f8f24388ceec20c88a475e1aa9d4276be0`
