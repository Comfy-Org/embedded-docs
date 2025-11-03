> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateHookModelAsLoraModelOnly/zh-TW.md)

此節點建立一個掛鉤，該掛鉤應用 LoRA（低秩適應）模型來僅修改神經網路的模型組件。它載入一個檢查點檔案，並以指定的強度將其應用於模型，同時保持 CLIP 組件不變。這是一個實驗性節點，擴展了基礎 CreateHookModelAsLora 類別的功能。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `ckpt_name` | STRING | 是 | 提供多個選項 | 要作為 LoRA 模型載入的檢查點檔案。可用選項取決於 checkpoints 資料夾的內容。 |
| `strength_model` | FLOAT | 是 | -20.0 至 20.0 | 應用 LoRA 到模型組件的強度乘數（預設值：1.0） |
| `prev_hooks` | HOOKS | 否 | - | 可選的先前掛鉤，用於與此掛鉤鏈接 |

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `hooks` | HOOKS | 建立的掛鉤群組，包含 LoRA 模型修改 |