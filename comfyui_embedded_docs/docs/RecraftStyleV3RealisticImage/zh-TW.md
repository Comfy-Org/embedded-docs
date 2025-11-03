> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftStyleV3RealisticImage/zh-TW.md)

此節點為 Recraft API 建立逼真影像風格配置。它允許您選擇 realistic_image 風格，並從多種子風格選項中選擇以自訂輸出外觀。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 參數說明 |
|-----------|-----------|----------|-------|-------------|
| `substyle` | STRING | 是 | 提供多個選項 | 要應用於 realistic_image 風格的特定子風格。如果設定為 "None"，則不會應用任何子風格。 |

## 輸出結果

| 輸出名稱 | 資料類型 | 輸出說明 |
|-------------|-----------|-------------|
| `recraft_style` | STYLEV3 | 返回包含 realistic_image 風格和所選子風格設定的 Recraft 風格配置物件。 |