> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AutogrowPrefixTestNode/zh-TW.md)

AutogrowPrefixTestNode 是一個用於測試自動增長輸入功能的邏輯節點。它接受動態數量的浮點數輸入，將它們的值組合成一個逗號分隔的字串，並輸出該字串。

## 輸入參數

| 參數 | 資料類型 | 必填 | 範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `autogrow` | AUTOGROW | 是 | 1 到 10 個輸入 | 一個動態輸入群組，可以接受 1 到 10 個浮點數值。群組中的每個輸入都是 FLOAT 類型。 |

**注意：** `autogrow` 輸入是一個特殊的動態輸入。您可以向此群組添加多個浮點數輸入，最多可達 10 個。節點將處理所有提供的值。

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `output` | STRING | 一個包含所有輸入浮點數值的單一字串，以逗號分隔。 |
