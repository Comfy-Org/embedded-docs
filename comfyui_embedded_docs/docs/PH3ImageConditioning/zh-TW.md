# p-h3-image Conditioning

此節點會使用 p-h3-image 將提示詞轉換為 conditioning，並為單張靜態影像產生空白 latent。未連接影像時，即為文字轉影像；連接影像後，`image_1` 是正在編輯的影像，其他插槽則作為參考，提示詞會以 `<Picture 1>`、`<Picture 2>` 等方式指稱這些參考影像。取樣器需要一個由 MiniMax H3 sigma shift 節點修補過的模型，且兩個 shift 值都設為 1.0。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `clip` | 用於將提示詞（包括任何參考影像）分詞，並編碼 conditioning 的 p-h3-image CLIP 模型。 | CLIP | 是 | - |
| `prompt` | 要生成什麼，或如何編輯 `image_1`。連接影像時，簡短指令前方會加上 `Edit <Picture 1>. `。若指令已以 `Edit <Picture` 開頭，或是由提示詞放大器（prompt upsampler）產生的編輯簡述，則會完全照原樣使用。 | STRING | 是 | - |
| `width` | 輸出寬度（像素）。0 會使用縮放後 `image_1` 的寬度；未連接影像時則使用 2912（預設：0）。 | INT | 是 | 0 至 MAX_RESOLUTION |
| `height` | 輸出高度（像素）。0 會使用縮放後 `image_1` 的高度；未連接影像時則使用 2912（預設：0）。 | INT | 是 | 0 至 MAX_RESOLUTION |
| `vae` | p-h3-image 的 VAE。一旦連接影像插槽就必填，因為參考 latent 會用它來編碼。 | VAE | 否 | - |
| `images` | 最多 9 張影像的可增長群組，包含 `image_1` 到 `image_9`。`image_1` 是正在編輯的影像，其餘插槽為參考影像。 | AUTOGROW | 否 | 0 至 9 張影像 |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `positive` | 供 p-h3-image 取樣器使用的 conditioning。連接影像時，也會攜帶打包後的參考 latent。 | CONDITIONING |
| `latent` | 單一靜態影格的空白 latent，包含模型預期的兩個音訊 latent。 | LATENT |

**注意：** 影像需要 `vae` 輸入。若連接影像但沒有 VAE 就執行此節點，會引發錯誤。

**注意：** conditioning 僅涵蓋單一影格。若要用於影片或音訊，請改用 MiniMax H3 影片節點。

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PH3ImageConditioning/zh-TW.md)

---
**Source fingerprint (SHA-256):** `f1f5e5b2d3ff9bc2f3b81f3d0dd722e725c7930c6f95bf44ad83bc64357d2fb7`
