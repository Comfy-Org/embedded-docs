# Google Gemini Decision (Yes/No)

對你連接的文字、影像、音訊或影片提出一個是非題，並取得可用於分流的布林值。將 `result` 連接到 If/Else Switch 節點，即可讓執行流程走向兩條路徑之一；當你想了解模型為何給出該答案時，可讀取 `answer` 與 `probability`。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | 要使用的模型（預設：`"gemini-decision-1"`）。 | COMBO | 是 | `"gemini-decision-1"` |
| `question` | 針對所連接內容的是非題，最多 5000 個字元。提問時請讓「是」代表你想要採取行動的情況（預設："Is there a person in the image?"）。 | STRING | 是 | 1 至 5000 個字元 |
| `threshold` | `result` 變成 true 的「是」機率門檻。明確的「是」答案分數約為 0.85 至 0.92，因此設為 0.9 或更高會排除其中許多答案（預設：0.5）。 | FLOAT | 是 | 0.01 至 0.99（步進值：0.01） |
| `images` | 要提問的影像，透過可增長的插槽（`image_1` ... `image_16`）最多可連接 16 張。批次影像會依每張影像各計一次。 | IMAGE | 否 | 最多 16 張影像 |
| `audio` | 要提問的音訊片段。 | AUDIO | 否 | - |
| `video` | 要提問的影片片段。 | VIDEO | 否 | - |
| `text` | 問題所針對的文字，例如提示詞或 LLM 回應，最多 20000 個字元。 | STRING | 否 | 最多 20000 個字元 |

至少需連接 `text`、`images`、`audio` 或 `video` 其中之一；若沒有任何可供檢視的內容，節點會引發錯誤。若有多張影像，請在問題中以 `image_1`、`image_2` 等名稱指稱它們。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `result` | 以布林值表示的答案：true 代表「是」，false 代表「否」。 | BOOLEAN |
| `answer` | 以字串 `"yes"` 或 `"no"` 表示的答案。 | STRING |
| `probability` | 「是」的機率，介於 0 與 1 之間。 | FLOAT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiDecisionYesNo/zh-TW.md)

---
**Source fingerprint (SHA-256):** `0339031baf5648609b82526bed97ce8744986878bcbb706dcd3aa79a7370d83f`
