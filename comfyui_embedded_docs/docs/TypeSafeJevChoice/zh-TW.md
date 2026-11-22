# TypeSafe Jev (Choice)

TypeSafe Jev (Choice) 節點會針對所連接的文字、影像或兩者，從您自訂的選項中挑選一個。將 `choice` 連接到輸入帶有選項名稱的 Branch 節點，或使用 `option_index` 依所選選項的位置進行切換。此為 API 節點，需要 Comfy.org 帳號與 API 金鑰。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 要使用的 Jev 模型。目前僅有一個模型可用：`jev-1.14.0`。 | COMBO | 是 | `"jev-1.14.0"` |
| `question` | 這些選項所要回答的問題。若有多個影像插槽，請使用其名稱，例如 `Which season is shown in image_1?`（預設：`What style is the image?`）。 | STRING | 是 | 1 至 1000 個字元 |
| `options` | 可供選擇的選項，每行一個。可新增如 `other` 的選項，用於不符合任何選項的輸入（預設：`photo`、`illustration`、`3d render`、`anime`、`sketch` 和 `other`，每行一個）。 | STRING | 是 | 2 至 50 個選項，每個最多 40 個字元 |
| `images` | 問題所針對的影像。總共最多 32 張影像；批次輸入會依影像數量計次，超過 4 張影像時會以較小尺寸傳送。 | AUTOGROW | 否 | 0 至 32 張影像 |
| `text` | 問題所針對的文字，例如提示詞或 LLM 回應。 | STRING | 否 | 0 至 3000 個字元 |

**注意事項：**

- 請連接文字或至少一張影像；兩者皆為空時節點會引發錯誤。
- 當提供的選項少於 2 個或多於 50 個、某個選項超過 40 個字元，或兩個選項僅大小寫不同時，節點會引發錯誤。
- `option_index` 從 0 開始計數，因此清單中的第一個選項索引為 0。
- 計費以權杖（token）為基礎；節點上的價格標籤顯示每 1M 個權杖的約略費率。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `choice` | 所選的選項，完全依照 `options` 中出現的內容書寫。 | STRING |
| `option_index` | 所選選項在選項清單中的位置，從 0 開始。 | INT |
| `confidence` | Jev 的確信程度，從 0（沒有明確勝出者）到 1（確定）。 | FLOAT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TypeSafeJevChoice/zh-TW.md)

---
**Source fingerprint (SHA-256):** `b1cd36d600f5c07935c455d9e926e6c0a53f172fcc1a6f602c8d4dc70eeffabe`
