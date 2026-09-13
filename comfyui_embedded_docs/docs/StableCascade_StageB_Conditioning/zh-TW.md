# StableCascade 階段 B 條件設定

StableCascade_StageB_Conditioning 節點會將現有的條件資料與 Stage C 產生的先驗潛在表示結合，藉此為 Stable Cascade Stage B 生成準備條件資料。它會複製每個條件項目，並將 Stage C 的潛在樣本存入其中，以便後續生成步驟能使用這項先驗資訊，獲得更連貫的結果。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `條件設定` | 要使用 Stage C 先驗資訊修改的條件資料。列表中的每個項目都會被複製，並加入 Stage C 的樣本。 | CONDITIONING | 是 | - |
| `stage_c` | Stage C 的潛在表示。其 `samples` 值會作為先驗資訊加入條件資料中。 | LATENT | 是 | - |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `CONDITIONING` | 已整合 Stage C 先驗資訊的修改後條件資料。 | CONDITIONING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_StageB_Conditioning/zh-TW.md)

---
**Source fingerprint (SHA-256):** `3154457773465e5b93221b6d83d2064b565cb653403e12e88615652c7832d1e8`
