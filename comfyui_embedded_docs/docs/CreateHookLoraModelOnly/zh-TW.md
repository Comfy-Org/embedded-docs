> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateHookLoraModelOnly/zh-TW.md)

此節點建立一個僅應用於模型組件的 LoRA（低秩適應）掛鉤，讓您能夠修改模型行為而不影響 CLIP 組件。它會載入 LoRA 檔案並以指定的強度應用於模型，同時保持 CLIP 組件不變。此節點可與先前的掛鉤鏈結，以建立複雜的修改管線。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `lora_name` | STRING | 是 | 提供多個選項 | 要從 loras 資料夾載入的 LoRA 檔案名稱 |
| `strength_model` | FLOAT | 是 | -20.0 至 20.0 | 應用 LoRA 到模型組件的強度乘數（預設值：1.0） |
| `prev_hooks` | HOOKS | 否 | - | 可選的先前掛鉤，可與此掛鉤鏈結 |

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `hooks` | HOOKS | 建立的 LoRA 掛鉤，可應用於模型處理 |