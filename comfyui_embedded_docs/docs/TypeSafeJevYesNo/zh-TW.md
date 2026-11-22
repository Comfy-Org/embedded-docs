# TypeSafe Jev (Yes/No)

TypeSafe Jev（是/否）節點會針對所連接的文字、影像或兩者提出一個是/否問題，並以布林值回傳答案。將 `result` 連接到 If/Else Switch 節點即可路由工作流程，或讀取 `probability` 以依據模型的确信程度採取行動。此為 API 節點：它會在 Comfy 的伺服器上執行，並需要具備額度的 Comfy.org 帳號。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 要使用的 Jev 模型。目前僅有一個模型可用：`jev-1.14.0`。 | COMBO | 是 | `"jev-1.14.0"` |
| `question` | 連接的文字與影像所要回答的是/否問題。提問時請讓「是」代表你想要採取行動的情況；若有多個影像插槽，請使用其名稱，例如 `Does image_2 show the same person as image_1?`（預設：`Is there a person in the image?`）。 | STRING | 是 | 1 至 1000 個字元 |
| `threshold` | 當「是」的機率至少達到此值時，答案即為是（預設 0.5）。 | FLOAT | 是 | 0.01 至 0.99（步進值：0.01） |
| `images` | 問題所針對的影像。總計最多 32 張影像；批次輸入中的每張影像各計一次。每張影像的長邊會依影像總數而受限：最多 4 張時為 1568 px、最多 8 張時為 1024 px、最多 16 張時為 768 px、最多 32 張時為 512 px，因此批次越大，每張影像的細節可能會越少。 | AUTOGROW | 否 | 0 至 32 張影像 |
| `text` | 問題所針對的文字，例如提示詞或 LLM 回應。 | STRING | 否 | 0 至 3000 個字元 |

**備註：**

- 請連接文字或至少一張影像；兩者皆為空時，節點會引發錯誤。
- 當 `probability` 至少達到 `threshold` 時，`result` 為 true，而 `answer` 會以 `yes` 或 `no` 回傳相同的判定結果。
- 計費以 token 為單位；節點上的價格標籤會顯示每 1M token 的約略費率。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `result` | 以布林值表示的答案：當「是」的機率至少達到 `threshold` 時為 true。 | BOOLEAN |
| `answer` | 以文字 `yes` 或 `no` 表示的答案。 | STRING |
| `probability` | 「是」的機率，從 0（確定為否）到 1（確定為是）。 | FLOAT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TypeSafeJevYesNo/zh-TW.md)

---
**Source fingerprint (SHA-256):** `e8c7de5558c61e7c9058b28104a72d8d8961165983d02d63a5c9078c40855385`
