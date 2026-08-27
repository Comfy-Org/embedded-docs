# 建立訓練資料集

此節點透過編碼圖像和文字來準備訓練資料。它接收圖像列表和對應的文字標題列表，然後使用 VAE 模型將圖像轉換為潛在表示，並使用 CLIP 模型將文字轉換為 conditioning 資料。產生的成對 latents 和 conditioning 會以列表形式輸出，可直接用於訓練工作流程。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `圖片` | 要編碼的圖像列表。 | IMAGE | 是 | N/A |
| `vae` | 用於將圖像編碼為 latents 的 VAE 模型。 | VAE | 是 | N/A |
| `clip` | 用於將文字編碼為 conditioning 的 CLIP 模型。 | CLIP | 是 | N/A |
| `文字` | 文字標題列表。長度可為 n（與圖像數量相同）、1（對所有圖像重複），或省略（使用空字串）。 | STRING | 否 | 0、1 或 n 個項目（n = 圖像數量） |

**參數約束：**

* `texts` 列表中的項目數量必須為 0、1 或與 `images` 列表中的項目數量完全相符。如果為 0，則所有圖像使用空字串。如果為 1，則該單一文字會重複用於所有圖像。任何其他長度都會引發錯誤。
* 輸出 `latents` 和 `conditioning` 列表的項目數量始終與 `images` 列表相同，因此每個 latent 都與其對應標題的 conditioning 配對。

## 輸出

| 輸出名 | 描述 | 資料類型 |
| --- | --- | --- |
| `latents` | latent 字典列表。 | LATENT |
| `conditioning` | conditioning 列表的列表。 | CONDITIONING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MakeTrainingDataset/zh-TW.md)

---
**Source fingerprint (SHA-256):** `244adc98810a874cfe42f834e89f96da300d883faeb5791dff19607c13d0c0db`
