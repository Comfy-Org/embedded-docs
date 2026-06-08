此節點透過編碼影像和文字來準備訓練資料。它接收一組影像列表及對應的文字說明列表，然後使用 VAE 模型將影像轉換為潛在表示，並使用 CLIP 模型將文字轉換為條件資料。產生的配對潛在資料和條件資料會以列表形式輸出，可直接用於訓練工作流程。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `圖片` | 要編碼的影像列表。 | IMAGE | 是 | N/A |
| `vae` | 用於將影像編碼為潛在表示的 VAE 模型。 | VAE | 是 | N/A |
| `clip` | 用於將文字編碼為條件資料的 CLIP 模型。 | CLIP | 是 | N/A |
| `文字` | 文字說明列表。長度可為 n（與影像數量相符）、1（套用至所有影像），或省略（使用空字串）。 | STRING | 否 | N/A |

**參數限制：**

* `texts` 列表中的項目數量必須為 0、1，或與 `images` 列表中的項目數量完全相符。若為 0，則所有影像使用空字串。若為 1，則該單一文字會套用至所有影像。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `conditioning` | 潛在字典列表。 | LATENT |
| `conditioning` | 條件列表列表。 | CONDITIONING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MakeTrainingDataset/zh-TW.md)

---
**Source fingerprint (SHA-256):** `95947c03f140f527f3db54d0b0131d956646055542ddb546ae5eaa82e4e8cefa`
