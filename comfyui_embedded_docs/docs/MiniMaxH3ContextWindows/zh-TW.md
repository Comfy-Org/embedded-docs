# MiniMax H3 Context Windows

將取樣分割成彼此重疊的上下文視窗，讓 MiniMax H3 影片可以長於模型的單次通過視窗。這些視窗會置於模型的 17 幀區塊上，使生成的影片與音訊在視窗邊界之間保持對齊。將回傳的模型連接到取樣器，以取代原始模型。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 要在取樣期間套用上下文視窗的模型。 | MODEL | 是 | - |
| `context_length` | 上下文視窗的長度，以實際幀數表示。必須為 17*n + 5（預設值：124）。 | INT | 是 | 22 至 16384（MAX_RESOLUTION），步進值：17 |
| `context_overlap` | 上下文視窗的重疊長度，以實際幀數表示。必須為 17*n + 5（預設值：39）。 | INT | 是 | 5 或更高，步進值：17 |
| `fuse_method` | 用於融合上下文視窗的方法（預設值：`"pyramid"`）。 | COMBO | 是 | `"pyramid"`<br>`"relative"`<br>`"flat"`<br>`"overlap-linear"` |
| `freenoise` | 是否套用 FreeNoise 雜訊洗牌，可改善視窗混合（預設值：True，進階參數）。 | BOOLEAN | 是 | true<br>false |
| `split_conds_to_windows` | 是否根據區域索引，將多個條件（由 ConditionCombine 建立）分割到各個視窗（預設值：False，進階參數）。 | BOOLEAN | 是 | true<br>false |

這兩個長度皆以實際幀數指定，並在取樣前轉換為 latent：`context_length` 在 5 幀或更少時會變成 2 個 latent，否則為 `((frames - 5) / 17) * 5 + 2`。`context_overlap` 以相同方式轉換，然後上限設為 `context_length` 減 5，因此重疊部分始終會留下一個完整區塊可往前推進。此節點一律使用步幅為 1 的靜態排程，在 latent 時間維度上套用視窗，且不加入因果修正幀，因為每個視窗都從區塊邊界開始。`split_conds_to_windows` 預期使用由 ConditionCombine 節點建立的多個條件。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `model` | 已套用上下文視窗設定的模型。 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MiniMaxH3ContextWindows/zh-TW.md)

---
**Source fingerprint (SHA-256):** `e9e019d0bc870abfe226ef1aafb2607f55c0cc1b297884db35fe98c465cc0d91`
