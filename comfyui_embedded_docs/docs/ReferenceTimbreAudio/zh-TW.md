# ReferenceTimbreAudio

此節點設定參考音色，用於「ace step 1.5」流程。它接受 conditioning 輸入和可選的音頻潛在表示，然後將該潛在資料附加到 conditioning，以便工作流程中的後續節點可以將其用作參考音頻。如果未提供潛在變量，則 conditioning 保持不變。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `conditioning` | 將附加參考音頻資訊的 conditioning 資料。 | CONDITIONING | 是 |  |
| `latent` | 參考音頻的可選潛在表示。提供時，其樣本會添加到 conditioning 中。 | LATENT | 否 |  |

當提供 `latent` 時，其樣本會附加到 conditioning 的參考音色潛在變量中。如果未提供 `latent`，則原始 conditioning 會原封不動地傳遞。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `conditioning` | 修改後的 conditioning 資料，如果提供了可選的 `latent` 輸入，現在包含參考音色潛在變量。如果未提供潛在變量，則原始 conditioning 保持不變返回。 | CONDITIONING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReferenceTimbreAudio/zh-TW.md)

---
**Source fingerprint (SHA-256):** `2ddccb7676fc45a5324ba32dde0cd2f8f24388ceec20c88a475e1aa9d4276be0`
