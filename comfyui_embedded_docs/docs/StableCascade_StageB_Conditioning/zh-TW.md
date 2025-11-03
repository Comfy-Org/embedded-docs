> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_StageB_Conditioning/zh-TW.md)

StableCascade_StageB_Conditioning 節點透過將現有的調節資訊與來自 Stage C 的先驗潛在表示相結合，為 Stable Cascade Stage B 生成準備調節資料。它修改調節資料以包含來自 Stage C 的潛在樣本，使生成過程能夠利用先驗資訊來產生更連貫的輸出。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `conditioning` | CONDITIONING | 是 | - | 將使用 Stage C 先驗資訊進行修改的調節資料 |
| `stage_c` | LATENT | 是 | - | 來自 Stage C 的潛在表示，包含用於調節的先驗樣本 |

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `CONDITIONING` | CONDITIONING | 已整合 Stage C 先驗資訊的修改後調節資料 |