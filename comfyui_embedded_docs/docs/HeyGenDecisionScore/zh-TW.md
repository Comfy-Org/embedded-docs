# HeyGen Decision (Score)

將你連接的文字、影像、音訊或影片評分為 1 到 10，取得分數以及一個會在你設定的閾值處翻轉的布林值。用它來篩選或排序輸出，並將 `result` 連接到 If/Else Switch 節點，以根據分數採取動作。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | 要使用的模型。`heygen-decision-1-turbo` 比 `heygen-decision-1` 更快且成本更低（預設：`"heygen-decision-1"`）。 | COMBO | 是 | `"heygen-decision-1"`<br>`"heygen-decision-1-turbo"` |
| `question` | 要評分的內容，並說明 1 與 10 代表什麼（預設："Rate the technical quality of the image from 1 (worst) to 10 (best)."）。 | STRING | 是 | 1 至 5000 個字元 |
| `threshold` | 當分數至少為此值時，`result` 為 true。乾淨銳利的影像得分約為 7，嚴重損壞的影像約為 3 至 5（預設：6.0）。 | FLOAT | 是 | 1.0 至 10.0（步進值：0.1） |
| `images` | 要評分的影像，總共最多 4 張，批次中的每一幀都會計入。它們會依插槽順序編號為 `image_1` 至 `image_4`。 | IMAGE | 否 | 最多 4 張影像 |
| `audio_1` | 要評分的音訊，最長 30 分鐘。 | AUDIO | 否 | 最多 30 分鐘 |
| `video_1` | 要評分的影片，最長 60 秒。 | VIDEO | 否 | 最多 60 秒 |
| `text` | 問題所針對的文字，例如提示詞或 LLM 回應，最多 20000 個字元。 | STRING | 否 | 最多 20000 個字元 |

至少連接一個要評分的輸入，並在問題中以插槽名稱指稱它們，例如 "How sharp is image_1?"。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `result` | 當分數至少為 `threshold` 時為 true，否則為 false。 | BOOLEAN |
| `score` | 1 到 10 的評分。 | FLOAT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenDecisionScore/zh-TW.md)

---
**Source fingerprint (SHA-256):** `47f7aeab15292a2156b8da23c9911f4155c5b05c9ea9c0c502c30221aa522b58`
