# 參考潛在空間

此節點為編輯模型設定引導 latent。它接收 conditioning 資料與可選的 latent 輸入，然後修改 conditioning 以納入參考 latent 資訊。若模型支援，你可以串接多個 Set Reference Latent 節點來設定多張參考影像。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `條件設定` | 要使用參考 latent 資訊修改的 conditioning 資料 | CONDITIONING | 是 | - |
| `潛在空間` | 可選的 latent 資料，用作編輯模型的參考。若未提供，則會原樣返回 conditioning | LATENT | 否 | - |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `output` | 包含參考 latent 資訊的修改後 conditioning 資料 | CONDITIONING |

## 備註

- 參考 latent 會以樣本張量清單的形式儲存，因此依序連接多個 Set Reference Latent 節點時，會附加額外的參考，而不是取代先前的參考。
- 當未連接 `latent` 時，此節點會將傳入的 `conditioning` 原樣傳遞，不做任何變更。

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReferenceLatent/zh-TW.md)

---
**Source fingerprint (SHA-256):** `40b02df8ac436480f478fcfa929cc2e13181954507f4bdcd70aade051a25f7d5`
