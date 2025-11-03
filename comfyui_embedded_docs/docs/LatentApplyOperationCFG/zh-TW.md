> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentApplyOperationCFG/zh-TW.md)

LatentApplyOperationCFG 節點透過對潛在表示應用操作來修改模型中的條件引導過程。該節點在分類器自由引導（CFG）採樣過程中攔截條件輸出，並在潛在表示用於生成之前對其應用指定操作。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 參數說明 |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | 是 | - | 將要應用 CFG 操作的模型 |
| `operation` | LATENT_OPERATION | 是 | - | 在 CFG 採樣過程中要應用的潛在操作 |

## 輸出結果

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `model` | MODEL | 已在其採樣過程中應用 CFG 操作的修改後模型 |