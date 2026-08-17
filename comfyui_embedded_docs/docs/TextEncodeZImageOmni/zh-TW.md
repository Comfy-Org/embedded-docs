# TextEncodeZImageOmni

TextEncodeZImageOmni 節點是一個進階的 conditioning 節點，可將文字提示與可選的參考圖片編碼為適合影像生成模型的 conditioning 格式。它最多能處理三張圖片，並可選擇使用視覺編碼器和／或 VAE 對圖片進行編碼以產生參考潛在變量，再透過特定的模板結構將這些視覺參考與文字提示整合。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `clip` | 用於對文字提示進行分詞與編碼的 CLIP 模型。 | CLIP | 是 |  |
| `image_encoder` | 可选的視覺編碼器模型。若提供，將用於編碼輸入圖片，並將產生的嵌入加入 conditioning。 | CLIPVision | 否 |  |
| `prompt` | 要編碼的文字提示。此欄位支援多行輸入與動態提示。 | STRING | 是 |  |
| `auto_resize_images` | 啟用時（預設為 True），輸入圖片會先依其像素面積自動調整大小，再傳遞給 VAE 進行編碼。這是進階設定。 | BOOLEAN | 否 |  |
| `vae` | 可选的 VAE 模型。若提供，將用於將輸入圖片編碼為潛在表示，並作為參考潛在變量加入 conditioning。 | VAE | 否 |  |
| `image1` | 第一張可選的參考圖片。 | IMAGE | 否 |  |
| `image2` | 第二張可選的參考圖片。 | IMAGE | 否 |  |
| `image3` | 第三張可選的參考圖片。 | IMAGE | 否 |  |

**注意：** 此節點最多接受三張圖片（`image1`、`image2`、`image3`）。只有在提供至少一張圖片時，才會使用 `image_encoder` 與 `vae` 輸入。當 `auto_resize_images` 為 True 且已連接 `vae` 時，圖片會先調整大小，使總像素面積接近 1024x1024 像素，並將尺寸取為 8 的倍數，然後再進行編碼。若未提供任何圖片，此節點會在沒有任何視覺參考的情況下編碼文字提示。

## 輸出

| 輸出名 | 描述 | 資料類型 |
| --- | --- | --- |
| `CONDITIONING` | 最終的 conditioning 輸出，包含已編碼的文字提示；若提供了圖片，也可能包含已編碼的影像嵌入和／或參考潛在變量。 | CONDITIONING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeZImageOmni/zh-TW.md)

---
**Source fingerprint (SHA-256):** `b40a3150f536b6f37e2b53e6d9992fcb4fd32dceb540c0a76773a7ba1af9a7b8`
