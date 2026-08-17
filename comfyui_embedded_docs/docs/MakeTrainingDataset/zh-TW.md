# 建立訓練資料集

此節點透過編碼圖片和文字來準備訓練資料。它接收圖片列表及對應的文字說明列表，然後使用 VAE 模型將圖片轉換為潛在表示，並使用 CLIP 模型將文字轉換為條件資料。產生的成對潛在表示與條件資料會以列表形式輸出，可供訓練工作流程使用。

## 輸入
| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `images` | 要編碼的圖片列表。 | IMAGE | 是 | N/A |
| `vae` | 用於將圖片編碼為潛在表示的 VAE 模型。 | VAE | 是 | N/A |
| `clip` | 用於將文字編碼為條件資料的 CLIP 模型。 | CLIP | 是 | N/A |
| `texts` | 文字說明列表。長度可為 n（與圖片數量匹配）、1（對所有圖片重複使用），或省略（使用空字串）。 | STRING | 否 | N/A |

**參數約束：**

`texts` 列表中的項目數量必須為 0、1，或與 `images` 列表中的項目數量完全相符。若為 0，則所有圖片使用空字串；若為 1，則該單一文字會對所有圖片重複使用；若為其他數量，節點會產生錯誤。

## 輸出
| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `latents` | 潛在字典列表。 | LATENT |
| `conditioning` | 條件列表的列表。 | CONDITIONING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MakeTrainingDataset/zh-TW.md)

---
**Source fingerprint (SHA-256):** `244adc98810a874cfe42f834e89f96da300d883faeb5791dff19607c13d0c0db`
