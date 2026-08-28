# 取得 IC-LoRA 參數

此節點從已載入 LoRA 的模型中讀取元數據，以提取 IC-LoRA 參數，例如參考降採樣因子（reference downscale factor）。它會將這些參數輸出為結構化物件，當 LoRA 需要對引導（guides）進行特殊處理時，可連接到 LTXVAddGuide 節點。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `iclora_model` | 特定 IC-LoRA 的 LoRA 載入器直接輸出，用於從中提取元數據。 | MODEL | 是 | N/A |

注意：如果 LoRA 元數據缺失或不包含 `reference_downscale_factor` 條目，此節點將輸出預設值 1。若該因子存在，則會進行四捨五入，並設定最小值為 1。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `iclora_parameters` | 從 LoRA 元數據中提取的 IC-LoRA 參數（例如 `reference_downscale_factor`）。如果 LoRA 需要對引導進行特殊處理，請連接到 LTXVAddGuide。 | IC_LORA_PARAMETERS |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GetICLoRAParameters/zh-TW.md)

---
**Source fingerprint (SHA-256):** `5f6becad0c7673b8cde1e099bd7ba5be7106da958b8967f8e693ba2a704baaef`
