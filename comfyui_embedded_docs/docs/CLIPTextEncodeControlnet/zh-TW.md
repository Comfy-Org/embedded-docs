> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeControlnet/zh-TW.md)

CLIPTextEncodeControlnet 節點使用 CLIP 模型處理文字輸入，並將其與現有的條件資料結合，為 controlnet 應用創建增強的條件輸出。它會將輸入文字進行標記化處理，透過 CLIP 模型進行編碼，並將產生的嵌入向量作為 cross-attention controlnet 參數添加到提供的條件資料中。

## 輸入參數

| 參數名稱 | 資料類型 | 輸入類型 | 預設值 | 範圍 | 描述 |
|-----------|-----------|------------|---------|-------|-------------|
| `clip` | CLIP | 必填 | - | - | 用於文字標記化和編碼的 CLIP 模型 |
| `conditioning` | CONDITIONING | 必填 | - | - | 將透過 controlnet 參數增強的現有條件資料 |
| `text` | STRING | 多行文字，動態提示詞 | - | - | 由 CLIP 模型處理的文字輸入 |

**注意：** 此節點需要同時提供 `clip` 和 `conditioning` 輸入才能正常運作。`text` 輸入支援動態提示詞和多行文字，以實現靈活的文字處理。

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `CONDITIONING` | CONDITIONING | 帶有新增 controlnet cross-attention 參數的增強條件資料 |