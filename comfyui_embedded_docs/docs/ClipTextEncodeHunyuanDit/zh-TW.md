# CLIPTextEncodeHunyuanDiT

`CLIPTextEncodeHunyuanDiT` 節點將文字描述轉換為 HunyuanDiT 模型可理解的格式。這是一個專為 HunyuanDiT 雙文字編碼器架構設計的高級條件節點，透過不同的分詞器處理兩個獨立的文字輸入。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `clip` | 用於文字分詞和編碼的 CLIP 模型實例，是生成條件的核心元件。 | CLIP | 是 | - |
| `bert` | 透過 BERT 分詞器進行編碼的文字輸入。建議使用短語和關鍵詞。支援多行和動態提示詞。 | STRING | 是 | - |
| `mt5xl` | 透過 mT5-XL 分詞器進行編碼的文字輸入。支援多行和動態提示詞（多語言）。可使用完整句子和複雜描述。 | STRING | 是 | - |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `CONDITIONING` | 編碼後的條件輸出，結合了 BERT 和 mT5-XL 分詞器的文字處理結果，用於生成任務的後續處理。 | CONDITIONING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeHunyuanDiT/zh-TW.md)

---
**Source fingerprint (SHA-256):** `6a8d649708b315c42b7933b52fad7e0b45aa34c168616f18a2178041148eeea1`
