# Google Gemini Decision (Choice)

針對你連接的文字、影像、音訊或影片，從你自己提供的選項中挑選一個，並取回所選的選項、其位置與信心分數。將 `choice` 連接到 Branch 節點，該節點的輸入需帶有相同的選項名稱；或依 `option_index` 進行路由。Branch 節點最多接受 32 個輸入，因此選項數量較多時請使用 `option_index` 來路由。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | 要使用的模型（預設：`"gemini-decision-1"`）。 | COMBO | 是 | `"gemini-decision-1"` |
| `question` | 選項要回答的問題，最多 5000 個字元（預設："What style is the image?"）。 | STRING | 是 | 1 至 5000 個字元 |
| `options` | 每行一個選項，依輸入原樣使用，每個最多 128 個字元。為不符合任何選項的輸入新增如 `other` 的選項（預設：`photo`、`illustration`、`3d render`、`anime`、`sketch`、`other`）。 | STRING | 是 | 2 至 255 個選項 |
| `images` | 要分類的影像，跨可擴充的插槽（`image_1` ... `image_16`）最多 16 張。批次影像中的每張影像各計一次。 | IMAGE | 否 | 最多 16 張影像 |
| `audio` | 要分類的音訊片段。 | AUDIO | 否 | - |
| `video` | 要分類的影片片段。 | VIDEO | 否 | - |
| `text` | 問題所關於的文字，例如提示詞或 LLM 回應，最多 20000 個字元。 | STRING | 否 | 最多 20000 個字元 |

至少提供 2 個、最多 255 個選項，且不得重複列出任何選項；否則節點會引發錯誤。請至少連接 `text`、`images`、`audio` 或 `video` 其中之一，並在問題中以 `image_1`、`image_2` 等名稱來指稱多張影像。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `choice` | 所選的選項，與 `options` 中撰寫的內容完全相同。 | STRING |
| `option_index` | 所選選項在 `options` 中的位置，從 0 開始。 | INT |
| `confidence` | 對此選擇的信心程度，介於 0 與 1 之間。 | FLOAT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiDecisionChoice/zh-TW.md)

---
**Source fingerprint (SHA-256):** `200c63a9197cd95ba0a21da88c5f3117014b37b0651541094a775219381afe43`
