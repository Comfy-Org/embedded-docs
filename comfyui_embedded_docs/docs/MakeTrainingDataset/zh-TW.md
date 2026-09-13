# 建立訓練資料集

此節點透過編碼影像與文字來準備訓練資料。它接收一組影像列表與對應的文字標註列表，接著使用 VAE 模型將影像轉換為 latent 表示，並使用 CLIP 模型將文字轉換為 conditioning 資料。產生的成對 latents 與 conditioning 會以列表形式輸出，可直接用於訓練工作流程。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `圖片` | 要編碼的影像列表。 | IMAGE | 是 | N/A |
| `vae` | 用於將影像編碼為 latents 的 VAE 模型。 | VAE | 是 | N/A |
| `clip` | 用於將文字編碼為 conditioning 的 CLIP 模型。 | CLIP | 是 | N/A |
| `文字` | 文字標註列表。長度可為 n（與影像數量相符）、1（重複套用於所有影像），或省略（使用空字串）。 | STRING | 否 | 0, 1, or n items (n = number of images) |

**參數限制：**

* 此節點使用列表輸入：`images` 與 `texts` 會以列表處理，而 `vae` 與 `clip` 各自接受單一模型（使用所提供列表的第一個項目）。
* `texts` 列表中的項目數量必須為 0、1，或與 `images` 列表中的項目數量完全相同。若為 0 或省略，則所有影像都會使用空字串。若為 1，則該單一文字會重複套用至所有影像。任何其他長度都會引發錯誤。
* 輸出的 `latents` 與 `conditioning` 列表一律會包含與 `images` 列表相同數量的項目，因此每個 latent 都會與其對應標註的 conditioning 配對。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `latents` | latent 字典的列表。 | LATENT |
| `conditioning` | conditioning 列表的列表。 | CONDITIONING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MakeTrainingDataset/zh-TW.md)

---
**Source fingerprint (SHA-256):** `244adc98810a874cfe42f834e89f96da300d883faeb5791dff19607c13d0c0db`
