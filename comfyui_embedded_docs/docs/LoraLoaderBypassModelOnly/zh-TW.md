# 載入 LoRA（繞過模式，僅模型）（除錯用）

## 概述

此節點將 LoRA（低秩適應）應用於模型以修改其行為，但僅影響模型本身。它會載入指定的 LoRA 檔案，並以給定的強度調整模型的權重，而其他元件（如 CLIP 文字編碼器）則保持不變。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 將套用 LoRA 調整的基礎模型。 | MODEL | 是 | - |
| `lora_name` | 要載入並套用的 LoRA 檔案名稱。選項來自 `loras` 目錄中的檔案。 | STRING | 是 | （可用的 LoRA 檔案列表） |
| `strength_model` | LoRA 對模型權重的影響強度。正值套用 LoRA，負值套用反向效果，值為 0 則無效果（預設值：1.0）。 | FLOAT | 是 | -100.0 至 100.0 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `model` | 已將 LoRA 調整套用至其權重的修改後模型。 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoraLoaderBypassModelOnly/zh-TW.md)

---
**Source fingerprint (SHA-256):** `e0e1ad2d6481a1b9771d7eae833ffab0737a967d4af6e57b946d1b2223fe45bf`
