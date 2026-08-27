# ClipTextEncodeHunyuanDit

`CLIPTextEncodeHunyuanDiT` 節點將文字描述轉換為 HunyuanDiT 模型可以理解的格式。它是一個進階的 conditioning 節點，專為 HunyuanDiT 的雙文字編碼器架構設計，透過不同的 tokenizer 處理兩個獨立的文字輸入，並將它們的結果組合成單一的 conditioning 輸出。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `clip` | 用於文字 tokenization 和編碼的 CLIP 模型實例，是產生條件的核心。 | CLIP | 是 | - |
| `bert` | 透過 BERT tokenizer 進行編碼的文字輸入。偏好片語和關鍵字。支援多行和動態提示詞。 | STRING | 是 | - |
| `mt5xl` | 透過 mT5-XL tokenizer 進行編碼的文字輸入。支援多行和動態提示詞（多語言）。可以使用完整句子和複雜描述。 | STRING | 是 | - |

## 輸出

| 輸出名 | 描述 | 資料類型 |
| --- | --- | --- |
| `CONDITIONING` | 編碼後的 conditioning 輸出，結合了 BERT 和 mT5-XL tokenized 文字，用於生成任務中的進一步處理。 | CONDITIONING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ClipTextEncodeHunyuanDit/zh-TW.md)

---
**Source fingerprint (SHA-256):** `550e8c09b8b74974576a852a9b690a87a0156ef49fe7ec1050b10415c6af78aa`
