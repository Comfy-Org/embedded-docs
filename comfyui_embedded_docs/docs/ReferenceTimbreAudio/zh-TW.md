此節點設定參考音色，用於「ace step 1.5」流程中。其運作方式是接收條件輸入，並可選擇性地接收音訊的潛在表示，然後將該潛在資料附加到條件中，供工作流程中的後續節點使用。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `條件` | 將附加參考音訊資訊的條件資料。 | CONDITIONING | 是 |  |
| `latent` | 可選的參考音訊潛在表示。當提供時，其樣本會被添加到條件中。 | LATENT | 否 |  |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `條件` | 修改後的條件資料，若提供了可選的 `latent` 輸入，則現在包含參考音訊音色的潛在變量。 | CONDITIONING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReferenceTimbreAudio/zh-TW.md)

---
**Source fingerprint (SHA-256):** `2d39399eb79cfe76b72d01326b89863e2553bc23414b1166d310e5222b215b29`
