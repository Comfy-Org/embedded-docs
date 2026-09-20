# TextEncodeQwenImage21

TextEncodeQwenImage21 節點會為 Qwen-Image 2.1 模型編碼提示詞與負向提示詞，並可選擇附加參考影像。參考影像會由文字編碼器檢視，且當連接 VAE 時，也會編碼為 latent 並拼接至序列中，因此條件化會同時攜帶文字指令與視覺參考。此節點會回傳正向與負向條件化，以及一個尺寸設為第一張參考影像的空 latent，可直接進行取樣。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `clip` | 用於將提示詞分詞與編碼的 Qwen-Image 2.1 文字編碼器。 | CLIP | 是 | - |
| `prompt` | 描述要生成影像或要套用編輯的文字提示詞。支援多行輸入與動態提示詞。 | STRING | 是 | Any text |
| `negative_prompt` | 描述結果應避免什麼的文字提示詞。支援多行輸入與動態提示詞。 | STRING | 是 | Any text |
| `vae` | 用於將參考影像編碼為參考 latent 的 VAE。省略時，參考影像僅透過文字編碼器對結果進行條件化。 | VAE | 否 | - |
| `resolution` | 參考影像會調整為約 `resolution` x `resolution` 像素，並以 32 的倍數為單位，同時保持長寬比。0 會讓每張參考影像維持自身尺寸，並四捨五入為 32 的倍數（預設：1024）。 | INT | 是 | 0 至 4096（步進值 32） |
| `images` | 參考影像，會由文字編碼器檢視，並作為 VAE latent 拼接進序列。可增長插槽：最多可連接 16 張影像（`image_1` ... `image_16`）。 | IMAGE | 否 | 0 至 16 張影像 |

空的 latent 輸出會以第一張已連接的參考影像尺寸為準；若未連接任何參考影像，則以 `resolution` 為準。請在此節點回傳的 latent 尺寸進行取樣：使用任何其他尺寸都會使編輯結果偏移。當連接 VAE 時，相同的參考 latent 會同時附加到正向與負向條件化，因此單一取樣器步驟即可對兩者進行去雜訊。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `positive` | 為提示詞編碼後的條件化；當連接 VAE 時會攜帶參考 latent。 | CONDITIONING |
| `negative` | 為負向提示詞編碼後的條件化，並帶有相同的參考 latent。 | CONDITIONING |
| `latent` | 空 latent，尺寸為第一張參考影像的大小；若未連接參考影像，則為 1024 x 1024。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeQwenImage21/zh-TW.md)

---
**Source fingerprint (SHA-256):** `3870f04597d12b593498c12ca139428af2d717b65aa40c889de9373ae9eb475e`
