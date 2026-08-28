# TextEncodeQwenImageEdit

TextEncodeQwenImageEdit 節點將文字提示和可選圖像轉換為 conditioning 資料，用於圖像生成或編輯。它使用 CLIP 模型對輸入進行分詞，並可選擇使用 VAE 將參考圖像編碼為參考 latents。當提供圖像時，它會自動調整大小，以保持一致的處理尺度。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `clip` | 用於文字和圖像分詞的 CLIP 模型 | CLIP | 是 | - |
| `提示詞` | 用於 conditioning 生成的文字提示，支援多行輸入和動態提示 | STRING | 是 | - |
| `vae` | 可選的 VAE 模型，用於將參考圖像編碼為 latents | VAE | 否 | - |
| `圖像` | 可選的輸入圖像，用於參考或編輯目的 | IMAGE | 否 | - |

**注意：** 當提供圖像時，它會被調整大小，使其總像素數保持在接近 1,048,576（1024 × 1024），且僅使用其 RGB 通道。調整大小後的圖像會與提示一起傳遞給 CLIP 分詞器。當同時提供 `image` 和 `vae` 時，節點還會將圖像編碼為參考 latents，並將其附加到 conditioning 輸出。

## 輸出

| 輸出名 | 說明 | 資料類型 |
| --- | --- | --- |
| `CONDITIONING` | 包含文字 tokens 和可選參考 latents 的 conditioning 資料，用於圖像生成 | CONDITIONING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeQwenImageEdit/zh-TW.md)

---
**Source fingerprint (SHA-256):** `ec6980a63eab0d6c95be3abea00b2bf3018d30a1267f0b39a21be29a3e9228fe`
