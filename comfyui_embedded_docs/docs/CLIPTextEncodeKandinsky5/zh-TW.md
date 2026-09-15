# CLIPTextEncodeKandinsky5

CLIP Text Encode (Kandinsky 5) 節點會準備要與 Kandinsky 5 模型搭配使用的文字提示詞。它接收兩個獨立的文字輸入，使用提供的 CLIP 模型將它們分詞，並將它們合併成單一條件輸出，以引導圖像生成流程。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `clip` | 用於將文字提示詞分詞與編碼的 CLIP 模型。 | CLIP | 是 |  |
| `clip_l` | 主要文字提示詞。此輸入支援多行文字與動態提示詞。 | STRING | 是 |  |
| `qwen25_7b` | 次要文字提示詞。此輸入支援多行文字與動態提示詞。 | STRING | 是 |  |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `CONDITIONING` | 由兩個文字提示詞合併產生的條件資料，可直接饋入 Kandinsky 5 模型以進行圖像生成。 | CONDITIONING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeKandinsky5/zh-TW.md)

---
**Source fingerprint (SHA-256):** `d988c47ab9a5f01549a3ae01b365d39e9fa2464bb69ea018ec20151939dcfc56`
