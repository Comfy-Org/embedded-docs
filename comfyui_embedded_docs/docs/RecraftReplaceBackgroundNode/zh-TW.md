# Recraft 更換背景

根據提供的提示詞替換圖片背景。此節點使用 Recraft API，根據您的文字描述為圖片生成新的背景，讓您可以在保持主體不變的情況下完全轉換背景。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `image` | 要處理的輸入圖片 | IMAGE | 是 | - |
| `prompt` | 圖片生成的提示詞（預設為空白） | STRING | 是 | - |
| `n` | 要生成的圖片數量（預設：1） | INT | 是 | 1-6 |
| `seed` | 用於決定節點是否重新執行的種子；無論種子為何，實際結果皆為非確定性（預設：0） | INT | 是 | 0-18446744073709551615 |
| `recraft_style` | 可選的背景生成樣式。若未提供，預設使用「realistic_image」樣式 | STYLEV3 | 否 | - |
| `negative_prompt` | 圖片上不希望出現元素的可選文字描述（預設為空白） | STRING | 否 | - |

**注意：** `seed` 參數控制節點何時重新執行，但由於外部 API 的性質，無法保證結果具有確定性。

**注意：** 輸入批次中的每張圖片都會被單獨處理；節點會為每張輸入圖片回傳 `n` 張背景替換後的圖片。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `IMAGE` | 背景替換後的生成圖片 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftReplaceBackgroundNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `45a2607ae73cc67caa98d33bf536feda83a2021d960dec7cca76cbe0b9fc47ef`
