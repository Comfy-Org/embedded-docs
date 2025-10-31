> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/T5TokenizerOptions/zh-TW.md)

T5TokenizerOptions 節點允許您為各種 T5 模型類型配置標記化器設定。它為多個 T5 模型變體（包括 t5xxl、pile_t5xl、t5base、mt5xl 和 umt5xxl）設定最小填充和最小長度參數。該節點接收 CLIP 輸入，並返回應用指定標記化器選項的修改後 CLIP。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `clip` | CLIP | 是 | - | 要配置標記化器選項的 CLIP 模型 |
| `最小填充` | INT | 否 | 0-10000 | 為所有 T5 模型類型設定的最小填充值（預設值：0） |
| `最小長度` | INT | 否 | 0-10000 | 為所有 T5 模型類型設定的最小長度值（預設值：0） |

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `output` | CLIP | 已更新標記化器選項的修改後 CLIP 模型，所有 T5 變體均已應用更新 |