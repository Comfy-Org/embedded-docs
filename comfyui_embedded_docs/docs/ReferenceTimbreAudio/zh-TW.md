# ReferenceTimbreAudio

此節點設定參考音色，用於「ace step 1.5」流程。它藉由接收 `conditioning` 輸入，並可選擇接收音訊的潛在表示（latent），然後將該潛在資料附加到 `conditioning` 上，供工作流程中的後續節點使用。此節點目前標記為實驗性。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `條件` | 將被附加參考音色資訊的 conditioning 資料。 | CONDITIONING | 是 |  |
| `latent` | 可選的參考音訊潛在表示。若提供，其樣本將被添加（附加）到 conditioning 中，以便用作參考音色潛在表示。 | LATENT | No |  |

## 輸出

| 輸出名 | 描述 | 資料類型 |
| --- | --- | --- |
| `conditioning` | 修改後的 conditioning 資料，若提供了可選的 `latent` 輸入，則現在包含參考音色潛在表示。 | CONDITIONING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReferenceTimbreAudio/zh-TW.md)

---
**Source fingerprint (SHA-256):** `2ddccb7676fc45a5324ba32dde0cd2f8f24388ceec20c88a475e1aa9d4276be0`
