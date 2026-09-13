# 標準化注意力引導

NAGuidance 節點會將正規化注意力引導（Normalized Attention Guidance）套用至模型。此技術會在採樣過程中修改模型的注意力機制，使蒸餾或 schnell 模型也能使用負向提示詞，以引導生成結果遠離不想要的概念。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 要套用正規化注意力引導的模型。 | MODEL | 是 | - |
| `nag_scale` | 引導縮放係數。數值越高，生成結果會越遠離負向提示詞。（預設值：5.0） | FLOAT | 是 | 0.0 - 50.0 |
| `nag_alpha` | 正規化注意力的混合係數。值為 1.0 時會完全取代原始注意力，而 0.0 則不產生影響。（預設值：0.5） | FLOAT | 是 | 0.0 - 1.0 |
| `nag_tau` | 用於限制正規化比例的縮放係數。（預設值：1.5） | FLOAT | 是 | 1.0 - 10.0 |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `model` | 已啟用正規化注意力引導的修補後模型。 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/NAGuidance/zh-TW.md)

---
**Source fingerprint (SHA-256):** `42b4d601312dcbb1c934c6a79bbb5e9fd6598fa5f32b18f5c0affcb596672cba`
