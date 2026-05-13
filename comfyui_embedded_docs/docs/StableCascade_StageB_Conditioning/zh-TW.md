> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_StageB_Conditioning/zh-TW.md)

StableCascade_StageB_Conditioning 節點透過將現有的條件資訊與來自 Stage C 的先驗潛在表示相結合，為 Stable Cascade Stage B 的生成準備條件資料。它修改條件資料以包含來自 Stage C 的潛在樣本，使生成過程能夠利用先驗資訊產生更連貫的輸出。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `條件設定` | CONDITIONING | 是 | - | 將使用 Stage C 先驗資訊修改的條件資料 |
| `stage_c` | LATENT | 是 | - | 來自 Stage C 的潛在表示，包含用於條件化的先驗樣本 |

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `CONDITIONING` | CONDITIONING | 已整合 Stage C 先驗資訊的修改後條件資料 |

---
**Source fingerprint (SHA-256):** `f6ee524889aa324151a91c200fdc2692754cbd1348e32fbc05a26fd7ba27c755`
