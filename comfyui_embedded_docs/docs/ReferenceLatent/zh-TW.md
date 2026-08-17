# 參考潛在空間

此節點為編輯模型設定引導潛在變量。它接收 conditioning 資料與可選的 latent 輸入，然後修改 conditioning 以納入參考潛在資料資訊。若模型支援，您可以串連多個 ReferenceLatent 節點來設定多張參考圖片。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `conditioning` | 要透過參考潛在資料修改的 conditioning 資料 | CONDITIONING | 是 | - |
| `latent` | 可選的潛在資料，用作編輯模型的參考 | LATENT | 否 | - |

## 輸出

| 輸出名 | 描述 | 資料類型 |
| --- | --- | --- |
| `output` | 包含參考潛在資料的已修改 conditioning 資料 | CONDITIONING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReferenceLatent/zh-TW.md)

---
**Source fingerprint (SHA-256):** `40b02df8ac436480f478fcfa929cc2e13181954507f4bdcd70aade051a25f7d5`
