# 儲存 LoRA 權重

SaveLoRA 節點會將 LoRA（低秩適應）模型儲存到檔案。它接受 LoRA 模型作為輸入，並將其寫入輸出目錄中的 `.safetensors` 檔案。您可以指定檔名前綴，以及選用的步數，以便加入最終檔案名稱。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `lora` | 要儲存的 LoRA 模型。請勿使用已套用 LoRA 層的模型。 | LORA_MODEL | 是 | N/A |
| `prefix` | 儲存 LoRA 檔案時使用的前綴（預設值："loras/ComfyUI_trained_lora"）。 | STRING | 是 | N/A |
| `steps` | 選用：LoRA 已訓練的步數，用於命名儲存的檔案。 | INT | 否 | N/A |

**注意：** `lora` 輸入必須是純 LoRA 模型。請勿提供已套用 LoRA 層的基礎模型。

**注意：** 檔案會以 `.safetensors` 副檔名儲存在 ComfyUI 輸出目錄中。檔案名稱由 `prefix` 和一個零填充計數器（5 位數）組成，以避免覆寫既有檔案。當提供 `steps` 時，步數也會包含在檔案名稱中（例如，1000 步會顯示為 `1000_steps`）。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| *None* | 此節點不會向工作流程輸出任何資料。它是一個輸出節點，負責將檔案儲存到磁碟。 | N/A |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveLoRA/zh-TW.md)

---
**Source fingerprint (SHA-256):** `02f1d15dd7a5181666f2dbf06c45c07b12c4a178985464e07b5f613bd628f906`
