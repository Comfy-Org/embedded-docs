# TextEncodeFibo2

將 Fibo 2.0 提示詞編碼為 conditioning 與相符的空 latent。提示詞可以是純文字或結構化 JSON 描述文字；連接圖片後，它會成為編輯指令，或成為結果的 JSON 描述文字，並在 `edit_instruction` 鍵中描述變更；當連接 VAE 時，這些圖片會作為兩個輸出的參考 latent。對 `latent` 輸出進行取樣，其尺寸即為圖片被裁切成的尺寸。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `clip` | 用於將提示詞分詞並編碼的 Fibo 2.0 文字編碼器。 | CLIP | 是 | - |
| `prompt` | 要據以生成的描述文字；連接圖片時則為編輯指令。請以 `<image_1>`、`<image_2>` 等方式指稱圖片。也可以使用預期結果的 JSON 描述文字，並在其 `edit_instruction` 鍵中描述變更。 | STRING | 是 | - |
| `negative_prompt` | 要避開的描述文字，會編碼為負向 conditioning。空值則為 Fibo 2.0 在無分類器引導（classifier-free guidance）訓練時所使用的空描述文字（預設：空）。 | STRING | 是 | - |
| `vae` | 用於將圖片編碼為參考 latent 的 VAE。若未提供，圖片僅會影響文字編碼。 | VAE | 否 | - |
| `images` | 要編輯的圖片，最多 16 張。單張圖片會縮放並置中裁切至結果尺寸，因為編輯會與其逐像素對齊；多張圖片則各自縮放至其訓練尺寸。 | IMAGE | 否 | 0 至 16 張影像 |
| `width` | 結果寬度，會向下取整至 16 的倍數。0 會使用 Fibo 2.0 依第一張圖片長寬比所訓練的尺寸，約 1 百萬像素；沒有圖片時則為 1024（預設：0）。 | INT | 是 | 0 至 16384 （步進值：16） |
| `height` | 結果高度，會向下取整至 16 的倍數。0 會使用 Fibo 2.0 依第一張圖片長寬比所訓練的尺寸，約 1 百萬像素；沒有圖片時則為 1024（預設：0）。 | INT | 是 | 0 至 16384 （步進值：16） |
| `batch_size` | 批次中要建立的 latent 數量（預設：1）。 | INT | 是 | 1 至 4096 |

參考 latent 會附加到兩個輸出，因此圖片會隨 conditioning 一起傳遞，而不只隨正向分支傳遞。未連接 VAE 時，圖片只會提供給文字編碼器，且不會加入任何參考 latent。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `positive` | 提示詞的 conditioning；當連接 VAE 與圖片時，會附帶參考 latent。 | CONDITIONING |
| `negative` | `negative_prompt` 的 conditioning，僅含文字，並附帶相同的參考 latent。 | CONDITIONING |
| `latent` | 所要求尺寸的空 latent，可直接取樣。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeFibo2/zh-TW.md)

---
**Source fingerprint (SHA-256):** `f400d041a3dd224e30c0fa2acc803e3de11d6c10654bde122e8d569fa1cd1d79`
