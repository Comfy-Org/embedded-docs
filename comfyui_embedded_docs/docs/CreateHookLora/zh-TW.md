> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateHookLora/zh-TW.md)

Create Hook LoRA 節點會生成掛鉤物件，用於對模型應用 LoRA（低秩適應）修改。它會載入指定的 LoRA 檔案並建立可調整模型和 CLIP 強度的掛鉤，然後將這些掛鉤與傳遞給它的任何現有掛鉤合併。該節點透過快取先前載入的 LoRA 檔案來有效管理 LoRA 載入，避免重複操作。

## 輸入參數

| 參數名稱 | 資料類型 | 是否必填 | 數值範圍 | 參數說明 |
|-----------|-----------|----------|-------|-------------|
| `lora_name` | STRING | 是 | 提供多個選項 | 要從 loras 目錄載入的 LoRA 檔案名稱 |
| `strength_model` | FLOAT | 是 | -20.0 至 20.0 | 模型調整的強度乘數（預設值：1.0） |
| `strength_clip` | FLOAT | 是 | -20.0 至 20.0 | CLIP 調整的強度乘數（預設值：1.0） |
| `prev_hooks` | HOOKS | 否 | 不適用 | 可選的現有掛鉤群組，將與新的 LoRA 掛鉤合併 |

**參數限制條件：**

- 如果 `strength_model` 和 `strength_clip` 均設為 0，節點將跳過建立新的 LoRA 掛鉤並直接返回未變更的現有掛鉤
- 節點會快取最後載入的 LoRA 檔案，以便在重複使用相同 LoRA 時優化效能

## 輸出結果

| 輸出名稱 | 資料類型 | 輸出說明 |
|-------------|-----------|-------------|
| `HOOKS` | HOOKS | 包含合併後的 LoRA 掛鉤及任何先前掛鉤的掛鉤群組 |