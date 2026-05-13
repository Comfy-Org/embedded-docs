> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/NAGuidance/zh-TW.md)

## 概述

NAGuidance 節點將正規化注意力引導（Normalized Attention Guidance）應用於模型。此技術透過在取樣過程中修改模型的注意力機制，引導生成結果遠離不想要的概念，從而實現對蒸餾或快速模型使用負面提示詞。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | 是 | - | 要套用正規化注意力引導的模型。 |
| `nag_scale` | FLOAT | 是 | 0.0 - 50.0 | 引導比例因子。數值越高，生成結果越偏離負面提示詞。（預設值：5.0） |
| `nag_alpha` | FLOAT | 是 | 0.0 - 1.0 | 正規化注意力的混合因子。值為 1.0 時完全取代原始注意力，值為 0.0 時則無效果。（預設值：0.5） |
| `nag_tau` | FLOAT | 是 | 1.0 - 10.0 | 用於限制正規化比率的縮放因子。（預設值：1.5） |

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `model` | MODEL | 已啟用正規化注意力引導的修補後模型。 |

---
**Source fingerprint (SHA-256):** `ea3d7fea94e62c8a0784887f3df9d8a503c3dbaa552bf860bd4dde1ae576fa9c`
