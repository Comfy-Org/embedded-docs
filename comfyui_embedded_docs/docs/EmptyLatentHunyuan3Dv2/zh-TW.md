# EmptyLatentHunyuan3Dv2

EmptyLatentHunyuan3Dv2 節點會建立專為 Hunyuan3Dv2 3D 生成模型格式化的空白潛在張量。它會生成具有 Hunyuan3Dv2 架構所需正確維度和結構的空白潛在空間，讓您可以從頭開始 3D 生成工作流程。該節點產生填充零的潛在張量，作為後續 3D 生成程序的基礎。

## 輸入
| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `解析度` | 潛在空間的解析度維度（預設值：3072） | INT | 是 | 1 - 8192 |
| `批次大小` | 批次中的潛在影像數量（預設值：1） | INT | 是 | 1 - 4096 |

## 輸出
| 輸出名 | 描述 | 資料類型 |
| --- | --- | --- |
| `LATENT` | 傳回包含標記為「hunyuan3dv2」類型的空樣本的潛在張量，格式化為 Hunyuan3Dv2 3D 生成 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyLatentHunyuan3Dv2/zh-TW.md)

---
**Source fingerprint (SHA-256):** `e9061301341ab84290cd2b16d5307636310a0772562cf485e3444876e4786ddd`
