> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeLumina2/zh-TW.md)

此節點使用 CLIP 模型將系統提示和使用者提示編碼為嵌入向量，可用於引導擴散模型生成特定圖像。它將預定義的系統提示與您的自訂文字提示相結合，並透過 CLIP 模型進行處理，以創建用於圖像生成的條件化資料。

## 輸入參數

| 參數名稱 | 資料類型 | 輸入類型 | 預設值 | 數值範圍 | 描述 |
|-----------|-----------|------------|---------|-------|-------------|
| `system_prompt` | STRING | COMBO | - | "superior", "alignment" | Lumina2 提供兩種類型的系統提示：Superior：您是一個旨在根據文字提示或使用者提示生成具有卓越圖文對齊度的優質圖像的助手。Alignment：您是一個旨在根據文字提示生成具有最高圖文對齊度的高品質圖像的助手。 |
| `user_prompt` | STRING | STRING | - | - | 要進行編碼的文字內容。 |
| `clip` | CLIP | CLIP | - | - | 用於文字編碼的 CLIP 模型。 |

**注意：** `clip` 輸入為必需參數且不能為 None。如果 clip 輸入無效，節點將報錯提示檢查點可能不包含有效的 CLIP 或文字編碼器模型。

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `CONDITIONING` | CONDITIONING | 包含嵌入文字的條件化資料，用於引導擴散模型。 |