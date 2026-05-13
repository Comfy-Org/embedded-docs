> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelPatchLoader/zh-TW.md)

## 概述

ModelPatchLoader 節點會從 model_patches 資料夾載入專門的模型修補程式。它會自動偵測修補程式檔案的類型，載入適當的模型架構，然後將其包裝在 ModelPatcher 中，以便在工作流程中使用。此節點支援不同的修補程式類型，包括 controlnet 區塊、特徵嵌入模型及其他專門架構。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `name` | STRING | 是 | model_patches 資料夾中所有可用的模型修補程式檔案 | 要從 model_patches 目錄載入的模型修補程式檔案名稱 |

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `MODEL_PATCH` | MODEL_PATCH | 已載入的模型修補程式，包裝在 ModelPatcher 中，可供工作流程使用 |

---
**Source fingerprint (SHA-256):** `e394e165cf416019ed53d9fde42d97c3c9b9f9afd843b12371a624467a4841bf`
