> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeLumina2/zh-TW.md)

# CLIP Text Encode for Lumina2 節點

此節點使用 CLIP 模型將系統提示詞和使用者提示詞編碼為嵌入向量，以引導擴散模型生成特定圖像。它將預定義的系統提示詞與您的自訂文字提示詞結合，並透過 CLIP 模型處理，為圖像生成建立條件資料。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `system_prompt` | STRING | 是 | `"superior"`<br>`"alignment"` | Lumina2 提供兩種系統提示詞類型："superior" 可生成具有優異圖文對齊效果的圖像；"alignment" 則生成具有最高圖文對齊程度的優質圖像。 |
| `user_prompt` | STRING | 是 | 不適用 | 要編碼的文字。支援多行輸入和動態提示詞。 |
| `clip` | CLIP | 是 | 不適用 | 用於編碼文字的 CLIP 模型。 |

**注意：** `clip` 輸入為必要項目，不可為空值。如果 clip 輸入無效，節點將引發錯誤，表示檢查點可能不包含有效的 CLIP 或文字編碼器模型。

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `CONDITIONING` | CONDITIONING | 包含嵌入文字的條件資料，用於引導擴散模型。 |

---
**Source fingerprint (SHA-256):** `fcc0802180ffc2c0757b395850d54632da011473da0c6b1c5268b42da3747024`
