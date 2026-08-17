# TextEncodeQwenImageEdit

TextEncodeQwenImageEdit 節點處理文字提示詞與可選圖片，以生成用於影像生成或編輯的 conditioning 資料。它使用 CLIP 模型對輸入進行標記化（tokenize），並可選擇使用 VAE 將參考圖片編碼為參考潛在變數（reference latents）。當提供圖片時，節點會自動調整圖片尺寸，以維持一致的處理維度。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `clip` | 用於文字和圖片標記化的 CLIP 模型 | CLIP | 是 | - |
| `prompt` | 用於生成 conditioning 的文字提示詞，支援多行輸入和動態提示詞 | STRING | 是 | - |
| `vae` | 可選的 VAE 模型，用於將參考圖片編碼為潛在變數 | VAE | 否 | - |
| `image` | 可選的輸入圖片，用於參考或編輯用途 | IMAGE | 否 | - |

**注意：** 當同時提供 `image` 和 `vae` 時，節點會將圖片編碼為參考潛在變數，並將其附加到 conditioning 輸出。圖片會自動調整尺寸，以維持約 1024x1024 像素的一致處理比例。

## 輸出

| 輸出名 | 說明 | 資料類型 |
| --- | --- | --- |
| `CONDITIONING` | 包含文字 token 及可選參考潛在變數的 conditioning 資料，用於影像生成 | CONDITIONING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeQwenImageEdit/zh-TW.md)

---
**Source fingerprint (SHA-256):** `ec6980a63eab0d6c95be3abea00b2bf3018d30a1267f0b39a21be29a3e9228fe`
