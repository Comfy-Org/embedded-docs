# 參考潛在空間

此節點用於設定編輯模型的引導潛在變量。它接受 conditioning 資料和一個可選的 latent 輸入，然後修改 conditioning 以包含參考潛在資訊。如果模型支援，您可以鏈接多個 ReferenceLatent 節點來設定多個參考影像。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `條件設定` | 要透過參考潛在資訊修改的 conditioning 資料 | CONDITIONING | 是 | - |
| `潛在空間` | 可選的潛在資料，用作編輯模型的參考。如果未提供，則 conditioning 保持不變 | LATENT | 否 | - |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `output` | 包含參考潛在資訊的已修改 conditioning 資料 | CONDITIONING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReferenceLatent/zh-TW.md)

---
**Source fingerprint (SHA-256):** `40b02df8ac436480f478fcfa929cc2e13181954507f4bdcd70aade051a25f7d5`
