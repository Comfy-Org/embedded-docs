## 概述

TextEncodeAceStepAudio 節點透過將標籤和歌詞組合成標記，再以可調整的歌詞強度進行編碼，來處理音頻條件化的文字輸入。此節點接收 CLIP 模型以及文字描述和歌詞，將其共同標記化，並產生適用於音頻生成任務的條件化資料。該節點允許透過強度參數微調歌詞的影響力，以控制其對最終輸出的作用。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `clip` | 用於標記化和編碼的 CLIP 模型 | CLIP | 是 | - |
| `標籤` | 用於音頻條件化的文字標籤或描述（支援多行輸入和動態提示） | STRING | 是 | - |
| `歌詞` | 用於音頻條件化的歌詞文字（支援多行輸入和動態提示） | STRING | 是 | - |
| `歌詞強度` | 控制歌詞對條件化輸出影響的強度（預設值：1.0，步長：0.01） | FLOAT | 否 | 0.0 - 10.0 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `conditioning` | 編碼後的條件化資料，包含已處理的文字標記並套用了指定的歌詞強度 | CONDITIONING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeAceStepAudio/zh-TW.md)

---
**Source fingerprint (SHA-256):** `89600133d8b0edaa36958530dacffe812675b595b0d77db702bb7709567cd83d`
