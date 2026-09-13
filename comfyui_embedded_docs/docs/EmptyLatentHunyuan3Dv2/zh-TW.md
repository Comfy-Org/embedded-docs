# EmptyLatentHunyuan3Dv2

此節點會建立一批空的（全零）潛在樣本，其格式適用於 Hunyuan3Dv2 3D 生成模型。它會產生形狀正確的潛在張量，作為 3D 生成工作流程的起點，並將該潛在資料標記為類型 "hunyuan3dv2"。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `解析度` | 要建立的潛在空間解析度維度（預設：3072） | INT | 是 | 1 - 8192 |
| `批次大小` | 批次中的潛在影像數量（預設：1） | INT | 是 | 1 - 4096 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `LATENT` | 形狀為 [batch_size, 64, resolution] 的空潛在張量，包含以零填充的樣本，並標記為類型 "hunyuan3dv2" | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyLatentHunyuan3Dv2/zh-TW.md)

---
**Source fingerprint (SHA-256):** `e9061301341ab84290cd2b16d5307636310a0772562cf485e3444876e4786ddd`
