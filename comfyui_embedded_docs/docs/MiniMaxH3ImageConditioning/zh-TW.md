# MiniMax H3 Image Conditioning

使用 MiniMax H3 Image 將提示詞轉換為 conditioning，並為靜態影像產生空的 latent。未連接影像時即為文字生圖；連接影像後則會編輯這些影像，而提示詞會以 `<Picture 1>`、`<Picture 2>` 等形式引用它們。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `clip` | MiniMax H3 Image 的 CLIP 模型，會將提示詞與任何參考影像一併進行 tokenize，並編碼 conditioning。 | CLIP | 是 | - |
| `vae` | MiniMax H3 Image 的 VAE。提供此項時，影像也會被錨定為參考 latent；未提供時，影像僅用於調節文字編碼器。 | VAE | 否 | - |
| `prompt` | 要生成的內容，或如何編輯參考影像。 | STRING | 是 | 多行文字 |
| `width` | 輸出寬度（像素）。設為 0 時使用 `image_1` 經參考縮放後的寬度；若無影像則使用 2048。預設：0。 | INT | 是 | 0 至 MAX_RESOLUTION（步進值：32） |
| `height` | 輸出高度（像素）。設為 0 時使用 `image_1` 經參考縮放後的高度；若無影像則使用 2048。預設：0。 | INT | 是 | 0 至 MAX_RESOLUTION（步進值：32） |
| `images` | 可增長的參考影像群組，從 `image_1` 開始往上；`image_1` 是要編輯的影像。提示詞會以 `<Picture n>` 引用它們。 | AUTOGROW | 否 | 0 至 100 張影像 |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `positive` | 供 MiniMax H3 Image 取樣器使用的 conditioning，連接影像時會一併附上參考 latent。 | CONDITIONING |
| `latent` | 單張影像的空 latent，24 個通道，尺寸為輸出大小的十六分之一。 | LATENT |

注意：模型的調校基準為 2048x2048 像素的面積，因此除非需要不同的畫布，請將 `width` 與 `height` 保持為 0。

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MiniMaxH3ImageConditioning/zh-TW.md)

---
**Source fingerprint (SHA-256):** `b0927bbc44ac82e8a23b1edb5470c0cc8945844c326a352d75495ed801d11b1d`
