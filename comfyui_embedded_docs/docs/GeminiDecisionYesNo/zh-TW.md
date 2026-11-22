# Google Gemini Decision (Yes/No)

針對您連接的文字、影像、音訊或影片提出是非題，並取得可用於路由的布林值。將 `result` 連接到 If/Else Switch 節點，即可讓執行流程走向兩條路徑之一；當您想了解模型為何如此回答時，可讀取 `answer` 與 `probability`。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `模型` | 要使用的模型（預設：`"gemini-decision-1"`）。 | COMBO | 是 | `"gemini-decision-1"` |
| `問題` | 關於所連接內容的是非題，最多 5000 個字元。請將問題設計成「yes」代表您要採取行動的情況（預設："Is there a person in the image?"）。 | STRING | 是 | 1 至 5000 個字元 |
| `閾值` | 當「yes」的機率達到此值時，`result` 會變為 True。明確的「yes」答案分數約為 0.85 至 0.92，因此 0.9 以上會拒絕其中許多答案（預設：0.5）。 | FLOAT | 是 | 0.01 至 0.99（步進值：0.01） |
| `影像` | 要提問的影像，最多可在可擴充插槽（`image_1` ... `image_16`）中提供 16 張。批次影像中的每一張影像各計為一次。 | IMAGE | 否 | 最多 16 張影像 |
| `音訊` | 要提問的音訊片段。 | AUDIO | 否 | - |
| `影片` | 要提問的影片片段。 | VIDEO | 否 | - |
| `文字` | 問題所針對的文字，例如提示詞或 LLM 回應，最多 20000 個字元。 | STRING | 否 | 最多 20000 個字元 |

至少連接 `text`、`images`、`audio` 或 `video` 其中一項；若沒有任何可供檢視的內容，節點會引發錯誤。使用多張影像時，請在問題中以 `image_1`、`image_2` 等名稱指稱它們：批次會逐幀展開，因此編號會依連接順序跨插槽計算個別影格。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `result` | 當「yes」的機率達到 `threshold` 時為 True，否則為 False。 | BOOLEAN |
| `answer` | 判定結果，為字串 `"yes"` 或 `"no"`，並遵循與 `result` 相同的 `threshold`。 | STRING |
| `probability` | 「yes」的機率，介於 0 與 1 之間。 | FLOAT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiDecisionYesNo/zh-TW.md)

---
**Source fingerprint (SHA-256):** `0339031baf5648609b82526bed97ce8744986878bcbb706dcd3aa79a7370d83f`
