# TextEncodeZImageOmni

TextEncodeZImageOmni 會將文字提示與最多三張可選參考圖像一起編碼為圖像生成模型使用的 conditioning 格式。提示會以 CLIP 模型進行分詞並編碼，而每張已連接的圖像可選擇性地經由視覺編碼器與/或 VAE 處理，使視覺參考能與文字一同嵌入。此節點被標記為實驗性。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `clip` | 用於對文字提示進行分詞和編碼的 CLIP 模型。 | CLIP | 是 |  |
| `圖像編碼器` | 可選的視覺編碼器模型。若提供，則用於編碼輸入圖像，並將產生的嵌入添加到 conditioning 中。 | CLIP_VISION | 否 |  |
| `提示詞` | 要編碼的文字提示。支援多行輸入和動態提示。 | STRING | 是 |  |
| `自動調整圖像尺寸` | 啟用時（預設：True），輸入圖像會在 VAE 編碼前自動調整大小，使其總畫素面積接近 1024x1024，且尺寸四捨五入為 8 的倍數。 | BOOLEAN | 否 | True<br>False |
| `vae` | 可選的 VAE 模型。若提供，則用於將輸入圖像編碼為潛在表示，並作為參考潛在表示添加到 conditioning 中。 | VAE | 否 |  |
| `圖像1` | 第一張可選參考圖像。 | IMAGE | 否 |  |
| `圖像2` | 第二張可選參考圖像。 | IMAGE | 否 |  |
| `圖像3` | 第三張可選參考圖像。 | IMAGE | 否 |  |

**注意：** 此節點最多接受三張圖像（`image1`、`image2`、`image3`）。僅在至少提供一張圖像時，才會使用 `image_encoder` 和 `vae` 輸入；當兩者都連接時，每張圖像會同時由兩者處理。當 `auto_resize_images` 為 True 且已連接 `vae` 時，圖像在編碼前會調整大小，使總畫素面積接近 1024x1024。

## 輸出

| 輸出名 | 描述 | 資料類型 |
| --- | --- | --- |
| `CONDITIONING` | 最終的 conditioning 輸出。它包含編碼後的文字提示；當提供圖像時，也可能包含編碼後的圖像嵌入、參考潛在表示，以及從圖像佔位符模板衍生的額外文字嵌入。 | CONDITIONING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeZImageOmni/zh-TW.md)

---
**Source fingerprint (SHA-256):** `b40a3150f536b6f37e2b53e6d9992fcb4fd32dceb540c0a76773a7ba1af9a7b8`
