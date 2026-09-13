# TextEncodeZImageOmni

TextEncodeZImageOmni 會將文字提示詞以及最多三張可選的參考影像，編碼成供影像生成模型使用的條件格式。提示詞會透過 CLIP 模型進行分詞與編碼，而每個已連接的影像可選擇性地由視覺編碼器和/或 VAE 處理，使視覺參考能與文字一併嵌入。此節點標記為實驗性。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `clip` | 用於將文字提示詞分詞與編碼的 CLIP 模型。 | CLIP | 是 |  |
| `圖像編碼器` | 可選的視覺編碼器模型。若提供，會用於編碼輸入影像，並將產生的嵌入加入條件中。 | CLIP_VISION | 否 |  |
| `提示詞` | 要編碼的文字提示詞。支援多行輸入與動態提示詞。 | STRING | 是 |  |
| `自動調整圖像尺寸` | 啟用時（預設：True），輸入影像會在 VAE 編碼前自動調整大小，使其總像素面積接近 1024x1024，且尺寸會取整為 8 的倍數。 | BOOLEAN | 是 | True<br>False |
| `vae` | 可選的 VAE 模型。若提供，會用於將輸入影像編碼為潛在表示，並以參考潛在表示的形式加入條件中。 | VAE | 否 |  |
| `圖像1` | 第一張可選的參考影像。 | IMAGE | 否 |  |
| `圖像2` | 第二張可選的參考影像。 | IMAGE | 否 |  |
| `圖像3` | 第三張可選的參考影像。 | IMAGE | 否 |  |

**注意：** 此節點最多接受三張影像（`image1`、`image2`、`image3`）。`image_encoder` 和 `vae` 輸入僅在至少提供一張影像時才會使用；當兩者皆連接時，每張影像都會由兩者處理。當 `auto_resize_images` 為 True 且連接了 `vae` 時，影像會在編碼前調整大小，使其總像素面積接近 1024x1024。若未提供任何影像，則只會編碼文字提示詞。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `CONDITIONING` | 最終的條件輸出。它包含已編碼的文字提示詞；當提供影像時，可能包含已編碼的影像嵌入、參考潛在表示，以及衍生自影像佔位符範本的額外文字嵌入。 | CONDITIONING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeZImageOmni/zh-TW.md)

---
**Source fingerprint (SHA-256):** `b40a3150f536b6f37e2b53e6d9992fcb4fd32dceb540c0a76773a7ba1af9a7b8`
