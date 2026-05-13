> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveLoRA/zh-TW.md)

## 概述

SaveLoRA 節點可將 LoRA（低秩適應）模型儲存為檔案。它接收 LoRA 模型作為輸入，並將其寫入輸出目錄中的 `.safetensors` 檔案。您可以指定檔案名稱前綴，以及可選的步數（step count）以包含在最終檔案名稱中。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `lora` | LORA_MODEL | 是 | 不適用 | 要儲存的 LoRA 模型。請勿使用已套用 LoRA 層的模型。 |
| `prefix` | STRING | 是 | 不適用 | 用於已儲存 LoRA 檔案的前綴（預設值："loras/ComfyUI_trained_lora"）。 |
| `steps` | INT | 否 | 不適用 | 可選：LoRA 已訓練的步數，用於命名已儲存的檔案。 |

**注意：** `lora` 輸入必須是純粹的 LoRA 模型。請勿提供已套用 LoRA 層的基礎模型。

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| *無* | 不適用 | 此節點不會向工作流程輸出任何資料。它是一個輸出節點，負責將檔案儲存至磁碟。 |

---
**Source fingerprint (SHA-256):** `e68a449d741c908f23fc1585d848254d78c310ad19efbd139c33c9ddef3145c7`
