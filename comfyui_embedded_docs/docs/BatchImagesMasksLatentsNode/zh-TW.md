# BatchImagesMasksLatentsNode

批次影像/遮罩/潛在空間節點可將多個相同類型的輸入組合成單一批次。它會自動偵測輸入為影像、遮罩或潛在表示，並使用適當的批次處理方法。此功能有助於準備多個項目，供接受批次輸入的節點進行處理。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `inputs` | 要組合成批次的動態輸入清單。您可以新增 1 到 50 個項目。所有項目必須為相同類型（全部為影像、全部為遮罩或全部為潛在空間）。 | IMAGE、MASK 或 LATENT | 是 | 1 至 50 個輸入 |

**注意：** 節點會根據 `inputs` 清單中的第一個項目自動判斷資料類型（IMAGE、MASK 或 LATENT）。所有後續項目必須與此類型相符。若嘗試混合不同資料類型，節點將會失敗。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `output` | 單一批次輸出。資料類型與輸入類型相符（批次 IMAGE、批次 MASK 或批次 LATENT）。 | IMAGE、MASK 或 LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BatchImagesMasksLatentsNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `6f3037bc00fd8526f42ad2d79a0f27434f58bd6dd0338a585cc707a771ac0989`
