## 概述

此節點從已載入 LoRA 模型的元資料中提取 IC-LoRA 參數。它會讀取 safetensors 元資料以尋找如參考降採樣因子（reference downscale factor）等數值，並將其輸出為結構化的參數物件，可連接到 LTXVAddGuide 節點以進行特殊的引導處理。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `iclora_model` | 直接從 LoRA 載入器輸出，用於指定要提取元資料的特定 IC-LoRA。 | MODEL | 是 | 無 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `iclora_parameters` | 從 LoRA 元資料中提取的 IC-LoRA 參數（例如：reference_downscale_factor）。如果該 LoRA 需要對引導進行特殊處理，請連接到 LTXVAddGuide。 | IC_LORA_PARAMETERS |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GetICLoRAParameters/zh-TW.md)

---
**Source fingerprint (SHA-256):** `44673f0b06cb258014efd77f734c076865d59338ddf825598d85592f000aca50`
