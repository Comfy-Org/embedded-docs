# 取得 IC-LoRA 參數

## 概述

此節點從已載入的 LoRA 模型元資料中擷取 IC-LoRA 參數。它會讀取 safetensors 元資料，以尋找參考降縮因子（reference downscale factor）等數值，並將它們輸出為結構化參數物件，可連接到 LTXVAddGuide 節點以進行特殊的 guide 處理。若元資料缺失或無法讀取參考降縮因子，該數值預設為 1；若成功讀取，則會將數值四捨五入並限制為最小值 1。

## 輸入

| 參數 | 說明 | 資料型態 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `iclora_model` | 從特定 IC-LoRA 的 LoRA 載入器直接輸出的模型，用於從中擷取元資料。 | MODEL | 是 | N/A |

## 輸出

| 輸出名 | 說明 | 資料型態 |
| --- | --- | --- |
| `iclora_parameters` | 從 LoRA 元資料中擷取的 IC-LoRA 參數（例如：reference_downscale_factor）。若該 LoRA 需要對 guides 進行特殊處理，請連接到 LTXVAddGuide。 | IC_LORA_PARAMETERS |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GetICLoRAParameters/zh-TW.md)

---
**Source fingerprint (SHA-256):** `5f6becad0c7673b8cde1e099bd7ba5be7106da958b8967f8e693ba2a704baaef`
