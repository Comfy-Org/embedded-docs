> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateHookLoraModelOnly/zh-TW.md)

此節點建立一個僅套用於模型元件的 LoRA（低秩適應）掛鉤，完全保留 CLIP 元件不變。它會載入 LoRA 檔案，並以指定的強度套用至模型，同時將 CLIP 強度設為零。此節點可與先前的掛鉤串聯，以建構複雜的修改流程。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `lora_name` | STRING | 是 | 提供多個選項 | 要從 loras 資料夾載入的 LoRA 檔案名稱 |
| `strength_model` | FLOAT | 是 | -20.0 至 20.0 | 將 LoRA 套用至模型元件的強度乘數（預設值：1.0） |
| `prev_hooks` | HOOKS | 否 | - | 可選的先前的掛鉤，用於與此掛鉤串聯 |

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `hooks` | HOOKS | 已建立的 LoRA 掛鉤，可套用至模型處理流程 |

---
**Source fingerprint (SHA-256):** `10adbdfc2e37fcf317e93130f87d9a7038d00b091cb6d1b45f4658c81632ef80`
