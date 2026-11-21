# Google Gemini Decision (Score)

對你連接的文字、影像、音訊或影片進行 1 到 10 分的評分，並取得分數，以及一個會在你設定的閾值處翻轉的布林值。可用它來篩選或排序輸出，例如只保留分數至少 7 分的影像，並將 `result` 連接到 If/Else Switch 節點以據此採取動作。每次執行會把你連接的內容當作整體來評分，因此若要篩選個別影像，就必須逐一評分。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | 要使用的模型（預設：`"gemini-decision-1"`）。 | COMBO | 是 | `"gemini-decision-1"` |
| `question` | 要評分的內容，並說明 1 與 10 分別代表什麼（預設："Rate the technical quality of the image from 1 (worst) to 10 (best)."）。 | STRING | 是 | 1 至 5000 個字元 |
| `threshold` | 當分數至少達到此值時，`result` 為 true。乾淨、清晰的影像約得分 7 至 8，嚴重損壞的影像約 3 至 5（預設：6.0）。 | FLOAT | 是 | 1.0 至 10.0（步進值：0.1） |
| `images` | 要評分的影像，透過可擴充的插槽（`image_1` ... `image_16`）最多可達 16 張。批次中的每張影像各計一次。 | IMAGE | 否 | 最多 16 張影像 |
| `audio` | 要評分的音訊片段。 | AUDIO | 否 | - |
| `video` | 要評分的影片片段。 | VIDEO | 否 | - |
| `text` | 問題所針對的文字，例如提示詞或 LLM 回應，最多 20000 個字元。 | STRING | 否 | 最多 20000 個字元 |

至少須連接 `text`、`images`、`audio` 或 `video` 其中之一；若沒有任何可評分的內容，節點會引發錯誤。若有多張影像，請在問題中以 `image_1`、`image_2` 等名稱稱呼它們。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `result` | 當分數至少達到 `threshold` 時為 true，否則為 false。 | BOOLEAN |
| `score` | 1 到 10 的評分。 | FLOAT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiDecisionScore/zh-TW.md)

---
**Source fingerprint (SHA-256):** `9b0a68cc7f29b1d4d23e23e051a008f34932aac6d1fe1a16e45a0e70b4df412f`
