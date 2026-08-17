# StableCascade 階段 B 條件設定

StableCascade_StageB_Conditioning 節點透過將現有的條件資訊與 Stage C 的先驗潛在表示結合，為 Stable Cascade Stage B 生成準備條件資料。它會修改每個條件條目，以納入 Stage C 的潛在樣本，使生成過程能夠利用先驗資訊來產生更為連貫的輸出。

## 輸入

| 參數 | 描述 | 資料型態 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `conditioning` | 要透過 Stage C 先驗資訊修改的條件資料 | CONDITIONING | 是 | - |
| `stage_c` | 來自 Stage C 的潛在表示，包含用於條件化的先驗樣本 | LATENT | 是 | - |

## 輸出

| 輸出名 | 描述 | 資料型態 |
| --- | --- | --- |
| `CONDITIONING` | 已整合 Stage C 先驗資訊的修改後條件資料 | CONDITIONING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_StageB_Conditioning/zh-TW.md)

---
**Source fingerprint (SHA-256):** `3154457773465e5b93221b6d83d2064b565cb653403e12e88615652c7832d1e8`
