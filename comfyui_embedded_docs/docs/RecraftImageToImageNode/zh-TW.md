# Recraft 影像轉影像

此節點根據文字提示和強度參數修改現有影像。它使用 Recraft API 根據提供的描述轉換輸入影像，同時根據強度設定保持與原始影像的些許相似性。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `image` | 要修改的輸入影像 | IMAGE | 是 | - |
| `prompt` | 影像生成的提示詞（預設值：""，最大長度：1000 個字元） | STRING | 是 | - |
| `n` | 要生成的影像數量（預設值：1） | INT | 是 | 1-6 |
| `strength` | 定義與原始影像的差異，應介於 [0, 1] 之間，其中 0 表示幾乎相同，1 表示幾乎沒有相似性（預設值：0.5） | FLOAT | 是 | 0.0-1.0 |
| `seed` | 用於決定節點是否應重新執行的種子；無論種子為何，實際結果皆為非確定性（預設值：0） | INT | 是 | 0-18446744073709551615 |
| `recraft_style` | 影像生成的選擇性樣式。若未提供，預設為 `realistic_image` | STYLEV3 | 否 | - |
| `negative_prompt` | 關於影像上不希望出現元素的可選文字描述（預設值：""） | STRING | 否 | - |
| `recraft_controls` | 透過 Recraft Controls 節點對生成進行選擇性附加控制 | CONTROLS | 否 | - |

**注意：** `seed` 參數僅觸發節點重新執行，但不保證確定性結果。內部會將 strength 參數四捨五入至小數點後 2 位。提示詞會經過驗證，且不得超過 1000 個字元。若未提供 `recraft_style`，節點預設使用 `realistic_image` 樣式。若您使用來自 Infinite Style Library 的 `style_id`，請確保它不是向量藝術樣式，因為這可能會導致節點接收 SVG 資料而非影像，從而產生錯誤。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `image` | 根據輸入影像和提示詞生成的影像。對於每個輸入影像，會生成 `n` 個影像，因此總輸出數量等於輸入數量乘以 `n`。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftImageToImageNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `1932e55d1dc392e6bd42a0bd29f5aaba44b65997b597648a927fba38a27c90ad`
