> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxKontextMultiReferenceLatentMethod/zh-TW.md)

FluxKontextMultiReferenceLatentMethod 節點透過設定特定的參考潛在空間方法來修改條件化資料。它會將選定的方法附加到條件化輸入中，這會影響後續生成步驟中參考潛在空間的處理方式。此節點標記為實驗性功能，屬於 Flux 條件化系統的一部分。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `conditioning` | CONDITIONING | 是 | - | 要使用參考潛在空間方法修改的條件化資料 |
| `reference_latents_method` | STRING | 是 | `"offset"`<br>`"index"`<br>`"uxo/uno"` | 用於參考潛在空間處理的方法。如果選擇 "uxo" 或 "uso"，將被轉換為 "uxo" |

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `conditioning` | CONDITIONING | 已應用參考潛在空間方法的修改後條件化資料 |