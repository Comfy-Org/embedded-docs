# TypeSafe Jev (Choice)

TypeSafe Jev (Choice) 節點會從您自訂的選項中，為連接的文字、影像或兩者擇一。將 `choice` 連接到 Branch 節點，並讓其輸入帶有選項名稱；或使用 `option_index` 依所選選項的位置進行切換。Branch 節點最多接受 32 個輸入，因此選項數量超過此上限的清單只能透過 `option_index` 來路由。這是 API 節點：它在 Comfy 的伺服器上執行，需要具備額度的 Comfy.org 帳號。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 要使用的 Jev 模型。目前僅有一個模型可用：`jev-1.14.0`。 | COMBO | 是 | `"jev-1.14.0"` |
| `question` | 選項所回答的問題。若有多個影像插槽，請使用它們的名稱，例如 `Which season is shown in image_1?`（預設：`What style is the image?`）。 | STRING | 是 | 1 至 1000 個字元 |
| `options` | 供選擇的選項，每行一個。每行的開頭與結尾空白會被去除，且選項在忽略大小寫的情況下必須唯一，因此重複的選項或僅大小寫不同的兩個選項都會被拒絕。請為不符合任何選項的輸入新增一個選項，例如 `other`（預設：`photo`、`illustration`、`3d render`、`anime`、`sketch` 與 `other`，每行一個）。 | STRING | 是 | 2 至 50 個選項，每個最多 40 個字元 |
| `images` | 問題所針對的影像。總共最多 32 張影像；批次輸入會依每張影像各計一次。每張影像的長邊會依影像總數而受到限制：最多 4 張影像時為 1568 px，最多 8 張時為 1024 px，最多 16 張時為 768 px，最多 32 張時為 512 px，因此較大的批次可能會降低每張影像的細節。 | AUTOGROW | 否 | 0 至 32 張影像 |
| `text` | 問題所針對的文字，例如提示詞或 LLM 回應。 | STRING | 否 | 0 至 3000 個字元 |

**備註：**

- 請連接文字或至少一張影像；當兩者皆為空時，節點會引發錯誤。
- 當提供的選項少於 2 個或多於 50 個、某個選項長度超過 40 個字元，或兩個選項在忽略大小寫的情況下相同時，節點會引發錯誤。
- `option_index` 從 0 開始計數，因此清單中的第一個選項索引為 0。
- 計費以 token 為基礎；節點上的價格標示會顯示每 1M 個 token 的約略費率。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `choice` | 所選的選項，其開頭與結尾空白會被去除。若 Branch 輸入的名稱保留了這些空白，將不會相符。 | STRING |
| `option_index` | 所選選項在選項清單中的位置，從 0 開始。 | INT |
| `confidence` | Jev 的確信程度，從 0（沒有明顯勝出者）到 1（確定）。 | FLOAT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TypeSafeJevChoice/zh-TW.md)

---
**Source fingerprint (SHA-256):** `b1cd36d600f5c07935c455d9e926e6c0a53f172fcc1a6f602c8d4dc70eeffabe`
