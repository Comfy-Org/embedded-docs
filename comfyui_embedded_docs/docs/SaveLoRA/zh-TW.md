# 儲存 LoRA 權重

SaveLoRA 節點會將 LoRA（Low-Rank Adaptation）模型儲存至檔案。它接收 LoRA 模型作為輸入，並將其寫入輸出目錄中的 `.safetensors` 檔案。您可以指定檔名前綴，以及選擇性加入最終檔名中的步數計數。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `lora` | 要儲存的 LoRA 模型。請勿使用已套用 LoRA 層的模型。 | LORA_MODEL | 是 | N/A |
| `prefix` | 用於已儲存 LoRA 檔案的前綴（預設："loras/ComfyUI_trained_lora"）。 | STRING | 是 | N/A |
| `steps` | 選擇性：LoRA 已訓練的步數，用於命名已儲存的檔案。 | INT | 否 | N/A |

**注意：** `lora` 輸入必須是純 LoRA 模型。請勿提供已套用 LoRA 層的基礎模型。

**注意：** 檔案會以 `.safetensors` 副檔名儲存於 ComfyUI 輸出目錄中。檔名由 `prefix` 與補零計數器（5 位數）組成，以避免覆寫現有檔案。當提供 `steps` 時，步數也會包含在檔名中（例如，1000 步時為 `1000_steps`）。

**注意：** 此節點標記為實驗性。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| *None* | 此節點不會向工作流程輸出任何資料。它是一個會將檔案儲存至磁碟的輸出節點。 | N/A |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveLoRA/zh-TW.md)

---
**Source fingerprint (SHA-256):** `02f1d15dd7a5181666f2dbf06c45c07b12c4a178985464e07b5f613bd628f906`
