# 參考潛在空間

此節點為編輯模型設定引導潛在空間。它接收條件化資料與可選的潛在輸入，然後修改條件化以包含參考潛在資訊。如果模型支援，您可以串聯多個 ReferenceLatent 節點來設定多個參考影像。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `條件設定` | 將使用參考潛在資訊修改的條件化資料 | CONDITIONING | 是 | - |
| `潛在空間` | 可選的潛在資料，用作編輯模型的參考 | LATENT | 否 | - |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `output` | 包含參考潛在資訊的修改後條件化資料 | CONDITIONING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReferenceLatent/zh-TW.md)

---
**Source fingerprint (SHA-256):** `d233778cfa7d6f057509f93f8445a0bbf151308e430fc50e28577f48cf136b53`
