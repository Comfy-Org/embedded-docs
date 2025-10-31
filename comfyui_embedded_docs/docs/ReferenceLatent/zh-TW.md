> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReferenceLatent/zh-TW.md)

此節點為編輯模型設定引導潛在變數。它接收條件化資料和一個可選的潛在輸入，然後修改條件化以包含參考潛在資訊。如果模型支援，您可以串聯多個 ReferenceLatent 節點來設定多個參考影像。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `conditioning` | CONDITIONING | 是 | - | 將被修改以包含參考潛在資訊的條件化資料 |
| `latent` | LATENT | 否 | - | 可選的潛在資料，用作編輯模型的參考 |

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `output` | CONDITIONING | 包含參考潛在資訊的修改後條件化資料 |