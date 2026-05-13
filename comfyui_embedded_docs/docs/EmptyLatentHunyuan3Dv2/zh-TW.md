> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyLatentHunyuan3Dv2/zh-TW.md)

## 概述

EmptyLatentHunyuan3Dv2 節點會建立專門為 Hunyuan3Dv2 3D 生成模型格式化的空白潛在張量。它會生成具有 Hunyuan3Dv2 架構所需正確維度與結構的空白潛在空間，讓您可以從頭開始啟動 3D 生成工作流程。此節點會產生填充零值的潛在張量，作為後續 3D 生成過程的基礎。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `resolution` | INT | 是 | 1 - 8192 | 潛在空間的解析度維度（預設值：3072） |
| `batch_size` | INT | 是 | 1 - 4096 | 批次中的潛在影像數量（預設值：1） |

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `LATENT` | LATENT | 回傳包含為 Hunyuan3Dv2 3D 生成格式化的空白樣本之潛在張量 |

---
**Source fingerprint (SHA-256):** `f912b226bcec4e2edd52250682d0583ab378b5502173f8e027e0e8fbff1db08f`
