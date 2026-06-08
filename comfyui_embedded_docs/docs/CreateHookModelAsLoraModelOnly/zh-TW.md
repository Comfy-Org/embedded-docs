此節點建立一個鉤子，將 LoRA（低秩適應）模型應用於神經網路的模型組件。它會載入一個檢查點檔案，並以指定的強度將其應用於模型，同時保持 CLIP 組件不變。這是一個實驗性節點，擴展了基礎 CreateHookModelAsLora 類別的功能。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `ckpt_name` | 要作為 LoRA 模型載入的檢查點檔案。可用選項取決於檢查點資料夾的內容。 | STRING | 是 | 提供多個選項 |
| `strength_model` | 將 LoRA 應用於模型組件的強度乘數（預設值：1.0） | FLOAT | 是 | -20.0 至 20.0 |
| `prev_hooks` | 可選的先前鉤子，用於與此鉤子串聯 | HOOKS | 否 | - |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `hooks` | 包含 LoRA 模型修改的已建立鉤子群組 | HOOKS |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateHookModelAsLoraModelOnly/zh-TW.md)

---
**Source fingerprint (SHA-256):** `adbeaede65aa89d48c59225ca1c8edc4c9394a364f93a00dae4a83a2270f093b`
