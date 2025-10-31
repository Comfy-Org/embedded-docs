> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentApplyOperation/zh-TW.md)

LatentApplyOperation 節點會對潛在樣本套用指定的操作。它接收潛在資料和操作作為輸入，使用提供的操作處理潛在樣本，並返回修改後的潛在資料。此節點可讓您在工作流程中轉換或操作潛在表徵。

## 輸入參數

| 參數名稱 | 資料類型 | 是否必填 | 數值範圍 | 參數說明 |
|-----------|-----------|----------|-------|-------------|
| `樣本` | LATENT | 是 | - | 要透過操作進行處理的潛在樣本 |
| `操作` | LATENT_OPERATION | 是 | - | 要套用至潛在樣本的操作 |

## 輸出結果

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `output` | LATENT | 套用操作後修改完成的潛在樣本 |