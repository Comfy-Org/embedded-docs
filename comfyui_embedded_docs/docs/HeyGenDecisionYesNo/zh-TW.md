# HeyGen Decision (Yes/No)

對你連接的文字、影像、音訊或影片提出一個是非題，並取得一個可用於路由的布林值。將 `result` 連接到 If/Else Switch 節點，即可在兩條路徑之間選擇；讀取 `answer` 和 `probability` 可了解答案的明確程度。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `模型` | 要使用的模型。`heygen-decision-1-turbo` 比 `heygen-decision-1` 更快且成本更低（預設：`"heygen-decision-1"`）。 | COMBO | 是 | `"heygen-decision-1"`<br>`"heygen-decision-1-turbo"` |
| `問題` | 關於所連接內容的是非題，最多 5000 個字元。請以「是」代表你所要採取行動的情況來提問（預設："Is there a person in the image?"）。 | STRING | 是 | 1 至 5000 個字元 |
| `閾值` | 「是」的機率達到多少時 `result` 會變為 True；明確的答案會接近 0 或 1（預設：0.5）。 | FLOAT | 是 | 0.01 至 0.99（步進值：0.01） |
| `影像` | 要詢問的影像，總共最多 4 張，批次中的每個影格都會計入。它們會依序跨插槽編號為 `image_1` 至 `image_4`。 | IMAGE | 否 | 最多 4 張影像 |
| `音訊_1` | 要詢問的音訊，最長 30 分鐘。 | AUDIO | 否 | 最多 30 分鐘 |
| `影片_1` | 要詢問的影片，最長 60 秒。 | VIDEO | 否 | 最多 60 秒 |
| `文字` | 問題所針對的文字，例如提示詞或 LLM 回應，最多 20000 個字元。 | STRING | 否 | 最多 20000 個字元 |

至少連接 `text`、`images`、`audio_1` 或 `video_1` 其中之一，並在問題中以插槽名稱引用它們，例如 "Does image_2 show the same person as image_1?"。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `result` | 當「是」的機率達到 `threshold` 時為 True，否則為 False。 | BOOLEAN |
| `answer` | 判定結果，為字串 `"yes"` 或 `"no"`，依據與 `result` 相同的 `threshold`。 | STRING |
| `probability` | 「是」的機率，介於 0 與 1 之間。 | FLOAT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenDecisionYesNo/zh-TW.md)

---
**Source fingerprint (SHA-256):** `5a6a606d5c6ef62eb3424bd54a0da3dc177da7d0acf4b5c235a62b78ad8d2df1`
