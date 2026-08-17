# Recraft 影像修補

此節點根據文字提示和遮罩修改圖像的特定區域。它使用 Recraft API 智慧地僅編輯遮罩區域，同時保持圖像其餘部分不變。

## 輸入

| 參數 | 描述 | 資料型別 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `image` | 要修改的輸入圖像 | IMAGE | 是 | - |
| `mask` | 定義圖像中應修改區域的遮罩 | MASK | 是 | - |
| `prompt` | 圖像生成的提示詞（預設：空字串，最大長度：1000 個字元） | STRING | 是 | - |
| `n` | 要生成的圖像數量（預設：1，最小值：1，最大值：6） | INT | 是 | 1-6 |
| `seed` | 用於決定節點是否應重新執行的種子；無論種子如何，實際結果都是非確定性的（預設：0） | INT | 是 | 0-18446744073709551615 |
| `recraft_style` | Recraft API 的選用樣式參數。若未提供，預設為 "realistic_image" 樣式 | STYLEV3 | 否 | - |
| `negative_prompt` | 圖像上不希望出現元素的選用文字描述（預設：空字串） | STRING | 否 | - |

*注意：要使修補（inpainting）操作生效，必須同時提供 `image` 和 `mask`。遮罩會自動調整大小以匹配圖像尺寸。`prompt` 會經過驗證，且最大長度為 1000 個字元。如果使用了來自 Infinite Style Library 的 `style_id`，請確保它不是 Vector 藝術風格，因為這可能導致 API 返回 SVG 資料而不是圖像。*

## 輸出

| 輸出名稱 | 描述 | 資料型別 |
|-------------|-------------|-----------|
| `image` | 根據提示詞和遮罩生成的修改後圖像。每個輸入圖像乘以 `n` 參數返回一張圖像 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftImageInpaintingNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `539a49aec582f529a13059388222c3998e22d52618738843d9b2b6e0fb1ea5c3`
