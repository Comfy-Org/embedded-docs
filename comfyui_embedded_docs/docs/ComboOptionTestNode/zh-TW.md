> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComboOptionTestNode/zh-TW.md)

ComboOptionTestNode 是一個邏輯節點，用於測試並傳遞下拉式選單的選擇。它接收兩個下拉式選單輸入，每個選單都有一組預先定義的選項，並直接輸出所選的值而不進行修改。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `combo` | COMBO | 是 | `"option1"`<br>`"option2"`<br>`"option3"` | 從三個測試選項組中進行的第一個選擇。 |
| `combo2` | COMBO | 是 | `"option4"`<br>`"option5"`<br>`"option6"` | 從另一組三個測試選項中進行的第二個選擇。 |

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `output_1` | COMBO | 輸出從第一個下拉式選單 (`combo`) 中選擇的值。 |
| `output_2` | COMBO | 輸出從第二個下拉式選單 (`combo2`) 中選擇的值。 |
