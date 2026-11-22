# TypeSafe Jev (Pick Image)

TypeSafe Jev（Pick Image）節點會從一批影像中挑選一張影像。將 `index` 連接到 Get Image from Batch 以保留挑選的影像，或讀取 `confidence` 來判斷挑選結果是否夠好。此為 API 節點，需要 Comfy.org 帳號和 API 金鑰。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 要使用的 Jev 模型。目前僅有一個模型可用：`jev-1.14.0`。 | COMBO | 是 | `"jev-1.14.0"` |
| `question` | 要挑選哪張影像。將提示詞連接到 `text`，以挑選最符合該提示詞的影像（預設：`Which image best matches the prompt in text? If there is no text, which image has the best quality?`）。 | STRING | 是 | 1 至 1000 個字元 |
| `images` | 可供選擇的影像。批次輸入會依每張影像各計一次，因此批次中的每張影像都是候選。 | IMAGE | 是 | 2 至 32 張影像 |
| `text` | 問題所涉及的文字，例如產出這些影像所用的提示詞。 | STRING | 否 | 0 至 3000 個字元 |

**注意事項：**

- 當連接的影像少於 2 張或多於 32 張時，此節點會引發錯誤。
- `index` 從 0 開始計數，這是 Get Image from Batch 預期的位置。
- 計費以權杖（token）為單位；節點上的價格標籤會顯示每 100 萬個權杖的約略費率。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `index` | 挑選影像在批次中的位置，從 0 開始。 | INT |
| `confidence` | Jev 的確信程度，從 0（無明顯勝出者）到 1（確定）。 | FLOAT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TypeSafeJevPickImage/zh-TW.md)

---
**Source fingerprint (SHA-256):** `432ee9ba69ebc0b452de4b52e94abdc56a65dc694a463a3654efb62b172c7b93`
