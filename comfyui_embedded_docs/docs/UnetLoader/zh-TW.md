## 概述

UNETLoader 節點專為依名稱載入 U-Net 模型而設計，便於在系統中使用預先訓練好的 U-Net 架構。

此節點會偵測位於 `ComfyUI/models/diffusion_models` 資料夾中的模型。

## 輸入

| 參數 | 說明 | 資料類型 |
| --- | --- | --- |
| `unet_name` | 指定要載入的 U-Net 模型名稱。此名稱用於在預定義的目錄結構中定位模型，從而實現動態載入不同的 U-Net 模型。 | COMBO[STRING] |
| `weight_dtype` | 🚧 fp8_e4m3fn fp9_e5m2 | ... |

## 輸出

| 參數 | 說明 | 資料類型 |
| --- | --- | --- |
| `model` | 傳回已載入的 U-Net 模型，使其能夠在系統中用於進一步處理或推論。 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/UNETLoader/zh-TW.md)
