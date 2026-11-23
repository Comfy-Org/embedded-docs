# TypeSafe Jev (Score)

TypeSafe Jev (Score) 節點會對連接的文字、影像或兩者進行 1 到 10 的評分，並將評分與閾值比較。將 `result` 連接到 If/Else Switch 節點以根據分數採取動作，或讀取 `score` 以使用原始評分。這是 API 節點：它在 Comfy 的伺服器上執行，並需要具有額度的 Comfy.org 帳戶。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 要使用的 Jev 模型。目前僅有一個可用模型：`jev-1.14.0`。 | COMBO | 是 | `"jev-1.14.0"` |
| `question` | 要評分的內容，評分範圍為 1 到 10。說明 1 和 10 的含義，如同預設值（預設：`Rate the technical quality of the image from 1 (worst) to 10 (best).`）。 | STRING | 是 | 1 至 1000 個字元 |
| `threshold` | 當分數至少為此值時，`result` 為 true（預設：5.0）。 | FLOAT | 是 | 1.0 至 10.0（步進值：0.1） |
| `images` | 問題所針對的影像。總共最多 32 張影像；批次輸入會按每張影像各計一次。每張影像的長邊會受到影像總數限制：最多 4 張影像時為 1568 px，最多 8 張時為 1024 px，最多 16 張時為 768 px，最多 32 張時為 512 px，因此較大的批次可能會降低每張影像的細節。 | AUTOGROW | 否 | 0 至 32 張影像 |
| `text` | 問題所針對的文字，例如提示詞或 LLM 回應。 | STRING | 否 | 0 至 3000 個字元 |

**備註：**

- 連接文字或至少一張影像；當兩者皆為空時，節點會引發錯誤。
- 分數會以 1 到 10 回報，且當分數至少為 `threshold` 時，`result` 為 true。
- 計費以 token 為基礎；節點上的價格徽章會顯示每 100 萬個 token 的約略費率。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `result` | 當 `score` 至少為 `threshold` 時為 True。 | BOOLEAN |
| `score` | 從 1（最差）到 10（最佳）的評分。 | FLOAT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TypeSafeJevScore/zh-TW.md)

---
**Source fingerprint (SHA-256):** `7e1970e903d2099ab3d7481a758c5291e87614b9eaf116d0ced6a1bcd36dc126`
