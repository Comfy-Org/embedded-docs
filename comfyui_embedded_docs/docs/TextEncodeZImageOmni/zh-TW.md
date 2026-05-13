> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeZImageOmni/zh-TW.md)

# TextEncodeZImageOmni 節點

TextEncodeZImageOmni 節點是一個進階條件編碼節點，可將文字提示與可選的參考影像編碼為適合影像生成模型的條件格式。它能處理最多三張影像，可選擇使用視覺編碼器和/或 VAE 進行編碼以產生參考潛在表示，並使用特定的模板結構將這些視覺參考與文字提示整合。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `clip` | CLIP | 是 | | 用於標記化和編碼文字提示的 CLIP 模型。 |
| `image_encoder` | CLIPVision | 否 | | 可選的視覺編碼器模型。如果提供，將用於編碼輸入影像，所產生的嵌入將被添加到條件中。 |
| `prompt` | STRING | 是 | | 要編碼的文字提示。此欄位支援多行輸入和動態提示。 |
| `auto_resize_images` | BOOLEAN | 否 | | 啟用時（預設：True），輸入影像將根據其像素面積自動調整大小，然後再傳遞給 VAE 進行編碼。 |
| `vae` | VAE | 否 | | 可選的 VAE 模型。如果提供，將用於將輸入影像編碼為潛在表示，這些表示將作為參考潛在變量添加到條件中。 |
| `image1` | IMAGE | 否 | | 第一個可選的參考影像。 |
| `image2` | IMAGE | 否 | | 第二個可選的參考影像。 |
| `image3` | IMAGE | 否 | | 第三個可選的參考影像。 |

**注意：** 此節點最多可接受三張影像（`image1`、`image2`、`image3`）。`image_encoder` 和 `vae` 輸入僅在至少提供一張影像時才會被使用。當 `auto_resize_images` 為 True 且連接了 `vae` 時，影像會在編碼前調整大小，使其總像素面積接近 1024x1024。

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `CONDITIONING` | CONDITIONING | 最終的條件輸出，包含編碼後的文字提示，如果提供了影像，還可能包含編碼後的影像嵌入和/或參考潛在變量。 |

---
**Source fingerprint (SHA-256):** `daa4205acdf72503180eeedb4142708d239d4ff0f689012a298264ae2d8ea949`
