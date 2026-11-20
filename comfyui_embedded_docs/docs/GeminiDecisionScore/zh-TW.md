# Google Gemini Decision (Score)

對你連接的文字、影像、音訊或影片進行 1 至 10 的評分，並取得分數，以及一個會在你設定的閾值切換的布林值。可用來篩選或排序輸出，例如只保留評分至少為 7 的影像，並將 `result` 連接到 If/Else Switch 節點以據此採取動作。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | 要使用的模型（預設：`"gemini-decision-1"`）。 | COMBO | 是 | `"gemini-decision-1"` |
| `question` | 要評分的內容，並說明 1 與 10 分別代表什麼（預設："Rate the technical quality of the image from 1 (worst) to 10 (best)."）。 | STRING | 是 | 1 至 5000 個字元 |
| `threshold` | 當分數至少為此值時，`result` 為 true。乾淨、清晰的影像分數約為 7 至 8，嚴重損壞的影像約為 3 至 5（預設：6.0）。 | FLOAT | 是 | 1.0 至 10.0（步進值：0.1） |
| `images` | 要評分的影像，最多可透過可擴充插槽（`image_1` ... `image_16`）提供 16 張。批次影像中的每張影像各計一次。 | IMAGE | 否 | 最多 16 張影像 |
| `audio` | 要評分的音訊片段。 | AUDIO | 否 | - |
| `video` | 要評分的影片片段。 | VIDEO | 否 | - |
| `text` | 問題所針對的文字，例如提示詞或 LLM 回應，最多 20000 個字元。 | STRING | 否 | 最多 20000 個字元 |

請至少連接 `text`、`images`、`audio` 或 `video` 其中一項；當沒有可評分的內容時，節點會引發錯誤。若有多張影像，請在問題中將它們命名為 `image_1`、`image_2`，依此類推。

## 輸出

| 輸出名 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `result` | 當分數至少為 `threshold` 時為 true，否則為 false。 | BOOLEAN |
| `score` | 1 至 10 的評分。 | FLOAT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiDecisionScore/zh-TW.md)

---
**Source fingerprint (SHA-256):** `9b0a68cc7f29b1d4d23e23e051a008f34932aac6d1fe1a16e45a0e70b4df412f`
