> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/T5TokenizerOptions/zh-TW.md)

T5TokenizerOptions 節點可讓您為各種 T5 模型類型配置標記化器設定。它為多種 T5 模型變體（包括 t5xxl、pile_t5xl、t5base、mt5xl 和 umt5xxl）設定最小填充和最小長度參數。該節點接收 CLIP 輸入並返回應用指定標記化器選項的修改後 CLIP。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 參數說明 |
|-----------|-----------|----------|-------|-------------|
| `clip` | CLIP | 是 | - | 要配置標記化器選項的 CLIP 模型 |
| `min_padding` | INT | 否 | 0-10000 | 為所有 T5 模型類型設定的最小填充值（預設值：0） |
| `min_length` | INT | 否 | 0-10000 | 為所有 T5 模型類型設定的最小長度值（預設值：0） |

## 輸出結果

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `output` | CLIP | 已更新標記化器選項的修改後 CLIP 模型，適用於所有 T5 變體 |