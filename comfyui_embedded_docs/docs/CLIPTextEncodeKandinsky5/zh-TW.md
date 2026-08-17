# CLIPTextEncodeKandinsky5

CLIPTextEncodeKandinsky5 節點會準備文字提示，以供 Kandinsky 5 模型使用。它接受兩個獨立的文字輸入，使用提供的 CLIP 模型進行分詞，並將其組合成單一條件輸出。此輸出用於引導影像生成過程。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `clip` | 用於對文字提示進行分詞和編碼的 CLIP 模型。 | CLIP | 是 |  |
| `clip_l` | 主要文字提示。此輸入支援多行文字和動態提示。 | STRING | 是 |  |
| `qwen25_7b` | 次要文字提示。此輸入支援多行文字和動態提示。 | STRING | 是 |  |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `CONDITIONING` | 從兩個文字提示產生的組合條件資料，可直接饋入 Kandinsky 5 模型以進行影像生成。 | CONDITIONING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeKandinsky5/zh-TW.md)

---
**Source fingerprint (SHA-256):** `d988c47ab9a5f01549a3ae01b365d39e9fa2464bb69ea018ec20151939dcfc56`
